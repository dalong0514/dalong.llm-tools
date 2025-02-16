# -*- coding: utf-8 -*-
import subprocess
import os
import argparse
import json  # 添加导入

def extract_text_from_json(json_file, output_txt=None):
    """
    从转录的json文件中提取纯文本内容
    :param json_file: 输入的json文件路径
    :param output_txt: 输出的txt文件路径（可选）
    :return: 输出文件路径
    """
    if output_txt is None:
        output_txt = os.path.splitext(json_file)[0] + '.txt'
    
    try:
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # 提取所有chunks中的text并拼接
        # full_text = ' '.join(chunk['text'] for chunk in data['chunks'])
        # 直接提取text字段
        full_text = data['text']

        with open(output_txt, 'w', encoding='utf-8') as f:
            f.write(full_text)
        
        print(f"文本提取成功！输出文件: {output_txt}")
        return output_txt
    except Exception as e:
        print(f"文本提取失败: {e}")
        return None

def convert_video_to_wav(input_file, output_file=None):
    """
    将视频文件转换为WAV音频
    :param input_file: 输入视频文件路径
    :param output_file: 输出音频文件路径（可选）
    :return: 输出文件路径
    """
    if output_file is None:
        output_file = os.path.splitext(input_file)[0] + '.wav'
    
    command = [
        'ffmpeg',
        '-i', input_file,
        '-ar', '16000',  # 采样率
        '-ac', '1',      # 单声道
        '-c:a', 'pcm_s16le',  # 音频编码
        output_file
    ]
    
    try:
        subprocess.run(command, check=True)
        print(f"转换成功！输出文件: {output_file}")
        return output_file
    except subprocess.CalledProcessError as e:
        print(f"转换失败: {e}")
        return None

# ... existing code ...

def transcribe_audio(input_audio, model_path, output_json=None, language="zh", device="mps", batch_size=4):
    """
    使用insanely-fast-whisper将音频转录为文本
    :param input_audio: 输入音频文件路径
    :param model_path: whisper模型路径
    :param output_json: 输出json文件路径（可选）
    :param language: 语言代码
    :param device: 计算设备（mps/cpu/cuda）
    :param batch_size: 批处理大小
    :return: 输出文件路径
    """
    if output_json is None:
        output_json = os.path.splitext(input_audio)[0] + '.json'
    
    command = [
        'insanely-fast-whisper',
        '--model-name', model_path,
        '--file-name', input_audio,
        '--device', device,
        '--transcript-path', output_json,
        '--batch-size', str(batch_size),
        '--language', language
    ]
    
    try:
        subprocess.run(command, check=True)
        print(f"转录成功！输出文件: {output_json}")
        return output_json
    except subprocess.CalledProcessError as e:
        print(f"转录失败: {e}")
        return None

def video_to_text(input_video, model_path, output_dir=None, language="zh"):
    """
    将视频文件转换为文本
    :param input_video: 输入视频文件路径
    :param model_path: whisper模型路径
    :param output_dir: 输出目录（可选）
    :param language: 语言代码
    :return: 转录结果文件路径
    """
    # 转换视频为音频
    if output_dir:
        base_name = os.path.basename(input_video)
        audio_output = os.path.join(output_dir, os.path.splitext(base_name)[0] + '.wav')
    else:
        audio_output = None
        
    wav_file = convert_video_to_wav(input_video, audio_output)
    if not wav_file:
        return None
        
    # 转录音频为文本
    if output_dir:
        base_name = os.path.basename(wav_file)
        json_output = os.path.join(output_dir, os.path.splitext(base_name)[0] + '.json')
    else:
        json_output = None
        
    result = transcribe_audio(wav_file, model_path, json_output, language=language)
    
    # 删除临时wav文件
    if result and os.path.exists(wav_file):
        try:
            os.remove(wav_file)
            print(f"已删除临时音频文件: {wav_file}")
        except OSError as e:
            print(f"删除音频文件失败: {e}")
    
    # 在原有代码最后添加文本提取
    if result:
        if output_dir:
            base_name = os.path.basename(result)
            txt_output = os.path.join(output_dir, os.path.splitext(base_name)[0] + '.txt')
        else:
            txt_output = None
            
        final_result = extract_text_from_json(result, txt_output)
        return final_result
    
    return None

def parse_arguments():
    """
    解析命令行参数
    :return: 包含参数的命名空间
    """
    parser = argparse.ArgumentParser(description="将视频文件转换为文字转录")
    parser.add_argument('input_video', type=str, help='输入视频文件路径')
    parser.add_argument('--language', type=str, default='en', 
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
    
    # 如果没有指定输出目录，使用视频文件所在目录
    if args.output_dir is None:
        args.output_dir = os.path.dirname(args.input_video)
    
    video_to_text(args.input_video, args.model_path, args.output_dir, args.language)
