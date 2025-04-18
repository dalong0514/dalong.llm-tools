# -*- coding: utf-8 -*-
import os, sys, time, re
from pathlib import Path
import argparse
import subprocess
import json
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.utils import get_all_files_from_directory
import src.utils as common_tools
from src.helper import get_api_key, get_base_url
from src.utils import read_prompt_file

prompt_split = read_prompt_file("prompt_split_en")
system_prompt = read_prompt_file("prompt_translate")

api_key = get_api_key("deepseek")
base_url= get_base_url("deepseek")
model_name = "deepseek-chat"

model = ChatOpenAI(
    base_url=base_url,
    api_key=api_key,
    model_name=model_name
)

def translate_once(model, origin_content, filename):
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(origin_content + '\n\n')
    try:
        prompt_template = ChatPromptTemplate([
            ("system", system_prompt),
            ("user", "{content}")
        ])
        prompt = prompt_template.invoke({"content": origin_content})
        response = model.invoke(prompt)
        response_text = response.content

        out_content = common_tools.extract_translation(response_text)
        out_content = common_tools.modify_text(out_content)

        while out_content == "未找到意译内容":
            response = model.invoke(prompt)
            response_text = response.content
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
            return translate_once(model, origin_content, filename)
        return None

# 步骤二：批量处理内容
def process_chunks(model, chunks, filename):
    for i, chunk in enumerate(chunks):
        print(f"Processing chunk {i+1}/{len(chunks)}")
        if chunk.strip():  # 检查chunk是否为空或仅包含空白字符
            translate_once(model, chunk, filename)
        else:
            print(f"Skipping empty chunk {i+1}")
        # Add delay between requests to avoid rate limiting
        time.sleep(1)  # Adjust this value as needed

def translate(input_filename, output_filename):
    origin_content = common_tools.read_file(input_filename)
    chunks = common_tools.split_text_by_long_newline(origin_content)
    process_chunks(model, chunks, output_filename)


def split_translate_once(model, origin_content, filename):
    try:
        prompt_template = ChatPromptTemplate([
            ("system", prompt_split)
        ])
        prompt = prompt_template.invoke({"AUDIO_TRANSCRIPT": origin_content})
        response = model.invoke(prompt)
        response_text = response.content
        out_content = split_extract_translation(response_text)
        with open(filename, 'a', encoding='utf-8') as file:
            file.write(out_content + '\n\n')
    except Exception as e:
        print(f"Error processing chunk: {e}")
        # Wait and retry if it's a rate limit error
        if "429" in str(e):
            print("Rate limit exceeded, waiting 30 seconds...")
            time.sleep(30)
            return split_translate_once(model, origin_content, filename)
        return None

def split_extract_translation(text):
    pattern = r'<refined_translation>([\s\S]*?)(?:</refined_translation>|\Z)'
    match = re.search(pattern, text, re.DOTALL)
    if match:
        return match.group(1).strip()
    return "整理内容"

# 步骤二：批量处理内容
def split_process_chunks(model, chunks, filename):
    for i, chunk in enumerate(chunks):
        print(f"Processing chunk {i+1}/{len(chunks)}")
        split_translate_once(model, chunk, filename)
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

    chunks = common_tools.split_text_by_dot_length(origin_content, 20000)
    split_process_chunks(model, chunks, split_file)
    translate(split_file, output_file)


def extract_text_from_json(json_file, output_txt=None):
    """
    从转录的json文件中提取纯文本内容
    :param json_file: 输入的json文件路径
    :param output_txt: 输出的txt文件路径（可选）
    :return: 输出文件路径
    """
    if output_txt is None:
        output_txt = os.path.splitext(json_file)[0] + '.txt'
    
    try:
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # 提取所有chunks中的text并拼接
        # full_text = ' '.join(chunk['text'] for chunk in data['chunks'])
        # 直接提取text字段
        full_text = data['text']

        with open(output_txt, 'w', encoding='utf-8') as f:
            f.write(full_text)
        
        print(f"文本提取成功！输出文件: {output_txt}")
        return output_txt
    except Exception as e:
        print(f"文本提取失败: {e}")
        return None

def convert_video_to_wav(input_file, output_file=None):
    """
    将视频文件转换为WAV音频
    :param input_file: 输入视频文件路径
    :param output_file: 输出音频文件路径（可选）
    :return: 输出文件路径
    """
    if output_file is None:
        output_file = os.path.splitext(input_file)[0] + '.wav'
    
    command = [
        'ffmpeg',
        '-i', input_file,
        '-ar', '16000',  # 采样率
        '-ac', '1',      # 单声道
        '-c:a', 'pcm_s16le',  # 音频编码
        output_file
    ]
    
    try:
        subprocess.run(command, check=True)
        print(f"转换成功！输出文件: {output_file}")
        return output_file
    except subprocess.CalledProcessError as e:
        print(f"转换失败: {e}")
        return None


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

def video_to_text(input_video, model_path, output_dir=None, language="zh"):
    """
    将视频文件转换为文本
    :param input_video: 输入视频文件路径
    :param model_path: whisper模型路径
    :param output_dir: 输出目录（可选）
    :param language: 语言代码
    :return: 转录结果文件路径
    """
    # 转换视频为音频
    if output_dir:
        base_name = os.path.basename(input_video)
        audio_output = os.path.join(output_dir, os.path.splitext(base_name)[0] + '.wav')
    else:
        audio_output = None
        
    wav_file = convert_video_to_wav(input_video, audio_output)
    if not wav_file:
        return None
        
    # 转录音频为文本
    if output_dir:
        base_name = os.path.basename(wav_file)
        json_output = os.path.join(output_dir, os.path.splitext(base_name)[0] + '.json')
    else:
        json_output = None
        
    result = transcribe_audio(wav_file, model_path, json_output, language=language)
    
    # 删除临时wav文件
    if result and os.path.exists(wav_file):
        try:
            os.remove(wav_file)
            print(f"已删除临时音频文件: {wav_file}")
        except OSError as e:
            print(f"删除音频文件失败: {e}")
    
    # 在原有代码最后添加文本提取
    if result:
        if output_dir:
            base_name = os.path.basename(result)
            txt_output = os.path.join(output_dir, os.path.splitext(base_name)[0] + '.txt')
        else:
            txt_output = None
            
        final_result = extract_text_from_json(result, txt_output)
        return final_result
    
    return txt_output

def video_translate(args):
    txt_output = video_to_text(args.input_video, args.model_path, args.output_dir, args.language)
    split_translate(txt_output)


def parse_arguments():
    """
    解析命令行参数
    :return: 包含参数的命名空间
    """
    parser = argparse.ArgumentParser(description="将视频文件转换为文字转录")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('input_dir', type=str, help='输入视频文件夹路径，将处理该文件夹下所有视频文件')
    parser.add_argument('--video_ext', type=str, default='mp4', 
                       help='视频文件扩展名 (默认: mp4)，仅在使用--input_dir时有效')
    parser.add_argument('--language', type=str, default='en', 
                       help='音频语言代码 (默认: en)')
    parser.add_argument('--model_path', type=str, 
                       default='/Users/Daglas/dalong.modelsets/whisper-large-v3-turbo',
                       help='whisper模型路径')
    parser.add_argument('--output_dir', type=str, 
                       default=None,
                       help='输出目录 (默认: 视频文件所在目录)')
    return parser.parse_args()

def batch_video_translate(args):
    """
    批量处理目录下的所有视频文件
    :param args: 命令行参数
    """
    try:
        # 获取指定目录下所有指定扩展名的视频文件
        video_files = get_all_files_from_directory(args.input_dir, args.video_ext)
        
        if not video_files:
            print(f"在目录 {args.input_dir} 中未找到扩展名为 .{args.video_ext} 的视频文件")
            return
        
        print(f"找到 {len(video_files)} 个视频文件，开始处理...")
        
        # 如果没有指定输出目录，使用输入目录
        if args.output_dir is None:
            args.output_dir = args.input_dir
        
        # 处理每个视频文件
        for i, video_file in enumerate(video_files):
            print(f"\n[{i+1}/{len(video_files)}] 处理文件: {os.path.basename(video_file)}")
            
            # 创建一个新的参数对象，复制原始参数但替换input_video
            video_args = argparse.Namespace(
                input_video=video_file,
                language=args.language,
                model_path=args.model_path,
                output_dir=args.output_dir
            )
            
            # 处理单个视频文件
            video_translate(video_args)
            
    except Exception as e:
        print(f"批量处理视频文件时出错: {e}")

if __name__ == "__main__":
    args = parse_arguments()
    batch_video_translate(args)
    