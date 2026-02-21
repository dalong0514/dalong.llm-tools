#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = [
#   "playwright>=1.40.0",
# ]
# ///
"""
yunxuetang_video_capture.py - 捕获云学堂 DRM 视频的解密数据

策略: 拦截 SourceBuffer.appendBuffer() 和 MediaSource,
捕获 DRM SDK 解密后输入到 video 元素的原始媒体数据。
如果 SourceBuffer 方式失败, 使用 MediaRecorder 录制视频。
"""

import asyncio
import base64
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

# ──────── 配置 ────────
OUTPUT_DIR = Path("C:/Users/dalong0514/Downloads/yunxuetang")
CHROME_USER_DATA = Path("C:/Users/dalong0514/AppData/Local/Google/Chrome/User Data")


def log(msg: str):
    try:
        print(msg, flush=True)
    except UnicodeEncodeError:
        print(msg.encode('utf-8', errors='replace').decode('utf-8'), flush=True)


def copy_chrome_profile() -> Path:
    tmp = Path(tempfile.mkdtemp(prefix="yxt_cap_"))
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


# MediaRecorder 方式 - 在浏览器中录制 video 元素
RECORDER_SCRIPT = """
(function() {
    window.__yxt_recorder_chunks = [];
    window.__yxt_recorder = null;
    window.__yxt_recording_done = false;

    // Hook SourceBuffer.appendBuffer 来检测解密后的数据
    window.__yxt_sb_data = [];
    const origAppend = SourceBuffer.prototype.appendBuffer;
    SourceBuffer.prototype.appendBuffer = function(data) {
        try {
            const bytes = data instanceof ArrayBuffer ? new Uint8Array(data) :
                          ArrayBuffer.isView(data) ? new Uint8Array(data.buffer, data.byteOffset, data.byteLength) :
                          null;
            if (bytes) {
                // 检查是否包含 TS sync byte (0x47)
                const hasSync = bytes[0] === 0x47;
                console.log('__YXT_SB__:appendBuffer:' + bytes.length + ':sync=' + hasSync);
                // 不存储全部数据(太大), 只存前几个用于验证
                if (window.__yxt_sb_data.length < 3) {
                    // 存base64前100字节用于调试
                    const sample = Array.from(bytes.slice(0, 100)).map(b => b.toString(16).padStart(2, '0')).join('');
                    window.__yxt_sb_data.push({len: bytes.length, sync: hasSync, sample});
                }
            }
        } catch(e) {}
        return origAppend.call(this, data);
    };

    console.log('__YXT_RECORDER_READY__');
})();
"""

START_RECORDING_SCRIPT = """
async () => {
    const video = document.querySelector('video');
    if (!video) return { error: 'no video element' };

    try {
        // 等待视频有数据
        if (video.readyState < 2) {
            await new Promise((resolve, reject) => {
                const timeout = setTimeout(() => reject('timeout'), 15000);
                video.addEventListener('loadeddata', () => { clearTimeout(timeout); resolve(); }, { once: true });
            });
        }

        const duration = video.duration;
        const width = video.videoWidth;
        const height = video.videoHeight;

        // 使用 captureStream 获取视频流
        let stream;
        try {
            stream = video.captureStream();
        } catch(e) {
            // DRM 可能阻止 captureStream, 尝试 mozCaptureStream
            try {
                stream = video.mozCaptureStream();
            } catch(e2) {
                return { error: 'captureStream blocked by DRM: ' + e.message };
            }
        }

        // 创建 MediaRecorder
        const mimeType = MediaRecorder.isTypeSupported('video/webm;codecs=vp9,opus')
            ? 'video/webm;codecs=vp9,opus'
            : MediaRecorder.isTypeSupported('video/webm;codecs=vp8,opus')
            ? 'video/webm;codecs=vp8,opus'
            : 'video/webm';

        const recorder = new MediaRecorder(stream, { mimeType, videoBitsPerSecond: 4000000 });
        window.__yxt_recorder_chunks = [];
        window.__yxt_recording_done = false;

        recorder.ondataavailable = (e) => {
            if (e.data.size > 0) {
                window.__yxt_recorder_chunks.push(e.data);
            }
        };

        recorder.onstop = () => {
            window.__yxt_recording_done = true;
            console.log('__YXT_RECORDING_DONE__:' + window.__yxt_recorder_chunks.length + ' chunks');
        };

        window.__yxt_recorder = recorder;

        // 从头播放 (1x 正常速度, 保证音画质量)
        video.currentTime = 0;
        video.playbackRate = 1;
        await video.play();

        recorder.start(1000);  // 每秒收集一次数据

        return {
            duration: duration,
            width: width,
            height: height,
            mimeType: mimeType,
            playbackRate: 1,
            estimatedTime: Math.ceil(duration)
        };
    } catch(e) {
        return { error: e.message };
    }
}
"""

COLLECT_RECORDING_SCRIPT = """
async () => {
    const recorder = window.__yxt_recorder;
    if (recorder && recorder.state === 'recording') {
        recorder.stop();
        // 等待 onstop 事件
        await new Promise(resolve => {
            const check = setInterval(() => {
                if (window.__yxt_recording_done) {
                    clearInterval(check);
                    resolve();
                }
            }, 100);
            setTimeout(() => { clearInterval(check); resolve(); }, 5000);
        });
    }

    const chunks = window.__yxt_recorder_chunks;
    if (!chunks || chunks.length === 0) return { error: 'no data' };

    // 合并所有 chunks 成一个 Blob, 然后转 base64
    const blob = new Blob(chunks, { type: chunks[0].type || 'video/webm' });
    const buffer = await blob.arrayBuffer();
    const bytes = new Uint8Array(buffer);

    // 分块传输 (每块 500KB)
    const chunkSize = 512 * 1024;
    const totalChunks = Math.ceil(bytes.length / chunkSize);

    return {
        totalSize: bytes.length,
        totalChunks: totalChunks,
        mimeType: blob.type
    };
}
"""


async def capture_video(kng_id: str, name: str = ""):
    from playwright.async_api import async_playwright

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    video_url = (f"https://tz.yunxuetang.cn/kng/#/video/play"
                 f"?kngId={kng_id}&projectId=&btid=&gwnlUrl=")

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
            await page.add_init_script(RECORDER_SCRIPT)

            # Console 监听
            def on_console(msg):
                text = msg.text
                if text.startswith('__YXT_'):
                    log(f"  [JS] {text[:120]}")

            page.on('console', on_console)

            # 打开视频页面
            log(f"[Page] 打开视频页面...")
            try:
                await page.goto(video_url, wait_until="networkidle", timeout=30000)
            except Exception:
                pass
            await page.wait_for_timeout(3000)

            # 点击「开始学习」
            for sel in [
                "button:has-text('开始学习')", "a:has-text('开始学习')",
                "button:has-text('继续学习')",
            ]:
                try:
                    btn = await page.wait_for_selector(sel, timeout=2000)
                    if btn and await btn.is_visible():
                        await btn.click()
                        log("  已点击「开始学习」")
                        break
                except Exception:
                    pass

            await page.wait_for_timeout(5000)

            # 点击播放按钮
            for sel in [".vjs-big-play-button", ".vjs-play-control",
                        "[class*='play-btn']", "video"]:
                try:
                    el = await page.query_selector(sel)
                    if el and await el.is_visible():
                        await el.click()
                        log(f"  已点击播放 ({sel})")
                        break
                except Exception:
                    pass

            await page.wait_for_timeout(3000)

            # 尝试 JS 直接播放
            try:
                await page.evaluate("() => { const v = document.querySelector('video'); if(v) v.play(); }")
            except Exception:
                pass

            await page.wait_for_timeout(5000)

            # 检查 SourceBuffer 数据
            sb_data = await page.evaluate("() => window.__yxt_sb_data || []")
            log(f"\n[SourceBuffer] 捕获 {len(sb_data)} 个 appendBuffer 调用")
            for d in sb_data:
                log(f"  len={d.get('len',0)} sync={d.get('sync',False)} sample={d.get('sample','')[:60]}")

            # 开始 MediaRecorder 录制
            log("\n[录制] 启动 MediaRecorder...")
            result = await page.evaluate(START_RECORDING_SCRIPT)
            log(f"  结果: {result}")

            if 'error' in result:
                log(f"[ERR] MediaRecorder 失败: {result['error']}")
                # 截图留底
                await page.screenshot(path=str(OUTPUT_DIR / "debug_video_recorder.png"))
                await browser.close()
                return False

            duration = result.get('duration', 0)
            est_time = result.get('estimatedTime', 60)
            log(f"  视频时长: {duration:.0f}s = {duration/60:.1f}min")
            log(f"  预计录制时间: {est_time}s (4x加速)")

            # 等待视频播放完成
            for i in range(int(est_time) + 30):
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
                    if i % 10 == 0:
                        ct = status.get('currentTime', 0)
                        dur = status.get('duration', 0)
                        pct = (ct / dur * 100) if dur > 0 else 0
                        log(f"  进度: {ct:.0f}/{dur:.0f}s ({pct:.0f}%) "
                            f"chunks={status.get('chunks', 0)}")

                    if status.get('ended') or status.get('paused'):
                        log(f"  视频已结束/暂停")
                        break
                except Exception:
                    pass

            # 收集录制数据
            log("\n[收集] 停止录制并收集数据...")
            info = await page.evaluate(COLLECT_RECORDING_SCRIPT)
            log(f"  信息: {info}")

            if 'error' in info:
                log(f"[ERR] 收集失败: {info['error']}")
                await browser.close()
                return False

            total_size = info.get('totalSize', 0)
            total_chunks = info.get('totalChunks', 0)

            if total_size == 0:
                log("[ERR] 录制数据为空")
                await browser.close()
                return False

            log(f"  总大小: {total_size // 1024}KB, {total_chunks} 块")

            # 使用浏览器下载机制传输数据
            output_webm = OUTPUT_DIR / f"{name or kng_id}.webm"

            log("  通过浏览器下载机制保存录制文件...")

            # 使用 Playwright 的 download 事件来捕获文件
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
            file_size = output_webm.stat().st_size
            log(f"  下载完成: {file_size // 1024}KB")

            log(f"\n[OK] {output_webm.name} ({file_size // 1024}KB)")

            # 转换 WebM -> MP4 (如果有 ffmpeg)
            try:
                import imageio_ffmpeg
                ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()
                output_mp4 = output_webm.with_suffix('.mp4')
                log(f"[ffmpeg] 转换为 MP4...")
                r = subprocess.run(
                    [ffmpeg_exe, '-y', '-i', str(output_webm),
                     '-c:v', 'libx264', '-crf', '20', '-preset', 'fast',
                     '-c:a', 'aac', '-b:a', '192k',
                     str(output_mp4)],
                    capture_output=True, timeout=600
                )
                if r.returncode == 0 and output_mp4.exists():
                    log(f"[OK] {output_mp4.name} ({output_mp4.stat().st_size // 1024}KB)")
                    output_webm.unlink()
                else:
                    log(f"[WARN] MP4 转换失败, 保留 WebM")
            except ImportError:
                log("[WARN] 无 ffmpeg, 保留 WebM 格式")

            await browser.close()
            return True

    finally:
        shutil.rmtree(temp_profile, ignore_errors=True)


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--kng-id", required=True)
    parser.add_argument("--name", default="")
    args = parser.parse_args()
    asyncio.run(capture_video(args.kng_id, args.name))
