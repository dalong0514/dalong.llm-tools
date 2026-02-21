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
yunxuetang_doc_download.py - 从云学堂下载文档（通过浏览器滚动捕获所有页面图片URL）

用法:
  python scripts/yunxuetang_doc_download.py --kng-id <kngId> [--name <课程名>]

需要先关闭所有 Chrome 窗口。
"""

import asyncio
import json
import re
import shutil
import sys
import tempfile
from io import BytesIO
from pathlib import Path

import requests
from PIL import Image

# ──────── 配置 ────────
OUTPUT_DIR = Path("C:/Users/dalong0514/Downloads/yunxuetang")
CHROME_USER_DATA = Path("C:/Users/dalong0514/AppData/Local/Google/Chrome/User Data")


def safe_name(s: str) -> str:
    s = s.strip()
    s = re.sub(r'[<>:"/\\|?*\n\r\t]', '_', s)
    return re.sub(r'_+', '_', s)[:80] or "unnamed"


def log(msg: str):
    try:
        print(msg, flush=True)
    except UnicodeEncodeError:
        print(msg.encode('utf-8', errors='replace').decode('utf-8'), flush=True)


def copy_chrome_profile() -> Path:
    log("[Profile] 复制关键文件到临时目录...")
    tmp = Path(tempfile.mkdtemp(prefix="yxt_doc_"))
    for item, is_dir in [
        ("Local State", False),
        ("Default/Network/Cookies", False),
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
            elif not is_dir and src.is_file():
                shutil.copy2(src, dst)
        except Exception as e:
            log(f"  [WARN] {item}: {e}")
    return tmp


async def capture_doc_images(kng_id: str, course_name: str = ""):
    """打开文档页面，滚动捕获所有页面图片 URL，下载后合成 PDF"""
    from playwright.async_api import async_playwright

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    doc_url = (f"https://tz.yunxuetang.cn/kng/#/doc/play"
               f"?kngId={kng_id}&projectId=&btid=&gwnlUrl=")
    # 同时尝试 video URL（有些文档类型在 video 路径下）
    video_url = (f"https://tz.yunxuetang.cn/kng/#/video/play"
                 f"?kngId={kng_id}&projectId=&btid=&gwnlUrl=")

    img_urls: list[str] = []
    img_set: set[str] = set()  # 去重

    def make_request_handler():
        def h(req):
            u = req.url
            if ('cdn-tce-file' in u and '/100100/' in u
                    and u.split('?')[0].endswith('.jpg')):
                # 只保留第一次出现的每个页面 URL（相同基础路径）
                base = u.split('?')[0]
                if base not in img_set:
                    img_set.add(base)
                    img_urls.append(u)
        return h

    temp_profile = copy_chrome_profile()
    try:
        async with async_playwright() as p:
            log("[Playwright] 启动 Chrome...")
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

            page = await browser.new_page()
            handler = make_request_handler()
            page.on('request', handler)

            # 尝试文档页面
            log(f"[Page] 打开文档页面: {doc_url[:80]}...")
            try:
                await page.goto(doc_url, wait_until="networkidle", timeout=30000)
            except Exception:
                pass
            await page.wait_for_timeout(3000)

            # 检查是否需要点击「开始学习」
            for sel in [
                "button:has-text('开始学习')", "a:has-text('开始学习')",
                "button:has-text('继续学习')", "button:has-text('立即学习')",
                ".start-btn", "[class*='start-study']",
            ]:
                try:
                    btn = await page.wait_for_selector(sel, timeout=2000)
                    if btn and await btn.is_visible():
                        await btn.click()
                        log("  已点击「开始学习」")
                        await page.wait_for_timeout(3000)
                        break
                except Exception:
                    pass

            # 如果没有图片，尝试 video URL（有些课程类型不匹配）
            if not img_urls:
                log(f"[Page] 文档路径无图片，尝试视频路径...")
                try:
                    await page.goto(video_url, wait_until="networkidle", timeout=30000)
                except Exception:
                    pass
                await page.wait_for_timeout(3000)
                for sel in [
                    "button:has-text('开始学习')", "a:has-text('开始学习')",
                    "button:has-text('继续学习')",
                ]:
                    try:
                        btn = await page.wait_for_selector(sel, timeout=2000)
                        if btn and await btn.is_visible():
                            await btn.click()
                            log("  已点击「开始学习」")
                            await page.wait_for_timeout(3000)
                            break
                    except Exception:
                        pass

            log(f"  初始加载: {len(img_urls)} 页")

            # 获取页面标题
            if not course_name:
                try:
                    title = await page.title()
                    course_name = title.strip() or f"doc_{kng_id[:8]}"
                except Exception:
                    course_name = f"doc_{kng_id[:8]}"

            # ── 关键步骤：滚动文档容器以加载所有页面 ──
            log("[Scroll] 开始滚动加载全部页面...")

            # 尝试多种文档容器选择器
            scroll_selectors = [
                ".doc-preview-container",
                ".doc-content",
                "[class*='doc-preview']",
                "[class*='doc-container']",
                "[class*='preview-content']",
                "[class*='kng-doc']",
                ".main-content",
                "#content",
                ".el-main",
            ]

            scroll_target = None
            for sel in scroll_selectors:
                try:
                    el = await page.query_selector(sel)
                    if el:
                        box = await el.bounding_box()
                        if box and box['height'] > 100:
                            scroll_target = sel
                            log(f"  找到文档容器: {sel}")
                            break
                except Exception:
                    pass

            # 滚动策略：在文档容器或整个页面内逐步滚动
            prev_count = len(img_urls)
            max_no_new = 5  # 连续 N 次无新图片则停止
            no_new_count = 0

            for scroll_step in range(200):  # 最多滚动 200 次
                if scroll_target:
                    await page.evaluate(f"""
                        (step) => {{
                            const el = document.querySelector('{scroll_target}');
                            if (el) el.scrollTop = step * 800;
                        }}
                    """, scroll_step)
                else:
                    await page.evaluate(
                        "(step) => window.scrollTo(0, step * 800)",
                        scroll_step
                    )

                await page.wait_for_timeout(500)

                current_count = len(img_urls)
                if current_count > prev_count:
                    log(f"  滚动 {scroll_step}: 已加载 {current_count} 页")
                    prev_count = current_count
                    no_new_count = 0
                else:
                    no_new_count += 1
                    if no_new_count >= max_no_new:
                        log(f"  连续 {max_no_new} 次无新页面，停止滚动")
                        break

            # 额外等待一下确保最后的图片也加载了
            await page.wait_for_timeout(2000)
            log(f"\n[结果] 共捕获 {len(img_urls)} 页图片 URL")

            page.remove_listener('request', handler)
            await browser.close()

    finally:
        shutil.rmtree(temp_profile, ignore_errors=True)

    if not img_urls:
        log("[ERR] 未捕获到任何图片 URL")
        return False

    # ── 按页码排序 ──
    def page_num(url):
        m = re.search(r'/(\d+)\.jpg', url)
        return int(m.group(1)) if m else 0

    img_urls.sort(key=page_num)

    # ── 下载图片 ──
    log(f"\n[下载] 开始下载 {len(img_urls)} 页...")
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
                pg = page_num(url)
                print(f"  Page {pg} OK ({len(resp.content)//1024}KB)",
                      end="\r", flush=True)
            else:
                log(f"\n  Page {i+1} HTTP {resp.status_code}")
        except Exception as e:
            log(f"\n  Page {i+1} ERROR: {e}")

    if not images:
        log("\n[ERR] 未下载到任何图片")
        return False

    # ── 合成 PDF ──
    fname = safe_name(course_name)
    output_pdf = OUTPUT_DIR / f"{fname}.pdf"
    images[0].save(str(output_pdf), save_all=True, append_images=images[1:])
    log(f"\n[OK] {output_pdf.name} ({len(images)} 页, "
        f"{output_pdf.stat().st_size // 1024}KB)")
    return True


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--kng-id", required=True)
    parser.add_argument("--name", default="")
    args = parser.parse_args()
    asyncio.run(capture_doc_images(args.kng_id, args.name))
