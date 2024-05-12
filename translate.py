# -*- coding:utf-8 -*-
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
import time
import api_key as api
import common_tools as common_tools

api_key = api.deepseek_api_key()
base_url= 'https://api.deepseek.com/v1'
model_name='deepseek-chat'

model = ChatOpenAI(
    base_url=base_url,
    api_key=api_key,
    model_name=model_name,
    streaming=True
)

output_parser = StrOutputParser()

def translate_once(origin_content):
    chain = prompt | model | output_parser
    response = chain.invoke({"input": origin_content})
    out_content = common_tools.extract_translation(response)
    out_content = common_tools.modify_text(out_content)
    result = out_content
    # 使用format()方法拼接字符串并加入换行符
#     result = "{}\n\n{}".format(origin_content, out_content)
    return result

# 步骤二：处理内容
def process_chunks(chunks):
    processed_chunks = []
    for chunk in chunks:
        modified_chunk = translate_once(chunk)
        processed_chunks.append(modified_chunk)
    return processed_chunks

def merge_and_save_chunks(chunks, filename):
    merged_text = '\n\n'.join(chunks)
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(merged_text)

def translate():
    prompt_content = common_tools.read_file('./translate_prompt.md')
    origin_content = common_tools.read_file('/Users/Daglas/Desktop/暂存数据.md')
    prompt = ChatPromptTemplate.from_messages([
        ("system", prompt_content),
        ("user", "{input}")
    ])
    chunks = common_tools.split_text_by_length(origin_content, 2000)
    processed_chunks = process_chunks(chunks)
    merge_and_save_chunks(processed_chunks, '/Users/Daglas/Desktop/output.md')

if __name__ == '__main__':
    start_time = time.time()
    print('waiting...\n')
    translate()
    end_time = time.time()
    print('Time Used: ' + str((end_time - start_time)/60) + 'min')