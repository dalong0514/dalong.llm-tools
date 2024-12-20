# -*- coding:utf-8 -*-
# from langchain_openai import ChatOpenAI
# from langchain_core.prompts import ChatPromptTemplate
# from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
import time, os, re
import api_key as api
import common_tools as common_tools


api_key = api.gemini_api_key()
os.environ["GOOGLE_API_KEY"] = api_key
# model_name = 'gemini-1.5-flash'

# output_parser = StrOutputParser()

def test():
    # llm = ChatGoogleGenerativeAI(model=model_name)
    # response = llm.invoke("Sing a ballad of LangChain.")
    # print(response)
    llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-pro"
    )
    messages = [
        (
            "system",
            "You are a helpful assistant that translates English to French. Translate the user sentence.",
        ),
        ("human", "I love programming."),
    ]
    ai_msg = llm.invoke(messages)
    print(ai_msg.content)


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
