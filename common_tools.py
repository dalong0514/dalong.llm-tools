# -*- coding:utf-8 -*-
import pangu
import re

def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
    return content

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
        .replace('》(', '》（')\
        .replace(')」', '）」')\
        .replace('"。', '」。')
    new_text = new_text.strip()
    new_text = re.sub(r'(?<=[\u4e00-\u9fa5])\s+(?=[\u4e00-\u9fa5])', '', new_text)
    return new_text

def split_text_by_length(text, max_length=1000):
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
    segments = []
    current_segment = ""
    words = text.split('. ')  # 按英文句号分割文本为单词列表

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
    """
    将大段文本按换行符分割成数组，并合并短文本段落。

    参数:
    text (str): 要分割的文本

    返回:
    list: 分割后的文本数组
    """
    segments = text.split('\n\n')
    return segments

def split_text_by_long_newline(text):
    """
    将大段文本按换行符分割成数组，并合并短文本段落。

    参数:
    text (str): 要分割的文本

    返回:
    list: 分割后的文本数组
    """
    segments = text.split('\n\n')
    merged_segments = []
    i = 0
    while i < len(segments):
        current_segment = segments[i]
        # 如果当前段落小于150个字符，且不是最后一个段落
        if len(current_segment) < 160 and i + 1 < len(segments):
            # 合并当前段落和下一个段落
            merged_segment = current_segment + '\n\n' + segments[i + 1]
            merged_segments.append(merged_segment)
            i += 2  # 跳过下一个段落
        else:
            merged_segments.append(current_segment)
            i += 1
    return merged_segments

def extract_translation(text):
    pattern = r'<step3_refined_translation>([\s\S]*?)(?:</step3_refined_translation>|\Z)'
    match = re.search(pattern, text, re.DOTALL)
    if match:
        return match.group(1).strip()
    return "未找到意译内容"


if __name__ == "__main__":
    modify_text()
