# -*- coding:utf-8 -*-
import sys, time, os, re
import argparse
import pyperclip  # 新增导入
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.utils import capitalize_first_letter


def replace_space(args):
    # 读取输入文件内容
    origin_content = args.input_string
    
    # 剔除冒号、逗号等标点符号，包括|
    cleaned_content = re.sub(r'[：:，,、；;。.！!？?()（）|]', '', origin_content)
    
    # 用空格分割单词并将首字母大写
    words = re.split(r'\s+', cleaned_content.strip())
    capitalized_words = [capitalize_first_letter(word) for word in words if word]

    # 用 - 连接处理后的单词
    replaced_content = '-'.join(capitalized_words)

    # 将结果复制到剪贴板
    pyperclip.copy(replaced_content)
    print("内容已复制到剪贴板")
    


def parse_arguments():
    """
    解析命令行参数
    :return: 包含参数的命名空间
    """
    parser = argparse.ArgumentParser(description="替换空格为横向")
    parser.add_argument('input_string', type=str, help='输入字符串')
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_arguments()

    start_time = time.time()
    print('waiting...\n')
    replace_space(args)
    end_time = time.time()
    # 改进时间显示
    elapsed_time = end_time - start_time
    if elapsed_time < 60:
        print(f'Time Used: {elapsed_time:.2f} seconds')
    else:
        print(f'Time Used: {elapsed_time/60:.2f} minutes')
