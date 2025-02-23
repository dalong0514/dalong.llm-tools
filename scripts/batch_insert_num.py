# -*- coding:utf-8 -*-

import time

def batch_insert_num(start, end, date, file_path):
    # 使用with语句安全打开文件，并确保最后文件会被正确关闭
    with open(file_path, 'w') as file:
        # 循环生成每个单元
        for number in range(start, end + 1):
            # 格式化序号，确保序号总是两位数字
            formatted_number = f"{number:02}"
            # 写入标题，如 ### 91
            file.write(f"### {formatted_number}\n\n")
            # 写入日期
            file.write(f"{date}\n")
            # file.write(f"阳志平 {date}\n")
            # file.write(f"方军 {date}\n")
            # 写入两个单元之间的5行空格
            file.write("\n" * 5)
        print("Data written successfully.")

# 用户输入的参数
file_path = "/Users/Daglas/dalong.github/dalong.llm-tools/working/temp.md"  # 更改为你的实际路径
start = int(input("Enter start number: "))  # 例如输入91
end = int(input("Enter end number: "))     # 例如输入121
date = input("Enter the date: ")            # 例如输入2024-03-24


if __name__ == '__main__':
    start_time = time.time()
    batch_insert_num(start, end, date, file_path)
    end_time = time.time()
    print('OK!')
    print('Time Used: ' + str(end_time - start_time) + 's')
