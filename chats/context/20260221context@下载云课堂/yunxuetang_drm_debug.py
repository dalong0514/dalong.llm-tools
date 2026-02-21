"""
诊断 BaiduBCE DRM 的加密流程：
- 拦截所有 crypto.subtle.importKey / decrypt / encrypt 调用
- 记录 algorithm、key usages、data sizes
- 用于确定正确的解密密钥和模式
"""
# /// script
# requires-python = ">=3.10"
# dependencies = ["playwright"]
# ///

import asyncio
import json
import sys
import tempfile
import shutil
from pathlib import Path

OUTPUT_DIR = Path("C:/Users/dalong0514/Downloads/yunxuetang")
CHROME_USER_DATA = Path("C:/Users/dalong0514/AppData/Local/Google/Chrome/User Data")

# 视频课程 kngId
VIDEO_KNG_ID = "5d7314dd-bb0a-47ad-a1b8-bf45c6575e06"


def copy_chrome_profile() -> Path:
    tmp = Path(tempfile.mkdtemp(prefix="yxt_drm_debug_"))
    items = [
        ("Local State", False),
        ("Default/Network/Cookies", False),
        ("Default/Local Storage/", True),
        ("Default/IndexedDB/", True),
        ("Default/Session Storage/", True),
        ("Default/Preferences", False),
    ]
    for rel, is_dir in items:
        src = CHROME_USER_DATA / rel
        dst = tmp / rel
        try:
            if is_dir and src.is_dir():
                shutil.copytree(src, dst, dirs_exist_ok=True)
            elif src.is_file():
                dst.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(src, dst)
                print(f"  [OK] {rel}")
        except Exception:
            pass
    return tmp


# JS 注入脚本：拦截所有 crypto.subtle 操作
CRYPTO_INTERCEPT_JS = """
(function() {
    if (window.__drmDebugInit) return;
    window.__drmDebugInit = true;
    window.__drmOps = [];  // 记录所有操作

    function toHex(buf) {
        const arr = new Uint8Array(buf instanceof ArrayBuffer ? buf : buf.buffer || buf);
        return Array.from(arr.slice(0, 32)).map(b => b.toString(16).padStart(2, '0')).join('');
    }

    function toB64(buf) {
        const arr = new Uint8Array(buf instanceof ArrayBuffer ? buf : buf.buffer || buf);
        return btoa(String.fromCharCode.apply(null, Array.from(arr)));
    }

    try {
        const _subtle = crypto.subtle;

        // 拦截 importKey
        const origImportKey = _subtle.importKey.bind(_subtle);
        _subtle.importKey = async function(format, keyData, algorithm, extractable, keyUsages) {
            const result = await origImportKey(format, keyData, algorithm, extractable, keyUsages);
            try {
                let dataHex = '', dataLen = 0, dataB64 = '';
                if (format === 'raw' && keyData) {
                    const arr = new Uint8Array(keyData instanceof ArrayBuffer ? keyData : keyData.buffer);
                    dataLen = arr.length;
                    dataHex = toHex(arr);
                    dataB64 = toB64(arr);
                }
                const op = {
                    type: 'importKey',
                    format: format,
                    algorithm: typeof algorithm === 'string' ? algorithm : JSON.parse(JSON.stringify(algorithm)),
                    extractable: extractable,
                    keyUsages: Array.from(keyUsages),
                    dataLen: dataLen,
                    dataHex: dataHex,
                    dataB64: dataB64,
                    timestamp: Date.now()
                };
                window.__drmOps.push(op);
                console.log('__DRM_OP__:' + JSON.stringify(op));
            } catch(e) {}
            return result;
        };

        // 拦截 decrypt
        const origDecrypt = _subtle.decrypt.bind(_subtle);
        _subtle.decrypt = async function(algorithm, key, data) {
            const result = await origDecrypt(algorithm, key, data);
            try {
                const dataArr = new Uint8Array(data instanceof ArrayBuffer ? data : data.buffer);
                const resultArr = new Uint8Array(result);
                const algoInfo = typeof algorithm === 'string' ? {name: algorithm} : JSON.parse(JSON.stringify(algorithm));
                // 对于 IV，转换为 hex
                if (algorithm.iv) {
                    algoInfo.iv_hex = toHex(algorithm.iv);
                }
                if (algorithm.counter) {
                    algoInfo.counter_hex = toHex(algorithm.counter);
                }
                const op = {
                    type: 'decrypt',
                    algorithm: algoInfo,
                    inputLen: dataArr.length,
                    outputLen: resultArr.length,
                    inputHex: toHex(dataArr),
                    outputHex: toHex(resultArr),
                    timestamp: Date.now()
                };
                window.__drmOps.push(op);
                console.log('__DRM_OP__:' + JSON.stringify(op));
            } catch(e) {
                console.log('__DRM_OP_ERR__:decrypt:' + e.message);
            }
            return result;
        };

        // 拦截 encrypt
        const origEncrypt = _subtle.encrypt.bind(_subtle);
        _subtle.encrypt = async function(algorithm, key, data) {
            const result = await origEncrypt(algorithm, key, data);
            try {
                const op = {
                    type: 'encrypt',
                    algorithm: typeof algorithm === 'string' ? {name: algorithm} : JSON.parse(JSON.stringify(algorithm)),
                    inputLen: new Uint8Array(data instanceof ArrayBuffer ? data : data.buffer).length,
                    outputLen: new Uint8Array(result).length,
                    timestamp: Date.now()
                };
                window.__drmOps.push(op);
                console.log('__DRM_OP__:' + JSON.stringify(op));
            } catch(e) {}
            return result;
        };

        console.log('__DRM_DEBUG__:crypto.subtle intercepted');
    } catch(e) {
        console.log('__DRM_DEBUG_ERR__:' + e.message);
    }

    // 拦截 fetch（记录 tokenVideoKey 响应）
    const _fetch = window.fetch;
    window.fetch = async function(url, opts) {
        const resp = await _fetch.call(this, url, opts);
        try {
            const surl = typeof url === 'string' ? url : (url.url || String(url));
            if (surl.includes('tokenVideoKey')) {
                const clone = resp.clone();
                clone.text().then(function(txt) {
                    console.log('__DRM_TOKEN__:' + txt);
                });
            }
        } catch(e) {}
        return resp;
    };
})();
"""


async def run():
    from playwright.async_api import async_playwright

    print("[1] 复制 Chrome profile...")
    temp_profile = copy_chrome_profile()

    drm_ops = []

    try:
        async with async_playwright() as p:
            print("[2] 启动 Chrome...")
            browser = await p.chromium.launch_persistent_context(
                user_data_dir=str(temp_profile),
                channel="chrome",
                headless=False,
                args=[
                    "--disable-blink-features=AutomationControlled",
                    "--no-first-run", "--no-default-browser-check",
                    "--disable-sync", "--no-sandbox",
                ],
                timeout=30000,
            )
            page = await browser.new_page()

            # 注入 crypto 拦截
            await page.add_init_script(CRYPTO_INTERCEPT_JS)

            def handle_console(msg):
                text = msg.text
                if text.startswith('__DRM_OP__:'):
                    try:
                        op = json.loads(text[len('__DRM_OP__:'):])
                        drm_ops.append(op)
                        op_type = op.get('type', '?')
                        if op_type == 'importKey':
                            print(f"  [importKey] format={op.get('format')} "
                                  f"algo={op.get('algorithm')} "
                                  f"usages={op.get('keyUsages')} "
                                  f"len={op.get('dataLen')} "
                                  f"hex={op.get('dataHex', '')[:64]}")
                        elif op_type == 'decrypt':
                            algo = op.get('algorithm', {})
                            print(f"  [decrypt] algo={algo.get('name')} "
                                  f"iv={algo.get('iv_hex', 'N/A')[:32]} "
                                  f"input={op.get('inputLen')}B "
                                  f"output={op.get('outputLen')}B "
                                  f"out_hex={op.get('outputHex', '')[:32]}...")
                        elif op_type == 'encrypt':
                            print(f"  [encrypt] algo={op.get('algorithm')} "
                                  f"input={op.get('inputLen')}B")
                    except Exception as e:
                        print(f"  [parse error] {e}")
                elif text.startswith('__DRM_TOKEN__:'):
                    token = text[len('__DRM_TOKEN__:'):]
                    print(f"  [TOKEN] {token[:200]}")
                elif text.startswith('__DRM_DEBUG'):
                    print(f"  [DEBUG] {text}")

            page.on('console', handle_console)

            # 导航到视频课程
            video_url = (f"https://tz.yunxuetang.cn/kng/#/video/play"
                         f"?kngId={VIDEO_KNG_ID}&projectId=&btid=&gwnlUrl=")
            print(f"[3] 打开视频: {video_url[:80]}...")
            await page.goto(video_url, wait_until="networkidle", timeout=20000)
            await page.wait_for_timeout(2000)

            # 点击「开始学习」
            for sel in [
                'button:has-text("开始学习")',
                '.start-btn',
                'text=开始学习',
                '[class*="start"]',
            ]:
                try:
                    btn = page.locator(sel).first
                    if await btn.is_visible(timeout=1000):
                        await btn.click()
                        print(f"  [OK] 点击: {sel}")
                        break
                except Exception:
                    pass

            await page.wait_for_timeout(3000)

            # 尝试点击播放
            for sel in [
                'video',
                '.vjs-big-play-button',
                '.play-btn',
                '[class*="play"]',
            ]:
                try:
                    el = page.locator(sel).first
                    if await el.is_visible(timeout=1000):
                        await el.click()
                        print(f"  [OK] 点击播放: {sel}")
                        break
                except Exception:
                    pass

            # 等待 DRM 操作
            print("[4] 等待 DRM 操作 (20s)...")
            await page.wait_for_timeout(20000)

            # 从页面收集所有 ops
            try:
                page_ops = await page.evaluate("window.__drmOps || []")
                if page_ops:
                    for op in page_ops:
                        if op not in drm_ops:
                            drm_ops.append(op)
            except Exception:
                pass

            await browser.close()

    finally:
        try:
            shutil.rmtree(temp_profile, ignore_errors=True)
        except Exception:
            pass

    # 输出汇总
    print(f"\n{'='*60}")
    print(f"DRM 操作汇总: {len(drm_ops)} 个操作")
    print(f"{'='*60}")

    import_keys = [op for op in drm_ops if op.get('type') == 'importKey']
    decrypts = [op for op in drm_ops if op.get('type') == 'decrypt']
    encrypts = [op for op in drm_ops if op.get('type') == 'encrypt']

    print(f"\nimportKey: {len(import_keys)} 次")
    for i, op in enumerate(import_keys):
        print(f"  #{i+1}: format={op.get('format')} "
              f"algo={op.get('algorithm')} "
              f"usages={op.get('keyUsages')} "
              f"len={op.get('dataLen')} "
              f"hex={op.get('dataHex', '')}")

    print(f"\ndecrypt: {len(decrypts)} 次")
    for i, op in enumerate(decrypts[:5]):  # 只显示前5个
        algo = op.get('algorithm', {})
        print(f"  #{i+1}: algo={algo.get('name')} "
              f"iv={algo.get('iv_hex', 'N/A')} "
              f"input={op.get('inputLen')}B "
              f"output={op.get('outputLen')}B")

    print(f"\nencrypt: {len(encrypts)} 次")

    # 保存完整日志
    log_path = OUTPUT_DIR / "drm_debug.json"
    with open(log_path, 'w', encoding='utf-8') as f:
        json.dump(drm_ops, f, ensure_ascii=False, indent=2)
    print(f"\n完整日志: {log_path}")


if __name__ == "__main__":
    asyncio.run(run())
