# -*- coding: utf-8 -*-
import os, sys, time, re
import argparse
from pocketflow import Node, Flow
from openai import OpenAI
from src.helper import get_api_key, get_base_url


api_key = get_api_key("deepseek")
base_url= get_base_url("deepseek")
model_name = "deepseek-chat"


def call_llm(messages):
    client = OpenAI(api_key=api_key, base_url=base_url)
    
    response = client.chat.completions.create(
        model=model_name,
        messages=messages
    )
    
    return response.choices[0].message.content


class ChatNode(Node):
    def prep(self, shared):
        # 获取用户输入
        user_input = input("\nYou: ")
        
        # 检查是否退出
        if user_input.lower() == 'exit':
            return None
        
        # 返回用户消息
        return {"role": "user", "content": user_input}

    def exec(self, message):
        if message is None:
            return None
        
        # 调用 LLM 获取响应
        response = call_llm([message])
        return response

    def post(self, shared, prep_res, exec_res):
        if prep_res is None or exec_res is None:
            print("\nGoodbye!")
            return None
        
        # 打印助手响应
        print(f"\nAssistant: {exec_res}")
        
        # 继续对话
        return "continue"


def translate_video(args):
    # Create the flow with self-loop
    chat_node = ChatNode()
    chat_node - "continue" >> chat_node  # Loop back to continue conversation

    flow = Flow(start=chat_node)


def parse_arguments():
    """
    解析命令行参数
    :return: 包含参数的命名空间
    """
    parser = argparse.ArgumentParser(description="将视频文件转换为文字转录")
    parser.add_argument('input_video', type=str, help='输入视频文件路径')
    parser.add_argument('--language', type=str, default='en', 
                       help='音频语言代码 (默认: zh/en)')
    parser.add_argument('--model_path', type=str, 
                       default='/Users/Daglas/dalong.modelsets/whisper-large-v3-turbo',
                       help='whisper模型路径')
    parser.add_argument('--output_dir', type=str, 
                       default=None,
                       help='输出目录 (默认: 视频文件所在目录)')
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_arguments()
    # 如果没有指定输出目录，使用视频文件所在目录
    if args.output_dir is None:
        args.output_dir = os.path.dirname(args.input_video)
    translate_video(args)