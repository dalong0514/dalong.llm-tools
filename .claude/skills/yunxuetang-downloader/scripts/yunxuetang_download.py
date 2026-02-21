#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = [
#   "playwright>=1.40.0",
#   "requests>=2.31.0",
#   "pillow>=10.0.0",
# ]
# ///
"""
yunxuetang_download.py - 云学堂(yunxuetang.cn)视频/文档下载器

子命令:
  list     从目录页获取课程列表 -> course_list.json
  single   下载单个课程 (自动检测视频/文档)
  batch    批量下载课程列表中的所有课程

技术方案:
  视频: Playwright + MediaRecorder (绕过 Baidu BCE DRM) -> WebM -> MP4
  文档: Playwright 滚动捕获页面图片 URL -> 下载 -> PIL 合成 PDF

运行前请关闭所有 Chrome 窗口。
"""

import asyncio
import json
import re
import shutil
import subprocess
import sys
import tempfile
from io import BytesIO
from pathlib import Path

# ──────── 默认配置 ────────
DEFAULT_OUTPUT_DIR = Path.home() / "Downloads" / "yunxuetang"


def safe_name(s: str) -> str:
    s = s.strip()
    s = re.sub(r'[<>:"/\\|?*\n\r\t]', '_', s)
    return re.sub(r'_+', '_', s)[:80] or "unnamed"


def log(msg: str):
    try:
        print(msg, flush=True)
    except UnicodeEncodeError:
        print(msg.encode('utf-8', errors='replace').decode('utf-8'), flush=True)


# ──────── Chrome Profile ────────

def find_chrome_profile() -> Path | None:
    """自动检测 Chrome 用户数据目录"""
    candidates = []
    if sys.platform == 'win32':
        local = Path.home() / "AppData" / "Local"
        candidates = [
            local / "Google" / "Chrome" / "User Data",
            local / "Google" / "Chrome Beta" / "User Data",
        ]
    elif sys.platform == 'darwin':
        candidates = [
            Path.home() / "Library" / "Application Support" / "Google" / "Chrome",
        ]
    else:
        candidates = [
            Path.home() / ".config" / "google-chrome",
            Path.home() / ".config" / "chromium",
        ]
    for p in candidates:
        if p.exists():
            return p
    return None


def copy_chrome_profile(chrome_data: Path) -> Path:
    """复制 Chrome 关键文件到临时目录 (保留登录状态)"""
    log("[Profile] 复制 Chrome 登录数据...")
    tmp = Path(tempfile.mkdtemp(prefix="yxt_dl_"))
    for item, is_dir in [
        ("Local State", False),
        ("Default/Network/Cookies", False),
        ("Default/Local Storage", True),
        ("Default/IndexedDB", True),
        ("Default/Session Storage", True),
        ("Default/Preferences", False),
    ]:
        src = chrome_data / item
        dst = tmp / item
        dst.parent.mkdir(parents=True, exist_ok=True)
        try:
            if is_dir and src.is_dir():
                shutil.copytree(src, dst, dirs_exist_ok=True)
            elif not is_dir and src.is_file():
                shutil.copy2(src, dst)
        except Exception:
            pass
    return tmp


def get_ffmpeg_exe() -> str | None:
    for name in ['ffmpeg', 'ffmpeg.exe']:
        r = shutil.which(name)
        if r:
            return r
    try:
        import imageio_ffmpeg
        p = imageio_ffmpeg.get_ffmpeg_exe()
        if p and Path(p).exists():
            return p
    except Exception:
        pass
    return None


# ──────── 页面操作 ────────

async def click_start_button(page) -> bool:
    """点击「开始学习」/「继续学习」按钮"""
    for sel in [
        "button:has-text('开始学习')", "a:has-text('开始学习')",
        "button:has-text('继续学习')", "button:has-text('立即学习')",
        ".start-btn", "[class*='start-study']", "[class*='startStudy']",
    ]:
        try:
            btn = await page.wait_for_selector(sel, timeout=2000)
            if btn and await btn.is_visible():
                await btn.click()
                return True
        except Exception:
            pass
    # 兜底: 遍历所有按钮
    try:
        for btn in await page.query_selector_all("button, [role='button']"):
            try:
                text = (await btn.inner_text()).strip()
                if any(kw in text for kw in ['开始', '学习', '播放', '继续']):
                    if await btn.is_visible():
                        await btn.click()
                        return True
            except Exception:
                pass
    except Exception:
        pass
    return False


async def click_play_button(page) -> bool:
    """点击视频播放按钮"""
    for sel in [".vjs-big-play-button", ".vjs-play-control",
                "[class*='play-btn']", "[class*='play_btn']", "video"]:
        try:
            el = await page.query_selector(sel)
            if el and await el.is_visible():
                await el.click()
                return True
        except Exception:
            pass
    try:
        await page.evaluate("() => { const v = document.querySelector('video'); if(v) v.play().catch(()=>{}); }")
    except Exception:
        pass
    return False


# ──────── 课程列表获取 ────────

def extract_courses_from_api(data) -> list:
    """从 API 响应 JSON 中递归提取课程数据"""
    courses = []

    def search(obj, depth=0):
        if depth > 8 or not obj:
            return
        if isinstance(obj, list):
            for item in obj:
                search(item, depth + 1)
        elif isinstance(obj, dict):
            kng_id = (obj.get('kngId') or obj.get('id') or
                      obj.get('knowledgeId') or obj.get('kng_id') or '')
            name = (obj.get('name') or obj.get('title') or
                    obj.get('kngName') or obj.get('courseName') or '')
            type_val = (obj.get('type') or obj.get('kngType') or
                        obj.get('mediaType') or obj.get('contentType') or '')
            if kng_id and name and len(str(kng_id)) > 10:
                type_str = str(type_val).lower()
                if any(kw in type_str for kw in ['video', '1', 'mp4', 'stream']):
                    ctype = 'video'
                elif any(kw in type_str for kw in ['doc', '2', 'pdf', 'ppt', 'word']):
                    ctype = 'doc'
                else:
                    ctype = 'unknown'
                courses.append({'kngId': str(kng_id), 'name': str(name), 'type': ctype})
            for v in obj.values():
                if isinstance(v, (dict, list)):
                    search(v, depth + 1)

    search(data)
    seen = set()
    return [c for c in courses if c['kngId'] not in seen and not seen.add(c['kngId'])]


async def fetch_course_list(catalog_url: str, output_dir: Path,
                            chrome_data: Path) -> list:
    """打开目录页, 拦截 API 获取课程列表"""
    from playwright.async_api import async_playwright

    all_courses: list[dict] = []
    api_event = asyncio.Event()

    async def handle_response(response):
        if 'pagelist' not in response.url or response.status != 200:
            return
        ct = response.headers.get('content-type', '')
        if 'json' not in ct:
            return
        try:
            data = await response.json()
            courses = extract_courses_from_api(data)
            if courses:
                log(f"  [API] 获取 {len(courses)} 个课程")
                seen = {c['kngId'] for c in all_courses}
                for c in courses:
                    if c['kngId'] not in seen:
                        all_courses.append(c)
                        seen.add(c['kngId'])
                api_event.set()
        except Exception:
            pass

    async def boost_limit(route, request):
        url = request.url
        if 'pagelist' in url:
            new_url = re.sub(r'limit=\d+', 'limit=500', url)
            await route.continue_(url=new_url)
        else:
            await route.continue_()

    temp_profile = copy_chrome_profile(chrome_data)
    try:
        async with async_playwright() as p:
            log("[Playwright] 启动 Chrome...")
            browser = await p.chromium.launch_persistent_context(
                user_data_dir=str(temp_profile), channel="chrome",
                headless=False,
                args=["--disable-blink-features=AutomationControlled",
                      "--no-first-run", "--no-default-browser-check",
                      "--disable-sync", "--no-sandbox"],
                timeout=60000,
            )
            page = await browser.new_page()
            await page.route('**/pagelist**', boost_limit)
            page.on('response', handle_response)

            log(f"[Page] 打开目录页...")
            try:
                await page.goto(catalog_url, wait_until="networkidle", timeout=30000)
            except Exception:
                pass
            await page.wait_for_timeout(3000)

            try:
                await asyncio.wait_for(api_event.wait(), timeout=12)
            except asyncio.TimeoutError:
                pass

            log(f"  首次获取: {len(all_courses)} 个课程")

            # UI 翻页补充
            if len(all_courses) < 100:
                for _ in range(20):
                    prev = len(all_courses)
                    api_event = asyncio.Event()
                    clicked = False
                    for sel in [".el-pagination .btn-next:not([disabled])",
                                "button.btn-next:not([disabled])",
                                "[class*='pagination'] [class*='next']:not([disabled])"]:
                        try:
                            btn = await page.query_selector(sel)
                            if btn and await btn.is_visible() and await btn.is_enabled():
                                await btn.click()
                                clicked = True
                                break
                        except Exception:
                            pass
                    if not clicked:
                        break
                    try:
                        await asyncio.wait_for(api_event.wait(), timeout=5)
                    except asyncio.TimeoutError:
                        pass
                    await page.wait_for_timeout(500)
                    if len(all_courses) == prev:
                        break
                    log(f"  翻页: 累计 {len(all_courses)} 个课程")

            await page.unroute('**/pagelist**')
            page.remove_listener('response', handle_response)
            await browser.close()
    finally:
        shutil.rmtree(temp_profile, ignore_errors=True)

    log(f"\n[课程列表] 共 {len(all_courses)} 个课程")
    list_file = output_dir / "course_list.json"
    with open(list_file, 'w', encoding='utf-8') as f:
        json.dump(all_courses, f, ensure_ascii=False, indent=2)
    log(f"  保存到: {list_file}")
    return all_courses


# ──────── 视频录制 (MediaRecorder) ────────

RECORDER_INIT_JS = """
(function() {
    window.__yxt_recorder_chunks = [];
    window.__yxt_recorder = null;
    window.__yxt_recording_done = false;
    console.log('__YXT_RECORDER_READY__');
})();
"""

START_RECORDING_JS = """
async () => {
    const video = document.querySelector('video');
    if (!video) return { error: 'no video element' };
    try {
        if (video.readyState < 2) {
            await new Promise((resolve, reject) => {
                const timeout = setTimeout(() => reject('timeout'), 15000);
                video.addEventListener('loadeddata', () => { clearTimeout(timeout); resolve(); }, { once: true });
            });
        }
        const duration = video.duration;
        const width = video.videoWidth;
        const height = video.videoHeight;
        let stream;
        try { stream = video.captureStream(); }
        catch(e) {
            try { stream = video.mozCaptureStream(); }
            catch(e2) { return { error: 'captureStream blocked: ' + e.message }; }
        }
        const mimeType = MediaRecorder.isTypeSupported('video/webm;codecs=vp9,opus')
            ? 'video/webm;codecs=vp9,opus'
            : MediaRecorder.isTypeSupported('video/webm;codecs=vp8,opus')
            ? 'video/webm;codecs=vp8,opus' : 'video/webm';
        const recorder = new MediaRecorder(stream, { mimeType, videoBitsPerSecond: 4000000 });
        window.__yxt_recorder_chunks = [];
        window.__yxt_recording_done = false;
        recorder.ondataavailable = (e) => {
            if (e.data.size > 0) window.__yxt_recorder_chunks.push(e.data);
        };
        recorder.onstop = () => {
            window.__yxt_recording_done = true;
            console.log('__YXT_RECORDING_DONE__:' + window.__yxt_recorder_chunks.length + ' chunks');
        };
        window.__yxt_recorder = recorder;
        video.currentTime = 0;
        video.playbackRate = 1;
        await video.play();
        recorder.start(1000);
        return { duration, width, height, mimeType, estimatedTime: Math.ceil(duration) };
    } catch(e) { return { error: e.message }; }
}
"""

COLLECT_RECORDING_JS = """
async () => {
    const recorder = window.__yxt_recorder;
    if (recorder && recorder.state === 'recording') {
        recorder.stop();
        await new Promise(resolve => {
            const check = setInterval(() => {
                if (window.__yxt_recording_done) { clearInterval(check); resolve(); }
            }, 100);
            setTimeout(() => { clearInterval(check); resolve(); }, 5000);
        });
    }
    const chunks = window.__yxt_recorder_chunks;
    if (!chunks || chunks.length === 0) return { error: 'no data' };
    const blob = new Blob(chunks, { type: chunks[0].type || 'video/webm' });
    return { totalSize: blob.size, totalChunks: Math.ceil(blob.size / (512*1024)), mimeType: blob.type };
}
"""


async def download_video(page, name: str, output_dir: Path) -> bool:
    """通过 MediaRecorder 录制视频 (1x 速度)"""
    output_webm = output_dir / f"{safe_name(name)}.webm"
    output_mp4 = output_dir / f"{safe_name(name)}.mp4"

    # 跳过已下载
    if output_mp4.exists() and output_mp4.stat().st_size > 100_000:
        log(f"  [SKIP] {output_mp4.name}")
        return True

    await page.evaluate(RECORDER_INIT_JS)
    await page.wait_for_timeout(3000)

    # 点击播放
    await click_play_button(page)
    await page.wait_for_timeout(5000)

    # 启动录制
    log("  [录制] 启动 MediaRecorder (1x 速度)...")
    result = await page.evaluate(START_RECORDING_JS)
    if 'error' in result:
        log(f"  [ERR] MediaRecorder 失败: {result['error']}")
        return False

    duration = result.get('duration', 0)
    log(f"  视频时长: {duration:.0f}s = {duration/60:.1f}min")

    # 等待播放完成
    for i in range(int(duration) + 60):
        await page.wait_for_timeout(1000)
        try:
            status = await page.evaluate("""
                () => {
                    const v = document.querySelector('video');
                    return {
                        currentTime: v?.currentTime || 0,
                        duration: v?.duration || 0,
                        paused: v?.paused || false,
                        ended: v?.ended || false,
                        chunks: window.__yxt_recorder_chunks?.length || 0
                    };
                }
            """)
            if i % 30 == 0:
                ct = status.get('currentTime', 0)
                dur = status.get('duration', 0)
                pct = (ct / dur * 100) if dur > 0 else 0
                log(f"  进度: {ct:.0f}/{dur:.0f}s ({pct:.0f}%) chunks={status.get('chunks', 0)}")
            if status.get('ended') or status.get('paused'):
                log(f"  视频播放结束")
                break
        except Exception:
            pass

    # 收集录制数据
    log("  [收集] 停止录制...")
    info = await page.evaluate(COLLECT_RECORDING_JS)
    if 'error' in info:
        log(f"  [ERR] 收集失败: {info['error']}")
        return False

    total_size = info.get('totalSize', 0)
    if total_size == 0:
        log("  [ERR] 录制数据为空")
        return False

    log(f"  总大小: {total_size // 1024}KB")

    # 通过浏览器下载
    async with page.expect_download(timeout=60000) as download_info:
        await page.evaluate("""
            () => {
                const chunks = window.__yxt_recorder_chunks;
                const blob = new Blob(chunks, { type: 'video/webm' });
                const url = URL.createObjectURL(blob);
                const a = document.createElement('a');
                a.href = url;
                a.download = 'recording.webm';
                document.body.appendChild(a);
                a.click();
                document.body.removeChild(a);
                URL.revokeObjectURL(url);
            }
        """)

    download = await download_info.value
    await download.save_as(str(output_webm))
    log(f"  下载完成: {output_webm.stat().st_size // 1024}KB")

    # WebM -> MP4
    ffmpeg_exe = get_ffmpeg_exe()
    if ffmpeg_exe:
        log("  [ffmpeg] 转换为 MP4...")
        r = subprocess.run(
            [ffmpeg_exe, '-y', '-i', str(output_webm),
             '-c:v', 'libx264', '-crf', '20', '-preset', 'fast',
             '-c:a', 'aac', '-b:a', '192k',
             str(output_mp4)],
            capture_output=True, timeout=600
        )
        if r.returncode == 0 and output_mp4.exists():
            log(f"  [OK] {output_mp4.name} ({output_mp4.stat().st_size // 1024}KB)")
            output_webm.unlink()
        else:
            log(f"  [WARN] MP4 转换失败, 保留 WebM")
    else:
        log("  [WARN] 无 ffmpeg, 保留 WebM 格式")

    return True


# ──────── 文档下载 (滚动截图) ────────

async def download_doc(page, kng_id: str, name: str, output_dir: Path) -> bool:
    """对齐成功脚本: 先挂 listener → 再导航到 doc URL → 点击开始 → 滚动捕获全部图片 URL → 下载 → PDF"""
    import requests
    from PIL import Image

    output_pdf = output_dir / f"{safe_name(name)}.pdf"
    if output_pdf.exists() and output_pdf.stat().st_size > 1000:
        log(f"  [SKIP] {output_pdf.name}")
        return True

    img_urls: list[str] = []
    img_set: set[str] = set()

    def on_request(req):
        u = req.url
        if ('cdn-tce-file' in u and '/100100/' in u
                and u.split('?')[0].endswith('.jpg')):
            base = u.split('?')[0]
            if base not in img_set:
                img_set.add(base)
                img_urls.append(u)

    # 1. 先挂 listener
    page.on('request', on_request)

    # 2. 再导航 (listener 在导航过程中捕获图片请求)
    for url_template in [
        f"https://tz.yunxuetang.cn/kng/#/doc/play?kngId={kng_id}&projectId=&btid=&gwnlUrl=",
        f"https://tz.yunxuetang.cn/kng/#/video/play?kngId={kng_id}&projectId=&btid=&gwnlUrl=",
    ]:
        try:
            await page.goto(url_template, wait_until="networkidle", timeout=30000)
        except Exception:
            pass
        await page.wait_for_timeout(3000)

        # 3. 点击「开始学习」
        clicked = await click_start_button(page)
        if clicked:
            log("  已点击「开始学习」")
        await page.wait_for_timeout(5000)

        if img_urls:
            log(f"  初始加载: {len(img_urls)} 页")
            break
        log(f"  URL {url_template.split('#')[1][:20]} 无图片, 尝试下一个...")

    if not img_urls:
        page.remove_listener('request', on_request)
        log("  [ERR] 未捕获到图片 URL")
        return False

    # 4. 滚动加载剩余页面
    scroll_target = None
    for sel in [".doc-preview-container", ".doc-content",
                "[class*='doc-preview']", "[class*='doc-container']",
                "[class*='preview-content']", "[class*='kng-doc']",
                ".main-content", "#content", ".el-main"]:
        try:
            el = await page.query_selector(sel)
            if el:
                box = await el.bounding_box()
                if box and box['height'] > 100:
                    scroll_target = sel
                    break
        except Exception:
            pass

    prev_count = len(img_urls)
    no_new_count = 0
    for step in range(200):
        if scroll_target:
            await page.evaluate(
                f"(s) => {{ const el = document.querySelector('{scroll_target}'); if(el) el.scrollTop = s * 800; }}",
                step)
        else:
            await page.evaluate("(s) => window.scrollTo(0, s * 800)", step)
        await page.wait_for_timeout(500)

        if len(img_urls) > prev_count:
            prev_count = len(img_urls)
            no_new_count = 0
        else:
            no_new_count += 1
            if no_new_count >= 5:
                break

    page.remove_listener('request', on_request)
    await page.wait_for_timeout(1000)
    log(f"  共捕获 {len(img_urls)} 页图片 URL")

    # 5. 按页码排序, 用各自的签名 URL 下载 (token 是按页签名的)
    def page_num(url):
        m = re.search(r'/(\d+)\.jpg', url)
        return int(m.group(1)) if m else 0
    img_urls.sort(key=page_num)

    session = requests.Session()
    session.headers.update({
        'Referer': 'https://tz.yunxuetang.cn/',
        'User-Agent': ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                       'AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36'),
    })

    images = []
    for i, url in enumerate(img_urls):
        try:
            resp = session.get(url, timeout=30)
            if resp.status_code == 200 and len(resp.content) > 500:
                images.append(Image.open(BytesIO(resp.content)).convert('RGB'))
            else:
                log(f"  Page {i + 1} HTTP {resp.status_code}")
        except Exception as e:
            log(f"  Page {i + 1} ERROR: {e}")

    if not images:
        log("  [ERR] 未下载到任何图片")
        return False

    output_pdf.parent.mkdir(parents=True, exist_ok=True)
    images[0].save(str(output_pdf), save_all=True, append_images=images[1:])
    log(f"  [OK] {output_pdf.name} ({len(images)} 页, {output_pdf.stat().st_size // 1024}KB)")
    return True


# ──────── 文档: 在当前页面滚动捕获并下载 ────────

async def _scroll_and_download_doc(page, on_request, doc_img_urls: list[str],
                                    doc_img_set: set[str], name: str,
                                    output_dir: Path) -> bool:
    """在当前已加载的文档页面上滚动, 捕获懒加载图片 URL, 下载并合成 PDF.

    on_request listener 仍然挂着, 本函数负责滚动、等待、最后移除 listener.
    doc_img_urls / doc_img_set 已在类型检测阶段收集了初始 URL.
    """
    import requests
    from PIL import Image

    output_pdf = output_dir / f"{safe_name(name)}.pdf"
    if output_pdf.exists() and output_pdf.stat().st_size > 1000:
        page.remove_listener('request', on_request)
        log(f"  [SKIP] {output_pdf.name}")
        return True

    log(f"  初始加载: {len(doc_img_urls)} 页")

    # 文档查看器是翻页式的, 每次加载10页为一批
    # 需要点击"下一页"按钮翻过批次边界 (第11, 21, 31...页) 触发下一批加载

    # 1. 从页面获取总页数和下一页按钮信息
    viewer_info = await page.evaluate("""
        () => {
            const info = { totalPages: 0, nextBtn: null };

            // 查找页码指示器 (如 "1/17", "1 / 17")
            const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
            let node;
            while (node = walker.nextNode()) {
                const text = node.textContent.trim();
                const m = text.match(/(\\d+)\\s*[/／]\\s*(\\d+)/);
                if (m && parseInt(m[2]) > 1) {
                    info.totalPages = parseInt(m[2]);
                    break;
                }
            }

            // 查找下一页按钮: 在页面右侧的小型可点击元素
            const vpW = window.innerWidth;
            const vpH = window.innerHeight;
            const candidates = [];
            const all = document.querySelectorAll('*');
            for (const el of all) {
                const rect = el.getBoundingClientRect();
                if (rect.width === 0 || rect.height === 0) continue;
                if (rect.width > 150 || rect.height > 150) continue;
                // 只看页面右半部分的元素
                if (rect.x + rect.width / 2 < vpW * 0.6) continue;

                const cls = (el.className?.baseVal || el.className || '').toString();
                const tag = el.tagName.toLowerCase();
                const style = getComputedStyle(el);
                const clickable = style.cursor === 'pointer' || tag === 'button' ||
                                  tag === 'a' || tag === 'svg' || tag === 'i' ||
                                  el.onclick || el.getAttribute('role') === 'button';
                if (!clickable) continue;

                candidates.push({
                    cls: cls.substring(0, 100),
                    tag, x: Math.round(rect.x), y: Math.round(rect.y),
                    w: Math.round(rect.width), h: Math.round(rect.height),
                    centerX: Math.round(rect.x + rect.width / 2),
                    centerY: Math.round(rect.y + rect.height / 2)
                });
            }
            info.candidates = candidates;
            return info;
        }
    """)

    total_pages = viewer_info.get('totalPages', 0)
    candidates = viewer_info.get('candidates', [])
    log(f"  总页数: {total_pages or '未知'}, 候选按钮: {len(candidates)} 个")
    for c in candidates[:5]:
        log(f"    <{c['tag']}> cls={c['cls'][:50]} pos=({c['x']},{c['y']}) size={c['w']}x{c['h']}")

    # 2. 确定翻页按钮的点击坐标 (左=上一页, 右=下一页)
    vp = page.viewport_size or {'width': 1280, 'height': 800}

    # 在页面右侧 (>70% 宽度), 垂直居中区域 (20%-80%) 找下一页按钮
    next_btn, prev_btn = None, None
    for c in candidates:
        cy_ok = vp['height'] * 0.2 < c['centerY'] < vp['height'] * 0.8
        if not cy_ok:
            continue
        if c['centerX'] > vp['width'] * 0.7:
            if next_btn is None or c['centerX'] > next_btn['centerX']:
                next_btn = c
        elif c['centerX'] < vp['width'] * 0.3:
            if prev_btn is None or c['centerX'] < prev_btn['centerX']:
                prev_btn = c

    if next_btn:
        log(f"  下一页按钮: ({next_btn['centerX']},{next_btn['centerY']}) cls={next_btn['cls'][:40]}")
    if prev_btn:
        log(f"  上一页按钮: ({prev_btn['centerX']},{prev_btn['centerY']}) cls={prev_btn['cls'][:40]}")

    # 3. 双向翻页: 先往前翻到第1页, 再往后翻到最后一页
    #    这样无论从哪页开始, 都能捕获所有批次 (每10页一批)
    async def flip_pages(direction: str, max_steps: int):
        """direction: 'prev' 或 'next'"""
        nonlocal prev_count, no_new_count
        btn = prev_btn if direction == 'prev' else next_btn
        key = 'ArrowLeft' if direction == 'prev' else 'ArrowRight'
        prev_count = len(doc_img_urls)
        no_new_count = 0
        for step in range(max_steps):
            if btn:
                await page.mouse.click(btn['centerX'], btn['centerY'])
                await page.wait_for_timeout(300)
            await page.keyboard.press(key)
            await page.wait_for_timeout(500)

            if len(doc_img_urls) > prev_count:
                log(f"  [{direction}] 翻页 {step}: 已加载 {len(doc_img_urls)} 页")
                prev_count = len(doc_img_urls)
                no_new_count = 0
            else:
                no_new_count += 1
                if no_new_count >= 15:
                    break

    prev_count = len(doc_img_urls)
    no_new_count = 0
    max_steps = (total_pages + 5) if total_pages > 0 else 500

    # 先往前翻 (回到第1页, 触发加载前面的批次)
    log("  [phase1] 往前翻页...")
    await flip_pages('prev', max_steps)

    # 再往后翻 (翻到最后一页, 触发加载后面的批次)
    log("  [phase2] 往后翻页...")
    await flip_pages('next', max_steps)

    # 滚动完毕, 移除 listener
    page.remove_listener('request', on_request)
    await page.wait_for_timeout(2000)
    log(f"  共捕获 {len(doc_img_urls)} 页图片 URL")

    if not doc_img_urls:
        log("  [ERR] 未捕获到图片 URL")
        return False

    # 按页码排序 (每个 URL 带各自的签名 token)
    def page_num(url):
        m = re.search(r'/(\d+)\.jpg', url)
        return int(m.group(1)) if m else 0
    doc_img_urls.sort(key=page_num)

    # 下载图片
    session = requests.Session()
    session.headers.update({
        'Referer': 'https://tz.yunxuetang.cn/',
        'User-Agent': ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                       'AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36'),
    })

    images = []
    for i, url in enumerate(doc_img_urls):
        try:
            resp = session.get(url, timeout=30)
            if resp.status_code == 200 and len(resp.content) > 500:
                images.append(Image.open(BytesIO(resp.content)).convert('RGB'))
            else:
                log(f"  Page {i + 1} HTTP {resp.status_code}")
        except Exception as e:
            log(f"  Page {i + 1} ERROR: {e}")

    if not images:
        log("  [ERR] 未下载到任何图片")
        return False

    output_pdf.parent.mkdir(parents=True, exist_ok=True)
    images[0].save(str(output_pdf), save_all=True, append_images=images[1:])
    log(f"  [OK] {output_pdf.name} ({len(images)} 页, {output_pdf.stat().st_size // 1024}KB)")
    return True


# ──────── 单课程下载 ────────

async def download_single_course(kng_id: str, name: str, output_dir: Path,
                                 chrome_data: Path) -> bool:
    """下载单个课程 (自动检测视频/文档类型)"""
    from playwright.async_api import async_playwright

    output_dir.mkdir(parents=True, exist_ok=True)
    m3u8_detected = False
    img_detected = False
    doc_img_urls: list[str] = []
    doc_img_set: set[str] = set()

    def on_request(req):
        nonlocal m3u8_detected, img_detected
        u = req.url
        if ('m3u8' in u and ('streamobs' in u or 'yunxuetang' in u)):
            m3u8_detected = True
        elif 'cdn-tce-file' in u and '/100100/' in u and u.split('?')[0].endswith('.jpg'):
            img_detected = True
            base = u.split('?')[0]
            if base not in doc_img_set:
                doc_img_set.add(base)
                doc_img_urls.append(u)

    temp_profile = copy_chrome_profile(chrome_data)
    try:
        async with async_playwright() as p:
            log("[Playwright] 启动 Chrome...")
            browser = await p.chromium.launch_persistent_context(
                user_data_dir=str(temp_profile), channel="chrome",
                headless=False,
                args=["--disable-blink-features=AutomationControlled",
                      "--no-first-run", "--no-default-browser-check",
                      "--disable-sync", "--no-sandbox",
                      "--autoplay-policy=no-user-gesture-required"],
                timeout=60000,
            )
            page = await browser.new_page()

            # 注入录制脚本 (万一是视频)
            await page.add_init_script(RECORDER_INIT_JS)
            page.on('request', on_request)

            # 尝试 video URL
            video_url = (f"https://tz.yunxuetang.cn/kng/#/video/play"
                         f"?kngId={kng_id}&projectId=&btid=&gwnlUrl=")
            log(f"[Page] 打开课程页面...")
            try:
                await page.goto(video_url, wait_until="networkidle", timeout=30000)
            except Exception:
                pass
            await page.wait_for_timeout(3000)

            # 点击「开始学习」
            clicked = await click_start_button(page)
            if clicked:
                log("  已点击「开始学习」")
            await page.wait_for_timeout(5000)

            # 如果没有检测到内容, 尝试 doc URL
            if not m3u8_detected and not img_detected:
                doc_url = (f"https://tz.yunxuetang.cn/kng/#/doc/play"
                           f"?kngId={kng_id}&projectId=&btid=&gwnlUrl=")
                log("[Page] 尝试文档路径...")
                try:
                    await page.goto(doc_url, wait_until="networkidle", timeout=30000)
                except Exception:
                    pass
                await page.wait_for_timeout(3000)
                clicked = await click_start_button(page)
                if clicked:
                    log("  已点击「开始学习」")
                await page.wait_for_timeout(5000)

            # 根据检测结果下载
            if img_detected:
                log(f"[类型] 文档 (已捕获 {len(doc_img_urls)} 页)")
                # listener 仍然挂着, 在当前页面滚动捕获更多图片
                ok = await _scroll_and_download_doc(
                    page, on_request, doc_img_urls, doc_img_set,
                    name or kng_id, output_dir)
            elif m3u8_detected:
                page.remove_listener('request', on_request)
                log(f"[类型] 视频 (检测到 m3u8)")
                await click_play_button(page)
                await page.wait_for_timeout(3000)
                ok = await download_video(page, name or kng_id, output_dir)
            else:
                page.remove_listener('request', on_request)
                # 检查是否有 video 元素
                has_video = await page.evaluate(
                    "() => !!document.querySelector('video')?.src || !!document.querySelector('video source')?.src"
                )
                if has_video:
                    log(f"[类型] 视频 (检测到 video 元素)")
                    await click_play_button(page)
                    await page.wait_for_timeout(3000)
                    ok = await download_video(page, name or kng_id, output_dir)
                else:
                    log("[ERR] 无法检测课程类型")
                    await page.screenshot(path=str(output_dir / f"debug_{kng_id[:8]}.png"))
                    ok = False

            await browser.close()
            return ok
    finally:
        shutil.rmtree(temp_profile, ignore_errors=True)


# ──────── 顺序下载 (逐个独立子进程) ────────

def run_all_sequential(course_list_file: Path, output_dir: Path,
                       start_index: int = 0):
    """逐个课程独立子进程下载, 每完成一个保存进度"""
    with open(course_list_file, encoding='utf-8') as f:
        courses = json.load(f)

    output_dir.mkdir(parents=True, exist_ok=True)
    progress_file = output_dir / "download_progress.json"

    # 加载进度
    done_ids: set[str] = set()
    if progress_file.exists():
        try:
            with open(progress_file, encoding='utf-8') as f:
                progress = json.load(f)
            done_ids = set(progress.get('done', []))
        except Exception:
            pass

    total = len(courses)
    log(f"[进度] 已完成 {len(done_ids)}/{total}, 从第 {start_index + 1} 个开始")

    script_path = str(Path(__file__).resolve())
    failed = []

    for idx, course in enumerate(courses):
        if idx < start_index:
            continue

        kng_id = course.get('kngId', '')
        name = course.get('name', f'item_{idx + 1}')

        if kng_id in done_ids:
            continue

        log(f"\n{'='*60}")
        log(f"[{idx + 1}/{total}] {name[:60]}")
        log(f"  已完成: {len(done_ids)}, 剩余: {total - len(done_ids)}")

        # 用独立子进程调用 single 模式
        result = subprocess.run(
            [sys.executable, script_path,
             "--output-dir", str(output_dir),
             "single",
             "--kng-id", kng_id,
             "--name", name],
            timeout=None,
        )

        if result.returncode == 0:
            done_ids.add(kng_id)
            with open(progress_file, 'w', encoding='utf-8') as f:
                json.dump({'done': list(done_ids)}, f, ensure_ascii=False)
            log(f"  [OK] 进度已保存 ({len(done_ids)}/{total})")
        else:
            log(f"  [FAIL] {name}")
            failed.append(name)

    log(f"\n{'='*60}")
    log(f"完成: 成功 {len(done_ids)}, 失败 {len(failed)}")
    for f in failed:
        log(f"  FAIL: {f}")


# ──────── CLI ────────

def main():
    import argparse
    parser = argparse.ArgumentParser(description="云学堂视频/文档下载器")
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR,
                        help="输出目录")
    parser.add_argument("--chrome-profile", type=Path, default=None,
                        help="Chrome 用户数据目录 (自动检测)")
    sub = parser.add_subparsers(dest="command", required=True)

    # list
    p_list = sub.add_parser("list", help="获取课程列表")
    p_list.add_argument("--url", required=True, help="目录页 URL")

    # single
    p_single = sub.add_parser("single", help="下载单个课程")
    p_single.add_argument("--kng-id", required=True, help="课程 kngId")
    p_single.add_argument("--name", default="", help="课程名称")

    # run-all
    p_run = sub.add_parser("run-all", help="顺序逐个下载 (每个课程独立进程)")
    p_run.add_argument("--courses", type=Path, required=True,
                       help="course_list.json 路径")
    p_run.add_argument("--start", type=int, default=0,
                       help="起始索引 (跳过前 N 个)")

    args = parser.parse_args()

    # Chrome profile
    chrome_data = args.chrome_profile or find_chrome_profile()
    if not chrome_data or not chrome_data.exists():
        log("[ERR] 找不到 Chrome 用户数据目录, 请用 --chrome-profile 指定")
        sys.exit(1)

    args.output_dir.mkdir(parents=True, exist_ok=True)

    if args.command == 'list':
        asyncio.run(fetch_course_list(args.url, args.output_dir, chrome_data))
    elif args.command == 'single':
        ok = asyncio.run(download_single_course(
            args.kng_id, args.name, args.output_dir, chrome_data))
        sys.exit(0 if ok else 1)
    elif args.command == 'run-all':
        run_all_sequential(args.courses, args.output_dir, args.start)


if __name__ == "__main__":
    main()
