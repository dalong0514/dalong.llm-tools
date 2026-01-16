# -*- coding:utf-8 -*-

import os
import sys
import time
from pathlib import Path

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import argparse

import pyperclip

from src.utils import modify_text, modify_text_en


def modify_single_file_content(args):
    default_path = (
        Path(__file__).resolve().parent.parent / "working" / "temp.md"
    )
    file_name = Path(args.file).expanduser() if args.file else default_path
    if not file_name.is_file():
        raise FileNotFoundError(f"File not found: {file_name}")

    with file_name.open(encoding="UTF-8") as file_obj:
        lines = file_obj.readlines()

    processed_lines = []
    for line in lines:
        if line != "\n":
            new_content = modify_text_en(line) if args.lg == "en" else modify_text(line)
            processed_lines.append(new_content)

    processed_text = "\n\n".join(processed_lines)
    if processed_lines:
        processed_text += "\n\n"
    pyperclip.copy(processed_text)


def parse_arguments():
    """
    解析命令行参数
    :return: 包含参数的命名空间
    """
    parser = argparse.ArgumentParser(description="整理文字格式")
    parser.add_argument(
        "--lg", type=str, default="zh", help="音频语言代码 (默认: zh/en)"
    )
    parser.add_argument("--file", type=str, help="输入文件路径 (可选)")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_arguments()
    start_time = time.time()
    modify_single_file_content(args)
    end_time = time.time()
    print("OK!")
    print("Time Used: " + str(end_time - start_time) + "s")
