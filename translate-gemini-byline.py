# -*- coding:utf-8 -*-
import os, time
from pathlib import Path
import google.generativeai as genai
from dotenv import load_dotenv
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

def translate_once(model, origin_content, filename):
    try:
        response = model.generate_content(origin_content)
        # Convert response to text first
        response_text = response.text if hasattr(response, 'text') else str(response)
        out_content = common_tools.extract_translation(response_text)
        out_content = common_tools.modify_text(out_content)
        with open(filename, 'a', encoding='utf-8') as file:
            file.write('\n' + origin_content + '\n\n' + out_content + '\n')
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

def translate():
    system_prompt = common_tools.read_file('/Users/Daglas/dalong.llm/dalong.langchain/prompt_translate.md')
    origin_content = common_tools.read_file('/Users/Daglas/Desktop/input.md')
    chunks = common_tools.split_text_by_long_newline(origin_content)
    model = genai.GenerativeModel(
        model_name = model_name,
        system_instruction = system_prompt
    )
    process_chunks(model, chunks, '/Users/Daglas/Desktop/output.md')

if __name__ == "__main__":
    initialize_gemini()
    start_time = time.time()
    print('waiting...\n')
    translate()
    end_time = time.time()
    elapsed_time = end_time - start_time
    if elapsed_time < 60:
        print(f'Time Used: {elapsed_time:.2f} seconds')
    else:
        print(f'Time Used: {elapsed_time/60:.2f} minutes')