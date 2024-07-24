# -*- coding:utf-8 -*-
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage
import time, os, glob
import api_key as api
import common_tools as common_tools
from PIL import Image
from io import BytesIO
import base64

api_key = api.openai_api_key()
# 将API Key保存为环境变量
os.environ["OPENAI_API_KEY"] = api_key
model_name = "gpt-4o-mini"
# model_name = "gpt-4o"

def image_summarize(img_base64, prompt):
    chat = ChatOpenAI(model_name=model_name)
    message = HumanMessage(
        content=[
            {"type": "text", "text": prompt},
            {
                "type": "image_url",
                "image_url": {"url": f"data:image/jpeg;base64,{img_base64}"}
            }
        ]
    )
    response = chat.invoke([message])  # 使用 invoke 方法代替直接调用
    return response.content

def convert_to_base64(pil_image):
    buffered = BytesIO()
    pil_image.save(buffered, format="png")
    img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
    return img_str

def get_sorted_desktop_files(extension="png"):
    # 获取桌面上指定扩展名的所有文件（完整路径）
    desktop_files = glob.glob(f"/Users/Daglas/Desktop/*.{extension}")
    # 对完整路径进行排序
    sorted_files = sorted(desktop_files)
    return sorted_files

def chat_with_one_image(file, out_file_name):
    pil_image = Image.open(file)  # 打开实际的图像文件
    img_base64 = convert_to_base64(pil_image) 
    output = image_summarize(img_base64, "将以下图片中的公式转为LaTeX语法，并以markdown格式打印出来")
    with open(out_file_name, "a", encoding="utf-8") as file:
        file.write(output + "\n\n")

def chat_with_image():
    sorted_png_files = get_sorted_desktop_files("png")
    for file in sorted_png_files:
        chat_with_one_image(file, '/Users/Daglas/Desktop/output.md')

if __name__ == "__main__":
    start_time = time.time()
    print('waiting...\n')
    chat_with_image()
    end_time = time.time()
    print('Time Used: ' + str((end_time - start_time)/60) + 'min')