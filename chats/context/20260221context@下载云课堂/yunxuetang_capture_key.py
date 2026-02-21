#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = [
#   "playwright>=1.40.0",
# ]
# ///
"""
yunxuetang_capture_key.py - 捕获云学堂视频 DRM 的真实 AES-128 解密密钥

通过 Playwright 打开视频页面, 注入 JS 拦截 crypto.subtle.importKey/decrypt,
捕获浏览器实际使用的解密密钥。
"""

import asyncio
import json
import shutil
import tempfile
from pathlib import Path

# ──────── 配置 ────────
OUTPUT_DIR = Path("C:/Users/dalong0514/Downloads/yunxuetang")
KEY_DIR = OUTPUT_DIR / "keys"
CHROME_USER_DATA = Path("C:/Users/dalong0514/AppData/Local/Google/Chrome/User Data")


def log(msg: str):
    try:
        print(msg, flush=True)
    except UnicodeEncodeError:
        print(msg.encode('utf-8', errors='replace').decode('utf-8'), flush=True)


def copy_chrome_profile() -> Path:
    log("[Profile] 复制关键文件...")
    tmp = Path(tempfile.mkdtemp(prefix="yxt_key_"))
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
        except Exception:
            pass
    return tmp


# 全面拦截 JS - 在页面任何脚本加载前注入
INTERCEPT_SCRIPT = """
(function() {
    // 全局存储
    window.__yxt_keys = [];
    window.__yxt_key_id = '';

    // 1. 拦截 fetch - 记录 tokenVideoKey 请求的 kid
    const origFetch = window.fetch;
    window.fetch = async function(...args) {
        const url = typeof args[0] === 'string' ? args[0] : (args[0]?.url || '');
        const resp = await origFetch.apply(this, args);
        try {
            if (url.includes('tokenVideoKey')) {
                const kid = (url.split('videoKeyId=')[1] || '').split('&')[0];
                if (kid) window.__yxt_key_id = kid;
                console.log('__YXT_KEY_REQ__:' + kid);
            }
        } catch(e) {}
        return resp;
    };

    // 2. 拦截 XMLHttpRequest
    const origXHROpen = XMLHttpRequest.prototype.open;
    XMLHttpRequest.prototype.open = function(method, url, ...rest) {
        try {
            if (typeof url === 'string' && url.includes('tokenVideoKey')) {
                const kid = (url.split('videoKeyId=')[1] || '').split('&')[0];
                if (kid) window.__yxt_key_id = kid;
                console.log('__YXT_KEY_REQ__:' + kid);
            }
        } catch(e) {}
        return origXHROpen.call(this, method, url, ...rest);
    };

    // 3. 拦截 crypto.subtle.importKey - 捕获导入的原始密钥
    try {
        const subtle = window.crypto.subtle;
        const origImportKey = subtle.importKey.bind(subtle);
        subtle.importKey = async function(format, keyData, algo, extractable, usages) {
            try {
                if (format === 'raw') {
                    let bytes;
                    if (keyData instanceof ArrayBuffer) {
                        bytes = new Uint8Array(keyData);
                    } else if (ArrayBuffer.isView(keyData)) {
                        bytes = new Uint8Array(keyData.buffer, keyData.byteOffset, keyData.byteLength);
                    }
                    if (bytes && (bytes.length === 16 || bytes.length === 32)) {
                        const hex = Array.from(bytes).map(b => b.toString(16).padStart(2, '0')).join('');
                        const kid = window.__yxt_key_id || 'unknown';
                        const algoName = typeof algo === 'string' ? algo : (algo?.name || 'unknown');
                        console.log('__YXT_IMPORT_KEY__:' + kid + ':' + hex + ':' + algoName + ':' + bytes.length);
                        window.__yxt_keys.push({kid, hex, algo: algoName, len: bytes.length, source: 'importKey'});
                    }
                }
            } catch(e) {
                console.log('__YXT_ERR__:importKey:' + e.message);
            }
            return origImportKey(format, keyData, algo, extractable, usages);
        };

        // 4. 拦截 crypto.subtle.decrypt
        const origDecrypt = subtle.decrypt.bind(subtle);
        subtle.decrypt = async function(algo, key, data) {
            try {
                const algoName = typeof algo === 'string' ? algo : (algo?.name || 'unknown');
                let ivHex = '';
                if (algo?.iv) {
                    const ivBytes = new Uint8Array(
                        algo.iv instanceof ArrayBuffer ? algo.iv :
                        ArrayBuffer.isView(algo.iv) ?
                            algo.iv.buffer.slice(algo.iv.byteOffset, algo.iv.byteOffset + algo.iv.byteLength) :
                            new ArrayBuffer(0)
                    );
                    ivHex = Array.from(ivBytes).map(b => b.toString(16).padStart(2, '0')).join('');
                }
                console.log('__YXT_DECRYPT__:' + algoName + ':iv=' + ivHex + ':dataLen=' + (data?.byteLength || 0));
            } catch(e) {}
            return origDecrypt(algo, key, data);
        };
    } catch(e) {
        console.log('__YXT_ERR__:subtle_hook:' + e.message);
    }

    // 5. 监控 WebAssembly.instantiate（Baidu DRM 可能用 WASM）
    try {
        const origWasmInstantiate = WebAssembly.instantiate;
        WebAssembly.instantiate = function(...args) {
            console.log('__YXT_WASM__:instantiate');
            return origWasmInstantiate.apply(this, args);
        };
        const origWasmInstantiateStreaming = WebAssembly.instantiateStreaming;
        if (origWasmInstantiateStreaming) {
            WebAssembly.instantiateStreaming = function(...args) {
                console.log('__YXT_WASM__:instantiateStreaming');
                return origWasmInstantiateStreaming.apply(this, args);
            };
        }
    } catch(e) {}

    console.log('__YXT_HOOK_READY__');
})();
"""


async def capture_video_key(kng_id: str):
    from playwright.async_api import async_playwright

    KEY_DIR.mkdir(parents=True, exist_ok=True)
    video_url = (f"https://tz.yunxuetang.cn/kng/#/video/play"
                 f"?kngId={kng_id}&projectId=&btid=&gwnlUrl=")

    captured_keys: list[dict] = []

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
                    "--autoplay-policy=no-user-gesture-required",
                ],
                timeout=60000,
            )

            page = await browser.new_page()

            # 注入拦截脚本（在所有页面 JS 之前）
            await page.add_init_script(INTERCEPT_SCRIPT)

            # 监听 console 消息
            def on_console(msg):
                text = msg.text
                if text.startswith('__YXT_'):
                    log(f"  [JS] {text[:120]}")

                    if text.startswith('__YXT_IMPORT_KEY__:'):
                        parts = text[len('__YXT_IMPORT_KEY__:'):].split(':')
                        if len(parts) >= 3:
                            kid, key_hex, algo = parts[0], parts[1], parts[2]
                            key_len = int(parts[3]) if len(parts) > 3 else len(key_hex) // 2
                            entry = {'kid': kid, 'hex': key_hex, 'algo': algo, 'len': key_len}
                            captured_keys.append(entry)
                            # Save key immediately
                            key_bytes = bytes.fromhex(key_hex)
                            fname = f"real_{kid}.bin" if kid != 'unknown' else f"real_unknown_{len(captured_keys)}.bin"
                            (KEY_DIR / fname).write_bytes(key_bytes)
                            log(f"  [KEY] 保存密钥: {fname} ({key_len}B, algo={algo})")

            page.on('console', on_console)

            # 也拦截 DRM key 网络请求
            m3u8_urls: list[str] = []

            def on_request(req):
                u = req.url
                if 'tokenVideoKey' in u:
                    log(f"  [NET] tokenVideoKey: {u[:100]}")
                elif 'm3u8' in u and 'streamobs' in u:
                    if u not in m3u8_urls:
                        m3u8_urls.append(u)
                        log(f"  [NET] m3u8: {u[:100]}")

            page.on('request', on_request)

            # 打开视频页面
            log(f"\n[Page] 打开视频页面...")
            try:
                await page.goto(video_url, wait_until="networkidle", timeout=30000)
            except Exception:
                pass
            await page.wait_for_timeout(3000)

            # 点击「开始学习」
            for sel in [
                "button:has-text('开始学习')", "a:has-text('开始学习')",
                "button:has-text('继续学习')", "button:has-text('立即学习')",
            ]:
                try:
                    btn = await page.wait_for_selector(sel, timeout=2000)
                    if btn and await btn.is_visible():
                        await btn.click()
                        log("  已点击「开始学习」")
                        break
                except Exception:
                    pass

            await page.wait_for_timeout(3000)

            # 点击视频播放按钮
            for sel in [".vjs-big-play-button", ".vjs-play-control",
                        "[class*='play-btn']", "[class*='play_btn']", "video"]:
                try:
                    el = await page.query_selector(sel)
                    if el and await el.is_visible():
                        await el.click()
                        log(f"  已点击播放按钮 ({sel})")
                        break
                except Exception:
                    pass

            # JS 直接播放
            try:
                await page.evaluate("""
                    () => {
                        const v = document.querySelector('video');
                        if (v) { v.play().catch(()=>{}); return true; }
                        return false;
                    }
                """)
            except Exception:
                pass

            # 等待密钥捕获
            log("\n[等待] 等待 DRM 密钥捕获 (最长 30 秒)...")
            for i in range(30):
                await page.wait_for_timeout(1000)
                if captured_keys:
                    log(f"  已捕获 {len(captured_keys)} 个密钥!")
                    # 等更多密钥
                    await page.wait_for_timeout(3000)
                    break
                if i % 5 == 4:
                    log(f"  等待中... ({i+1}s)")

            if not captured_keys:
                log("\n[!] 30秒内未捕获到任何密钥")
                log("  尝试从页面获取更多信息...")
                keys_from_page = await page.evaluate("""
                    () => window.__yxt_keys || []
                """)
                if keys_from_page:
                    log(f"  从 window.__yxt_keys 获取到 {len(keys_from_page)} 个密钥")
                    captured_keys.extend(keys_from_page)

            # 保存截图
            await page.screenshot(path=str(OUTPUT_DIR / "debug_video_page.png"))

            page.remove_listener('request', on_request)
            page.remove_listener('console', on_console)
            await browser.close()

    finally:
        shutil.rmtree(temp_profile, ignore_errors=True)

    log(f"\n[结果] 捕获 {len(captured_keys)} 个密钥")
    for k in captured_keys:
        log(f"  kid={k.get('kid','?')} hex={k.get('hex','?')[:32]}... "
            f"algo={k.get('algo','?')} len={k.get('len','?')}")

    return captured_keys


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--kng-id", required=True)
    args = parser.parse_args()
    asyncio.run(capture_video_key(args.kng_id))
