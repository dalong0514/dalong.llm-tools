# -*- coding:utf-8 -*-
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
import common_tools as common_tools
import time, os, re
import api_key as api
import argparse

api_key = api.deepseek_api_key()
base_url= 'https://api.deepseek.com/v1'
model_name='deepseek-chat'

model = ChatOpenAI(
    base_url=base_url,
    api_key=api_key,
    model_name=model_name
)

output_parser = StrOutputParser()

def translate_once(prompt, origin_content, filename):
    chain = prompt | model | output_parser
    response = chain.invoke({"AUDIO_TRANSCRIPT": origin_content})
    out_content = extract_translation(response)
    out_content = common_tools.modify_text(out_content)
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(out_content + '\n\n')

def process_chunks(prompt, chunks, filename):
    for chunk in chunks:
        translate_once(prompt, chunk, filename)

def extract_translation(text):
    pattern = r'<refined_translation>([\s\S]*?)(?:</refined_translation>|\Z)'
    match = re.search(pattern, text, re.DOTALL)
    if match:
        return match.group(1).strip()
    return "未找到意译内容"

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
                       default='/Users/Daglas/dalong.llm/dalong.langchain/prompt_translate_audio.md',
                       help='翻译提示词文件路径')
    return parser.parse_args()

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