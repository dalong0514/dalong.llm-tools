# -*- coding: utf-8 -*-
import sys, time, os, re
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from src.helper import get_api_key, get_base_url
from src.utils import read_prompt_file
import src.utils as common_tools
from src.asr_funasr import funasr_transcribe_local_file
import argparse
from datetime import datetime

system_prompt = read_prompt_file("prompt_translate_audio_zh")

api_key = get_api_key("deepseek")
base_url= get_base_url("deepseek")
model_name = "deepseek-chat"

model = ChatOpenAI(
    base_url=base_url,
    api_key=api_key,
    model_name=model_name
)

def translate_once(prompt_template, origin_content, filename):
    try:
        prompt = prompt_template.invoke({"content": origin_content})
        response = model.invoke(prompt)
        out_content = response.content
        out_content = common_tools.modify_text(out_content)
        with open(filename, 'a', encoding='utf-8') as file:
            file.write(out_content + '\n\n')
    except Exception as e:
        print(f"Error during translation: {str(e)}")
        print(f"Original content: {origin_content[:200]}...")  # Print first 200 chars for debugging
        print("Rate limit exceeded, waiting 40 seconds...")
        time.sleep(40)
        return translate_once(prompt_template, origin_content, filename)
        raise

def process_chunks(prompt_template, chunks, filename):
    for i, chunk in enumerate(chunks):
        print(f"Processing chunk {i+1}/{len(chunks)}")
        if chunk.strip():  # 检查chunk是否为空或仅包含空白字符
            translate_once(prompt_template, chunk, filename)
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
    prompt_template = ChatPromptTemplate([
        ("system", system_prompt),
        ("user", "{content}")
    ])
    
    input_filename = os.path.basename(txt_output)
    output_filename = os.path.splitext(input_filename)[0] + '_origin.md'
    output_file = os.path.join(os.path.dirname(txt_output), output_filename)
    
    chunks = common_tools.split_text_by_char_length(origin_content, 800)
    process_chunks(prompt_template, chunks, output_file)

def _resolve_diarization_from_multi(multi_val: str):
    # '1' => single speaker (no diarization)
    # '2'/'3'/'4' => diarization with fixed count
    # 'n' => diarization enabled with unknown count
    multi_val = (multi_val or '1').strip().lower()
    if multi_val == '1':
        return False, None
    if multi_val in ('2', '3', '4'):
        return True, int(multi_val)
    if multi_val == 'n':
        return True, None
    # fallback safe default
    return False, None


def video_translate(args):
    # 仅支持本地文件路径；调用工具函数（自动上传到 OSS + Fun-ASR）
    input_path = args.input_video
    if not os.path.exists(input_path):
        print(f'本地文件不存在: {input_path}')
        return None

    # 输出目录：与输入文件所在目录相同（若未显式传入）
    out_dir = args.output_dir or os.path.dirname(os.path.abspath(input_path))
    os.makedirs(out_dir, exist_ok=True)

    diarization_enabled, speaker_count = _resolve_diarization_from_multi(args.multi)
    txt_output = funasr_transcribe_local_file(
        input_path,
        out_dir,
        model='fun-asr', # fun-asr 支持中文、英文；fun-asr-mtl 支持中文， 粤语、英文、日语、 泰语、 越南语、印尼语
        diarization_enabled=diarization_enabled,
        speaker_count=speaker_count,
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
    parser = argparse.ArgumentParser(description="将本地音/视频转成文本后进行 DeepSeek 翻译（自动上传至阿里云OSS+Fun-ASR）")
    parser.add_argument('input_video', type=str, help='输入音/视频：本地文件路径（会自动上传到 OSS）')
    parser.add_argument('--language', type=str, default='zh', 
                       help='音频语言代码 (默认: zh/en)')
    parser.add_argument('--model_path', type=str, 
                       default='/Users/Daglas/dalong.modelsets/whisper-large-v3-turbo',
                       help='whisper模型路径')
    parser.add_argument('--output_dir', type=str, 
                       default=None,
                       help='输出目录 (默认: 视频文件所在目录)')
    parser.add_argument('--multi', type=str, default='1', choices=['1','2','3','4','n'],
                        help='多人转录模式：1=单人(默认,不分离)；2/3/4=固定人数说话人分离；n=自动多人分离')
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_arguments()
    # 如果没有指定输出目录，使用输入文件所在目录
    if args.output_dir is None and os.path.exists(args.input_video):
        args.output_dir = os.path.dirname(os.path.abspath(args.input_video))
    start_time = time.time()
    print('waiting...\n')
    video_translate(args)
    end_time = time.time()
    elapsed_time = end_time - start_time
    if elapsed_time < 60:
        print(f'Time Used: {elapsed_time:.2f} seconds')
    else:
        print(f'Time Used: {elapsed_time/60:.2f} minutes')
