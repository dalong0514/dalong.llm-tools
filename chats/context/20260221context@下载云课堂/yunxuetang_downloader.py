#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = [
#   "playwright>=1.40.0",
#   "requests>=2.31.0",
#   "pillow>=10.0.0",
#   "yt-dlp>=2024.1.1",
#   "imageio-ffmpeg>=0.4.0",
#   "pycryptodomex>=3.20.0",
# ]
# ///
"""
yunxuetang_downloader.py - 从云学堂下载视频和文档 (共189个课程)

策略:
1. Playwright 用临时 Profile 启动 Chrome（保留登录）
2. 拦截目录页 API 响应 -> 获取所有课程的 kngId 和类型
3. 逐一访问每个课程页 -> 点击「开始学习」-> 拦截真实 URL
4. 视频: yt-dlp 下载 m3u8  |  文档: 下载所有页图片 -> PDF

【运行前】请关闭所有 Chrome 窗口
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

# ──────── 配置 ────────
CATALOG_URL = (
    "https://tz.yunxuetang.cn/kng/#/list"
    "?catalogId=95a02ce6-05b2-4691-b0fc-5c0cfa8b43bb"
    "&cid=8fc01ff6-0759-43e1-829b-9763781f0f27"
    "&order=0&sort=0&type="
)
OUTPUT_DIR = Path("C:/Users/dalong0514/Downloads/yunxuetang")
COOKIES_FILE = OUTPUT_DIR / "yunxuetang_cookies.txt"
CAPTURES_FILE = OUTPUT_DIR / "captures.json"
COURSE_LIST_FILE = OUTPUT_DIR / "course_list.json"
KEY_DIR = OUTPUT_DIR / "keys"          # AES-128 密钥文件目录
CHROME_USER_DATA = Path("C:/Users/dalong0514/AppData/Local/Google/Chrome/User Data")
PYTHON_EXE = sys.executable
TEMP_DIR: Path | None = None
KEY_SERVER_PORT = 18765               # 本地 key 服务器端口

# ── 测试模式：只处理指定 kngId，空列表 = 处理全部 ──
# course 2 (实际视频): 5d7314dd-bb0a-47ad-a1b8-bf45c6575e06
# course 1 (实际文档): 99ed7903-fc49-4dad-a287-01a57aa0bc43
TEST_KNGIDS: list[str] = []  # 空 = 使用已有 captures.json 直接下载


# ──────── 工具 ────────

def safe_name(s: str) -> str:
    s = s.strip()
    s = re.sub(r'[<>:"/\\|?*\n\r\t]', '_', s)
    return re.sub(r'_+', '_', s)[:80] or "unnamed"


def log(msg: str):
    try:
        print(msg, flush=True)
    except UnicodeEncodeError:
        print(msg.encode('utf-8', errors='replace').decode('utf-8'), flush=True)


def save_cookies(cookies: list, path: Path):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write("# Netscape HTTP Cookie File\n")
        for c in cookies:
            d = c.get('domain', '')
            f.write(f"{d}\t{'TRUE' if d.startswith('.') else 'FALSE'}\t"
                    f"{c.get('path','/')}\t"
                    f"{'TRUE' if c.get('secure') else 'FALSE'}\t"
                    f"{max(0, int(c.get('expires', 0) or 0))}\t"
                    f"{c.get('name','')}\t{c.get('value','')}\n")
    log(f"[Cookies] 已保存 {len(cookies)} 条")


# ──────── 复制 Chrome Profile ────────

def copy_chrome_profile() -> Path:
    global TEMP_DIR
    if TEMP_DIR and TEMP_DIR.exists():
        return TEMP_DIR

    log("[Profile] 复制关键文件到临时目录...")
    tmp = Path(tempfile.mkdtemp(prefix="yxt_chrome_"))

    for item, is_dir in [
        ("Local State", False),
        ("Default/Network/Cookies", False),   # Chrome 127+ 移到了此路径
        ("Default/Local Storage", True),
        ("Default/IndexedDB", True),
        ("Default/Session Storage", True),
        ("Default/Preferences", False),
    ]:
        src = CHROME_USER_DATA / item
        dst = tmp / item
        dst.parent.mkdir(parents=True, exist_ok=True)
        try:
            if is_dir and src.is_dir():
                shutil.copytree(src, dst, dirs_exist_ok=True)
                log(f"  [OK] {item}/")
            elif not is_dir and src.is_file():
                shutil.copy2(src, dst)
                log(f"  [OK] {item}")
            else:
                log(f"  [SKIP] {item} (not found)")
        except Exception as e:
            log(f"  [ERR] {item}: {e}")

    TEMP_DIR = tmp
    return tmp


def cleanup():
    global TEMP_DIR
    if TEMP_DIR and TEMP_DIR.exists():
        shutil.rmtree(TEMP_DIR, ignore_errors=True)
        log(f"[Profile] 已清理临时目录")
        TEMP_DIR = None


# ──────── AES Key 解析与服务 ────────

def parse_key_response(body: bytes) -> bytes | None:
    """解析 DRM 密钥响应，可能是原始二进制或 JSON (含 hex/base64 编码 key)"""
    import base64 as _b64

    # 原始 16 字节 key
    if len(body) == 16:
        return body

    # JSON 响应：递归搜索所有字段
    try:
        data = json.loads(body)

        def _search(obj, depth=0):
            if depth > 5:
                return None
            if isinstance(obj, str):
                # 32 hex chars = 16 bytes
                if len(obj) == 32:
                    try:
                        return bytes.fromhex(obj)
                    except ValueError:
                        pass
                # base64 encoded 16 bytes = 24 chars (with padding)
                try:
                    decoded = _b64.b64decode(obj + '==')
                    if len(decoded) == 16:
                        return decoded
                except Exception:
                    pass
            elif isinstance(obj, dict):
                for v in obj.values():
                    r = _search(v, depth + 1)
                    if r:
                        return r
            elif isinstance(obj, list):
                for v in obj:
                    r = _search(v, depth + 1)
                    if r:
                        return r
            return None

        result = _search(data)
        if result:
            return result
    except (json.JSONDecodeError, ValueError):
        pass
    return None

def start_local_key_server():
    """启动本地 HTTP 服务器，提供 AES-128 密钥和 m3u8 manifest"""
    import threading
    from http.server import HTTPServer, BaseHTTPRequestHandler

    class _KeyHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            path = self.path.strip('/')
            # 提供 m3u8 manifest 文件
            if path.endswith('.m3u8'):
                mf = KEY_DIR / path
                if mf.exists():
                    data = mf.read_bytes()
                    self.send_response(200)
                    self.send_header('Content-Type', 'application/vnd.apple.mpegurl')
                    self.send_header('Content-Length', str(len(data)))
                    self.end_headers()
                    self.wfile.write(data)
                    return
            # 提供 AES 密钥
            kf = KEY_DIR / f"{path}.bin"
            if kf.exists():
                data = kf.read_bytes()
                self.send_response(200)
                self.send_header('Content-Type', 'application/octet-stream')
                self.send_header('Content-Length', str(len(data)))
                self.end_headers()
                self.wfile.write(data)
            else:
                self.send_response(404)
                self.end_headers()
        def log_message(self, *a): pass  # 静默

    try:
        srv = HTTPServer(('127.0.0.1', KEY_SERVER_PORT), _KeyHandler)
        t = threading.Thread(target=srv.serve_forever, daemon=True)
        t.start()
        log(f"[KeyServer] 启动在 127.0.0.1:{KEY_SERVER_PORT}")
    except Exception as e:
        log(f"[KeyServer] 启动失败: {e}")


def get_ffmpeg_exe() -> str | None:
    """尝试获取 ffmpeg 路径（优先系统 PATH，次选 imageio-ffmpeg 内置）"""
    # 1. 系统 PATH
    for name in ['ffmpeg', 'ffmpeg.exe']:
        r = shutil.which(name)
        if r:
            return r
    # 2. imageio-ffmpeg 内置
    try:
        import imageio_ffmpeg
        p = imageio_ffmpeg.get_ffmpeg_exe()
        if p and Path(p).exists():
            return p
    except Exception:
        pass
    return None


def patch_m3u8_for_local_keys(m3u8_url: str) -> str:
    """
    下载 m3u8 manifest，将 DRM key URI 替换为本地 key server URL。
    返回临时 m3u8 文件路径（若替换成功）或原始 URL（若密钥未捕获）。
    """
    import requests as _req

    if not KEY_DIR.exists():
        return m3u8_url

    try:
        resp = _req.get(m3u8_url,
                        headers={'Referer': 'https://tz.yunxuetang.cn/',
                                 'User-Agent': 'Mozilla/5.0'},
                        timeout=15)
        if not resp.ok:
            return m3u8_url
        content = resp.text.replace('\r\n', '\n').replace('\r', '\n')

        # 找出所有 key ID
        key_ids = re.findall(r'videoKeyId=([^"&\s]+)', content)
        if not key_ids:
            return m3u8_url

        # 检查是否有本地密钥
        missing = [kid for kid in key_ids if not (KEY_DIR / f"{kid}.bin").exists()]
        if missing:
            log(f"  [AES] 缺少 {len(missing)}/{len(key_ids)} 个密钥，尝试直接下载")
            return m3u8_url

        # 替换 key URI 并移除 DRM 特定属性（KEYFORMAT, KEYFORMATVERSIONS）
        new_content = re.sub(
            r'#EXT-X-KEY:[^\n]*URI="https://drm\.media\.baidubce\.com/v1/tokenVideoKey\?videoKeyId=([^"&]+)[^"]*"[^\n]*',
            lambda m: f'#EXT-X-KEY:METHOD=AES-128,URI="http://127.0.0.1:{KEY_SERVER_PORT}/{m.group(1)}"',
            content
        )
        # 修复相对路径为绝对 URL（.ts 片段及其他媒体文件）
        base_url = m3u8_url.rsplit('/', 1)[0] + '/'
        lines = new_content.split('\n')
        for i, line in enumerate(lines):
            stripped = line.strip()
            if stripped and not stripped.startswith('#') and not stripped.startswith('http'):
                lines[i] = base_url + stripped
        new_content = '\n'.join(lines)

        # 调试：显示 key 行
        for line in new_content.split('\n'):
            if '#EXT-X-KEY' in line:
                log(f"  [AES] patched key: {line[:120]}")
                break

        # 保存到 KEY_DIR，通过本地 key server 提供
        manifest_name = "manifest.m3u8"
        manifest_path = KEY_DIR / manifest_name
        manifest_path.write_text(new_content, encoding='utf-8')
        local_url = f"http://127.0.0.1:{KEY_SERVER_PORT}/{manifest_name}"
        log(f"  [AES] 本地密钥，m3u8 URL: {local_url}")
        return local_url
    except Exception as e:
        log(f"  [AES] patch 失败: {e}")
        return m3u8_url


# ──────── Step 1: 获取课程列表 (拦截 API) ────────

async def fetch_course_list(page, context) -> list:
    """
    策略：
    1. 先用 route 拦截修改 limit 参数（改为 500），让浏览器用自身 auth 上下文
       一次性获取尽可能多的课程。
    2. 若结果不足，再通过 UI 点击翻页，拦截后续 API 响应补充数据。
    """
    log("\n[课程列表] 开始收集...")

    all_courses: list[dict] = []
    api_events: list[asyncio.Event] = [asyncio.Event()]

    # ── 响应拦截 ──
    async def handle_response(response):
        url = response.url
        if 'pagelist' not in url:
            return
        if response.status != 200:
            return
        ct = response.headers.get('content-type', '')
        if 'json' not in ct:
            return
        try:
            data = await response.json()
            courses = extract_courses_from_api(data)
            if courses:
                log(f"  [API] {url[:80]} -> {len(courses)} 个课程")
                seen = {c['kngId'] for c in all_courses}
                for c in courses:
                    if c['kngId'] not in seen:
                        all_courses.append(c)
                        seen.add(c['kngId'])
                api_events[0].set()
        except Exception:
            pass

    # ── 路由拦截：把 limit 参数替换为 500 ──
    async def boost_limit(route, request):
        url = request.url
        if 'pagelist' in url:
            import re as re_mod
            new_url = re_mod.sub(r'limit=\d+', 'limit=500', url)
            log(f"  [Route] 修改 limit -> 500")
            await route.continue_(url=new_url)
        else:
            await route.continue_()

    await page.route('**/pagelist**', boost_limit)
    page.on('response', handle_response)

    # ── 打开目录页 ──
    try:
        await page.goto(CATALOG_URL, wait_until="networkidle", timeout=30000)
    except Exception as e:
        log(f"  页面加载超时: {e}")
    await page.wait_for_timeout(3000)

    shot = OUTPUT_DIR / "debug_catalog.png"
    await page.screenshot(path=str(shot), full_page=True)
    log(f"  截图: {shot}")

    try:
        await asyncio.wait_for(api_events[0].wait(), timeout=12)
    except asyncio.TimeoutError:
        log("  [!] 首次 API 超时")

    log(f"  [Route] 首次获取: {len(all_courses)} 个课程")

    # ── 如果还不够，通过 UI 翻页补充 ──
    if len(all_courses) < 100:
        log("  [UI 翻页] 首次数据不足，尝试点击翻页...")
        for _ in range(20):
            prev = len(all_courses)
            api_events[0] = asyncio.Event()

            clicked = False
            for sel in [
                ".el-pagination .btn-next:not([disabled])",
                "button.btn-next:not([disabled])",
                "[class*='pagination'] [class*='next']:not([disabled])",
                "button:has-text('>')",
                "li.next:not(.disabled)",
            ]:
                try:
                    btn = await page.query_selector(sel)
                    if btn and await btn.is_visible() and await btn.is_enabled():
                        await btn.click()
                        clicked = True
                        break
                except Exception:
                    pass

            if not clicked:
                log("  [UI 翻页] 没有更多页面或找不到按钮")
                break

            try:
                await asyncio.wait_for(api_events[0].wait(), timeout=5)
            except asyncio.TimeoutError:
                pass

            await page.wait_for_timeout(500)
            added = len(all_courses) - prev
            log(f"  [UI 翻页] 新增 {added} 个，累计 {len(all_courses)} 个")
            if added == 0:
                break

    await page.unroute('**/pagelist**')
    page.remove_listener('response', handle_response)

    log(f"\n  [课程列表] 共获取 {len(all_courses)} 个课程")
    return all_courses


def extract_courses_from_api(data) -> list:
    """从 API 响应 JSON 中提取课程数据"""
    courses = []

    def search(obj, depth=0):
        if depth > 8 or not obj:
            return
        if isinstance(obj, list):
            for item in obj:
                search(item, depth+1)
        elif isinstance(obj, dict):
            # 检查是否是课程对象（含有 kngId 或 id 字段）
            kng_id = (obj.get('kngId') or obj.get('id') or
                      obj.get('knowledgeId') or obj.get('kng_id') or '')
            name = (obj.get('name') or obj.get('title') or
                    obj.get('kngName') or obj.get('courseName') or '')
            type_val = (obj.get('type') or obj.get('kngType') or
                        obj.get('mediaType') or obj.get('contentType') or '')

            if kng_id and name and len(str(kng_id)) > 10:
                # 判断类型
                type_str = str(type_val).lower()
                if any(kw in type_str for kw in ['video', '1', 'mp4', 'stream']):
                    ctype = 'video'
                elif any(kw in type_str for kw in ['doc', '2', 'pdf', 'ppt', 'word']):
                    ctype = 'doc'
                else:
                    ctype = 'unknown'

                courses.append({
                    'kngId': str(kng_id),
                    'name': str(name),
                    'type': ctype,
                })
            # 继续递归搜索
            for v in obj.values():
                if isinstance(v, (dict, list)):
                    search(v, depth+1)

    search(data)
    # 去重
    seen = set()
    unique = []
    for c in courses:
        k = c['kngId']
        if k not in seen:
            seen.add(k)
            unique.append(c)
    return unique


async def extract_courses_from_dom(page) -> list:
    """从 DOM 中提取课程数据（包括 data 属性和 Vue 状态）"""
    return await page.evaluate("""
        () => {
            const results = [];
            const seen = new Set();

            // 方法1: 直接找有 kngId 数据属性的元素
            document.querySelectorAll('[data-kng-id],[data-kngid],[data-id]').forEach(el => {
                const id = el.dataset.kngId || el.dataset.kngid || el.dataset.id;
                if (!id || seen.has(id)) return;
                seen.add(id);
                const name = (
                    el.querySelector('[class*="title"],[class*="name"]')?.innerText ||
                    el.innerText || ''
                ).trim().split('\\n')[0].trim();
                results.push({ kngId: id, name: name || id, type: 'unknown' });
            });

            // 方法2: 找包含课程名称的链接（可能是视频/文档播放页）
            document.querySelectorAll('a[href*="kngId"]').forEach(el => {
                const href = el.href || '';
                const m = href.match(/kngId=([a-f0-9-]+)/i);
                if (!m || seen.has(m[1])) return;
                seen.add(m[1]);
                const type = href.includes('/video/') ? 'video' :
                             href.includes('/doc/')   ? 'doc'   : 'unknown';
                results.push({
                    kngId: m[1],
                    name: (el.innerText||'').trim() || m[1],
                    type,
                    href
                });
            });

            // 方法3: 从 Vue 实例中获取数据（如果可访问）
            try {
                const app = document.querySelector('#app')?.__vue_app__;
                if (app) {
                    // 尝试从 Vuex store 读取
                    // (不同版本结构不同，这里只是尝试)
                }
            } catch(e) {}

            // 方法4: 找所有课程卡片，提取 onclick 或路由信息
            document.querySelectorAll(
                '[class*="kng-item"],[class*="course-item"],[class*="kng-card"],[class*="knowledge"]'
            ).forEach(el => {
                const text = el.innerText?.trim() || '';
                if (!text) return;
                // 尝试从内部链接或属性中找 kngId
                const inner = el.innerHTML || '';
                const m = inner.match(/kngId[=:]["']?([a-f0-9-]{36})/i) ||
                          inner.match(/["']kngId["']\s*:\s*["']([a-f0-9-]{36})/i);
                if (m) {
                    const id = m[1];
                    if (!seen.has(id)) {
                        seen.add(id);
                        const name = text.split('\\n')[0].trim();
                        results.push({ kngId: id, name, type: 'unknown' });
                    }
                }
            });

            return results;
        }
    """)


async def load_all_pages(page, initial_courses: list) -> list:
    """处理分页，加载所有课程（共189个）"""
    all_courses = list(initial_courses)
    log(f"\n  [分页] 当前 {len(all_courses)} 个，尝试加载更多...")

    # 检查是否有"加载更多"按钮或分页
    for attempt in range(30):  # 最多30次翻页
        try:
            # 查找"下一页"或"加载更多"按钮
            next_btn = None
            for sel in [
                "button:has-text('下一页')", ".el-pagination .btn-next:not([disabled])",
                ".pagination .next:not(.disabled)", "[class*='next']:not([disabled])",
                "button:has-text('加载更多')",
            ]:
                try:
                    btn = await page.query_selector(sel)
                    if btn and await btn.is_visible():
                        next_btn = btn
                        break
                except Exception:
                    pass

            if not next_btn:
                log(f"  [分页] 没有更多页面，共 {len(all_courses)} 个课程")
                break

            prev_count = len(all_courses)
            await next_btn.click()
            await page.wait_for_timeout(2000)

            # 获取新增的课程
            new_courses = await extract_courses_from_dom(page)
            added = 0
            seen = {c['kngId'] for c in all_courses}
            for c in new_courses:
                if c['kngId'] not in seen:
                    all_courses.append(c)
                    seen.add(c['kngId'])
                    added += 1

            log(f"  [分页] 第 {attempt+2} 页: 新增 {added} 个")
            if added == 0:
                break

        except Exception as e:
            log(f"  [分页] 异常: {e}")
            break

    return all_courses


# ──────── Step 2: 逐一访问课程页面，捕获真实 URL ────────

async def capture_course_urls(page, context, courses: list) -> list:
    """访问每个课程页面，点击「开始学习」，拦截 m3u8/图片 URL 及 AES-128 密钥"""
    import re as re_mod

    # 断点续传：加载已有的 captures.json
    captured = []
    captured_kng_ids: set[str] = set()
    if CAPTURES_FILE.exists():
        try:
            with open(CAPTURES_FILE, encoding='utf-8') as f:
                captured = json.load(f)
            captured_kng_ids = {c.get('kngId', '') for c in captured}
            log(f"  [续传] 已有 {len(captured)} 条记录，跳过已采集课程")
        except Exception:
            pass

    # 共享状态：记录最近一次 tokenVideoKey 请求的 kid（跨闭包共享）
    state = {'last_kid': ''}

    # ── 方式1: page.route 拦截（被动捕获——若视频播放器请求 key）──
    async def key_route_handler(route, request):
        try:
            response = await route.fetch()
            body = await response.body()
            kid = request.url.split('videoKeyId=')[-1].split('&')[0]
            if kid:
                state['last_kid'] = kid
            log(f"    >> [AES-ROUTE] 响应: {kid[:25]} ({len(body)}B) hex={body[:24].hex()}")
            key_bytes = parse_key_response(body)
            if key_bytes:
                key_path = KEY_DIR / f"{kid}.bin"
                key_path.write_bytes(key_bytes)
                log(f"    >> [AES-ROUTE] 密钥已保存: {kid[:25]} ({len(key_bytes)}B)")
            await route.fulfill(response=response)
        except Exception as e:
            log(f"    >> [AES-ROUTE] 处理失败: {e}")
            try:
                await route.continue_()
            except Exception:
                pass

    await page.route(re_mod.compile(r'tokenVideoKey'), key_route_handler)

    # ── 方式2: page.on('response') 拦截并解析密钥 ──
    async def response_key_interceptor(response):
        try:
            if 'tokenVideoKey' not in response.url:
                return
            body = await response.body()
            kid = response.url.split('videoKeyId=')[-1].split('&')[0]
            log(f"  [AES] tokenVideoKey响应: status={response.status}, "
                f"len={len(body)}, body前50={body[:50]}")

            key_bytes = None
            if len(body) == 16:
                # 直接是原始 16 字节 key
                key_bytes = body
            elif len(body) > 16:
                # 可能是 JSON 包裹的 key
                try:
                    import json as _json
                    data = _json.loads(body)
                    # 尝试常见字段名
                    import base64 as _b64
                    for field in ['key', 'data', 'videoKey', 'encryptKey', 'aesKey']:
                        val = data.get(field)
                        if val:
                            if isinstance(val, str):
                                try:
                                    decoded = _b64.b64decode(val)
                                    if len(decoded) == 16:
                                        key_bytes = decoded
                                        break
                                except Exception:
                                    pass
                            elif isinstance(val, dict):
                                for f2 in ['key', 'encryptKey', 'aesKey']:
                                    v2 = val.get(f2)
                                    if v2 and isinstance(v2, str):
                                        try:
                                            decoded = _b64.b64decode(v2)
                                            if len(decoded) == 16:
                                                key_bytes = decoded
                                                break
                                        except Exception:
                                            pass
                                if key_bytes:
                                    break
                except Exception as je:
                    log(f"  [AES] JSON解析失败: {je}")

            if key_bytes and kid:
                key_path = KEY_DIR / f"{kid}.bin"
                key_path.write_bytes(key_bytes)
                log(f"  [AES] 密钥已捕获: {kid[:30]}... ({len(key_bytes)}字节)")
        except Exception as e:
            log(f"  [AES] response处理失败: {e}")

    page.on('response', response_key_interceptor)

    # ── 方式3: JS注入拦截 fetch 和 crypto.subtle.importKey ──
    await page.add_init_script("""
        (function() {
            // 全局跟踪最近的 tokenVideoKey key ID
            if (typeof window.__yxtKeyId === 'undefined') window.__yxtKeyId = '';

            // 拦截 fetch（记录 key ID，同时尝试直接从响应捕获 16B key）
            const _fetch = window.fetch;
            window.fetch = async function(url, opts) {
                const resp = await _fetch.call(this, url, opts);
                try {
                    const surl = typeof url === 'string' ? url : (url.url || String(url));
                    if (surl.includes('tokenVideoKey')) {
                        const kid = (surl.split('videoKeyId=')[1] || '').split('&')[0];
                        if (kid) window.__yxtKeyId = kid;
                        const clone = resp.clone();
                        clone.arrayBuffer().then(function(buf) {
                            const arr = new Uint8Array(buf);
                            if (arr.length === 16) {
                                const b64 = btoa(String.fromCharCode.apply(null, Array.from(arr)));
                                console.log('__AES_KEY__:' + kid + ':' + b64);
                            }
                        });
                    }
                } catch(e) {}
                return resp;
            };

            // 拦截 crypto.subtle.importKey（捕获 DRM SDK 导入的实际 AES 密钥）
            try {
                const _subtle = window.crypto.subtle;
                const origImportKey = _subtle.importKey.bind(_subtle);
                _subtle.importKey = async function(format, keyData, algorithm, extractable, keyUsages) {
                    try {
                        if (format === 'raw') {
                            let bytes;
                            if (keyData instanceof ArrayBuffer) {
                                bytes = new Uint8Array(keyData);
                            } else if (ArrayBuffer.isView(keyData)) {
                                bytes = new Uint8Array(keyData.buffer, keyData.byteOffset, keyData.byteLength);
                            }
                            if (bytes && bytes.length === 16) {
                                const kid = window.__yxtKeyId || '';
                                const b64 = btoa(String.fromCharCode.apply(null, Array.from(bytes)));
                                console.log('__AES_IMPORT_KEY__:' + kid + ':' + b64);
                            }
                        }
                    } catch(e) {}
                    return origImportKey(format, keyData, algorithm, extractable, keyUsages);
                };
            } catch(e) {}
        })();
    """)

    # ── JS console 消息处理（方式3的接收端）──
    async def handle_console(msg):
        import base64 as _b64
        try:
            text = msg.text
            if text.startswith('__AES_KEY__:') or text.startswith('__AES_IMPORT_KEY__:'):
                is_import = text.startswith('__AES_IMPORT_KEY__:')
                prefix = '__AES_IMPORT_KEY__:' if is_import else '__AES_KEY__:'
                rest = text[len(prefix):]
                colon_pos = rest.find(':')
                if colon_pos < 0:
                    return
                kid = rest[:colon_pos]
                key_b64 = rest[colon_pos + 1:]
                key_bytes = _b64.b64decode(key_b64 + '==')  # 补全 padding
                if len(key_bytes) == 16:
                    src = 'importKey' if is_import else 'fetch'
                    if not kid:
                        kid = state['last_kid']  # Python 侧记录的 kid
                    if kid:
                        key_path = KEY_DIR / f"{kid}.bin"
                        key_path.write_bytes(key_bytes)
                        log(f"  [AES] JS捕获密钥({src}): {kid[:30]}...")
                    else:
                        import time as _t
                        ts = int(_t.time() * 1000) % 1000000
                        key_path = KEY_DIR / f"import_{ts}.bin"
                        key_path.write_bytes(key_bytes)
                        log(f"  [AES] JS捕获密钥({src})(无ID): {key_path.name}")
        except Exception:
            pass

    page.on('console', handle_console)

    browser_closed = False

    def on_browser_disconnected():
        nonlocal browser_closed
        browser_closed = True
        log("\n[!] 浏览器已断开连接")

    context.on('close', on_browser_disconnected)
    for idx, course in enumerate(courses):
        if browser_closed:
            break

        kng_id = course.get('kngId', '')
        name = course.get('name', f'item_{idx+1}')
        ctype = course.get('type', 'unknown')

        if not kng_id:
            continue

        # 测试模式：跳过不在列表中的课程
        if TEST_KNGIDS and kng_id not in TEST_KNGIDS:
            continue

        # 断点续传：跳过已采集的课程
        if kng_id in captured_kng_ids:
            log(f"\n[{idx+1}/{len(courses)}] {name[:55]} [SKIP-已采集]")
            continue

        # API 类型标签往往有误，两种 URL 都尝试
        urls_to_try = [
            f"https://tz.yunxuetang.cn/kng/#/video/play?kngId={kng_id}&projectId=&btid=&gwnlUrl=",
            f"https://tz.yunxuetang.cn/kng/#/doc/play?kngId={kng_id}&projectId=&btid=&gwnlUrl=",
        ]

        log(f"\n[{idx+1}/{len(courses)}] {name[:55]} (api_type={ctype})")

        m3u8_urls: list[str] = []
        img_urls: list[str] = []
        detected_type = ctype

        for visit_url in urls_to_try:
            if m3u8_urls or img_urls:
                break

            def make_handler(m3, img):
                def h(req):
                    u = req.url
                    # 诊断：记录所有 baidubce.com 请求
                    if 'tokenVideoKey' in u:
                        log(f"    >> [KEY_REQ] {u[:120]}")
                    # 拦截 m3u8 及 DRM 追踪 URL（含真实 m3u8）
                    if (('m3u8' in u and ('streamobs' in u or 'yunxuetang' in u))
                            or ('drm.media.baidubce.com' in u and 'sdk-player' in u)):
                        if u not in m3:
                            m3.append(u)
                            log(f"    >> [m3u8] {u[:120]}")
                    elif ('cdn-tce-file' in u and '/100100/' in u
                          and u.split('?')[0].endswith('.jpg')):
                        if u not in img:
                            img.append(u)
                            log(f"    >> [img]  {u[:120]}")
                return h

            h = make_handler(m3u8_urls, img_urls)
            page.on('request', h)

            try:
                await page.goto(visit_url, wait_until="networkidle", timeout=20000)
                await page.wait_for_timeout(2000)

                # 确认实际类型（根据页面 URL 判断，比 API 类型准确）
                curr_url = page.url
                if '/video/play' in curr_url:
                    detected_type = 'video'
                elif '/doc/play' in curr_url:
                    detected_type = 'doc'

                clicked = await click_start_button(page)
                if clicked:
                    log(f"    >> 已点击「开始学习」")
                    if detected_type == 'video':
                        # 等播放器加载，尝试点击 play，再等密钥加载
                        await page.wait_for_timeout(3000)
                        if browser_closed:
                            break
                        await click_video_play(page)
                        log(f"    >> 等待视频和密钥加载(15s)...")
                        # 分段等待：最多15秒，若已有图片且无m3u8则提前退出
                        for _ in range(3):
                            if browser_closed:
                                break
                            await page.wait_for_timeout(5000)
                            # 若已获得图片且无视频流，说明是PDF课程，无需继续等待
                            if img_urls and not m3u8_urls:
                                break
                    else:
                        await page.wait_for_timeout(5000)
                else:
                    log(f"    >> 未找到「开始学习」，等待自动加载...")
                    if detected_type == 'video':
                        for _ in range(3):
                            if browser_closed:
                                break
                            await page.wait_for_timeout(5000)
                            if img_urls and not m3u8_urls:
                                break
                    else:
                        await page.wait_for_timeout(5000)

            except Exception as e:
                err_msg = str(e)
                log(f"    >> 异常: {e}")
                if 'Target page, context or browser has been closed' in err_msg:
                    browser_closed = True
                    break
            finally:
                try:
                    page.remove_listener('request', h)
                except Exception:
                    pass

        # ── 方式2: 主动获取 AES-128 密钥（比被动拦截更可靠）──
        if m3u8_urls and not browser_closed:
            try:
                await fetch_aes_keys(page, context, m3u8_urls)
            except Exception as e:
                err_msg = str(e)
                log(f"    >> [AES] fetch_aes_keys 异常: {e}")
                if 'Target page, context or browser has been closed' in err_msg:
                    browser_closed = True

        # 即使 browser_closed，也保存已采集到的数据（m3u8/img 可能在关闭前已捕获）
        if m3u8_urls or img_urls:
            captured.append({
                'name': name,
                'type': detected_type,
                'kngId': kng_id,
                'm3u8_urls': m3u8_urls,
                'img_urls': img_urls,
            })
            # 增量保存（每个课程采集后立即保存，防止浏览器崩溃丢失进度）
            try:
                with open(CAPTURES_FILE, 'w', encoding='utf-8') as f:
                    json.dump(captured, f, ensure_ascii=False, indent=2)
            except Exception:
                pass
        log(f"    >> 结果: m3u8={len(m3u8_urls)}, img={len(img_urls)}, "
            f"keys={len(list(KEY_DIR.glob('*.bin')))}")

    try:
        await page.unroute(re_mod.compile(r'tokenVideoKey'))
    except Exception:
        pass
    try:
        page.remove_listener('response', response_key_interceptor)
        page.remove_listener('console', handle_console)
    except Exception:
        pass

    if browser_closed:
        log(f"\n[!] 浏览器已关闭，已采集 {len(captured)} 条记录（共 {len(courses)} 课程）")

    return captured


# ──────── 主流程 ────────

async def run():
    from playwright.async_api import async_playwright

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # 检查 Chrome 是否运行（仅警告，脚本使用独立临时 profile 可以并行运行）
    if is_chrome_running():
        log("[!] Chrome 进程已在运行，脚本将使用独立 profile 启动（可忽略此警告）")

    # 如果已有完整捕获记录（非测试模式），检查是否需要继续采集
    if CAPTURES_FILE.exists() and not TEST_KNGIDS:
        with open(CAPTURES_FILE, encoding='utf-8') as f:
            existing_captured = json.load(f)
        # 检查是否所有课程都已采集（对比课程列表 kngId）
        need_more = False
        if COURSE_LIST_FILE.exists():
            try:
                with open(COURSE_LIST_FILE, encoding='utf-8') as f:
                    all_courses = json.load(f)
                captured_ids = {c.get('kngId') for c in existing_captured}
                total_ids = {c.get('kngId') for c in all_courses}
                missing = total_ids - captured_ids
                if missing:
                    log(f"[捕获] 已有 {len(captured_ids)}/{len(total_ids)} 条记录，"
                        f"还需采集 {len(missing)} 条")
                    need_more = True
            except Exception:
                pass
        if not need_more:
            log(f"[捕获] 使用已有记录: {CAPTURES_FILE} ({len(existing_captured)} 条)")
            start_local_key_server()
            await download_all(existing_captured)
            return

    KEY_DIR.mkdir(parents=True, exist_ok=True)

    # 如果已有课程列表，先加载（不需要浏览器）
    courses = []
    if COURSE_LIST_FILE.exists():
        try:
            with open(COURSE_LIST_FILE, encoding='utf-8') as f:
                courses = json.load(f)
            log(f"[课程] 使用已有列表: {len(courses)} 个课程")
        except Exception:
            pass

    # ── 采集阶段：自动重启浏览器直到全部完成 ──
    MAX_BROWSER_RETRIES = 10
    captured = []

    for attempt in range(MAX_BROWSER_RETRIES):
        # 检查是否所有课程都已采集
        if courses and CAPTURES_FILE.exists():
            try:
                with open(CAPTURES_FILE, encoding='utf-8') as f:
                    captured = json.load(f)
                captured_ids = {c.get('kngId') for c in captured}
                total_ids = {c.get('kngId') for c in courses}
                missing = total_ids - captured_ids
                if not missing:
                    log(f"\n[捕获] 全部 {len(captured)} 条已采集完成！")
                    break
                log(f"\n[重试 {attempt+1}/{MAX_BROWSER_RETRIES}] "
                    f"还需采集 {len(missing)}/{len(total_ids)} 条")
            except Exception:
                pass

        temp_profile = copy_chrome_profile()
        try:
            async with async_playwright() as p:
                log(f"\n[Playwright] 启动 Chrome... (第 {attempt+1} 次)")

                try:
                    browser = await p.chromium.launch_persistent_context(
                        user_data_dir=str(temp_profile),
                        channel="chrome",
                        headless=False,
                        args=[
                            "--disable-blink-features=AutomationControlled",
                            "--no-first-run", "--no-default-browser-check",
                            "--disable-sync", "--no-sandbox",
                        ],
                        timeout=60000,
                    )
                except Exception as e:
                    log(f"[!] Chrome 启动失败: {e}")
                    continue

                page = await browser.new_page()

                # 先访问主页，确认登录状态
                log("\n[Auth] 验证登录状态...")
                try:
                    await page.goto("https://tz.yunxuetang.cn",
                                    wait_until="domcontentloaded", timeout=20000)
                    await page.wait_for_timeout(2000)
                    title = await page.title()
                    log(f"  页面标题: {title}")
                except Exception as e:
                    log(f"[!] 主页访问失败: {e}")
                    try:
                        await browser.close()
                    except Exception:
                        pass
                    continue

                # 导出 cookies
                try:
                    all_cookies = await browser.cookies()
                    save_cookies(all_cookies, COOKIES_FILE)
                except Exception:
                    pass

                # Step 1: 获取课程列表（仅首次）
                if not courses:
                    courses = await fetch_course_list(page, browser)
                    log(f"\n[课程] 共 {len(courses)} 个课程")
                    if not courses:
                        log("[!] 获取课程列表失败，退出")
                        await browser.close()
                        return
                    with open(COURSE_LIST_FILE, 'w', encoding='utf-8') as f:
                        json.dump(courses, f, ensure_ascii=False, indent=2)
                    log(f"[课程] 列表保存到: {COURSE_LIST_FILE}")

                # Step 2: 逐一捕获真实 URL（内部增量保存 captures.json）
                try:
                    captured = await capture_course_urls(page, browser, courses)
                except Exception as e:
                    log(f"\n[!] 采集过程异常: {e}")
                    captured = []
                    if CAPTURES_FILE.exists():
                        try:
                            with open(CAPTURES_FILE, encoding='utf-8') as f:
                                captured = json.load(f)
                        except Exception:
                            pass
                    log(f"[!] 已保存 {len(captured)} 条采集记录")

                # 刷新 cookies
                try:
                    fresh = await browser.cookies()
                    save_cookies(fresh, COOKIES_FILE)
                except Exception:
                    pass

                try:
                    await browser.close()
                except Exception:
                    pass

        finally:
            cleanup()

        log(f"[AES] 已捕获 {len(list(KEY_DIR.glob('*.bin')))} 个密钥文件")

        # 浏览器关闭后等待 3 秒再重启
        import asyncio as _aio
        await _aio.sleep(3)
    else:
        log(f"\n[!] 已达到最大重试次数 ({MAX_BROWSER_RETRIES})，停止采集")

    # 加载最终的 captures.json
    if CAPTURES_FILE.exists():
        with open(CAPTURES_FILE, encoding='utf-8') as f:
            captured = json.load(f)
        log(f"\n[捕获] 最终 {len(captured)} 条记录")
    else:
        log("\n[!] 无采集记录")
        return

    # 启动本地 key server 后下载
    start_local_key_server()
    await download_all(captured)


# ──────── 页面辅助 ────────

def is_chrome_running() -> bool:
    try:
        r = subprocess.run(
            ["tasklist", "/FI", "IMAGENAME eq chrome.exe", "/NH"],
            capture_output=True, text=True, timeout=5
        )
        return "chrome.exe" in r.stdout.lower()
    except Exception:
        return False


async def scroll_to_bottom(page):
    prev = 0
    for _ in range(25):
        curr = await page.evaluate("document.body.scrollHeight")
        if curr == prev:
            break
        await page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        await page.wait_for_timeout(800)
        prev = curr
    await page.evaluate("window.scrollTo(0, 0)")


async def click_start_button(page) -> bool:
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


async def click_video_play(page) -> bool:
    """尝试点击视频播放器的 play 按钮（不是页面的「开始学习」按钮）"""
    for sel in [
        ".vjs-big-play-button",
        ".vjs-play-control",
        ".mejs__play",
        "[class*='play-btn']",
        "[class*='play_btn']",
        "[class*='playBtn']",
        "video",
    ]:
        try:
            el = await page.query_selector(sel)
            if el and await el.is_visible():
                await el.click()
                log(f"    >> 已点击播放按钮 ({sel})")
                return True
        except Exception:
            pass
    # JS 直接播放
    try:
        played = await page.evaluate("""
            () => {
                const v = document.querySelector('video');
                if (v) { v.play().catch(()=>{}); return true; }
                return false;
            }
        """)
        if played:
            log(f"    >> 已触发 video.play()")
            return True
    except Exception:
        pass
    return False


async def fetch_aes_keys(page, context, m3u8_urls: list) -> int:
    """主动从 m3u8 manifest 中提取并获取 AES-128 解密密钥"""
    from urllib.parse import urlparse, parse_qs

    # 找直接的 streamobs m3u8 URL
    direct_urls = []
    for u in m3u8_urls:
        if u.startswith('https://streamobs.yunxuetang.cn') and '.m3u8' in u:
            if u not in direct_urls:
                direct_urls.append(u)

    # 从 DRM 追踪 URL 中提取
    if not direct_urls:
        for dmu in m3u8_urls:
            if 'drm.media.baidubce.com' not in dmu:
                continue
            try:
                params = parse_qs(urlparse(dmu).query, keep_blank_values=True)
                for param in ['url', 'videoUrl']:
                    v = (params.get(param) or [None])[0]
                    if v and 'streamobs.yunxuetang.cn' in v and '.m3u8' in v:
                        direct_urls.append(v)
                        break
            except Exception:
                pass
            if direct_urls:
                break

    if not direct_urls:
        log(f"    >> [AES] 无直接 m3u8 URL，跳过密钥获取")
        return 0

    m3u8_url = direct_urls[0]

    # Step 1: 下载 m3u8 manifest
    content = None

    # 方法A: context.request（绕过 CORS，带 cookies）
    try:
        resp = await context.request.get(m3u8_url, headers={
            'Referer': 'https://tz.yunxuetang.cn/',
        })
        if resp.ok:
            content = await resp.text()
            log(f"    >> [AES] m3u8 manifest OK ({len(content)} chars)")
        else:
            log(f"    >> [AES] m3u8 HTTP {resp.status}")
    except Exception as e:
        log(f"    >> [AES] context.request 失败: {e}")

    # 方法B: page.evaluate(fetch)
    if not content:
        try:
            content = await page.evaluate(
                """async (url) => {
                    try {
                        const r = await fetch(url, {credentials:'include'});
                        return r.ok ? await r.text() : null;
                    } catch(e) { return null; }
                }""", m3u8_url)
            if content:
                log(f"    >> [AES] m3u8 manifest OK via page.evaluate ({len(content)} chars)")
        except Exception as e:
            log(f"    >> [AES] page.evaluate m3u8 失败: {e}")

    if not content:
        log(f"    >> [AES] m3u8 manifest 获取失败")
        return 0

    # Step 2: 解析 key URI
    key_matches = re.findall(r'URI="([^"]*videoKeyId=([^"&\s]+)[^"]*)"', content)
    if not key_matches:
        for line in content.split('\n')[:3]:
            log(f"    >> [AES-DBG] {line[:120]}")
        return 0

    # 去重
    seen_kids = set()
    unique_keys = []
    for key_url, kid in key_matches:
        if kid not in seen_kids:
            seen_kids.add(kid)
            unique_keys.append((key_url, kid))
    log(f"    >> [AES] 发现 {len(unique_keys)} 个密钥ID")

    captured_count = 0
    for key_url, kid in unique_keys:
        key_path = KEY_DIR / f"{kid}.bin"
        if key_path.exists():
            log(f"    >> [AES] 密钥已存在: {kid[:25]}")
            captured_count += 1
            continue

        body = None

        # 方法A: context.request
        try:
            key_resp = await context.request.get(key_url)
            if key_resp.ok:
                body = await key_resp.body()
                log(f"    >> [AES] 密钥响应: {len(body)}B via context.request")
            else:
                log(f"    >> [AES] 密钥 HTTP {key_resp.status}")
        except Exception as e:
            log(f"    >> [AES] context.request key 失败: {e}")

        # 方法B: page.evaluate(fetch)
        if not body:
            try:
                body_array = await page.evaluate(
                    """async (url) => {
                        try {
                            const r = await fetch(url, {credentials:'include'});
                            if (!r.ok) return null;
                            const buf = await r.arrayBuffer();
                            return Array.from(new Uint8Array(buf));
                        } catch(e) { return null; }
                    }""", key_url)
                if body_array:
                    body = bytes(body_array)
                    log(f"    >> [AES] 密钥响应: {len(body)}B via page.evaluate")
            except Exception as e:
                log(f"    >> [AES] page.evaluate key 失败: {e}")

        if body and len(body) > 0:
            key_bytes = parse_key_response(body)
            if key_bytes:
                key_path.write_bytes(key_bytes)
                log(f"    >> [AES] 密钥已保存: {kid[:25]} ({len(key_bytes)}B)")
                captured_count += 1
            else:
                log(f"    >> [AES] 密钥响应无法解析: {body[:60]}")
        else:
            log(f"    >> [AES] 密钥获取失败: {kid[:25]}")

    return captured_count


# ──────── 下载 ────────

async def download_all(captured: list):
    log(f"\n{'='*60}\n下载 {len(captured)} 个内容\n{'='*60}")
    ok_v = ok_d = 0
    failed = []

    from urllib.parse import urlparse, parse_qs

    for idx, item in enumerate(captured):
        name = safe_name(item.get('name', f'item_{idx+1}'))
        m3u8s = item.get('m3u8_urls', [])
        imgs = item.get('img_urls', [])

        # ── 步骤1：只保留直接的 streamobs m3u8 URL（排除 DRM 追踪 URL）
        real_m3u8s = [u for u in m3u8s
                      if u.startswith('https://streamobs.yunxuetang.cn')
                      and '.m3u8' in u]

        # ── 步骤2：若无直接 URL 且非图片课程，从 DRM 追踪 URL 的 url= 参数中提取真实 m3u8
        # （图片课程的 m3u8_urls 可能包含上一课程视频播放器的 service worker 请求，需排除）
        if not real_m3u8s and not imgs:
            for dmu in m3u8s:
                if 'drm.media.baidubce.com' not in dmu:
                    continue
                try:
                    params = parse_qs(urlparse(dmu).query, keep_blank_values=True)
                    for param in ['url', 'videoUrl']:
                        v = (params.get(param) or [None])[0]
                        if v and 'streamobs.yunxuetang.cn' in v and '.m3u8' in v:
                            real_m3u8s.append(v)
                            break
                except Exception:
                    pass
                if real_m3u8s:
                    break

        log(f"\n[{idx+1}/{len(captured)}] {name}")

        # 优先下载图片型 PDF（img_urls 有内容 → 该课程是 PDF/图片类型）
        # 视频课程不会加载 cdn-tce-file 的 /100100/ 图片，因此 imgs 有内容即为 PDF
        if imgs:
            log(f"  -> 文档 ({len(imgs)} 页图片)")
            ok = download_doc_to_pdf(imgs[0], OUTPUT_DIR / f"{name}.pdf")
            ok_d += int(ok)
            if not ok:
                failed.append(f"[doc] {name}")
        elif real_m3u8s:
            log(f"  -> 视频 (m3u8={real_m3u8s[0][40:90]}...)")
            ok = download_video(real_m3u8s[0], OUTPUT_DIR / f"{name}.mp4")
            ok_v += int(ok)
            if not ok:
                failed.append(f"[video] {name}")
        else:
            log(f"  [SKIP] 无可用 URL (m3u8={len(m3u8s)}, img={len(imgs)})")
            failed.append(f"[no-url] {name}")

    log(f"\n{'='*60}\n完成: 视频 {ok_v}, 文档 {ok_d}, 失败 {len(failed)}")
    for f in failed:
        log(f"  - {f}")
    log(f"输出: {OUTPUT_DIR}")


def download_video(m3u8_url: str, output_path: Path) -> bool:
    # 跳过已有的完整文件
    for ext in ['.mp4', '.ts', '.mkv']:
        p = output_path.with_suffix(ext)
        if p.exists() and p.stat().st_size > 100_000:
            log(f"  [SKIP] {p.name}")
            return True

    log(f"  下载视频: {output_path.name}")

    # 尝试用本地 key server 修补 m3u8（绕过 DRM key 验证）
    # patched 现在是 http://127.0.0.1:PORT/manifest.m3u8（本地 HTTP URL）
    patched = patch_m3u8_for_local_keys(m3u8_url)

    ffmpeg_exe = get_ffmpeg_exe()
    ffmpeg_args = ["--ffmpeg-location", ffmpeg_exe] if ffmpeg_exe else []
    cookie_args = ["--cookies", str(COOKIES_FILE)] if COOKIES_FILE.exists() else []

    # 尝试的 URL 列表：patched (本地 http) 优先，原始 m3u8 备选
    urls = [patched, m3u8_url] if patched != m3u8_url else [m3u8_url]

    for url_to_try in urls:
        cmd = ([PYTHON_EXE, "-m", "yt_dlp"]
               + cookie_args + ffmpeg_args
               + ["--no-playlist", "--merge-output-format", "mp4",
                  "--concurrent-fragments", "4",
                  "--add-headers", "Referer:https://tz.yunxuetang.cn/",
                  "-o", str(output_path),
                  url_to_try])
        try:
            r = subprocess.run(cmd, capture_output=True, text=True, timeout=7200)
            if r.returncode == 0:
                for ext in ['.mp4', '.ts', '.mkv', '.m4a']:
                    p = output_path.with_suffix(ext)
                    if p.exists() and p.stat().st_size > 100_000:
                        log(f"  [OK] {p.name} ({p.stat().st_size // 1024}KB)")
                        return True
            else:
                stderr = r.stderr or ''
                if len(stderr) > 500:
                    stderr = stderr[:200] + "\n...\n" + stderr[-200:]
                log(f"  [ERR] {stderr}")
        except Exception as e:
            log(f"  [ERR] {e}")

    return False


def download_doc_to_pdf(first_img_url: str, output_pdf: Path) -> bool:
    import requests
    from PIL import Image

    if output_pdf.exists() and output_pdf.stat().st_size > 1000:
        log(f"  [SKIP] {output_pdf.name}")
        return True

    m = re.match(
        r'(https://cdn-tce-file\.yunxuetang\.cn/.+?/\d+/)(\d+)(\.jpg)(\?.*)',
        first_img_url, re.DOTALL
    )
    if not m:
        log("  [ERR] URL 格式无法解析")
        return False

    base, ext, query = m.group(1), m.group(3), m.group(4)
    log(f"  下载文档图片...")

    session = requests.Session()
    session.headers.update({
        'Referer': 'https://tz.yunxuetang.cn/',
        'User-Agent': ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                       'AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36'),
    })
    if COOKIES_FILE.exists():
        with open(COOKIES_FILE, encoding='utf-8', errors='ignore') as f:
            for line in f:
                parts = line.strip().split('\t')
                if len(parts) == 7:
                    domain, _, _, _, _, name, value = parts
                    session.cookies.set(name, value, domain=domain.lstrip('.'))

    images = []
    pg = 1
    while pg <= 500:
        url = f"{base}{pg}{ext}{query}"
        try:
            resp = session.get(url, timeout=30)
            if resp.status_code == 200 and len(resp.content) > 500:
                images.append(Image.open(BytesIO(resp.content)).convert('RGB'))
                print(f"  第{pg}页 OK", end="\r", flush=True)
                pg += 1
            elif resp.status_code in (400, 403, 404):
                log(f"\n  共 {pg - 1} 页")
                break
            else:
                log(f"\n  HTTP {resp.status_code}")
                break
        except Exception as e:
            log(f"\n  第{pg}页: {e}")
            break

    if not images:
        log("  [ERR] 未下载到图片")
        return False

    output_pdf.parent.mkdir(parents=True, exist_ok=True)
    images[0].save(str(output_pdf), save_all=True, append_images=images[1:])
    log(f"  [OK] {output_pdf.name} ({len(images)}页, {output_pdf.stat().st_size//1024}KB)")
    return True


# ──────── 入口 ────────

if __name__ == "__main__":
    asyncio.run(run())
