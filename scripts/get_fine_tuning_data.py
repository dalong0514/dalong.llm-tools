# -*- coding: utf-8 -*-
import time
import json


def get_fine_tuing_data():
    # 获取原始字符串
    # 读取指定文件内容
    file_path = '/Users/Daglas/dalong.github/dalong.chatrecord/chatrecord-fine-tuning/20250225125253RAG-用一份数据集进行大模型微调fine-tuning需要将数据集分成训练集和测试集建议按什么比例来划分.md'
    with open(file_path, 'r', encoding='utf-8') as f:
        original_str = f.read()

    # 提取question和answer
    question_start = original_str.find('[question]:') + len('[question]:')
    question_end = original_str.find('[index_names]:')
    question = original_str[question_start:question_end].strip()

    answer_start = original_str.find('[answer]:') + len('[answer]:')
    answer_end = original_str.find('[source_datas]:')
    answer = original_str[answer_start:answer_end].strip()

    # 组装为json
    output = json.dumps({question: answer}, ensure_ascii=False, indent=2)
    # 将output写入指定文件
    with open('/Users/Daglas/Desktop/output.json', 'w', encoding='utf-8') as f:
        f.write(output)
    print(output)


if __name__ == '__main__':
    start_time = time.time()
    get_fine_tuing_data()
    end_time = time.time()
    print('OK!')
    print('Time Used: ' + str(end_time - start_time) + 's')