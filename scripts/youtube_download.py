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
        # 使用更灵活的格式选择策略
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        'outtmpl': os.path.join(os.path.abspath(output_path), '%(title)s.%(ext)s'),  # 使用绝对路径
        'proxy': PROXY,  # 设置代理
        'noplaylist': True,  # 不下载播放列表
        'quiet': False,  # 显示进度信息
        'no_warnings': False,  # 显示警告信息
        'retries': 10,  # 增加重试次数
        'socket_timeout': 30,  # 设置超时时间
        'extract_flat': False,
        # 添加更多选项以提高兼容性
        'merge_output_format': 'mp4',  # 合并输出格式为mp4
        'writesubtitles': False,  # 不下载字幕
        'writeautomaticsub': False,  # 不下载自动字幕
        'ignoreerrors': False,  # 不忽略错误
        # 处理年龄限制和登录要求
        'age_limit': None,
        # 添加用户代理
        'http_headers': {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
    }

    try:
        with YoutubeDL(ydl_opts) as ydl:
            # 先获取视频信息但不下载
            print(f"正在获取视频信息...")
            info_dict = ydl.extract_info(video_url, download=False)
            
            # 检查是否有可用格式
            if 'formats' in info_dict and info_dict['formats']:
                print(f"视频标题: {info_dict.get('title', 'Unknown')}")
                print(f"视频时长: {info_dict.get('duration', 'Unknown')} 秒")
                print(f"发现 {len(info_dict['formats'])} 种可用格式")
                
                # 开始下载
                print("开始下载...")
                ydl.download([video_url])
                print(f"视频已下载至: {output_path}")
            else:
                print("未找到可用的视频格式")
                return False
                
    except Exception as e:
        error_msg = str(e)
        print(f"下载失败: {error_msg}")
        
        # 根据不同错误类型提供具体建议
        if 'Requested format is not available' in error_msg:
            print("建议：视频格式不可用，尝试使用备用格式...")
            return try_fallback_download(video_url, output_path)
        elif 'Connection aborted' in error_msg:
            print("网络连接中断，请检查代理设置或网络连接")
            print("建议：1. 检查代理是否可用 2. 稍后重试 3. 更换网络环境")
        elif 'Sign in to confirm your age' in error_msg:
            print("视频有年龄限制，无法下载")
        elif 'Private video' in error_msg:
            print("这是私有视频，无法下载")
        elif 'Video unavailable' in error_msg:
            print("视频不可用，可能已被删除或设置为私有")
        else:
            print(f"未知错误: {error_msg}")
        return False
    
    return True

def try_fallback_download(video_url, output_path):
    """
    尝试使用备用格式下载视频
    """
    fallback_formats = [
        'worst[ext=mp4]/worst',  # 最低质量mp4
        'bestvideo+bestaudio/best',  # 最佳视频+音频
        'mp4',  # 任意mp4格式
        '',  # 任意格式
    ]
    
    for fmt in fallback_formats:
        print(f"尝试备用格式: {fmt if fmt else '任意格式'}")
        
        ydl_opts = {
            'format': fmt,
            'outtmpl': os.path.join(os.path.abspath(output_path), '%(title)s.%(ext)s'),
            'proxy': PROXY,
            'noplaylist': True,
            'quiet': True,  # 减少输出噪音
            'retries': 5,
            'socket_timeout': 30,
            'http_headers': {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            }
        }
        
        try:
            with YoutubeDL(ydl_opts) as ydl:
                ydl.download([video_url])
                print(f"使用备用格式下载成功: {fmt if fmt else '任意格式'}")
                return True
        except Exception as e:
            print(f"备用格式 {fmt if fmt else '任意格式'} 失败: {str(e)}")
            continue
    
    print("所有备用格式都失败了")
    return False

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
        
        if not urls:
            print("文件中没有找到有效的YouTube链接")
            return
        
        # 统计下载结果
        success_count = 0
        failed_urls = []
        
        # 逐个下载
        for i, url in enumerate(urls, 1):
            print(f"\n{'='*60}")
            print(f"正在下载第 {i}/{len(urls)} 个视频: {url}")
            print(f"{'='*60}")
            
            try:
                if download_youtube_video(url, output_path):
                    success_count += 1
                    print(f"✅ 第 {i} 个视频下载成功")
                else:
                    failed_urls.append((i, url))
                    print(f"❌ 第 {i} 个视频下载失败")
            except Exception as e:
                failed_urls.append((i, url))
                print(f"❌ 第 {i} 个视频下载异常: {str(e)}")
        
        # 输出最终统计结果
        print(f"\n{'='*60}")
        print("下载完成！统计结果：")
        print(f"总共视频数量: {len(urls)}")
        print(f"成功下载: {success_count}")
        print(f"失败数量: {len(failed_urls)}")
        print(f"成功率: {success_count/len(urls)*100:.1f}%")
        
        if failed_urls:
            print(f"\n失败的视频链接:")
            for idx, url in failed_urls:
                print(f"  {idx}. {url}")
        else:
            print("\n🎉 所有视频都下载成功！")
            
    except FileNotFoundError:
        print(f"错误：找不到文件 {file_path}")
        print("请确认文件路径是否正确")
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