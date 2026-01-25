# -*- coding: utf-8 -*-
import os
import re
import sys
import time

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import argparse

from audio2txt_tools import video_to_text
from src.device import get_default_whisper_model_path
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

import src.utils as common_tools
from src.helper import get_api_key, get_base_url
from src.utils import read_prompt_file

# "音频转录文本中一些常用的词汇如下：`阳志平`、`阳老师`。"

system_prompt = read_prompt_file("prompt_translate_audio_zh")

api_key = get_api_key("deepseek")
base_url = get_base_url("deepseek")
model_name = "deepseek-chat"

model = ChatOpenAI(base_url=base_url, api_key=api_key, model_name=model_name)


def translate_once(prompt_template, origin_content, filename):
    try:
        prompt = prompt_template.invoke({"content": origin_content})
        response = model.invoke(prompt)
        out_content = response.content
        out_content = common_tools.modify_text(out_content)
        with open(filename, "a", encoding="utf-8") as file:
            file.write(out_content + "\n\n")
    except Exception as e:
        print(f"Error during translation: {str(e)}")
        print(
            f"Original content: {origin_content[:200]}..."
        )  # Print first 200 chars for debugging
        print("Rate limit exceeded, waiting 40 seconds...")
        time.sleep(40)
        return translate_once(prompt_template, origin_content, filename)
        raise


def process_chunks(prompt_template, chunks, filename):
    for i, chunk in enumerate(chunks):
        print(f"Processing chunk {i + 1}/{len(chunks)}")
        if chunk.strip():  # 检查chunk是否为空或仅包含空白字符
            translate_once(prompt_template, chunk, filename)
        else:
            print(f"Skipping empty chunk {i + 1}")
        # Add delay between requests to avoid rate limiting
        time.sleep(1)  # Adjust this value as needed


def extract_translation(text):
    pattern = r"<refined_translation>([\s\S]*?)(?:</refined_translation>|\Z)"
    match = re.search(pattern, text, re.DOTALL)
    if match:
        return match.group(1).strip()
    return "未找到意译内容"


def translate(txt_output):
    origin_content = common_tools.read_file(txt_output)
    prompt_template = ChatPromptTemplate(
        [("system", system_prompt), ("user", "{content}")]
    )

    input_filename = os.path.basename(txt_output)
    output_filename = os.path.splitext(input_filename)[0] + "_origin.md"
    output_file = os.path.join(os.path.dirname(txt_output), output_filename)

    chunks = common_tools.split_text_by_char_length(origin_content, 800)
    process_chunks(prompt_template, chunks, output_file)


def video_translate(args):
    # 如果没有指定模型路径，根据设备自动选择
    model_path = args.model_path or get_default_whisper_model_path(args.device)
    txt_output = video_to_text(
        args.input_video,
        model_path,
        args.output_dir,
        args.language,
        device=args.device,
        num_speakers=args.num_speakers,
        min_speakers=args.min_speakers,
    )
    if txt_output and os.path.exists(txt_output):
        translate(txt_output)
    else:
        print("视频转文本失败，无法进行翻译")
        return None


def parse_arguments():
    """
    解析命令行参数
    :return: 包含参数的命名空间
    """
    parser = argparse.ArgumentParser(description="将视频文件转换为文字转录")
    parser.add_argument("input_video", type=str, help="输入视频文件路径")
    parser.add_argument(
        "--language", type=str, default="zh", help="音频语言代码 (默认: zh/en)"
    )
    parser.add_argument(
        "--model_path",
        type=str,
        default=None,
        help="whisper模型路径 (默认: 根据设备自动选择)",
    )
    parser.add_argument(
        "--output_dir", type=str, default=None, help="输出目录 (默认: 视频文件所在目录)"
    )
    parser.add_argument(
        "--num-speakers",
        dest="num_speakers",
        type=int,
        default=None,
        help="音频中说话人的精确数量，>=1。与 --min-speakers 不能同时使用。",
    )
    parser.add_argument(
        "--min-speakers",
        dest="min_speakers",
        type=int,
        default=None,
        help="说话人最小数量阈值，>=1。与 --num-speakers 不能同时使用。",
    )
    parser.add_argument(
        "--device",
        type=str,
        default=None,
        choices=["0", "mps", "cpu"],
        help="计算设备: 0=CUDA, mps=Apple芯片, cpu (默认: 自动检测)",
    )
    args = parser.parse_args()
    # 参数校验
    if args.num_speakers is not None and args.min_speakers is not None:
        parser.error("参数冲突：--num-speakers 与 --min-speakers 不能同时使用。")
    if args.num_speakers is not None and args.num_speakers < 1:
        parser.error("--num-speakers 必须 >= 1")
    if args.min_speakers is not None and args.min_speakers < 1:
        parser.error("--min-speakers 必须 >= 1")
    return args


if __name__ == "__main__":
    args = parse_arguments()
    # 如果没有指定输出目录，使用视频文件所在目录
    if args.output_dir is None:
        args.output_dir = os.path.dirname(args.input_video)
    start_time = time.time()
    print("waiting...\n")
    video_translate(args)
    end_time = time.time()
    elapsed_time = end_time - start_time
    if elapsed_time < 60:
        print(f"Time Used: {elapsed_time:.2f} seconds")
    else:
        print(f"Time Used: {elapsed_time / 60:.2f} minutes")
