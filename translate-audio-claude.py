# -*- coding:utf-8 -*-
from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
import time, os, re
import api_key as api
import common_tools as common_tools

api_key = api.claude_api_key()
# 将API Key保存为环境变量
os.environ["ANTHROPIC_API_KEY"] = api_key
model_name='claude-3-5-sonnet-20240620'

model = ChatAnthropic(
    model_name=model_name,
    max_tokens = 8192,
    extra_headers = {"anthropic-beta": "max-tokens-3-5-sonnet-2024-07-15"}
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
    processed_chunks = []
    for chunk in chunks:
        translate_once(prompt, chunk, filename)

def extract_translation(text):
    pattern = r'<refined_translation>([\s\S]*?)(?:</refined_translation>|\Z)'
    match = re.search(pattern, text, re.DOTALL)
    if match:
        return match.group(1).strip()
    return "未找到意译内容"

def translate():
    prompt_content = common_tools.read_file('/Users/Daglas/dalong.llm/dalong.langchain/prompt_translate_audio.md')
    origin_content = common_tools.read_file('/Users/Daglas/Desktop/input.md')
    prompt = ChatPromptTemplate.from_messages([
        ("user", prompt_content)
    ])
    chunks = common_tools.split_text_by_char_length(origin_content, 800)
    process_chunks(prompt, chunks, '/Users/Daglas/Desktop/output.md')

if __name__ == '__main__':
    start_time = time.time()
    print('waiting...\n')
    translate()
    end_time = time.time()
    print('Time Used: ' + str((end_time - start_time)/60) + 'min')
