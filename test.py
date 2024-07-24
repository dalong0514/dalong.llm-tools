import time
import common_tools as common_tools

def test1():
    origin_content = common_tools.read_file('/Users/Daglas/Desktop/input.md')
    chunks = common_tools.split_text_by_length(origin_content, 1200)
    for chunk in chunks:
        print(chunk + '\n\n\n')

def test():
    origin_content = common_tools.read_file('/Users/Daglas/Desktop/input.md')
    content = common_tools.extract_translation(origin_content)
    print(content)

if __name__ == '__main__':
    start_time = time.time()
    print('waiting...\n')
    test()
    end_time = time.time()
    print('Time Used: ' + str((end_time - start_time)/60) + 'min')