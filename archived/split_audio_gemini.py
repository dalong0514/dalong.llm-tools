# -*- coding:utf-8 -*-
import os, time, sys, re
from google import genai
from google.genai import types
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.helper import get_api_key, get_base_url
from src.utils import read_file
import src.utils as common_tools

system_prompt = common_tools.read_prompt_file("prompt_split_en")


api_key = get_api_key("google")
client = genai.Client(api_key=api_key)
model_name = "gemini-2.5-flash-lite"


def split_translate_once(origin_content, filename):
    try:
        response = client.models.generate_content(
            model=model_name,
            contents=origin_content,
            config=types.GenerateContentConfig(
                system_instruction=system_prompt,
                thinking_config=types.ThinkingConfig(thinking_budget=0)
            )
        )
        # Convert response to text first
        response_text = response.text if hasattr(response, 'text') else str(response)
        out_content = split_extract_translation(response_text)
        with open(filename, 'a', encoding='utf-8') as file:
            file.write(out_content + '\n\n')
    except Exception as e:
        print(f"Error processing chunk: {e}")
        # Wait and retry if it's a rate limit error
        if "429" in str(e):
            print("Rate limit exceeded, waiting 30 seconds...")
            time.sleep(30)
            return split_translate_once(origin_content, filename)
        return None

def split_extract_translation(text):
    pattern = r'<refined_translation>([\s\S]*?)(?:</refined_translation>|\Z)'
    match = re.search(pattern, text, re.DOTALL)
    if match:
        return match.group(1).strip()
    return "整理内容"


def split_audio():
    file_name = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "working", "input.md")
    output_file_name = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "working", "output.md")
    content = read_file(file_name)
    chunks = common_tools.split_text_by_dot_length(content, 5000)
    for i, chunk in enumerate(chunks):
        print(f"Processing chunk {i+1}/{len(chunks)}")
        split_translate_once(chunk, output_file_name)
        # Add delay between requests to avoid rate limiting
        time.sleep(1)  

if __name__ == "__main__":
    start_time = time.time()
    print('waiting...\n')
    split_audio()
    end_time = time.time()
    elapsed_time = end_time - start_time
    if elapsed_time < 60:
        print(f'Time Used: {elapsed_time:.2f} seconds')
    else:
        print(f'Time Used: {elapsed_time/60:.2f} minutes')
