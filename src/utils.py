# -*- coding:utf-8 -*-
import pangu
import re
from pathlib import Path
import os

def read_file(filename):
    """读取指定文件的内容
    
    Args:
        filename (str): 要读取的文件路径
        
    Returns:
        str: 文件的内容
    """
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
    return content

def get_all_files_from_directory(directory_path, file_extension=None):
    """获取指定目录下的所有文件路径，包括子文件夹中的文件
    
    Args:
        directory_path (str): 目录路径
        file_extension (str, optional): 文件扩展名，如"md"。默认为None，表示获取所有文件
    
    Returns:
        list: 包含所有文件路径的列表
    """
    path = Path(directory_path)
    if not path.exists() or not path.is_dir():
        raise ValueError(f"Invalid directory path: {directory_path}")
    
    if file_extension:
        return [str(file) for file in path.rglob(f"*.{file_extension}") if file.is_file()]
    else:
        return [str(file) for file in path.rglob("*") if file.is_file()]


def modify_text(text):
    """处理文字的格式"""
    # 去 \n 是转 pdf 时启用
    # line = line.replace('\n', '')
    text = pangu.spacing_text(text)
    new_text = text.replace(' “', '“')\
        .replace('” ', '”')\
        .replace('“', '「')\
        .replace('”', '」')\
        .replace('・', '·')\
        .replace(', ', '，')\
        .replace('。 ', '。')\
        .replace('’', '\'')\
        .replace(': ', '：')\
        .replace(') ', '）')\
        .replace(' (', '（')\
        .replace('  ', ' ')\
        .replace(' "', '「')\
        .replace('、"', '、「')\
        .replace('" ', '」')\
        .replace('"，', '」，')\
        .replace('"、', '」、')\
        .replace('"（', '」（')\
        .replace(')，', '），')\
        .replace(')。', '）。')\
        .replace(')、', '）、')\
        .replace('》(', '》（')\
        .replace(')」', '）」')\
        .replace(' 。', '。')\
        .replace('"。', '」。')
    new_text = new_text.strip()
    new_text = re.sub(r'(?<=[\u4e00-\u9fa5])\s+(?=[\u4e00-\u9fa5])', '', new_text)
    return new_text

def modify_text_en(line):
    """处理文字的格式"""
    # 去 \n 是转 pdf 时启用
    # line = line.replace('\n', '')
    line = pangu.spacing_text(line)
    new_line = line.replace('“', '"')\
        .replace('”', '"')\
        .replace('・', '·')\
        .replace('， ', '，')\
        .replace('。 ', '。')\
        .replace('’', '\'')\
        .replace('  ', ' ')
    new_line = new_line.strip()
    new_line = re.sub(r'(?<=[\u4e00-\u9fa5])\s+(?=[\u4e00-\u9fa5])', '', new_line)
    return new_line

def split_text_by_length(text, max_length=1000):
    """根据最大长度分割文本，保持段落完整性
    
    Args:
        text (str): 要分割的文本
        max_length (int, optional): 每个段落的最大长度，默认为1000
        
    Returns:
        list: 分割后的文本段落列表
    """
    paragraphs = text.split('\n')  # 根据换行符分割段落
    segments = []
    current_segment = ""

    for paragraph in paragraphs:
        # 检查加上新段落后长度是否超过最大值
        if len(current_segment) + len(paragraph) + 1 > max_length:  # 加1因为段落之间可能需要一个换行符
            segments.append(current_segment)
            current_segment = paragraph  # 开始新的段落
        else:
            # 如果不是第一个段落，加上换行符来连接
            if current_segment:
                current_segment += '\n'
            current_segment += paragraph

    # 确保最后的段落也被加入到segments中
    if current_segment:
        segments.append(current_segment)

    return segments

def split_text_by_char_length(text, max_length=1000):
    """按字符长度分割文本，每个段落不超过指定长度
    
    Args:
        text (str): 要分割的文本
        max_length (int, optional): 每个段落的最大字符数，默认为1000
        
    Returns:
        list: 分割后的文本段落列表
    """
    segments = []
    current_segment = ""

    for char in text:
        # 检查加上新字符后长度是否超过最大值
        if len(current_segment) + 1 > max_length:
            segments.append(current_segment)
            current_segment = char  # 开始新的段落
        else:
            current_segment += char

    # 确保最后的段落也被加入到segments中
    if current_segment:
        segments.append(current_segment)

    return segments


def split_text_by_dot_length(text, max_length=1000):
    """按英文句号分割文本，每个段落不超过指定长度
    
    Args:
        text (str): 要分割的文本
        max_length (int, optional): 每个段落的最大长度，默认为1000
        
    Returns:
        list: 分割后的文本段落列表
    """
    segments = []
    current_segment = ""
    words = text.split('.')  # 按英文句号分割文本为单词列表

    for word in words:
        # 检查加上新单词后长度是否超过最大值
        if len(current_segment) + len(word) + 1 > max_length:  # 加1是考虑空格
            segments.append(current_segment.strip())
            current_segment = word  # 开始新的段落
        else:
            # 如果不是第一个单词，加上空格来连接
            if current_segment:
                current_segment += ' '
            current_segment += word

    # 确保最后的段落也被加入到segments中
    if current_segment:
        segments.append(current_segment.strip())

    return segments

def split_text_by_newline(text):
    """将文本按双换行符分割成段落数组
    
    Args:
        text (str): 要分割的文本
        
    Returns:
        list: 分割后的文本段落列表
    """
    segments = text.split('\n\n')
    return segments

def split_text_by_long_newline(text, min_length=160):
    """将文本按双换行符分割，并合并过短的段落
    
    Args:
        text (str): 要分割的文本
        
    Returns:
        list: 分割后的文本段落列表，其中：
        - 长度小于160字符的相邻段落会被合并
        - 保持段落的语义完整性
    """
    segments = text.split('\n\n')
    merged_segments = []
    i = 0
    while i < len(segments):
        current_segment = segments[i]
        # 如果当前段落小于150个字符，且不是最后一个段落
        if len(current_segment) < min_length and i + 1 < len(segments):
            # 合并当前段落和下一个段落
            merged_segment = current_segment + '\n\n' + segments[i + 1]
            merged_segments.append(merged_segment)
            i += 2  # 跳过下一个段落
        else:
            merged_segments.append(current_segment)
            i += 1
    return merged_segments

def extract_translation(text):
    """从文本中提取翻译内容
    
    Args:
        text (str): 包含翻译标记的文本
        
    Returns:
        str: 提取出的翻译内容，如果未找到则返回"未找到意译内容"
    """
    pattern = r'<step3_refined_translation>([\s\S]*?)(?:</step3_refined_translation>|\Z)'
    match = re.search(pattern, text, re.DOTALL)
    if match:
        return match.group(1).strip()
    return "未找到意译内容"

def read_prompt_file(prompt_filename):
    """读取 prompt 文件夹下的指定 prompt 文件内容
    
    Args:
        prompt_filename (str): 要读取的 prompt 文件名，默认为 prompt_translate
    
    Returns:
        str: 指定 prompt 文件的内容
    """
    # 获取项目根目录路径
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # 构建指定 prompt 文件的完整路径
    prompt_file_path = os.path.join(project_root, "prompt", f"{prompt_filename}.md")
    
    if not os.path.exists(prompt_file_path):
        raise FileNotFoundError(f"文件不存在: {prompt_file_path}")
    
    with open(prompt_file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return content


def capitalize_first_letter(word: str) -> str:
    """将单词首字母转成大写 / Capitalize the first letter of the word.

    Args:
        word (str): 待处理的单词。

    Returns:
        str: 首字母大写后的单词。
    """
    if not word:
        return word

    first_char = word[0]
    if first_char.islower():
        return first_char.upper() + word[1:]
    return word


if __name__ == "__main__":
    print(read_prompt_file("prompt_translate"))
