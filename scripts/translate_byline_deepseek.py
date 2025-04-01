# -*- coding:utf-8 -*-
import os, time, sys
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.helper import get_api_key, get_base_url
from src.utils import read_file, split_text_by_long_newline, modify_text, extract_translation, read_prompt_file
import argparse

system_prompt = read_prompt_file("prompt_translate")

api_key = get_api_key("deepseek")
base_url= get_base_url("deepseek")
model_name = "deepseek-chat"

model = ChatOpenAI(
    base_url=base_url,
    api_key=api_key,
    model_name=model_name
)

def translate_once(model, origin_content, filename, mode):
    try:
        prompt_template = ChatPromptTemplate([
            ("system", system_prompt),
            ("user", "{content}")
        ])
        prompt = prompt_template.invoke({"content": origin_content})
        response = model.invoke(prompt)
        response_text = response.content

        out_content = extract_translation(response_text)
        while out_content == "未找到意译内容":
            response = model.invoke(prompt)
            response_text = response.content
            out_content = extract_translation(response_text)

        out_content = modify_text(out_content)
        with open(filename, 'a', encoding='utf-8') as file:
            # file.write(origin_content + '\n\n' + out_content + '\n')
            file.write(f"{origin_content}\n\n{out_content}\n\n")
    except Exception as e:
        print(f"Error processing chunk: {e}")
        # Wait and retry if it's a rate limit error
        if "429" in str(e):
            print("Rate limit exceeded, waiting 30 seconds...")
            time.sleep(30)
            return translate_once(model, origin_content, filename, mode)
        return None

# 步骤二：批量处理内容
def process_chunks(model, chunks, filename, mode):
    for i, chunk in enumerate(chunks):
        print(f"Processing chunk {i+1}/{len(chunks)}")
        if chunk.strip():  # 检查chunk是否为空或仅包含空白字符
            translate_once(model, chunk, filename, mode)
        else:
            print(f"Skipping empty chunk {i+1}")
        # Add delay between requests to avoid rate limiting
        time.sleep(1)  # Adjust this value as needed

def translate(mode):
    file_name = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "working", "input.md")
    origin_content = read_file(file_name)
    chunks = split_text_by_long_newline(origin_content)
    process_chunks(model, 
                   chunks, 
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