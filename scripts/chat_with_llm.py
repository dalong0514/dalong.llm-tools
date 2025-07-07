# -*- coding:utf-8 -*-
import os, time, sys
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.helper import get_api_key, get_base_url
from src.utils import read_file, read_prompt_file
import argparse

# system_prompt = read_prompt_file("prompt_chat")

api_key = get_api_key()
base_url= get_base_url()
model_name = "claude-opus-4-20250514"
# model_name = "o3"

model = ChatOpenAI(
    base_url=base_url,
    api_key=api_key,
    model_name=model_name
)

def chat_with_llm():
    file_name = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "working", "input.md")
    output_file_name = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "working", "output.md")
    prompt_content = read_file(file_name)
    try:
        prompt_template = ChatPromptTemplate([
            # ("system", system_prompt),
            ("user", "{content}")
        ])
        prompt = prompt_template.invoke({"content": prompt_content})
        response = model.invoke(prompt)
        out_content = response.content

        # out_content = modify_text(out_content)
        with open(output_file_name, 'a', encoding='utf-8') as file:
            # file.write(origin_content + '\n\n' + out_content + '\n')
            file.write(f"{prompt_content}\n\n{out_content}\n\n")
    except Exception as e:
        print(f"Error processing chunk: {e}")
        # Wait and retry if it's a rate limit error
        if "429" in str(e):
            print("Rate limit exceeded, waiting 30 seconds...")
            time.sleep(30)
            return chat_with_llm(mode)
        return None

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
    chat_with_llm()
    end_time = time.time()
    elapsed_time = end_time - start_time
    if elapsed_time < 60:
        print(f'Time Used: {elapsed_time:.2f} seconds')
    else:
        print(f'Time Used: {elapsed_time/60:.2f} minutes')
