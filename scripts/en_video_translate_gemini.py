# -*- coding: utf-8 -*-
import os, sys, time, re
from pathlib import Path
from google import genai
from google.genai import types
import argparse
import subprocess
import json
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.helper import get_api_key
import src.utils as common_tools
from split_audio_gemini import split_translate_once
from src.asr_funasr import funasr_transcribe_local_file

system_prompt = common_tools.read_prompt_file("prompt_translate")

api_key = get_api_key("google")
client = genai.Client(api_key=api_key)
# model_name = "gemini-2.5-pro"
model_name = "gemini-2.5-flash"


def translate_once(origin_content, filename):
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(origin_content + '\n\n')
    try:
        response = client.models.generate_content(
            model=model_name,
            contents=origin_content,
            config=types.GenerateContentConfig(
                system_instruction=system_prompt,
                thinking_config=types.ThinkingConfig(thinking_budget=0)
            )
        )
        # Convert response to text first
        response_text = response.text if hasattr(response, 'text') else str(response)
        out_content = common_tools.extract_translation(response_text)
        out_content = common_tools.modify_text(out_content)

        while out_content == "未找到意译内容":
            response = client.models.generate_content(
                model=model_name,
                contents=origin_content,
                config=types.GenerateContentConfig(
                    system_instruction=system_prompt,
                    thinking_config=types.ThinkingConfig(thinking_budget=0)
                )
            )
            response_text = response.text if hasattr(response, 'text') else str(response)
            out_content = common_tools.extract_translation(response_text)
            out_content = common_tools.modify_text(out_content)

        with open(filename, 'a', encoding='utf-8') as file:
            file.write(out_content + '\n\n')
    except Exception as e:
        print(f"Error processing chunk: {e}")
        # Wait and retry if it's a rate limit error
        if "429" in str(e):
            print("Rate limit exceeded, waiting 30 seconds...")
            time.sleep(30)
            return translate_once(origin_content, filename)
        return None

# 步骤二：批量处理内容
def process_chunks(chunks, filename):
    for i, chunk in enumerate(chunks):
        print(f"Processing chunk {i+1}/{len(chunks)}")
        if chunk.strip():  # 检查chunk是否为空或仅包含空白字符
            translate_once(chunk, filename)
        else:
            print(f"Skipping empty chunk {i+1}")
        # Add delay between requests to avoid rate limiting
        time.sleep(1)  # Adjust this value as needed

def translate(input_filename, output_filename):
    origin_content = common_tools.read_file(input_filename)
    chunks = common_tools.split_text_by_long_newline(origin_content)
    process_chunks(chunks, output_filename)

# 步骤二：批量处理内容
def split_process_chunks(chunks, filename):
    for i, chunk in enumerate(chunks):
        print(f"Processing chunk {i+1}/{len(chunks)}")
        split_translate_once(chunk, filename)
        # Add delay between requests to avoid rate limiting
        time.sleep(1)  

def split_translate(txt_output):
    origin_content = common_tools.read_file(txt_output)
    
    # 如果没有指定输出文件，使用输入文件同目录下相同文件名的 md 文件
    input_filename = os.path.basename(txt_output)
    output_filename = os.path.splitext(input_filename)[0] + '.md'
    output_file = os.path.join(os.path.dirname(txt_output), output_filename)
    split_filename = os.path.splitext(input_filename)[0] + '_origin.md'
    split_file = os.path.join(os.path.dirname(txt_output), split_filename)

    chunks = common_tools.split_text_by_dot_length(origin_content, 5000)
    split_process_chunks(chunks, split_file)
    translate(split_file, output_file)

def transcribe_audio(input_audio, model_path, output_json=None, language="zh", device="mps", batch_size=4):
    """
    使用insanely-fast-whisper将音频转录为文本
    :param input_audio: 输入音频文件路径
    :param model_path: whisper模型路径
    :param output_json: 输出json文件路径（可选）
    :param language: 语言代码
    :param device: 计算设备（mps/cpu/cuda）
    :param batch_size: 批处理大小
    :return: 输出文件路径
    """
    if output_json is None:
        output_json = os.path.splitext(input_audio)[0] + '.json'
    
    command = [
        'insanely-fast-whisper',
        '--model-name', model_path,
        '--file-name', input_audio,
        '--device', device,
        '--transcript-path', output_json,
        '--batch-size', str(batch_size),
        '--language', language
    ]
    
    try:
        subprocess.run(command, check=True)
        print(f"转录成功！输出文件: {output_json}")
        return output_json
    except subprocess.CalledProcessError as e:
        print(f"转录失败: {e}")
        return None

def video_translate(args):
    out_dir = args.output_dir or os.path.dirname(os.path.abspath(args.input_video))
    os.makedirs(out_dir, exist_ok=True)
    txt_output = funasr_transcribe_local_file(args.input_video, out_dir, model='fun-asr')
    if txt_output and os.path.exists(txt_output):
        split_translate(txt_output)
    else:
        print("视频转文本失败，无法进行翻译")


def parse_arguments():
    """
    解析命令行参数
    :return: 包含参数的命名空间
    """
    parser = argparse.ArgumentParser(description="将视频文件转换为文字转录")
    parser.add_argument('input_video', type=str, help='输入视频文件路径')
    parser.add_argument('--language', type=str, default='en', 
                       help='音频语言代码 (默认: zh/en)')
    parser.add_argument('--model_path', type=str, 
                       default='/Users/Daglas/dalong.modelsets/whisper-large-v3-turbo',
                       help='whisper模型路径')
    parser.add_argument('--output_dir', type=str, 
                       default=None,
                       help='输出目录 (默认: 视频文件所在目录)')
    return parser.parse_args()

if __name__ == "__main__":
    start_time = time.time()
    print('waiting...\n')
    args = parse_arguments()
    # 如果没有指定输出目录，使用视频文件所在目录
    if args.output_dir is None:
        args.output_dir = os.path.dirname(args.input_video)
    video_translate(args)
    end_time = time.time()
    elapsed_time = end_time - start_time
    if elapsed_time < 60:
        print(f'Time Used: {elapsed_time:.2f} seconds')
    else:
        print(f'Time Used: {elapsed_time/60:.2f} minutes')