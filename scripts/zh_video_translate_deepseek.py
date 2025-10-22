# -*- coding: utf-8 -*-
import sys, time, os, re, json
from http import HTTPStatus
from urllib.parse import urlparse
import requests
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from src.helper import get_api_key, get_base_url
from src.utils import read_prompt_file
import src.utils as common_tools
import argparse

# DashScope / Fun-ASR
try:
    import dashscope
    from dashscope.audio.asr import Transcription
except Exception:
    dashscope = None
    Transcription = None

system_prompt = read_prompt_file("prompt_translate_audio_zh")

api_key = get_api_key("deepseek")
base_url= get_base_url("deepseek")
model_name = "deepseek-chat"

model = ChatOpenAI(
    base_url=base_url,
    api_key=api_key,
    model_name=model_name
)

def translate_once(prompt_template, origin_content, filename):
    try:
        prompt = prompt_template.invoke({"content": origin_content})
        response = model.invoke(prompt)
        out_content = response.content
        out_content = common_tools.modify_text(out_content)
        with open(filename, 'a', encoding='utf-8') as file:
            file.write(out_content + '\n\n')
    except Exception as e:
        print(f"Error during translation: {str(e)}")
        print(f"Original content: {origin_content[:200]}...")  # Print first 200 chars for debugging
        print("Rate limit exceeded, waiting 40 seconds...")
        time.sleep(40)
        return translate_once(prompt_template, origin_content, filename)
        raise

def process_chunks(prompt_template, chunks, filename):
    for i, chunk in enumerate(chunks):
        print(f"Processing chunk {i+1}/{len(chunks)}")
        if chunk.strip():  # 检查chunk是否为空或仅包含空白字符
            translate_once(prompt_template, chunk, filename)
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

def translate(txt_output):
    origin_content = common_tools.read_file(txt_output)
    prompt_template = ChatPromptTemplate([
        ("system", system_prompt),
        ("user", "{content}")
    ])
    
    input_filename = os.path.basename(txt_output)
    output_filename = os.path.splitext(input_filename)[0] + '_origin.md'
    output_file = os.path.join(os.path.dirname(txt_output), output_filename)
    
    chunks = common_tools.split_text_by_char_length(origin_content, 800)
    process_chunks(prompt_template, chunks, output_file)

def _ensure_output_dir_for_url(url: str, output_dir: str | None) -> str:
    """Ensure an output directory exists. For URL inputs, default to working/ if none provided."""
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)
        return output_dir
    # 默认使用 working/ 作为落盘目录
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    out_dir = os.path.join(project_root, 'working')
    os.makedirs(out_dir, exist_ok=True)
    return out_dir


def _extract_text_from_result_json(obj: dict) -> str:
    """Best-effort extraction of full transcript text from Fun-ASR JSON."""
    # 1) 优先 transcripts[*].text 汇总
    transcripts = obj.get('transcripts')
    if isinstance(transcripts, list) and transcripts:
        pieces = []
        for item in transcripts:
            if isinstance(item, dict) and 'text' in item and isinstance(item['text'], str):
                txt = item['text'].strip()
                if txt:
                    pieces.append(txt)
            elif isinstance(item, dict) and 'sentences' in item and isinstance(item['sentences'], list):
                # 次选：拼 sentences[*].text
                sent_texts = []
                for s in item['sentences']:
                    if isinstance(s, dict) and isinstance(s.get('text'), str):
                        t = s['text'].strip()
                        if t:
                            sent_texts.append(t)
                if sent_texts:
                    pieces.append('\n'.join(sent_texts))
        if pieces:
            return '\n'.join(pieces)

    # 2) 顶层 text 兜底
    for key in ('text', 'transcript', 'transcription'):
        if isinstance(obj.get(key), str) and obj.get(key).strip():
            return obj.get(key).strip()

    # 3) 递归扫描，跳过逐词内容
    def scan(any_obj):
        if isinstance(any_obj, dict):
            # 先看当前层
            for key in ('text', 'transcript', 'transcription'):
                val = any_obj.get(key)
                if isinstance(val, str) and val.strip():
                    return val.strip()
            # 深入但跳过 words/sentences 这种碎片级别
            for k, v in any_obj.items():
                if str(k).lower() in ('words', 'word'):
                    continue
                found = scan(v)
                if found:
                    return found
        elif isinstance(any_obj, list):
            for v in any_obj:
                found = scan(v)
                if found:
                    return found
        return None

    t = scan(obj)
    return t if t else ''


def _fun_asr_transcribe_url(file_url: str, output_dir: str | None, model: str = 'fun-asr') -> str | None:
    """
    使用阿里 DashScope Fun-ASR 转写远程音/视频 URL。
    返回保存的 .txt 文件路径；失败返回 None。
    """
    if dashscope is None or Transcription is None:
        print('缺少 dashscope 依赖，请先安装：pip install dashscope')
        return None

    # API Key：优先 DASHSCOPE_API_KEY，兜底 BAILIAN_API_KEY（平台同源）
    api_key = os.getenv('DASHSCOPE_API_KEY') or get_api_key('bailian')
    if not api_key:
        print('缺少 API Key，请在环境变量 DASHSCOPE_API_KEY 或 .env 中配置 BAILIAN_API_KEY')
        return None
    dashscope.api_key = api_key

    # 准备输出目录
    out_dir = _ensure_output_dir_for_url(file_url, output_dir)

    # 提交并等待任务完成
    try:
        task_resp = Transcription.async_call(
            model=model,
            file_urls=[file_url],
            channel_id=[0]
        )
        transcribe_resp = Transcription.wait(task=task_resp.output.task_id)
    except Exception as e:
        print(f'调用 Fun-ASR 失败: {e}')
        return None

    if transcribe_resp.status_code != HTTPStatus.OK:
        print(f'转写失败，HTTP状态: {transcribe_resp.status_code}, message: {getattr(transcribe_resp, "message", "")}')
        return None

    output = getattr(transcribe_resp, 'output', None) or {}
    task_status = output.get('task_status')
    if task_status not in ('SUCCEEDED', 'RUNNING', 'PENDING'):
        print(f'任务状态异常: {task_status}')
        return None

    # 结果可能在 output.results[*].transcription_url 指向的 JSON
    results = output.get('results') or []
    texts: list[str] = []
    json_saved_path = None
    if isinstance(results, list) and results:
        for item in results:
            if not isinstance(item, dict):
                continue
            if item.get('subtask_status') != 'SUCCEEDED':
                code = item.get('code')
                msg = item.get('message')
                if code or msg:
                    print(f'子任务失败: code={code}, message={msg}')
                continue
            t_url = item.get('transcription_url')
            if not t_url:
                continue
            try:
                r = requests.get(t_url, timeout=60)
                r.raise_for_status()
                obj = r.json()
                # 保存原始 JSON 便于排查
                parsed = urlparse(file_url)
                base = os.path.basename(parsed.path) or 'audio'
                stem = os.path.splitext(base)[0]
                json_saved_path = os.path.join(out_dir, f'{stem}_funasr.json')
                with open(json_saved_path, 'w', encoding='utf-8') as f:
                    json.dump(obj, f, ensure_ascii=False, indent=2)
                text = _extract_text_from_result_json(obj)
                if text:
                    texts.append(text)
            except Exception as e:
                print(f'下载或解析转写结果失败: {e}')
                continue

    # 若未从结果文件中取到，尝试任务响应体本身是否含有 text
    if not texts:
        try:
            raw_obj = json.loads(json.dumps(transcribe_resp.output)) if hasattr(transcribe_resp, 'output') else {}
            inline_text = _extract_text_from_result_json(raw_obj)
            if inline_text:
                texts.append(inline_text)
        except Exception:
            pass

    if not texts:
        print('未获取到有效的转写文本')
        return None

    # 写入 .txt 输出
    parsed = urlparse(file_url)
    base = os.path.basename(parsed.path) or 'audio'
    stem = os.path.splitext(base)[0]
    txt_path = os.path.join(out_dir, f'{stem}.txt')
    with open(txt_path, 'w', encoding='utf-8') as f:
        f.write('\n\n'.join(texts))

    return txt_path


def video_translate(args):
    # Fun-ASR 仅支持公网可访问的 URL
    parsed = urlparse(args.input_video)
    if parsed.scheme not in ('http', 'https'):
        print('Fun-ASR 仅支持 http/https 的公网可访问 URL。请先将音频/视频上传到可访问地址（如 OSS），然后将该 URL 作为 input_video 传入。')
        return None

    # 这里不再使用本地 whisper 的 video_to_text，改为调用 Fun-ASR
    # model 可根据需要切换为 'fun-asr-mtl'（多语种）。
    model = 'fun-asr'
    txt_output = _fun_asr_transcribe_url(args.input_video, args.output_dir, model=model)
    if txt_output and os.path.exists(txt_output):
        translate(txt_output)
    else:
        print("视频转文本失败，无法进行翻译")
        return None

def parse_arguments():
    """
    解析命令行参数
    :return: 包含参数的命名空间
    """
    parser = argparse.ArgumentParser(description="将音/视频（URL）转成文本后进行 DeepSeek 翻译")
    parser.add_argument('input_video', type=str, help='输入音/视频的公网 URL（http/https）')
    parser.add_argument('--language', type=str, default='zh', 
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
    # Fun-ASR 模式下，如未指定输出目录，落盘到 working/
    if args.output_dir is None:
        # 若传的是 URL，这里不能使用其路径的目录；改在函数内部默认写入 working/
        pass
    start_time = time.time()
    print('waiting...\n')
    video_translate(args)
    end_time = time.time()
    elapsed_time = end_time - start_time
    if elapsed_time < 60:
        print(f'Time Used: {elapsed_time:.2f} seconds')
    else:
        print(f'Time Used: {elapsed_time/60:.2f} minutes')
