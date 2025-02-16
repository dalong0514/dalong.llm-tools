# -*- coding: utf-8 -*-
from yt_dlp import YoutubeDL
import os, sys

# 设置代理
PROXY = "http://127.0.0.1:7890"

def download_youtube_video(video_url, output_path="/Users/Daglas/Desktop"):
    """
    从给定的 YouTube 视频链接下载视频文件。

    参数：
    - video_url: str，YouTube 视频链接。
    - output_path: str，保存文件的路径（默认桌面）。
    """
    # 确保输出路径存在
    os.makedirs(output_path, exist_ok=True)
    
    # 配置 youtube-dl 选项
    ydl_opts = {
        'format': 'best',  # 下载最佳质量
        'outtmpl': os.path.join(os.path.abspath(output_path), '%(title)s.%(ext)s'),  # 使用绝对路径
        'proxy': PROXY,  # 设置代理
        'noplaylist': True,  # 不下载播放列表
        'quiet': False,  # 显示进度信息
        'no_warnings': False,  # 显示警告信息
        'retries': 10,  # 增加重试次数
        'socket_timeout': 30,  # 设置超时时间
        'extract_flat': False,
    }

    try:
        with YoutubeDL(ydl_opts) as ydl:
            # 开始下载
            info_dict = ydl.extract_info(video_url, download=True)
            print(f"视频已下载至: {os.path.join(output_path, info_dict['title'] + '.' + info_dict['ext'])}")
    except Exception as e:
        print(f"下载失败: {str(e)}")
        # 如果是网络错误，建议重试
        if 'Connection aborted' in str(e):
            print("网络连接中断，请检查代理设置或网络连接")
            print("建议：1. 检查代理是否可用 2. 稍后重试 3. 更换网络环境")


def batch_download_from_file(file_path, output_path="/Users/Daglas/Desktop"):
    """
    从文件中批量下载 YouTube 视频

    参数：
    - file_path: str，包含 YouTube 链接的文件路径
    - output_path: str，保存文件的路径（默认桌面）
    """
    try:
        # 读取文件中的所有链接
        with open(file_path, 'r') as file:
            urls = file.readlines()
        
        # 去除空白字符并过滤空行
        urls = [url.strip() for url in urls if url.strip()]
        
        # 逐个下载
        for i, url in enumerate(urls, 1):
            print(f"\n正在下载第 {i}/{len(urls)} 个视频: {url}")
            download_youtube_video(url, output_path)
            
        print("\n所有视频下载完成！")
    except Exception as e:
        print(f"批量下载失败: {str(e)}")

if __name__ == "__main__":
    # 设置默认文件路径
    # 设置默认文件路径
    default_list_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'working', 'youtube_download_list.txt')
    
    # 从命令行参数获取文件路径
    list_path = sys.argv[1] if len(sys.argv) > 1 else default_list_path
    
    # 开始批量下载
    batch_download_from_file(list_path)