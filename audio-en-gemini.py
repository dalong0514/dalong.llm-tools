# -*- coding:utf-8 -*-
import os, time, re
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
        out_content = extract_translation(response_text)
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

def extract_translation(text):
    pattern = r'<refined_translation>([\s\S]*?)(?:</refined_translation>|\Z)'
    match = re.search(pattern, text, re.DOTALL)
    if match:
        return match.group(1).strip()
    return "整理内容"

# 步骤二：批量处理内容
def process_chunks(model, chunks, filename):
    for i, chunk in enumerate(chunks):
        print(f"Processing chunk {i+1}/{len(chunks)}")
        translate_once(model, chunk, filename)
        # Add delay between requests to avoid rate limiting
        time.sleep(1)  

def translate():
    system_prompt = common_tools.read_file('/Users/Daglas/dalong.llm/dalong.langchain/prompt_translate_audio_en.md')
    origin_content = common_tools.read_file('/Users/Daglas/Desktop/input.md')
    model = genai.GenerativeModel(
        model_name = model_name,
        system_instruction = system_prompt
    )
    chunks = common_tools.split_text_by_dot_length(origin_content, 20000)
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