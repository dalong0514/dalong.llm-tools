# -*- coding:utf-8 -*-
import sys, time, os, re
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from src.helper import get_api_key, get_base_url
import src.utils as common_tools
import argparse

prompt_translate = '''
你是一名中文资深编辑，请将以下音频转录文本整理为正式书面语，保持原意和细节的同时，纠正语音识别中出现的错误和口头语，从头开始，不要遗漏任何内容！
音频转录文本中一些常见的词汇如下：`阳志平`、`阳老师`。
以下是一个示例：
原始文稿：
```第一个问题是柯翔的问题关于保持距离里面的一个认知工具叫墙上苍蝇关于墙上苍蝇怎么去理解我们的人的眼睛是向外看的所以很本能的我们就很难能向内看到自己那墙上苍蝇它其实就提供了一种视觉的辅助帮助我们去想象自己成为墙上的一个苍蝇它其实就提供了一种视觉的辅助帮助我们去想象自己成为墙上的一个苍蝇然后来看待自己这样很瞬间的就拉开了我们与自己的距离那如果这种视觉的辅助你觉得比较困难很难去想象那你可以想象自己现在如果是你现在正坐在座位上那么你可以站起身来然后再后退几步看着想象那个你还坐在原来座位上那么你可以站起身来然后再后退几步看着想象那个你还坐在原来的座位上然后后退一步的你去看那个坐在座位上的你你现在怎么去解读这个情境这种方式是通过一个身体的拉开所以这里的核心就是想象一个遥远的自我来看待当下的自己来解读现在的这个情境你就会发现说自己马上从这种情绪当中脱离出来了那如果在什么样的情况下去使用会比较好呢就是在你不断地进行无效的自我对话的时候使用墙上苍蝇这个视角会很快速地帮你去从情绪当中脱离出来第二个问题是海边看海的小组里面一个同学的一个问题情境概念中时空概念和认知工具中提到的时间旅行是一回事吗它其实是涉及到两个不同的概念第一个是情境可攻性的四个子维度情境可攻性的四个子维度情境可攻性其实我们怎么去理解它呢情境可攻性它其实是包含着两个集合它是两个集合的一个交集哪两个集合呢第一个集合呢就是情境它天然所带有的这个属性时间和空间就是属于不论人类是否存在这个情境它诞生的时候就存在的这个属性那第二个集合呢就是我们人类所感知到的这种时间人际人物空间而认知工具里面提到的时间旅行它其实指的是我们人类能够感知到的时间属性所以这中间还是有一点差别的第三个问题还是海边看海小组一个学员的问题他问的是在情绪意图中情境概念中时空概念需要多大的颗粒度表示出来比如说让他感受最困扰的是在工作的时候吵架或者是和恋人谈到某个问题的时候引发的一些情绪问题在这些情境当中时空的这个情境还重要吗这个问题问得非常的好这个问题其实也涉及到说昨天我在给大家去讲怎么去写情境模拟的时候可能有点漏掉了这个部分其实我们在写情境模拟的时候我们要去问自己一个问题我们模拟的这个情境它是否高频比如说你这里说你感受最困扰的就是工作的时候吵架那这里你就可以再问一问自己工作的时候吵架是不是就在某一个时间段它发生呢这个时间段有可能是宽泛的指工作日或者说就是在某一天或者某一个时间段一天当中的某个时间段或者它是在某一天或者某一个时间段,一天当中的某个时间段,或者它是在某个特定的空间里发生的,有可能是在会议当中,有可能是在私下办公室里面,或者是在邮件来往当中,还是在电话当中,有没有一个某个特定的空间里面,你会经常去吵架。还有呢,是不是跟某个特定的同间里面你会经常去吵架还有呢是不是跟某个特定的同事会去吵架或者呢是不是因为某个特定的工作某个特定的项目某个特定的任务找到那个你比较高频的情境如果你发现说你在工作是吵架它好像就是在某个特定的时间某个特定的空间里面经常发生那么很好你就可以把时间和空间的这个信息都放到你的情境模拟当中如果说你发现时间和空间都不是很高频但是人际很高频就是和某个同事或者任劅很高频就是和某个同事或者任务很高频就是因为某一项项目那也可以把这个最高频的情境把它模拟出来那为什么我们在课程当中会说时空信息最好不要省略呢这是从认知科学的角度出发因为时间和空间的这个线索在我们大脑当中都有定向的神经元所以如果有时空信息的模拟它在相应的情境之下还会更快速的去掉去但如果说时间空间发生的不是很高频那也没有关系在我课程当中有提到的袁家景教授他们的团队做了很多的实证研究其实发现说只要背试他使用如果那么的句式去调节情绪他就是要比直接使用认知重评他的效果要好得多得多```
整理后文稿如下：
```
第一个问题是关于柯翔提出的「保持距离」中的一个认知工具 ——「墙上苍蝇」。我们人的眼睛习惯向外看，很难向内审视自己。「墙上苍蝇」提供了一种视觉辅助，帮助我们想象自己变成墙上的苍蝇，从而以旁观者的角度看待自己，瞬间拉开与自我的距离。如果觉得这种视觉想象困难，可以尝试站起身，后退几步，看着原本坐着的自己。这种方式通过身体的距离拉开，核心在于想象一个遥远的自我来解读当下的情境。你会发现自己能迅速从情绪中脱离出来。这种方法适用于当你陷入无效的自我对话时，它可以快速帮你摆脱情绪困扰。
第二个问题来自「海边看海」小组的一位同学，他提问：情境概念中的时空概念和认知工具中提到的时间旅行是一回事吗？这实际上涉及两个不同的概念。情境可供性有四个子维度，它包含两个集合的交集。第一个集合是情境天然具有的属性，如时间和空间，它们在情境诞生时就存在，与人类无关。第二个集合是人类感知到的时间、人际、人物和空间。而认知工具中的「时间旅行」指的是人类能够感知到的时间属性。因此，两者存在差异。
第三个问题同样来自「海边看海」小组的学员，他问的是，在情绪意图中，情境概念中的时空概念需要多大的颗粒度来表示？例如，他感到困扰的是工作时吵架或与恋人谈论某些问题时引发的情绪。在这些情境中，时空概念还重要吗？这个问题非常好，也涉及我昨天在讲解情境模拟时可能遗漏的部分。在写情境模拟时，我们需要问自己：模拟的情境是否高频发生？如果你感到困扰的是工作时吵架，可以进一步思考，吵架是否总在某个时间段发生，比如工作日、某一天、一天中的某个时段？是否发生在某个特定的空间，比如会议室、办公室、邮件往来或电话中？或者，是否与某个特定的同事或因为某个特定的项目任务而吵架？找到你高频发生的情境。如果发现吵架经常发生在特定的时间或空间，那么就应该把时空信息加入情境模拟中。如果时空信息不是高频，但人际或任务是高频，也可以模拟最高频的情境。课程中提到不要省略时空信息，是因为时间和空间线索在大脑中有定向神经元，有时空信息的模拟能更快地触发情境反应。但如果时空并非高频，也没关系。袁家景教授的团队研究表明，使用「如果…… 那么……」句式调节情绪，比直接进行认知重评效果更好。
```
以下为音频转录文本：
<audio_transcript>
{AUDIO_TRANSCRIPT}
</audio_transcript>
严格按照如下格式返回，"[xxx]"表示占位符：
<refined_translation>
[意译结果]
</refined_translation>
'''

api_key = get_api_key()
base_url= get_base_url()
model_name = "deepseek-v3-huoshan"

model = ChatOpenAI(
    base_url=base_url,
    api_key=api_key,
    model_name=model_name
)

output_parser = StrOutputParser()

def translate_once(prompt, origin_content, filename):
    try:
        chain = prompt | model | output_parser
        response = chain.invoke({"AUDIO_TRANSCRIPT": origin_content})
        if not response:
            raise ValueError("Empty response from API")
        out_content = extract_translation(response)
        while out_content == "未找到意译内容":
            response = chain.invoke({"AUDIO_TRANSCRIPT": origin_content})
            out_content = extract_translation(response)
        out_content = common_tools.modify_text(out_content)
        with open(filename, 'a', encoding='utf-8') as file:
            file.write(out_content + '\n\n')
    except Exception as e:
        print(f"Error during translation: {str(e)}")
        print(f"Original content: {origin_content[:200]}...")  # Print first 200 chars for debugging
        print("Rate limit exceeded, waiting 40 seconds...")
        time.sleep(40)
        return translate_once(prompt, origin_content, filename)
        raise

def process_chunks(prompt, chunks, filename):
    for i, chunk in enumerate(chunks):
        print(f"Processing chunk {i+1}/{len(chunks)}")
        if chunk.strip():  # 检查chunk是否为空或仅包含空白字符
            translate_once(prompt, chunk, filename)
        else:
            print(f"Skipping empty chunk {i+1}")
        # Add delay between requests to avoid rate limiting
        time.sleep(1)  # Adjust this value as needed

def extract_translation(text):
    pattern = r'<refined_translation>([\s\S]*?)(?:</refined_translation>|\Z)'
    match = re.search(pattern, text, re.DOTALL)
    if match:
        return match.group(1).strip()
    return "未找到意译内容"

def translate(args):
    origin_content = common_tools.read_file(args.input_file)
    prompt = ChatPromptTemplate.from_messages([
        ("system", prompt_translate)
    ])
    
    # 如果没有指定输出文件，使用输入文件同目录下相同文件名的 md 文件
    if args.output_file is None:
        input_filename = os.path.basename(args.input_file)
        output_filename = os.path.splitext(input_filename)[0] + '.md'
        args.output_file = os.path.join(os.path.dirname(args.input_file), output_filename)
    
    chunks = common_tools.split_text_by_char_length(origin_content, 800)
    process_chunks(prompt, chunks, args.output_file)

def parse_arguments():
    """
    解析命令行参数
    :return: 包含参数的命名空间
    """
    parser = argparse.ArgumentParser(description="翻译音频转录文本")
    parser.add_argument('input_file', type=str, help='输入文本文件路径')
    parser.add_argument('--output_file', type=str, 
                       default=None,
                       help='输出文件路径')
    return parser.parse_args()

if __name__ == '__main__':
    args = parse_arguments()

    start_time = time.time()
    print('waiting...\n')
    translate(args)
    end_time = time.time()
    # 改进时间显示
    elapsed_time = end_time - start_time
    if elapsed_time < 60:
        print(f'Time Used: {elapsed_time:.2f} seconds')
    else:
        print(f'Time Used: {elapsed_time/60:.2f} minutes')