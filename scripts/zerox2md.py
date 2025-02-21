# -*- coding:utf-8 -*-
import glob, os, time, sys
from pyzerox import zerox
import os
import json
import asyncio
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.helper import get_api_key_google
import argparse

os.environ["http_proxy"] = "http://127.0.0.1:7890"
os.environ["https_proxy"] = "http://127.0.0.1:7890"
api_key_google = get_api_key_google()

### Model Setup (Use only Vision Models) Refer: https://docs.litellm.ai/docs/providers ###

## placeholder for additional model kwargs which might be required for some models
kwargs = {}

## system prompt to use for the vision model
custom_system_prompt = None

# to override
# custom_system_prompt = "For the below pdf page, do something..something..." ## example

###################### Example for OpenAI ######################
# model = "gpt-4o-mini" ## openai model
# os.environ["OPENAI_API_KEY"] = "" ## your-api-key


###################### Example for Azure OpenAI ######################
# model = "azure/gpt-4o-mini" ## "azure/<your_deployment_name>" -> format <provider>/<model>
# os.environ["AZURE_API_KEY"] = "" # "your-azure-api-key"
# os.environ["AZURE_API_BASE"] = "" # "https://example-endpoint.openai.azure.com"
# os.environ["AZURE_API_VERSION"] = "" # "2023-05-15"


###################### Example for Gemini ######################
model = "gemini/gemini-2.0-flash-exp" ## "gemini/<gemini_model>" -> format <provider>/<model>
os.environ['GEMINI_API_KEY'] = api_key_google # your-gemini-api-key


###################### Example for Anthropic ######################
# model="claude-3-opus-20240229"
# os.environ["ANTHROPIC_API_KEY"] = "" # your-anthropic-api-key

###################### Vertex ai ######################
# model = "vertex_ai/gemini-1.5-flash-001" ## "vertex_ai/<model_name>" -> format <provider>/<model>
## GET CREDENTIALS
## RUN ##
# !gcloud auth application-default login - run this to add vertex credentials to your env
## OR ##
# file_path = 'path/to/vertex_ai_service_account.json'
file_path = ""


def zerox_pdf2md():
    # # Load the JSON file
    # with open(file_path, 'r') as file:
    #     vertex_credentials = json.load(file)

    # # Convert to JSON string
    # vertex_credentials_json = json.dumps(vertex_credentials)

    # vertex_credentials=vertex_credentials_json

    ## extra args
    # kwargs = {"vertex_credentials": vertex_credentials}
    kwargs = {"vertex_credentials": ""}

    ###################### For other providers refer: https://docs.litellm.ai/docs/providers ######################

    # Define main async entrypoint
    async def main():
        file_path = "/Users/Daglas/Downloads/GB50016-2018建筑设计防火规范_26-27.pdf" ## local filepath and file URL supported

        ## process only some pages or all
        select_pages = None ## None for all, but could be int or list(int) page numbers (1 indexed)

        output_dir = "/Users/Daglas/Downloads" ## directory to save the consolidated markdown file
        result = await zerox(file_path=file_path, model=model, output_dir=output_dir,
                            custom_system_prompt=custom_system_prompt,select_pages=select_pages, **kwargs)
        return result


    # run the main function:
    result = asyncio.run(main())

    # print markdown result
    print(result)

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
    zerox_pdf2md()
    end_time = time.time()
    print('OK!')
    print('Time Used: ' + str(end_time - start_time) + 's')