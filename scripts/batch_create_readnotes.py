# -*- coding: utf-8 -*-
import time

def batch_create_readnotes():
    first_num = 1
    num = 15
    base_path = "/Users/Daglas/dalong.github/dalong.readnotes/20180101复制书籍"
    book_name = "2018059What-Intelligence-Tests-Miss"
    default_content = "Stanovich，K.E.(2010).2018059What-Intelligence-Tests-Miss.Yale University Press => Preface\n\nStanovich，K.E.(2015).2018059超越智商.(张斌译).机械工业出版社 => 导读"
    
    for i in range(0, num):
        # 格式化序号，确保是4位数字，前两位是批次号，后两位是01
        formatted_num = f"{first_num + i:02}01"
        file_name = f"{book_name}{formatted_num}.md"
        file_path = base_path + "/" + book_name + "/" + file_name
        
        # 创建文件并写入内容
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(default_content)
            
        print(f"已创建文件: {file_name}")

if __name__ == '__main__':
    start_time = time.time()
    print('waiting...\n')
    batch_create_readnotes()
    end_time = time.time()
    # 改进时间显示
    elapsed_time = end_time - start_time
    if elapsed_time < 60:
        print(f'Time Used: {elapsed_time:.2f} seconds')
    else:
        print(f'Time Used: {elapsed_time/60:.2f} minutes')