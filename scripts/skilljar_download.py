#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Skilljar视频下载脚本
用于下载anthropic.skilljar.com上的Claude Code in Action课程视频
"""

import os
import sys
import re
import json
import time
from urllib.parse import urljoin, urlparse
from yt_dlp import YoutubeDL
import requests
from bs4 import BeautifulSoup

# 代理设置（根据需要修改）
PROXY = "http://127.0.0.1:7890"

# 请求头
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
}

def get_page_content(url):
    """获取页面内容"""
    try:
        session = requests.Session()
        proxies = {'http': PROXY, 'https': PROXY} if PROXY else None
        
        response = session.get(url, headers=HEADERS, proxies=proxies, timeout=30)
        response.raise_for_status()
        return response.text
    except Exception as e:
        print(f"获取页面内容失败: {e}")
        return None

def extract_video_urls(html_content, base_url):
    """从HTML内容中提取视频URL"""
    video_urls = []
    
    if not html_content:
        return video_urls
    
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # 1. 查找JWPlayer配置
    script_tags = soup.find_all('script')
    for script in script_tags:
        if script.string:
            # 查找JWPlayer配置
            jwplayer_patterns = [
                r'videoJsArgs\.assetJWPlayerUrl\s*=\s*["\']([^"\']+)["\']',
                r'jwplayer\(["\']([^"\']+)["\']\)',
                r'content\.jwplatform\.com/players/([^"\']+)',
                r'file["\']?\s*[:=]\s*["\'](https?://[^"\']+\.(?:mp4|m3u8))["\']'
            ]
            
            for pattern in jwplayer_patterns:
                matches = re.findall(pattern, script.string, re.IGNORECASE)
                for match in matches:
                    if match.startswith('http'):
                        video_urls.append(match)
                    else:
                        # 构建JWPlayer URL
                        jw_url = f"https://content.jwplatform.com/players/{match}"
                        video_urls.append(jw_url)
    
    # 2. iframe嵌入
    for iframe in soup.find_all('iframe'):
        src = iframe.get('src', '')
        if src and any(keyword in src.lower() for keyword in ['video', 'player', 'vimeo', 'youtube', 'jwplayer']):
            video_urls.append(urljoin(base_url, src))
    
    # 3. video标签
    for video in soup.find_all('video'):
        src = video.get('src', '')
        if src:
            video_urls.append(urljoin(base_url, src))
        
        for source in video.find_all('source'):
            src = source.get('src', '')
            if src:
                video_urls.append(urljoin(base_url, src))
    
    # 4. 包含视频链接的a标签
    for a in soup.find_all('a', href=True):
        href = a['href']
        if any(ext in href.lower() for ext in ['.mp4', '.m3u8', '.m4v', '.mov', '.avi', '.webm', 'video', 'watch', 'player']):
            video_urls.append(urljoin(base_url, href))
    
    # 5. 其他JavaScript数据
    for script in script_tags:
        if script.string:
            patterns = [
                r'https?://[^"\']*\.(?:mp4|m3u8|m4v|mov|avi|webm)[^"\']*',
                r'src[:=]["\'](https?://[^"\']+)["\']',
                r'videoUrl[:=]["\'](https?://[^"\']+)["\']',
                r'url[:=]["\'](https?://[^"\']+)["\']',
                r'cloudfront\.net[^"\']*\.(?:mp4|m3u8)',
                r'aws[^"\']*\.(?:mp4|m3u8)'
            ]
            
            for pattern in patterns:
                matches = re.findall(pattern, script.string, re.IGNORECASE)
                for match in matches:
                    if not match.startswith('http'):
                        match = 'https://' + match
                    video_urls.append(match)
    
    # 6. 查找所有可能包含视频的URL
    all_urls = []
    for tag in soup.find_all(['a', 'link', 'script', 'img'], href=True):
        all_urls.append(urljoin(base_url, tag['href']))
    for tag in soup.find_all(['script', 'img', 'iframe'], src=True):
        all_urls.append(urljoin(base_url, tag['src']))
    
    # 过滤出可能包含视频的URL
    video_keywords = ['video', 'mp4', 'm3u8', 'm4v', 'mov', 'avi', 'webm', 'stream', 'player', 'jwplayer']
    for url in all_urls:
        if any(keyword in url.lower() for keyword in video_keywords):
            video_urls.append(url)
    
    # 去重
    video_urls = list(set(video_urls))
    return video_urls

def download_video(video_url, output_path="/Users/Daglas/Desktop/skilljar_videos"):
    """下载单个视频"""
    os.makedirs(output_path, exist_ok=True)
    
    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        'outtmpl': os.path.join(os.path.abspath(output_path), '%(title)s.%(ext)s'),
        'proxy': PROXY,
        'noplaylist': True,
        'quiet': False,
        'no_warnings': False,
        'retries': 10,
        'socket_timeout': 30,
        'merge_output_format': 'mp4',
        'http_headers': HEADERS,
        'ignoreerrors': True,  # 忽略错误继续下载其他视频
    }
    
    try:
        print(f"正在下载: {video_url}")
        with YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(video_url, download=True)
            if info_dict:
                print(f"✅ 下载成功: {info_dict.get('title', 'Unknown')}")
                return True
            else:
                print(f"❌ 无法获取视频信息")
                return False
    except Exception as e:
        print(f"❌ 下载失败: {e}")
        return False

def download_skilljar_course(course_url, output_path="/Users/Daglas/Desktop/skilljar_videos"):
    """下载整个Skilljar课程的视频"""
    print(f"开始处理课程页面: {course_url}")
    
    # 获取页面内容
    html_content = get_page_content(course_url)
    if not html_content:
        print("无法获取课程页面内容")
        return
    
    # 保存HTML内容用于调试
    debug_html_path = os.path.join(output_path, "debug_page.html")
    os.makedirs(output_path, exist_ok=True)
    with open(debug_html_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    print(f"页面内容已保存到: {debug_html_path}")
    
    # 提取视频URL
    video_urls = extract_video_urls(html_content, course_url)
    
    if not video_urls:
        print("未找到视频链接，尝试分析页面结构...")
        
        # 尝试从HTML中提取更多信息
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # 查找课程章节或模块
        course_modules = []
        for div in soup.find_all('div', class_=True):
            classes = div.get('class', [])
            if any(keyword in ' '.join(classes).lower() for keyword in ['module', 'lesson', 'chapter', 'course', 'video']):
                course_modules.append(div)
        
        print(f"找到 {len(course_modules)} 个可能的课程模块")
        
        # 如果还是找不到，建议手动分析
        print("\n建议手动分析方法:")
        print("1. 打开浏览器开发者工具 (F12)")
        print("2. 访问课程页面")
        print("3. 在网络(Network)标签页中筛选mp4/m3u8文件")
        print("4. 找到视频URL后，可以手动添加到下载列表中")
        
        # 创建手动下载模板
        manual_list_path = os.path.join(output_path, "manual_video_list.txt")
        with open(manual_list_path, 'w', encoding='utf-8') as f:
            f.write("# 手动添加视频URL到这里，每行一个\n")
            f.write("# 示例: https://example.com/video.mp4\n")
        print(f"手动下载模板已创建: {manual_list_path}")
        return
    
    print(f"找到 {len(video_urls)} 个可能的视频链接:")
    for i, url in enumerate(video_urls, 1):
        print(f"  {i}. {url}")
    
    # 保存URL列表
    url_list_path = os.path.join(output_path, "video_urls.txt")
    with open(url_list_path, 'w', encoding='utf-8') as f:
        for url in video_urls:
            f.write(f"{url}\n")
    print(f"视频URL列表已保存到: {url_list_path}")
    
    # 自动继续下载（非交互模式）
    print("\n开始自动下载...")
    
    # 下载所有视频
    success_count = 0
    failed_urls = []
    
    for i, video_url in enumerate(video_urls, 1):
        print(f"\n{'='*60}")
        print(f"正在下载第 {i}/{len(video_urls)} 个视频")
        print(f"URL: {video_url}")
        print(f"{'='*60}")
        
        if download_video(video_url, output_path):
            success_count += 1
            print(f"✅ 第 {i} 个视频下载成功")
        else:
            failed_urls.append((i, video_url))
            print(f"❌ 第 {i} 个视频下载失败")
        
        # 添加延迟避免请求过于频繁
        time.sleep(2)
    
    # 输出统计结果
    print(f"\n{'='*60}")
    print("下载完成！统计结果：")
    print(f"总共视频数量: {len(video_urls)}")
    print(f"成功下载: {success_count}")
    print(f"失败数量: {len(failed_urls)}")
    print(f"成功率: {success_count/len(video_urls)*100:.1f}%")
    
    if failed_urls:
        print(f"\n失败的视频链接:")
        for idx, url in failed_urls:
            print(f"  {idx}. {url}")

def main():
    """主函数"""
    # Skilljar课程URL
    course_url = "https://anthropic.skilljar.com/claude-code-in-action"
    
    # 输出目录
    output_path = "/Users/Daglas/Desktop/skilljar_videos"
    
    # 从命令行参数获取自定义路径
    if len(sys.argv) > 1:
        output_path = sys.argv[1]
    
    print("Skilljar视频下载工具")
    print("=" * 50)
    print(f"课程URL: {course_url}")
    print(f"输出目录: {output_path}")
    print("=" * 50)
    
    # 开始下载
    download_skilljar_course(course_url, output_path)

if __name__ == "__main__":
    main()