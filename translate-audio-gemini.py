# -*- coding:utf-8 -*-
import time, os, re
import api_key as api
import common_tools as common_tools
from vertexai import init
from vertexai.generative_models import (
    GenerativeModel,
    GenerationConfig,
    Part
)

# 初始化 Google Cloud 项目 ID 和区域
init(
    project="gen-lang-client-0760690769",  # 替换为你的 Google Cloud 项目 ID
    location="us-central1"  # 替换为你的区域，例如 "us-central1"
)

# os.environ["GOOGLE_CLOUD_PROJECT"] = "northern-shield-446616-k9"
# os.environ["GOOGLE_CLOUD_PROJECT"] = "gen-lang-client-0760690769"

gemini_model = GenerativeModel(
    "gemini-1.5-flash",
    generation_config=GenerationConfig(temperature=0),
)
chat = gemini_model.start_chat()

def test():
    response = chat.send_message("What is the current exchange rate for USD vs EUR ?")
    answer = response.candidates[0].content.parts[0].text
    print(answer)

# def translate_once(prompt, origin_content, filename):
#     chain = prompt | model | output_parser
#     response = chain.invoke({"AUDIO_TRANSCRIPT": origin_content})
#     out_content = extract_translation(response)
#     out_content = common_tools.modify_text(out_content)
#     with open(filename, 'a', encoding='utf-8') as file:
#         file.write(out_content + '\n\n')

# def process_chunks(prompt, chunks, filename):
#     for chunk in chunks:
#         translate_once(prompt, chunk, filename)

# def extract_translation(text):
#     pattern = r'<refined_translation>([\s\S]*?)(?:</refined_translation>|\Z)'
#     match = re.search(pattern, text, re.DOTALL)
#     if match:
#         return match.group(1).strip()
#     return "未找到意译内容"

# def translate():
#     prompt_content = common_tools.read_file('/Users/Daglas/dalong.llm/dalong.langchain/prompt_translate_audio.md')
#     origin_content = common_tools.read_file('/Users/Daglas/Desktop/input.md')
#     prompt = ChatPromptTemplate.from_messages([
#         ("user", prompt_content)
#     ])
#     chunks = common_tools.split_text_by_char_length(origin_content, 800)
#     process_chunks(prompt, chunks, '/Users/Daglas/Desktop/output.md')

if __name__ == '__main__':
    start_time = time.time()
    print('waiting...\n')
    test()
    end_time = time.time()
    print('Time Used: ' + str((end_time - start_time)/60) + 'min')
