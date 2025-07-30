# -*- coding:utf-8 -*-
import os, time, sys, re
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.helper import get_api_key, get_base_url
from src.utils import read_file
import src.utils as common_tools

system_prompt = common_tools.read_prompt_file("prompt_split_audio")

api_key = get_api_key("zhipu")
base_url= get_base_url("zhipu")
model_name = "glm-4.5-flash"

model = ChatOpenAI(
    base_url=base_url,
    api_key=api_key,
    model_name=model_name,
    streaming=True
)

def split_audio_once(content):
    try:
        prompt_template = ChatPromptTemplate([
            ("system", system_prompt),
            ("user", "{content}")
        ])
        prompt = prompt_template.invoke({"content": content})
        response = model.invoke(prompt)
        out_content = response.content
        return out_content
    except Exception as e:
        print(f"Error processing chunk: {e}")
        # Wait and retry if it's a rate limit error
        if "429" in str(e):
            print("Rate limit exceeded, waiting 30 seconds...")
            time.sleep(30)
            return split_audio_once(content)
        return None

if __name__ == "__main__":
    start_time = time.time()
    print('waiting...\n')
    end_time = time.time()
    elapsed_time = end_time - start_time
    if elapsed_time < 60:
        print(f'Time Used: {elapsed_time:.2f} seconds')
    else:
        print(f'Time Used: {elapsed_time/60:.2f} minutes')
