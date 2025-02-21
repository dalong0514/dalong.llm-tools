# -*- coding:utf-8 -*-

import glob, os, time, sys
from vision_parse import VisionParser
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.helper import get_api_key_google
import argparse

os.environ["http_proxy"] = "http://127.0.0.1:7890"
os.environ["https_proxy"] = "http://127.0.0.1:7890"
api_key_google = get_api_key_google()

def vision_parse():
    # Initialize parser with Google Gemini model
    parser = VisionParser(
        model_name="gemini-2.0-flash-exp",
        api_key=get_api_key_google, # Get the Gemini API key from https://aistudio.google.com/app/apikey
        temperature=0.7,
        top_p=0.4,
        image_mode="url",
        detailed_extraction=False, # Set to True for more detailed extraction
        enable_concurrency=True,
    )
    # Convert PDF to markdown
    pdf_path = "/Users/Daglas/Downloads/GB50016-2018建筑设计防火规范_26-27.pdf" # local path to your pdf file
    markdown_pages = parser.convert_pdf(pdf_path)

    # Process results
    for i, page_content in enumerate(markdown_pages):
        print(f"\n--- Page {i+1} ---\n{page_content}")
    # # Initialize parser with OpenAI model
    # parser = VisionParser(
    #     model_name="gpt-4o",
    #     api_key="your-openai-api-key", # Get the OpenAI API key from https://platform.openai.com/api-keys
    #     temperature=0.7,
    #     top_p=0.4,
    #     image_mode="url",
    #     detailed_extraction=False, # Set to True for more detailed extraction
    #     enable_concurrency=True,
    # )

    # # Initialize parser with Azure OpenAI model
    # parser = VisionParser(
    #     model_name="gpt-4o",
    #     image_mode="url",
    #     detailed_extraction=False, # Set to True for more detailed extraction
    #     enable_concurrency=True,
    #     openai_config={
    #         "AZURE_ENDPOINT_URL": "https://****.openai.azure.com/", # replace with your azure endpoint url
    #         "AZURE_DEPLOYMENT_NAME": "*******", # replace with azure deployment name, if needed
    #         "AZURE_OPENAI_API_KEY": "***********", # replace with your azure openai api key
    #         "AZURE_OPENAI_API_VERSION": "2024-08-01-preview", # replace with latest azure openai api version
    #     },
    # )

    # # Initialize parser with DeepSeek model
    # parser = VisionParser(
    #     model_name="deepseek-chat",
    #     api_key="your-deepseek-api-key", # Get the DeepSeek API key from https://platform.deepseek.com/api_keys
    #     temperature=0.7,
    #     top_p=0.4,
    #     image_mode="url",
    #     detailed_extraction=False, # Set to True for more detailed extraction
    #     enable_concurrency=True,
    # )

custom_prompt = """
Strictly preserve markdown formatting during text extraction from scanned document.
"""

def vision_parse_local():
# Initialize parser with Ollama configuration
    parser = VisionParser(
        model_name="llama3.2-vision:11b",
        temperature=0.7,
        top_p=0.6,
        num_ctx=4096,
        image_mode="base64",
        custom_prompt=custom_prompt,
        detailed_extraction=True,
        ollama_config={
            "OLLAMA_NUM_PARALLEL": 8,
            "OLLAMA_REQUEST_TIMEOUT": 240,
        },
        enable_concurrency=True,
    )

    # Convert PDF to markdown
    pdf_path = "/Users/Daglas/Downloads/GB50016-2018建筑设计防火规范_26-27.pdf" # local path to your pdf file
    markdown_pages = parser.convert_pdf(pdf_path)

    # Process results
    for i, page_content in enumerate(markdown_pages):
        print(f"\n--- Page {i+1} ---\n{page_content}")

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
    start_time = time.time()
    vision_parse_local()
    end_time = time.time()
    print('OK!')
    print('Time Used: ' + str(end_time - start_time) + 's')