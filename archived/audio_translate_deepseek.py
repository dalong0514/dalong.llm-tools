# -*- coding:utf-8 -*-
import sys, time, os, re
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from src.helper import get_api_key, get_base_url
from src.utils import read_prompt_file
import src.utils as common_tools
import argparse

prompt_translate = read_prompt_file("prompt_translate_audio")

api_key = get_api_key("deepseek")
base_url= get_base_url("deepseek")
model_name = "deepseek-chat"

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

def translate():
    input_file = "/Users/Daglas/dalong.github/dalong.llm-tools/working/input.md"
    output_file = "/Users/Daglas/dalong.github/dalong.llm-tools/working/output.md"
    origin_content = common_tools.read_file(input_file)
    prompt = ChatPromptTemplate.from_messages([
        ("system", prompt_translate)
    ])
    
    chunks = common_tools.split_text_by_char_length(origin_content, 800)
    process_chunks(prompt, chunks, output_file)

if __name__ == '__main__':
    start_time = time.time()
    print('waiting...\n')
    translate()
    end_time = time.time()
    # 改进时间显示
    elapsed_time = end_time - start_time
    if elapsed_time < 60:
        print(f'Time Used: {elapsed_time:.2f} seconds')
    else:
        print(f'Time Used: {elapsed_time/60:.2f} minutes')