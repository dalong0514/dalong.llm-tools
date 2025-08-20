# -*- coding: utf-8 -*-
import sys, time, os, re
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from src.helper import get_api_key, get_base_url
from src.utils import read_prompt_file
from audio2txt_tools import video_to_text
import src.utils as common_tools
import argparse

# "音频转录文本中一些常用的词汇如下：`阳志平`、`阳老师`。"

system_prompt = read_prompt_file("prompt_translate_audio_zh")

api_key = get_api_key()
base_url= get_base_url()
model_name = "gpt-5"

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
    start_time = time.time()
    print('waiting...\n')
    video_translate(args)
    end_time = time.time()
    elapsed_time = end_time - start_time
    if elapsed_time < 60:
        print(f'Time Used: {elapsed_time:.2f} seconds')
    else:
        print(f'Time Used: {elapsed_time/60:.2f} minutes')