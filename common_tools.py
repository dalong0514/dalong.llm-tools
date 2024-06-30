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
        .replace('， ', '，')\
        .replace('。 ', '。')\
        .replace('’', '\'')\
        .replace(': ', '：')\
        .replace(') ', '）')\
        .replace(' (', '（')\
        .replace('  ', ' ')
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


def extract_translation(text):
    # 正则表达式匹配意译部分
    pattern = r'### 意译\s+```(.*?)```'
    match = re.search(pattern, text, re.DOTALL)
    if match:
        return match.group(1).strip()
    return "未找到意译内容"

if __name__ == "__main__":
    modify_text()
