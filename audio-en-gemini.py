# -*- coding:utf-8 -*-
import os, time, re
from pathlib import Path
import google.generativeai as genai
from dotenv import load_dotenv
import argparse
import common_tools as common_tools

model_name = "gemini-2.0-flash-exp"

def initialize_gemini():
    # 1. 加载环境变量
    if (Path(__file__).parent / ".env").is_file():
        load_dotenv(dotenv_path=Path(__file__).parent / ".env")
    # 2. 配置 Gemini
    if "GOOGLE_API_KEY" not in os.environ:
        raise ValueError("GOOGLE_API_KEY environment variable is not set")
    genai.configure(api_key=os.environ["GOOGLE_API_KEY"], transport="rest")

def split_translate_once(model, origin_content, filename):
    try:
        response = model.generate_content(origin_content)
        # Convert response to text first
        response_text = response.text if hasattr(response, 'text') else str(response)
        out_content = split_extract_translation(response_text)
        with open(filename, 'a', encoding='utf-8') as file:
            file.write(out_content + '\n\n')
    except Exception as e:
        print(f"Error processing chunk: {e}")
        # Wait and retry if it's a rate limit error
        if "429" in str(e):
            print("Rate limit exceeded, waiting 60 seconds...")
            time.sleep(60)
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

def parse_arguments():
    """
    解析命令行参数
    :return: 包含参数的命名空间
    """
    parser = argparse.ArgumentParser(description="整理英文版音频转录文本")
    parser.add_argument('input_file', type=str, 
                       default='/Users/Daglas/Desktop/input.md',
                       help='输入文本文件路径')
    parser.add_argument('--output_file', type=str, 
                       default=None,
                       help='输出文件路径')
    parser.add_argument('--prompt_file', type=str,
                       default='/Users/Daglas/dalong.llm/dalong.langchain/prompt_translate_audio_en.md',
                       help='翻译提示词文件路径')
    return parser.parse_args()

def split_translate(args):  # Modified to accept args
    system_prompt = common_tools.read_file(args.prompt_file)
    origin_content = common_tools.read_file(args.input_file)
    
    # 如果没有指定输出文件，使用输入文件同目录下相同文件名的 md 文件
    if args.output_file is None:
        input_filename = os.path.basename(args.input_file)
        output_filename = os.path.splitext(input_filename)[0] + '.md'
        args.output_file = os.path.join(os.path.dirname(args.input_file), output_filename)
    
    model = genai.GenerativeModel(
        model_name = model_name,
        system_instruction = system_prompt
    )
    chunks = common_tools.split_text_by_dot_length(origin_content, 20000)
    split_process_chunks(model, chunks, args.output_file)
    translate(args.output_file)
    # 删除临时md文件
    if os.path.exists(args.output_file):
        try:
            os.remove(args.output_file)
            print(f"已删除临时分割的md文件: {args.output_file}")
        except OSError as e:
            print(f"删除临时分割的md文件失败: {e}")

def translate_once(model, origin_content, filename):
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(origin_content + '\n\n')
    try:
        response = model.generate_content(origin_content)
        # Convert response to text first
        response_text = response.text if hasattr(response, 'text') else str(response)
        out_content = common_tools.extract_translation(response_text)
        out_content = common_tools.modify_text(out_content)
        with open(filename, 'a', encoding='utf-8') as file:
            file.write(out_content + '\n\n')
    except Exception as e:
        print(f"Error processing chunk: {e}")
        # Wait and retry if it's a rate limit error
        if "429" in str(e):
            print("Rate limit exceeded, waiting 60 seconds...")
            time.sleep(60)
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

def translate(input_filename):
    system_prompt = common_tools.read_file('/Users/Daglas/dalong.llm/dalong.langchain/prompt_translate.md')
    origin_content = common_tools.read_file(input_filename)
    chunks = common_tools.split_text_by_long_newline(origin_content)
    model = genai.GenerativeModel(
        model_name = model_name,
        system_instruction = system_prompt
    )
    process_chunks(model, chunks, '/Users/Daglas/Desktop/output.md')


if __name__ == "__main__":
    initialize_gemini()
    args = parse_arguments()  # Add this line
    start_time = time.time()
    print('waiting...\n')
    split_translate(args)  # Pass args to split_translate
    end_time = time.time()
    elapsed_time = end_time - start_time
    if elapsed_time < 60:
        print(f'Time Used: {elapsed_time:.2f} seconds')
    else:
        print(f'Time Used: {elapsed_time/60:.2f} minutes')