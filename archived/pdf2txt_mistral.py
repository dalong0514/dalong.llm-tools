# -*- coding: utf-8 -*-
import time, os, sys
import argparse, json
from mistralai import Mistral
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.helper import get_api_key, get_base_url


api_key = get_api_key("mistral")
base_url = get_base_url("mistral")
client = Mistral(api_key=api_key)

from mistralai import Mistral
import os

api_key = os.environ["MISTRAL_API_KEY"]

client = Mistral(api_key=api_key)


def get_out_filename(pdf_path):
    file_name = os.path.basename(pdf_path)
    output_filename = os.path.splitext(file_name)[0] + '.json'
    return os.path.join(os.path.dirname(pdf_path), output_filename)


def ocr_pdf2txt(pdf_path):
    out_filename = get_out_filename(pdf_path)
    uploaded_pdf = client.files.upload(
        file={
            "file_name": pdf_path,
            "content": open(pdf_path, "rb"),
        },
        purpose="ocr"
    )  
    client.files.retrieve(file_id=uploaded_pdf.id)
    signed_url = client.files.get_signed_url(file_id=uploaded_pdf.id)
    ocr_response = client.ocr.process(
        model="mistral-ocr-latest",
        document={
            "type": "document_url",
            "document_url": signed_url.url,
        }
    )
    # Convert response to JSON
    ocr_json = ocr_response.model_dump_json()
    return ocr_json
    

def pdf2txt(pdf_path):
    out_filename = get_out_filename(pdf_path)
    ocr_json = ocr_pdf2txt(pdf_path)
    print(ocr_json)
    with open(ocr_json, 'w', encoding='utf-8') as f:
        f.write(ocr_json)
    # # 提取"markdown"字段并存为列表
    # markdown_list = [page["markdown"] for page in ocr_json["pages"]]

    # # 打印或后续处理
    # for idx, md in enumerate(markdown_list, start=1):
    #     print(f"Page {idx} Markdown:\n{md}\n{'-'*50}")


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
    pdf2txt(args.pdf_path)
    end_time = time.time()
    # 改进时间显示
    elapsed_time = end_time - start_time
    if elapsed_time < 60:
        print(f'Time Used: {elapsed_time:.2f} seconds')
    else:
        print(f'Time Used: {elapsed_time/60:.2f} minutes')