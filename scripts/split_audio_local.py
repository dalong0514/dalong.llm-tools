# -*- coding:utf-8 -*-
import os, time, sys, re
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.helper import get_api_key, get_base_url
from src.utils import read_file
import src.utils as common_tools

system_prompt = common_tools.read_prompt_file("prompt_split_audio")

api_key = get_api_key("local")
base_url= get_base_url("local")
model_name = "gpt-oss:120b"

model = ChatOpenAI(
    base_url=base_url,
    api_key=api_key,
    model_name=model_name,
    streaming=True
)

def split_translate_once(content, output_file_name):
    try:
        prompt_template = ChatPromptTemplate([
            ("system", system_prompt),
            ("user", "{content}")
        ])
        prompt = prompt_template.invoke({"content": content})
        response = model.invoke(prompt)
        out_content = response.content
        # 写入文件
        with open(output_file_name, 'a', encoding='utf-8') as file:
            file.write(out_content)

    except Exception as e:
        print(f"Error processing chunk: {e}")
        # Wait and retry if it's a rate limit error
        if "400" in str(e):
            print("Rate limit exceeded, waiting 30 seconds...")
            time.sleep(30)
            return split_translate_once(content, output_file_name)
        return None

def split_audio_once(content, output_file_name):
    try:
        prompt_template = ChatPromptTemplate([
            ("system", system_prompt),
            ("user", "{content}")
        ])
        prompt = prompt_template.invoke({"content": content})
        response = model.invoke(prompt)
        out_content = response.content
        # 写入文件
        with open(output_file_name, 'a', encoding='utf-8') as file:
            file.write(out_content)
    except Exception as e:
        print(f"Error processing chunk: {e}")
        # Wait and retry if it's a rate limit error
        if "400" in str(e):
            print("Rate limit exceeded, waiting 30 seconds...")
            time.sleep(30)
            return split_audio_once(content, output_file_name)
        return None

def split_audio():
    file_name = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "working", "input.md")
    output_file_name = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "working", "output.md")
    content = read_file(file_name)
    chunks = common_tools.split_text_by_dot_length(content, 5000)
    for i, chunk in enumerate(chunks):
        print(f"Processing chunk {i+1}/{len(chunks)}")
        split_audio_once(chunk, output_file_name)
        # Add delay between requests to avoid rate limiting
        time.sleep(1)  

if __name__ == "__main__":
    start_time = time.time()
    print('waiting...\n')
    split_audio()
    end_time = time.time()
    elapsed_time = end_time - start_time
    if elapsed_time < 60:
        print(f'Time Used: {elapsed_time:.2f} seconds')
    else:
        print(f'Time Used: {elapsed_time/60:.2f} minutes')
