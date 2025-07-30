# -*- coding:utf-8 -*-
import os, time, sys
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.helper import get_api_key, get_base_url
from src.utils import read_file
import src.utils as common_tools

system_prompt = "merge the line-broken statements into complete sentences. Requirements: 1) Preserve the original text without modifying any content, just merge the sentences! 2) Merge 2-4 sentences into one paragraph. 3) If there are multiple speakers, insert a line break when switching speakers."

api_key = get_api_key("zhipu")
base_url= get_base_url("zhipu")
model_name = "glm-4.5-flash"

model = ChatOpenAI(
    base_url=base_url,
    api_key=api_key,
    model_name=model_name,
    streaming=True
)

def merge_audio_once(content, output_file_name):
    try:
        prompt_template = ChatPromptTemplate([
            ("system", system_prompt),
            ("user", "{content}")
        ])
        prompt = prompt_template.invoke({"content": content})
        response = model.invoke(prompt)
        out_content = response.content
        # # 使用流式方式获取响应
        # out_content = ""
        # for chunk in model.stream(prompt):
        #     content = chunk.content
        #     if content:
        #         print(content, end='', flush=True)  # 流式打印，不换行
        #         out_content += content
        
        # print("\n")  # 打印完成后添加换行
        
        # 写入文件
        with open(output_file_name, 'a', encoding='utf-8') as file:
            file.write(out_content)
    except Exception as e:
        print(f"Error processing chunk: {e}")
        # Wait and retry if it's a rate limit error
        if "429" in str(e):
            print("Rate limit exceeded, waiting 30 seconds...")
            time.sleep(30)
            return merge_audio_once(content, output_file_name)
        return None

def merge_audio():
    file_name = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "working", "input.md")
    output_file_name = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "working", "output.md")
    content = read_file(file_name)
    chunks = common_tools.split_text_by_dot_length(content, 2000)
    for i, chunk in enumerate(chunks):
        print(f"Processing chunk {i+1}/{len(chunks)}")
        merge_audio_once(chunk, output_file_name)
        # Add delay between requests to avoid rate limiting
        time.sleep(1)  

if __name__ == "__main__":
    start_time = time.time()
    print('waiting...\n')
    merge_audio()
    end_time = time.time()
    elapsed_time = end_time - start_time
    if elapsed_time < 60:
        print(f'Time Used: {elapsed_time:.2f} seconds')
    else:
        print(f'Time Used: {elapsed_time/60:.2f} minutes')
