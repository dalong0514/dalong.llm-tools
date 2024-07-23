import time
import common_tools as common_tools

def test():
    origin_content = common_tools.read_file('/Users/Daglas/Desktop/input.md')
    chunks = common_tools.split_text_by_char_length(origin_content, 1500)
    print(chunks)

if __name__ == '__main__':
    start_time = time.time()
    print('waiting...\n')
    test()
    end_time = time.time()
    print('Time Used: ' + str((end_time - start_time)/60) + 'min')