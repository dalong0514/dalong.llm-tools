import time
import common_tools as common_tools

def test():
    origin_content = common_tools.read_file('/Users/Daglas/Desktop/input.md')
    content = common_tools.split_text_by_newline(origin_content)
    with open('/Users/Daglas/Desktop/output.md', 'w', encoding='utf-8') as file:
        for paragraph in content:
            file.write(paragraph + '\nKK\n')
    print(content)

if __name__ == '__main__':
    start_time = time.time()
    print('waiting...\n')
    test()
    end_time = time.time()
    print('Time Used: ' + str((end_time - start_time)/60) + 'min')