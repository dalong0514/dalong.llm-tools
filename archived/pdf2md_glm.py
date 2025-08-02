# -*- coding: utf-8 -*-
import time, os, sys
import argparse 
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.helper import get_api_key, get_base_url
from gptpdf import parse_pdf


api_key = get_api_key("zhipu")
base_url= get_base_url("zhipu")
## glm-4.1v-thinking-flash的效果耳反而比glm-4.1v-thinking-flashx 好很多，应该是推理起了反作用 2025-08-02
model_name = "glm-4.1v-thinking-flash"
# model_name = "glm-4.1v-thinking-flashx"

def get_out_filename(pdf_path):
    file_name = os.path.basename(pdf_path)
    name_without_extension = os.path.splitext(file_name)[0]
    return '/Users/Daglas/Downloads/' + name_without_extension

def gpt_pdf2txt(pdf_path):
    out_filename = get_out_filename(pdf_path)
    content, image_paths = parse_pdf(pdf_path, 
                                     output_dir=out_filename, 
                                     model=model_name,
                                     base_url=base_url,
                                     api_key=api_key)

def parse_arguments():
    """
    解析命令行参数
    :return: 包含参数的命名空间
    """
    parser = argparse.ArgumentParser(description="PDF to Text Conversion using GPT")
    parser.add_argument('pdf_path', type=str, help='Path to the PDF file')
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_arguments()
    start_time = time.time()
    print('waiting...\n')
    gpt_pdf2txt(args.pdf_path)
    end_time = time.time()
    # 改进时间显示
    elapsed_time = end_time - start_time
    if elapsed_time < 60:
        print(f'Time Used: {elapsed_time:.2f} seconds')
    else:
        print(f'Time Used: {elapsed_time/60:.2f} minutes')