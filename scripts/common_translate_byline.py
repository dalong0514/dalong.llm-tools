# -*- coding:utf-8 -*-
import time, os, sys, re
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.helper import get_api_key, get_base_url
import src.utils as common_tools


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

api_key = get_api_key()
base_url= get_base_url()
model_name='gemini-2.0-flash'

model = ChatOpenAI(
    base_url=base_url,
    api_key=api_key,
    model_name=model_name
)

input_file_name = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "working", "input.md")
out_file_name = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "working", "output.md")

def translate_once(prompt_template, origin_content):
    prompt = prompt_template.invoke({"input": origin_content})
    response = model.invoke(prompt)
    out_content = common_tools.extract_translation(response.content)
    out_content = common_tools.modify_text(out_content)
    while out_content == "未找到意译内容":
        response = model.invoke(prompt)
        out_content = common_tools.extract_translation(response.content)
        out_content = common_tools.modify_text(out_content)
        
    with open(out_file_name, 'a', encoding='utf-8') as file:
        file.write('\n' + origin_content + '\n\n' + out_content + '\n')

# 步骤二：批量处理内容
def process_chunks(prompt_template, chunks):
    for i, chunk in enumerate(chunks):
        print(f"Processing chunk {i+1}/{len(chunks)}")
        if chunk.strip():  # 检查chunk是否为空或仅包含空白字符
            translate_once(prompt_template, chunk)
        else:
            print(f"Skipping empty chunk {i+1}")

def translate():
    origin_content = common_tools.read_file(input_file_name)
    prompt_template = ChatPromptTemplate([
        ("system", system_prompt),
        ("user", "{input}")
    ])
    chunks = common_tools.split_text_by_long_newline(origin_content)
    process_chunks(prompt_template, chunks)

if __name__ == '__main__':
    start_time = time.time()
    print('waiting...\n')
    translate()
    end_time = time.time()
    print('Time Used: ' + str((end_time - start_time)/60) + 'min')