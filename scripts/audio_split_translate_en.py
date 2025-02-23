# -*- coding:utf-8 -*-
import os, sys, time, re
from pathlib import Path
import google.generativeai as genai
import argparse
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import src.utils as common_tools
from src.helper import get_api_key


prompt_split = '''
You are tasked with splitting a transcribed audio text into natural paragraphs. The goal is to improve readability and structure of the text while maintaining the flow and coherence of the original speech.
Your task is to split this text into logical paragraphs. Follow these guidelines:
1. Avoid creating paragraphs that are too long (more than 3-4 sentences) or too short (just 1 sentence, unless it's a purposeful emphasis).
2. Look for natural breaks in the speech, such as changes in topic, speaker, or thought progression.
3. Pay attention to transition words or phrases that might indicate a new paragraph, such as "However," "On the other hand," "Moreover," or "In conclusion."
4. Consider the overall flow and structure of the speech. Each paragraph should contain a main idea or theme.
5. Maintain the original wording and punctuation within each paragraph.
<example>
Welcome, everyone. Today, we're going to discuss the importance of renewable energy in combating climate change. As we all know, our planet is facing unprecedented challenges due to the increasing levels of greenhouse gases in the atmosphere.
Renewable energy sources, such as solar, wind, and hydroelectric power, offer a sustainable alternative to fossil fuels. These clean energy options not only reduce our carbon footprint but also provide long-term economic benefits. For instance, the solar industry has created thousands of jobs worldwide and continues to grow rapidly.
However, transitioning to renewable energy is not without its challenges. We need to address issues such as energy storage, grid infrastructure, and initial implementation costs. Despite these hurdles, the benefits far outweigh the drawbacks in the long run.
</example>

Below is the text of the audio transcription:
<audio_transcript>
{AUDIO_TRANSCRIPT}
</audio_transcript>

Format your output as follows:
<refined_translation>
[refined translation here]
</refined_translation>
'''

system_prompt = '''
你是一位精通简体中文的专业翻译，尤其擅长将专业学术论文翻译成浅显易懂的科普文章。请你帮我将以下英文段落翻译成中文，风格与中文科普读物相似。

规则：
- 翻译时要准确传达原文的事实和背景。
- 即使上意译也要保留原始段落格式，以及保留术语，例如 FLAC，JPEG 等。保留公司缩写，例如 Microsoft, Amazon, OpenAI 等。
- 人名不翻译
- 同时要保留引用的论文，例如 [20] 这样的引用。
- 对于 Figure 和 Table，翻译的同时保留原有格式，例如：“Figure 1: ”翻译为“图 1: ”，“Table 1: ”翻译为：“表 1: ”。
- 全角括号换成半角括号，并在左括号前面加半角空格，右括号后面加半角空格。
- 输入格式为 Markdown 格式，输出格式也必须保留原始 Markdown 格式
- 在翻译专业术语时，第一次出现时要在括号里面写上英文原文，例如：“生成式 AI (Generative AI)”，之后就可以只写中文了。
- 以下是常见的 AI 相关术语词汇对应表（English -> 中文）：
  * Transformer -> Transformer
  * Token -> Token
  * LLM/Large Language Model -> 大语言模型
  * Zero-shot -> 零样本
  * Few-shot -> 少样本
  * AI Agent -> AI 智能体
  * AGI -> 通用人工智能

策略：

分三步进行翻译工作，并打印每步的结果：
1. 根据英文内容直译，保持原有格式，不要遗漏任何信息
2. 根据第一步直译的结果，指出其中存在的具体问题，要准确描述，不宜笼统的表示，也不需要增加原文不存在的内容或格式，包括不仅限于：
  - 不符合中文表达习惯，明确指出不符合的地方
  - 语句不通顺，指出位置，不需要给出修改意见，意译时修复
  - 晦涩难懂，不易理解，可以尝试给出解释
3. 根据第一步直译的结果和第二步指出的问题，重新进行意译，保证内容的原意的基础上，使其更易于理解，更符合中文的表达习惯，同时保持原有的格式不变

严格按照如下格式返回，"[xxx]"表示占位符：

<step1_initial_translation>
[直译结果]
</step1_initial_translation>

<step2_reflection>
[直译的具体问题列表。请对翻译进行反思，并列出一系列具体、有益且富有建设性的改进建议。每条建议都应针对翻译中的某个特定方面。]
</step2_reflection>

<step3_refined_translation>
[意译结果]
</step3_refined_translation>

如果没有输出完整需要不停的输入 continue 直到结束。
'''

api_key = get_api_key("google")
genai.configure(api_key=api_key, transport="rest")
model_name = "gemini-2.0-flash-exp"

def split_translate_once(model, origin_content, filename):
    try:
        response = model.generate_content(origin_content)
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
            return split_translate_once(model, origin_content, filename)
        return None

def split_extract_translation(text):
    pattern = r'<refined_translation>([\s\S]*?)(?:</refined_translation>|\Z)'
    match = re.search(pattern, text, re.DOTALL)
    if match:
        return match.group(1).strip()
    return "整理内容"

# 步骤二：批量处理内容
def split_process_chunks(model, chunks, filename):
    for i, chunk in enumerate(chunks):
        print(f"Processing chunk {i+1}/{len(chunks)}")
        split_translate_once(model, chunk, filename)
        # Add delay between requests to avoid rate limiting
        time.sleep(1)  

def split_translate(args):  # Modified to accept args
    origin_content = common_tools.read_file(args.input_file)
    
    # 如果没有指定输出文件，使用输入文件同目录下相同文件名的 md 文件
    if args.output_file is None:
        input_filename = os.path.basename(args.input_file)
        output_filename = os.path.splitext(input_filename)[0] + '.md'
        args.output_file = os.path.join(os.path.dirname(args.input_file), output_filename)
        split_filename = os.path.splitext(input_filename)[0] + '_origin.md'
        split_file = os.path.join(os.path.dirname(args.input_file), split_filename)
    
    model = genai.GenerativeModel(
        model_name = model_name,
        system_instruction = prompt_split
    )
    chunks = common_tools.split_text_by_dot_length(origin_content, 20000)
    split_process_chunks(model, chunks, split_file)
    translate(split_file, args.output_file)
    # 删除临时md文件
    # if os.path.exists(args.output_file):
    #     try:
    #         os.remove(args.output_file)
    #         print(f"已删除临时分割的md文件: {args.output_file}")
    #     except OSError as e:
    #         print(f"删除临时分割的md文件失败: {e}")

def translate_once(model, origin_content, filename):
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(origin_content + '\n\n')
    try:
        response = model.generate_content(origin_content)
        # Convert response to text first
        response_text = response.text if hasattr(response, 'text') else str(response)
        out_content = common_tools.extract_translation(response_text)
        out_content = common_tools.modify_text(out_content)
        with open(filename, 'a', encoding='utf-8') as file:
            file.write(out_content + '\n\n')
    except Exception as e:
        print(f"Error processing chunk: {e}")
        # Wait and retry if it's a rate limit error
        if "429" in str(e):
            print("Rate limit exceeded, waiting 30 seconds...")
            time.sleep(30)
            return translate_once(model, origin_content, filename)
        return None

# 步骤二：批量处理内容
def process_chunks(model, chunks, filename):
    for i, chunk in enumerate(chunks):
        print(f"Processing chunk {i+1}/{len(chunks)}")
        if chunk.strip():  # 检查chunk是否为空或仅包含空白字符
            translate_once(model, chunk, filename)
        else:
            print(f"Skipping empty chunk {i+1}")
        # Add delay between requests to avoid rate limiting
        time.sleep(1)  # Adjust this value as needed

def translate(input_filename, output_filename):
    origin_content = common_tools.read_file(input_filename)
    chunks = common_tools.split_text_by_long_newline(origin_content)
    model = genai.GenerativeModel(
        model_name = model_name,
        system_instruction = system_prompt
    )
    process_chunks(model, chunks, output_filename)

def parse_arguments():
    """
    解析命令行参数
    :return: 包含参数的命名空间
    """
    parser = argparse.ArgumentParser(description="整理英文版音频转录文本")
    parser.add_argument('input_file', type=str, 
                       default='/Users/Daglas/Desktop/input.md',
                       help='输入文本文件路径')
    parser.add_argument('--output_file', type=str, 
                       default=None,
                       help='输出文件路径')
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_arguments()  # Add this line
    start_time = time.time()
    print('waiting...\n')
    split_translate(args)  # Pass args to split_translate
    end_time = time.time()
    elapsed_time = end_time - start_time
    if elapsed_time < 60:
        print(f'Time Used: {elapsed_time:.2f} seconds')
    else:
        print(f'Time Used: {elapsed_time/60:.2f} minutes')