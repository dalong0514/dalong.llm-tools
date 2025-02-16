# -*- coding:utf-8 -*-

import glob, os, time, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.utils import modify_text, modify_text_en
import argparse

def modify_single_file_content(args):
    file_name = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "working", "temp.md")
    with open(file_name, encoding='UTF-8') as file_obj:
        lines = file_obj.readlines()
    # 对文字处理并写入文件
    with open(file_name, 'w', encoding='UTF-8') as file_obj:
        for line in lines:
            if line != '\n':
                new_content = modify_text_en(line) if args.mode == 'en' else modify_text(line)
                file_obj.write(new_content + "\n\n")

def parse_arguments():
    """
    解析命令行参数
    :return: 包含参数的命名空间
    """
    parser = argparse.ArgumentParser(description="整理文字格式")
    parser.add_argument('--mode', type=str, default='zh', 
                       help='音频语言代码 (默认: zh/en)')
    return parser.parse_args()

if __name__ == '__main__':
    args = parse_arguments()
    start_time = time.time()
    modify_single_file_content(args)
    end_time = time.time()
    print('OK!')
    print('Time Used: ' + str(end_time - start_time) + 's')