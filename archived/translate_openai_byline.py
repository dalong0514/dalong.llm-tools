# -*- coding:utf-8 -*-
import time, os, sys, re
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.helper import get_api_key, get_base_url
import common_tools as common_tools

api_key = get_api_key()
base_url= get_base_url()
model_name='claude-3-5-sonnet-20241022'
# model_name='gpt-4o'

model = ChatOpenAI(
    base_url=base_url,
    api_key=api_key,
    model_name=model_name
)

output_parser = StrOutputParser()

def translate_once(prompt, origin_content, filename):
    chain = prompt | model | output_parser
    response = chain.invoke({"input": origin_content})
    out_content = common_tools.extract_translation(response)
    out_content = common_tools.modify_text(out_content)
    with open(filename, 'a', encoding='utf-8') as file:
        file.write('\n' + origin_content + '\n\n' + out_content + '\n')

# 步骤二：批量处理内容
def process_chunks(prompt, chunks, filename):
    for chunk in chunks:
        translate_once(prompt, chunk, filename)

def translate():
    prompt_content = common_tools.read_file('/Users/Daglas/dalong.github/dalong.llm-tools/prompt_translate.md')
    origin_content = common_tools.read_file('/Users/Daglas/Desktop/input.md')
    prompt = ChatPromptTemplate.from_messages([
        ("system", prompt_content),
        ("user", "{input}")
    ])
    chunks = common_tools.split_text_by_long_newline(origin_content)
    process_chunks(prompt, chunks, '/Users/Daglas/Desktop/output.md')

if __name__ == '__main__':
    start_time = time.time()
    print('waiting...\n')
    translate()
    end_time = time.time()
    print('Time Used: ' + str((end_time - start_time)/60) + 'min')