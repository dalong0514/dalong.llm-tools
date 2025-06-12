# -*- coding:utf-8 -*-
import os, time, sys
from google import genai
from google.genai import types
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.helper import get_api_key
import src.utils as utils
import argparse

system_prompt = utils.read_prompt_file("prompt_translate")
# system_prompt = utils.read_prompt_file("prompt_translate_common")

api_key = get_api_key("google")
client = genai.Client(api_key=api_key)

def translate_once(origin_content, filename, mode):
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash-preview-05-20",
            contents=origin_content,
            config=types.GenerateContentConfig(
                system_instruction=system_prompt,
                thinking_config=types.ThinkingConfig(thinking_budget=0)
            )
        )
        # thinkingBudget 必须是介于 0 到 24576 之间的整数
        # Convert response to text first
        response_text = response.text if hasattr(response, 'text') else str(response)
        out_content = utils.extract_translation(response_text)
        while out_content == "未找到意译内容":
            response = client.models.generate_content(
                model="gemini-2.5-flash-preview-05-20",
                contents=origin_content,
                config=types.GenerateContentConfig(
                    system_instruction=system_prompt,
                    thinking_config=types.ThinkingConfig(thinking_budget=0)
                )
            )
            response_text = response.text if hasattr(response, 'text') else str(response)
            out_content = utils.extract_translation(response_text)
        
        if mode == 'zh':
            out_content = utils.modify_text(out_content)
        else:
            out_content = utils.modify_text_en(out_content)
        with open(filename, 'a', encoding='utf-8') as file:
            file.write('\n' + origin_content + '\n\n' + out_content + '\n')
    except Exception as e:
        print(f"Error processing chunk: {e}")
        # Wait and retry if it's a rate limit error
        if "429" in str(e):
            print("Rate limit exceeded, waiting 30 seconds...")
            time.sleep(30)
            return translate_once(origin_content, filename, mode)
        return None

# 步骤二：批量处理内容
def process_chunks(chunks, filename, mode):
    for i, chunk in enumerate(chunks):
        print(f"Processing chunk {i+1}/{len(chunks)}")
        if chunk.strip():  # 检查chunk是否为空或仅包含空白字符
            translate_once(chunk, filename, mode)
        else:
            print(f"Skipping empty chunk {i+1}")
        # Add delay between requests to avoid rate limiting
        time.sleep(1)  # Adjust this value as needed

def translate(mode):
    file_name = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "working", "input.md")
    origin_content = utils.read_file(file_name)
    chunks = utils.split_text_by_long_newline(origin_content)
    process_chunks(chunks, 
                   os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "working", "output.md"), 
                   mode)

def parse_arguments():
    """
    解析命令行参数
    :return: 包含参数的命名空间
    """
    parser = argparse.ArgumentParser(description="翻译文本")
    parser.add_argument('--mode', type=str,
                       default='zh',
                       help='处理模式')
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_arguments()
    mode = args.mode
    start_time = time.time()
    print('waiting...\n')
    translate(mode)
    end_time = time.time()
    elapsed_time = end_time - start_time
    if elapsed_time < 60:
        print(f'Time Used: {elapsed_time:.2f} seconds')
    else:
        print(f'Time Used: {elapsed_time/60:.2f} minutes')