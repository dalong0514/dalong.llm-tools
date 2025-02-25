# -*- coding: utf-8 -*-
import time
import json


def read_file_content(file_path):
    """读取指定文件内容并返回字符串"""
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

def extract_qa_pairs(content):
    """从内容中提取question和answer"""
    question_start = content.find('[question]:') + len('[question]:')
    question_end = content.find('[index_names]:')
    question = content[question_start:question_end].strip()

    answer_start = content.find('[answer]:') + len('[answer]:')
    answer_end = content.find('[source_datas]:')
    answer = content[answer_start:answer_end].strip()

    return question, answer

def save_to_json(data, output_path):
    """将数据保存为json文件"""
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(data)
    print(data)

def get_fine_tuing_data():
    # 文件路径
    input_path = '/Users/Daglas/dalong.github/dalong.chatrecord/chatrecord-fine-tuning/20250225125253RAG-用一份数据集进行大模型微调fine-tuning需要将数据集分成训练集和测试集建议按什么比例来划分.md'
    output_path = '/Users/Daglas/Desktop/output.json'

    # 获取文件内容
    content = read_file_content(input_path)

    # 提取question和answer
    question, answer = extract_qa_pairs(content)

    # 组装为json并保存
    output = json.dumps({"question": question, "answer": answer}, ensure_ascii=False, indent=2)
    save_to_json(output, output_path)


if __name__ == '__main__':
    start_time = time.time()
    get_fine_tuing_data()
    end_time = time.time()
    print('OK!')
    print('Time Used: ' + str(end_time - start_time) + 's')