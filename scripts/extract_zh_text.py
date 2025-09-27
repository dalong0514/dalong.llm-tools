# -*- coding:utf-8 -*-

"""
提取中文段落 / Extract Chinese paragraphs.

功能说明 / Description:
- 读取 `working/input.md`，按空行分段，筛选包含中文字符的段落，
  并将结果写入 `working/output.md`。

使用 / Usage:
    python scripts/extract_zh_text.py
    # 或自定义路径
    python scripts/extract_zh_text.py --input working/input.md --output working/output.md

备注 / Notes:
- 脚本从仓库根目录运行，以保证相对路径一致。
"""

import argparse
import os, time
import re
import sys
from pathlib import Path

# 允许从 src 导入（遵循仓库中其他脚本的做法）
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


ZH_PATTERN = re.compile(r"[\u4e00-\u9fff]")


def contains_chinese(text: str) -> bool:
    """判断文本是否包含中文字符 / Check if text contains Chinese characters."""
    return bool(ZH_PATTERN.search(text))


def split_paragraphs(text: str) -> list[str]:
    """按空行分段（一个或多个空行作为段落分隔）/ Split text by blank lines.

    使用正则将一个或多个空行作为分隔符，尽量贴合 Markdown 段落习惯。
    """
    # 统一换行符，按空行（含空白字符）拆分
    normalized = text.replace("\r\n", "\n").replace("\r", "\n")
    parts = re.split(r"\n\s*\n+", normalized)
    # 去除段落首尾空白
    return [p.strip() for p in parts if p.strip()]


def extract_chinese_paragraphs(content: str) -> list[str]:
    """从文本中提取包含中文的段落 / Extract paragraphs that contain Chinese."""
    paragraphs = split_paragraphs(content)
    return [p for p in paragraphs if contains_chinese(p)]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="提取中文段落到 output.md / Extract Chinese paragraphs")
    repo_root = Path(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    default_input = repo_root / "working" / "input.md"
    default_output = repo_root / "working" / "output.md"
    parser.add_argument("--input", type=Path, default=default_input, help="输入文件路径 / Input file path")
    parser.add_argument("--output", type=Path, default=default_output, help="输出文件路径 / Output file path")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    input_path: Path = args.input
    output_path: Path = args.output

    if not input_path.exists():
        print(f"输入文件不存在: {input_path}")
        sys.exit(1)

    content = input_path.read_text(encoding="utf-8")
    zh_paragraphs = extract_chinese_paragraphs(content)

    # 如果没有中文段落，清空/创建输出文件
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_text = "\n\n".join(zh_paragraphs) + ("\n" if zh_paragraphs else "")
    output_path.write_text(output_text, encoding="utf-8")

    print(f"已将 {len(zh_paragraphs)} 个中文段落写入: {output_path}")


if __name__ == "__main__":
    start_time = time.time()
    print('waiting...\n')
    main()
    end_time = time.time()
    elapsed_time = end_time - start_time
    if elapsed_time < 60:
        print(f'Time Used: {elapsed_time:.2f} seconds')
    else:
        print(f'Time Used: {elapsed_time/60:.2f} minutes')