# -*- coding: utf-8 -*-
import os, sys, time, re
from pathlib import Path
import google.generativeai as genai
import argparse
import subprocess
import json
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.utils import get_all_files_from_directory
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


def translate_once(model, origin_content, filename):
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(origin_content + '\n\n')
    try:
        response = model.generate_content(origin_content)
        # Convert response to text first
        response_text = response.text if hasattr(response, 'text') else str(response)
        out_content = common_tools.extract_translation(response_text)
        out_content = common_tools.modify_text(out_content)

        while out_content == "未找到意译内容":
            response = model.generate_content(origin_content)
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

def split_translate(txt_output):
    origin_content = common_tools.read_file(txt_output)
    
    # 如果没有指定输出文件，使用输入文件同目录下相同文件名的 md 文件
    input_filename = os.path.basename(txt_output)
    output_filename = os.path.splitext(input_filename)[0] + '.md'
    output_file = os.path.join(os.path.dirname(txt_output), output_filename)
    split_filename = os.path.splitext(input_filename)[0] + '_origin.md'
    split_file = os.path.join(os.path.dirname(txt_output), split_filename)

    
    model = genai.GenerativeModel(
        model_name = model_name,
        system_instruction = prompt_split
    )
    chunks = common_tools.split_text_by_dot_length(origin_content, 20000)
    split_process_chunks(model, chunks, split_file)
    translate(split_file, output_file)





def extract_text_from_json(json_file, output_txt=None):
    """
    从转录的json文件中提取纯文本内容
    :param json_file: 输入的json文件路径
    :param output_txt: 输出的txt文件路径（可选）
    :return: 输出文件路径
    """
    if output_txt is None:
        output_txt = os.path.splitext(json_file)[0] + '.txt'
    
    try:
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # 提取所有chunks中的text并拼接
        # full_text = ' '.join(chunk['text'] for chunk in data['chunks'])
        # 直接提取text字段
        full_text = data['text']

        with open(output_txt, 'w', encoding='utf-8') as f:
            f.write(full_text)
        
        print(f"文本提取成功！输出文件: {output_txt}")
        return output_txt
    except Exception as e:
        print(f"文本提取失败: {e}")
        return None

def convert_video_to_wav(input_file, output_file=None):
    """
    将视频文件转换为WAV音频
    :param input_file: 输入视频文件路径
    :param output_file: 输出音频文件路径（可选）
    :return: 输出文件路径
    """
    if output_file is None:
        output_file = os.path.splitext(input_file)[0] + '.wav'
    
    command = [
        'ffmpeg',
        '-i', input_file,
        '-ar', '16000',  # 采样率
        '-ac', '1',      # 单声道
        '-c:a', 'pcm_s16le',  # 音频编码
        output_file
    ]
    
    try:
        subprocess.run(command, check=True)
        print(f"转换成功！输出文件: {output_file}")
        return output_file
    except subprocess.CalledProcessError as e:
        print(f"转换失败: {e}")
        return None


def transcribe_audio(input_audio, model_path, output_json=None, language="zh", device="mps", batch_size=4):
    """
    使用insanely-fast-whisper将音频转录为文本
    :param input_audio: 输入音频文件路径
    :param model_path: whisper模型路径
    :param output_json: 输出json文件路径（可选）
    :param language: 语言代码
    :param device: 计算设备（mps/cpu/cuda）
    :param batch_size: 批处理大小
    :return: 输出文件路径
    """
    if output_json is None:
        output_json = os.path.splitext(input_audio)[0] + '.json'
    
    command = [
        'insanely-fast-whisper',
        '--model-name', model_path,
        '--file-name', input_audio,
        '--device', device,
        '--transcript-path', output_json,
        '--batch-size', str(batch_size),
        '--language', language
    ]
    
    try:
        subprocess.run(command, check=True)
        print(f"转录成功！输出文件: {output_json}")
        return output_json
    except subprocess.CalledProcessError as e:
        print(f"转录失败: {e}")
        return None

def video_to_text(input_video, model_path, output_dir=None, language="zh"):
    """
    将视频文件转换为文本
    :param input_video: 输入视频文件路径
    :param model_path: whisper模型路径
    :param output_dir: 输出目录（可选）
    :param language: 语言代码
    :return: 转录结果文件路径
    """
    # 转换视频为音频
    if output_dir:
        base_name = os.path.basename(input_video)
        audio_output = os.path.join(output_dir, os.path.splitext(base_name)[0] + '.wav')
    else:
        audio_output = None
        
    wav_file = convert_video_to_wav(input_video, audio_output)
    if not wav_file:
        return None
        
    # 转录音频为文本
    if output_dir:
        base_name = os.path.basename(wav_file)
        json_output = os.path.join(output_dir, os.path.splitext(base_name)[0] + '.json')
    else:
        json_output = None
        
    result = transcribe_audio(wav_file, model_path, json_output, language=language)
    
    # 删除临时wav文件
    if result and os.path.exists(wav_file):
        try:
            os.remove(wav_file)
            print(f"已删除临时音频文件: {wav_file}")
        except OSError as e:
            print(f"删除音频文件失败: {e}")
    
    # 在原有代码最后添加文本提取
    if result:
        if output_dir:
            base_name = os.path.basename(result)
            txt_output = os.path.join(output_dir, os.path.splitext(base_name)[0] + '.txt')
        else:
            txt_output = None
            
        final_result = extract_text_from_json(result, txt_output)
        return final_result
    
    return txt_output

def video_translate(args):
    txt_output = video_to_text(args.input_video, args.model_path, args.output_dir, args.language)
    split_translate(txt_output)


def parse_arguments():
    """
    解析命令行参数
    :return: 包含参数的命名空间
    """
    parser = argparse.ArgumentParser(description="将视频文件转换为文字转录")
    parser.add_argument('input_video', type=str, help='输入视频文件路径')
    parser.add_argument('--language', type=str, default='en', 
                       help='音频语言代码 (默认: zh/en)')
    parser.add_argument('--model_path', type=str, 
                       default='/Users/Daglas/dalong.modelsets/whisper-large-v3-turbo',
                       help='whisper模型路径')
    parser.add_argument('--output_dir', type=str, 
                       default=None,
                       help='输出目录 (默认: 视频文件所在目录)')
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_arguments()
    # 如果没有指定输出目录，使用视频文件所在目录
    if args.output_dir is None:
        args.output_dir = os.path.dirname(args.input_video)
    video_translate(args)