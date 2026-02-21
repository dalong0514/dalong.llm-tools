---
name: yunxuetang-downloader
description: Download videos and documents from yunxuetang.cn (云学堂) course platform. Use when the user needs to batch download or individually download course content from a yunxuetang catalog page or by kngId. Handles DRM-protected videos (Baidu BCE DRM) via browser MediaRecorder and documents via scroll-capture to PDF. Triggers on requests mentioning yunxuetang, 云学堂, or course downloading from tz.yunxuetang.cn.
---

# Yunxuetang Course Downloader

Downloads videos and documents from yunxuetang.cn. Videos are DRM-protected (Baidu BCE proprietary encryption) and cannot be directly downloaded; this skill uses browser-based MediaRecorder to capture decoded output. Documents are rendered as per-page images with signed CDN URLs; this skill scrolls to capture all pages and creates PDFs.

## Prerequisites

- **Chrome** with an active yunxuetang.cn login session
- **Close all Chrome windows** before running the script
- Python packages: `playwright`, `requests`, `pillow`
- Optional: `imageio-ffmpeg` (for WebM → MP4 conversion)

Install dependencies:
```bash
pip install playwright requests pillow imageio-ffmpeg
playwright install chromium
```

## Workflow

### Step 1: Get Course List (optional for batch)

```bash
python scripts/yunxuetang_download.py list \
  --url "https://tz.yunxuetang.cn/kng/#/list?catalogId=xxx&cid=xxx" \
  --output-dir ~/Downloads/yunxuetang
```

Outputs `course_list.json` with all courses (kngId, name, type).

### Step 2: Download Courses

**Single course:**
```bash
python scripts/yunxuetang_download.py single \
  --kng-id "99ed7903-fc49-4dad-a287-01a57aa0bc43" \
  --name "课程名称" \
  --output-dir ~/Downloads/yunxuetang
```

**Batch download:**
```bash
python scripts/yunxuetang_download.py batch \
  --courses ~/Downloads/yunxuetang/course_list.json \
  --output-dir ~/Downloads/yunxuetang \
  --start 0
```

## Key Technical Details

| Aspect | Detail |
|--------|--------|
| Video DRM | Baidu BCE `KEYFORMAT=media-drm-token`, proprietary key derivation |
| Video method | `video.captureStream()` + `MediaRecorder` at **1x speed** (real-time) |
| Video output | WebM (VP9/Opus) → MP4 (H264/AAC) via ffmpeg |
| Doc method | Scroll page → intercept `cdn-tce-file` image requests → download → PIL PDF |
| Type detection | API labels unreliable; script visits page and detects m3u8 vs image requests |
| Auth | Copies Chrome profile (cookies/localStorage) to temp dir for login session |
| Resume | Batch mode tracks progress in `download_progress.json`, skips completed courses |
| Video duration | Recording takes real-time (a 10-min video needs 10 min to record) |

## Important Notes

- **Video recording is real-time**: A batch of many video courses will take hours. Plan accordingly.
- **Course type mismatch**: The API type field is often wrong (videos labeled as docs and vice versa). The script auto-detects by checking network requests.
- **Chrome must be closed**: The script launches Chrome with a copied profile; having another Chrome instance may cause conflicts.
- **ffmpeg optional**: Without ffmpeg, videos are saved as WebM. Install `imageio-ffmpeg` for automatic MP4 conversion.

## Troubleshooting

See [references/troubleshooting.md](references/troubleshooting.md) for common issues and solutions.

## Script Reference

The main script is `scripts/yunxuetang_download.py` with three subcommands:

| Subcommand | Purpose | Key Args |
|------------|---------|----------|
| `list` | Fetch course list from catalog URL | `--url` |
| `single` | Download one course by kngId | `--kng-id`, `--name` |
| `batch` | Download all courses from JSON list | `--courses`, `--start` |

Common options: `--output-dir`, `--chrome-profile` (auto-detected if omitted).
