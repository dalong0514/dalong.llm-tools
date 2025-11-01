# -*- coding: utf-8 -*-
"""
哔哩哔哩(Bilibili) 视频下载脚本

- 功能: 通过 yt-dlp 下载哔哩哔哩视频，支持单条 URL 或批量列表。
- 特色: 支持代理、可选 cookies 文件、失败后格式回退、可选下载多 P。

Usage 示例:
  - 单个视频:
    python scripts/bili_download.py --url "https://www.bilibili.com/video/BV1aP4y1Q7qU/"

  - 批量下载(每行一个 URL):
    python scripts/bili_download.py --list working/bili_download_list.txt

  - 指定输出目录、代理与 cookies:
    python scripts/bili_download.py --url <URL> --out /path/to/save --proxy http://127.0.0.1:7890 --cookies /path/to/cookies.txt

English:
  Bilibili video downloader using yt-dlp. Supports single URL or batch list,
  proxy, optional cookies file, and fallback formats on errors.
"""

from __future__ import annotations

import os
import sys
import argparse
from typing import Optional

from yt_dlp import YoutubeDL


# 默认代理（如无需代理可通过 --proxy 传入空字符串覆盖）
PROXY = "http://127.0.0.1:7890"


def _abs_outtmpl(output_path: str) -> str:
    """返回绝对路径 outtmpl 模板。"""
    return os.path.join(os.path.abspath(output_path), "%(title)s.%(ext)s")


def download_bili_video(
    video_url: str,
    output_path: str = "/Users/Daglas/Desktop",
    proxy: Optional[str] = PROXY,
    cookies: Optional[str] = None,
    all_parts: bool = False,
) -> bool:
    """
    下载哔哩哔哩视频。

    参数:
    - video_url: 视频页面 URL (如 https://www.bilibili.com/video/BV...)
    - output_path: 保存目录，默认桌面。
    - proxy: 代理地址，默认 "http://127.0.0.1:7890"；传入空字符串或 None 表示不用代理。
    - cookies: 可选 cookies 文件路径（Netscape 格式），用于下载受限清晰度或需要登录的视频。
    - all_parts: 若为 True，下载多 P 系列全部分 P；否则仅下载当前页面所指 P。

    Returns: True 下载成功；False 失败。
    """
    os.makedirs(output_path, exist_ok=True)

    ydl_opts = {
        # 通用的较稳格式选择策略
        "format": "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best",
        "outtmpl": _abs_outtmpl(output_path),
        "noplaylist": not all_parts,  # 默认不下整列表/多P
        "quiet": False,
        "no_warnings": False,
        "retries": 10,
        "socket_timeout": 30,
        "extract_flat": False,
        "merge_output_format": "mp4",
        "writesubtitles": False,
        "writeautomaticsub": False,
        "ignoreerrors": False,
        # B 站通常需要正确 UA 和 Referer
        "http_headers": {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
            ),
            "Referer": "https://www.bilibili.com/",
        },
    }

    if proxy:
        ydl_opts["proxy"] = proxy
    if cookies:
        ydl_opts["cookiefile"] = cookies

    try:
        with YoutubeDL(ydl_opts) as ydl:
            print("正在获取视频信息…")
            info = ydl.extract_info(video_url, download=False)

            # 对多 P 或单 P 打印关键信息
            title = info.get("title") if isinstance(info, dict) else None
            duration = info.get("duration") if isinstance(info, dict) else None
            if title:
                print(f"视频标题: {title}")
            if duration:
                print(f"视频时长: {duration} 秒")

            print("开始下载…")
            ydl.download([video_url])
            print(f"视频已下载至: {output_path}")
            return True

    except Exception as e:
        error_msg = str(e)
        print(f"下载失败: {error_msg}")

        # 常见错误提示
        if "403" in error_msg or "HTTP Error 403" in error_msg:
            print("提示：可能需要设置 Referer、代理或提供 cookies 文件。")
        if "Unsupported URL" in error_msg:
            print("提示：URL 可能无效，请确认是有效的 bilibili 视频页链接。")

        # 回退尝试
        return try_fallback_download(video_url, output_path, proxy=proxy, cookies=cookies, all_parts=all_parts)


def try_fallback_download(
    video_url: str,
    output_path: str,
    proxy: Optional[str] = PROXY,
    cookies: Optional[str] = None,
    all_parts: bool = False,
) -> bool:
    """使用多种格式策略依次回退尝试下载。"""
    fallback_formats = [
        # 尝试最小化要求，以增加成功概率
        "best[ext=mp4]/best",
        "best",
        "worst[ext=mp4]/worst",
        "",
    ]

    for fmt in fallback_formats:
        label = fmt if fmt else "任意格式"
        print(f"尝试备用格式: {label}")
        ydl_opts = {
            "format": fmt if fmt else None,
            "outtmpl": _abs_outtmpl(output_path),
            "noplaylist": not all_parts,
            "quiet": True,
            "retries": 5,
            "socket_timeout": 30,
            "merge_output_format": "mp4",
            "http_headers": {
                "User-Agent": (
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                    "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
                ),
                "Referer": "https://www.bilibili.com/",
            },
        }
        if proxy:
            ydl_opts["proxy"] = proxy
        if cookies:
            ydl_opts["cookiefile"] = cookies

        # 删除 None 的 format 键，避免 yt-dlp 解析异常
        if ydl_opts.get("format") is None:
            del ydl_opts["format"]

        try:
            with YoutubeDL(ydl_opts) as ydl:
                ydl.download([video_url])
                print(f"使用备用格式下载成功: {label}")
                return True
        except Exception as e:
            print(f"备用格式 {label} 失败: {e}")
            continue

    print("所有备用格式都失败了。")
    return False


def batch_download_from_file(
    file_path: str,
    output_path: str = "/Users/Daglas/Desktop",
    proxy: Optional[str] = PROXY,
    cookies: Optional[str] = None,
    all_parts: bool = False,
) -> None:
    """
    批量下载：从文件中读取哔哩哔哩视频链接逐个下载。

    文件格式: 每行一个 URL，空行会被忽略。
    """
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            urls = [line.strip() for line in f if line.strip()]

        if not urls:
            print("文件中没有找到有效的 Bilibili 链接")
            return

        success = 0
        failed: list[tuple[int, str]] = []

        for i, url in enumerate(urls, 1):
            print("\n" + "=" * 60)
            print(f"正在下载第 {i}/{len(urls)} 个视频: {url}")
            print("=" * 60)
            try:
                if download_bili_video(url, output_path, proxy=proxy, cookies=cookies, all_parts=all_parts):
                    success += 1
                    print(f"✅ 第 {i} 个视频下载成功")
                else:
                    failed.append((i, url))
                    print(f"❌ 第 {i} 个视频下载失败")
            except Exception as e:
                failed.append((i, url))
                print(f"❌ 第 {i} 个视频下载异常: {e}")

        print("\n" + "=" * 60)
        print("下载完成！统计结果：")
        print(f"总共视频数量: {len(urls)}")
        print(f"成功下载: {success}")
        print(f"失败数量: {len(failed)}")
        rate = (success / len(urls) * 100) if urls else 0
        print(f"成功率: {rate:.1f}%")
        if failed:
            print("\n失败的视频链接:")
            for idx, u in failed:
                print(f"  {idx}. {u}")
        else:
            print("\n🎉 所有视频都下载成功！")

    except FileNotFoundError:
        print(f"错误：找不到文件 {file_path}")
        print("请确认文件路径是否正确")
    except Exception as e:
        print(f"批量下载失败: {e}")


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="下载哔哩哔哩(Bilibili)视频")
    parser.add_argument("--url", type=str, help="单个视频页面 URL")
    parser.add_argument("--list", type=str, help="包含多个 URL 的文件路径", default="/Users/Daglas/dalong.github/dalong.llm-tools/working/youtube_download_list.txt")
    parser.add_argument("--out", type=str, default="/Users/Daglas/Desktop", help="输出目录")
    parser.add_argument("--proxy", type=str, default=PROXY, help="代理地址，留空表示不使用")
    parser.add_argument("--cookies", type=str, default=None, help="cookies 文件路径 (Netscape 格式)")
    parser.add_argument("--all-parts", action="store_true", help="下载多 P 视频的全部分 P")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_arguments()

    # 允许通过传入空字符串来禁用代理
    proxy_arg = args.proxy if args.proxy else None

    if args.url:
        ok = download_bili_video(
            args.url,
            output_path=args.out,
            proxy=proxy_arg,
            cookies=args.cookies,
            all_parts=args.all_parts,
        )
        sys.exit(0 if ok else 1)

    elif args.list:
        batch_download_from_file(
            args.list,
            output_path=args.out,
            proxy=proxy_arg,
            cookies=args.cookies,
            all_parts=args.all_parts,
        )
    else:
        print("请使用 --url 或 --list 指定下载来源。-h 查看帮助。")
        sys.exit(2)

