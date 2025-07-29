# -*- coding:utf-8 -*-

import glob, os, time, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def trim_extra_space():
    file_name = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "working", "temp.md")
    with open(file_name, encoding='UTF-8') as file_obj:
        lines = file_obj.readlines()
    
    # 处理空行逻辑
    processed_lines = []
    
    # 1. 跳过开头的所有空行
    start_index = 0
    for i, line in enumerate(lines):
        if line.strip():  # 如果行不为空（去除空白字符后）
            start_index = i
            break
    
    # 2. 处理剩余内容，压缩多个连续空行为一个
    i = start_index
    while i < len(lines):
        current_line = lines[i]
        processed_lines.append(current_line)
        
        # 如果当前行是空行，检查后续连续空行
        if not current_line.strip():
            empty_count = 1
            j = i + 1
            
            # 统计连续空行数量
            while j < len(lines) and not lines[j].strip():
                empty_count += 1
                j += 1
            
            # 如果有多个连续空行（2个或以上），跳过多余的空行
            if empty_count >= 2:
                i = j  # 跳过所有多余的空行
            else:
                i += 1  # 只有一个空行，正常继续
        else:
            i += 1
    
    # 写回文件
    with open(file_name, 'w', encoding='UTF-8') as file_obj:
        file_obj.writelines(processed_lines)


if __name__ == '__main__':
    start_time = time.time()
    trim_extra_space()
    end_time = time.time()
    print('OK!')
    print('Time Used: ' + str(end_time - start_time) + 's')