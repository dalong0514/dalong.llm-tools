# -*- coding: utf-8 -*-
import sys, time, os, re
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from src.helper import get_api_key, get_base_url
from src.utils import read_prompt_file
from src.utils import get_all_files_from_directory
import src.utils as common_tools
import argparse
import subprocess
import json

# "音频转录文本中一些常用的词汇如下：`阳志平`、`阳老师`。"

prompt_translate = read_prompt_file("prompt_translate_audio")

api_key = get_api_key()
base_url= get_base_url()
model_name = "claude-sonnet-4-20250514"

model = ChatOpenAI(
    base_url=base_url,
    api_key=api_key,
    model_name=model_name
)

output_parser = StrOutputParser()

def translate_once(prompt, origin_content, filename):
    try:
        chain = prompt | model | output_parser
        response = chain.invoke({"AUDIO_TRANSCRIPT": origin_content})
        if not response:
            raise ValueError("Empty response from API")
        out_content = extract_translation(response)
        while out_content == "未找到意译内容":
            response = chain.invoke({"AUDIO_TRANSCRIPT": origin_content})
            out_content = extract_translation(response)
        out_content = common_tools.modify_text(out_content)
        with open(filename, 'a', encoding='utf-8') as file:
            file.write(out_content + '\n\n')
    except Exception as e:
        print(f"Error during translation: {str(e)}")
        print(f"Original content: {origin_content[:200]}...")  # Print first 200 chars for debugging
        print("Rate limit exceeded, waiting 40 seconds...")
        time.sleep(40)
        return translate_once(prompt, origin_content, filename)
        raise

def process_chunks(prompt, chunks, filename):
    for i, chunk in enumerate(chunks):
        print(f"Processing chunk {i+1}/{len(chunks)}")
        if chunk.strip():  # 检查chunk是否为空或仅包含空白字符
            translate_once(prompt, chunk, filename)
        else:
            print(f"Skipping empty chunk {i+1}")
        # Add delay between requests to avoid rate limiting
        time.sleep(1)  # Adjust this value as needed

def extract_translation(text):
    pattern = r'<refined_translation>([\s\S]*?)(?:</refined_translation>|\Z)'
    match = re.search(pattern, text, re.DOTALL)
    if match:
        return match.group(1).strip()
    return "未找到意译内容"

def translate(txt_output):
    origin_content = common_tools.read_file(txt_output)
    prompt = ChatPromptTemplate.from_messages([
        ("system", prompt_translate)
    ])
    
    input_filename = os.path.basename(txt_output)
    output_filename = os.path.splitext(input_filename)[0] + '_origin.md'
    output_file = os.path.join(os.path.dirname(txt_output), output_filename)
    
    chunks = common_tools.split_text_by_char_length(origin_content, 800)
    process_chunks(prompt, chunks, output_file)


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
        base_name = os.path.splitext(input_file)[0]
        output_file = base_name + '_converted.wav'
    
    # 如果输入文件已经是wav格式且路径相同，创建一个新的输出路径
    if os.path.abspath(input_file) == os.path.abspath(output_file):
        base_name = os.path.splitext(output_file)[0]
        output_file = base_name + '_converted.wav'
    
    # 检查输入文件是否存在
    if not os.path.exists(input_file):
        print(f"输入文件不存在: {input_file}")
        return None
    
    command = [
        'ffmpeg',
        '-y',  # 自动覆盖输出文件
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
        audio_output = os.path.join(output_dir, os.path.splitext(base_name)[0] + '_converted.wav')
    else:
        audio_output = None
        
    wav_file = convert_video_to_wav(input_video, audio_output)
    if not wav_file:
        print("音频转换失败")
        return None
        
    # 转录音频为文本
    if output_dir:
        base_name = os.path.basename(wav_file)
        json_output = os.path.join(output_dir, os.path.splitext(base_name)[0] + '.json')
    else:
        json_output = None
        
    json_result = transcribe_audio(wav_file, model_path, json_output, language=language)
    
    # 删除临时wav文件
    if json_result and os.path.exists(wav_file):
        try:
            os.remove(wav_file)
            print(f"已删除临时音频文件: {wav_file}")
        except OSError as e:
            print(f"删除音频文件失败: {e}")
    
    # 提取文本
    if json_result:
        if output_dir:
            base_name = os.path.basename(json_result)
            txt_output = os.path.join(output_dir, os.path.splitext(base_name)[0] + '.txt')
        else:
            txt_output = None
            
        final_result = extract_text_from_json(json_result, txt_output)
        return final_result
    else:
        print("音频转录失败")
        return None

def video_translate(args):
    txt_output = video_to_text(args.input_video, args.model_path, args.output_dir, args.language)
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
    parser.add_argument('input_video', type=str, help='输入视频文件路径')
    parser.add_argument('--language', type=str, default='zh', 
                       help='音频语言代码 (默认: zh/en)')
    parser.add_argument('--model_path', type=str, 
                       default='/Users/Daglas/dalong.modelsets/whisper-large-v3-turbo',
                       help='whisper模型路径')
    parser.add_argument('--output_dir', type=str, 
                       default=None,
                       help='输出目录 (默认: 视频文件所在目录)')
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_arguments()
    # 如果没有指定输出目录，使用视频文件所在目录
    if args.output_dir is None:
        args.output_dir = os.path.dirname(args.input_video)
    video_translate(args)