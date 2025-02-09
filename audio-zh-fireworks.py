# -*- coding:utf-8 -*-
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
import common_tools as common_tools
import time, os, re
import api_key as api
import argparse

api_key = api.fireworks_api_key()
base_url= 'https://api.fireworks.ai/inference/v1'
# model_name='accounts/fireworks/models/deepseek-r1'
model_name='accounts/fireworks/models/deepseek-v3'

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
        out_content = common_tools.modify_text(out_content)
        with open(filename, 'a', encoding='utf-8') as file:
            file.write(out_content + '\n\n')
    except Exception as e:
        print(f"Error during translation: {str(e)}")
        print(f"Original content: {origin_content[:200]}...")  # Print first 200 chars for debugging
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

def translate(args):
    prompt_content = common_tools.read_file(args.prompt_file)
    origin_content = common_tools.read_file(args.input_file)
    prompt = ChatPromptTemplate.from_messages([
        ("user", prompt_content)
    ])
    
    # 如果没有指定输出文件，使用输入文件同目录下相同文件名的 md 文件
    if args.output_file is None:
        input_filename = os.path.basename(args.input_file)
        output_filename = os.path.splitext(input_filename)[0] + '.md'
        args.output_file = os.path.join(os.path.dirname(args.input_file), output_filename)
    
    chunks = common_tools.split_text_by_char_length(origin_content, 800)
    process_chunks(prompt, chunks, args.output_file)

def parse_arguments():
    """
    解析命令行参数
    :return: 包含参数的命名空间
    """
    parser = argparse.ArgumentParser(description="翻译音频转录文本")
    parser.add_argument('input_file', type=str, help='输入文本文件路径')
    parser.add_argument('--output_file', type=str, 
                       default=None,
                       help='输出文件路径')
    parser.add_argument('--prompt_file', type=str,
                       default='/Users/Daglas/dalong.github/dalong.langchain/prompt_translate_audio.md',
                       help='翻译提示词文件路径')
    return parser.parse_args()

if __name__ == '__main__':
    args = parse_arguments()

    start_time = time.time()
    print('waiting...\n')
    translate(args)
    end_time = time.time()
    # 改进时间显示
    elapsed_time = end_time - start_time
    if elapsed_time < 60:
        print(f'Time Used: {elapsed_time:.2f} seconds')
    else:
        print(f'Time Used: {elapsed_time/60:.2f} minutes')


