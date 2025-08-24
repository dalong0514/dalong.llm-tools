#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Skilljar视频下载脚本
用于下载anthropic.skilljar.com上的Claude Code in Action课程视频
支持下载整个课程或单个页面视频

用法:
1. 下载整个课程: python skilljar_download.py [输出目录]
2. 下载单个页面: python skilljar_download.py [页面URL] [输出目录]

示例:
- 下载整个课程到默认目录: python skilljar_download.py
- 下载整个课程到指定目录: python skilljar_download.py /path/to/output
- 下载单个页面: python skilljar_download.py https://anthropic.skilljar.com/claude-code-in-action/303235 /path/to/output
"""

import os
import sys
import re
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

def extract_lesson_urls(html_content, base_url):
    """从HTML内容中提取所有课程章节的URL"""
    lesson_urls = []
    
    if not html_content:
        return lesson_urls
    
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # 方法1: 查找data-url属性的课程链接
    for li in soup.find_all('li', {'data-url': True}):
        data_url = li.get('data-url', '')
        if data_url and '/claude-code-in-action/' in data_url:
            full_url = urljoin(base_url, data_url)
            if full_url not in lesson_urls:
                lesson_urls.append(full_url)
    
    # 方法2: 查找课程章节链接
    curriculum_selectors = [
        'a[href*="/lesson/"]',
        'a[href*="/module/"]', 
        'a[href*="/chapter/"]',
        '.lesson-row a',
        '.lesson-video a',
        '.dp-curriculum a',
        '#curriculum-list a',
        'li.lesson-video a',
        'li[class*="lesson-"] a'
    ]
    
    for selector in curriculum_selectors:
        for link in soup.select(selector):
            href = link.get('href', '')
            if href and ('/lesson/' in href or '/claude-code-in-action/' in href):
                full_url = urljoin(base_url, href)
                if full_url not in lesson_urls:
                    lesson_urls.append(full_url)
    
    # 方法3: 查找所有可能的链接
    for a in soup.find_all('a', href=True):
        href = a['href']
        if ('/lesson/' in href or '/claude-code-in-action/' in href) and not href.startswith('#'):
            full_url = urljoin(base_url, href)
            if full_url not in lesson_urls:
                lesson_urls.append(full_url)
    
    # 方法4: 查找JavaScript中的课程数据
    script_tags = soup.find_all('script')
    for script in script_tags:
        if script.string:
            # 查找课程URL模式
            patterns = [
                r'/claude-code-in-action/\d+',
                r'lesson/[\w-]+',
                r'https?://[^"\']*skilljar[^"\']*/claude-code-in-action[^"\']*'
            ]
            
            for pattern in patterns:
                matches = re.findall(pattern, script.string, re.IGNORECASE)
                for match in matches:
                    if match.startswith('http'):
                        lesson_urls.append(match)
                    else:
                        full_url = urljoin(base_url, match)
                        if full_url not in lesson_urls:
                            lesson_urls.append(full_url)
    
    return list(set(lesson_urls))

def extract_video_urls_from_lesson(html_content, base_url, lesson_number):
    """从单个课程页面提取视频URL"""
    video_urls = []
    
    if not html_content:
        return video_urls
    
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # 保存课程页面内容用于调试
    debug_dir = "/tmp/skilljar_debug"
    os.makedirs(debug_dir, exist_ok=True)
    debug_file = os.path.join(debug_dir, f"lesson_{lesson_number}.html")
    with open(debug_file, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    # 1. 查找JWPlayer配置
    script_tags = soup.find_all('script')
    for script in script_tags:
        if script.string:
            # 查找JWPlayer配置
            jwplayer_patterns = [
                r'videoJsArgs\.assetJWPlayerUrl\s*=\s*["\']([^"\']+)["\']',
                r'jwplayer\(["\']([^"\']+)["\']\)',
                r'content\.jwplatform\.com/players/([^"\']+)',
                r'file["\']?\s*[:=]\s*["\'](https?://[^"\']+\.(?:mp4|m3u8))["\']',
                r'videoUrl["\']?\s*[:=]\s*["\'](https?://[^"\']+)["\']',
                r'jwplayer\(\s*["\']([^"\']+)["\']\s*\)'
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
    
    # 2. 查找视频标题
    video_title = "Unknown"
    title_selectors = ['h1', 'h2', 'h3', '.video-title', '.lesson-title', '.title']
    for selector in title_selectors:
        title_elem = soup.select_one(selector)
        if title_elem and title_elem.text.strip():
            video_title = title_elem.text.strip()
            break
    
    # 3. iframe嵌入
    for iframe in soup.find_all('iframe'):
        src = iframe.get('src', '')
        if src and any(keyword in src.lower() for keyword in ['video', 'player', 'vimeo', 'youtube', 'jwplayer']):
            video_urls.append(urljoin(base_url, src))
    
    # 4. video标签
    for video in soup.find_all('video'):
        src = video.get('src', '')
        if src:
            video_urls.append(urljoin(base_url, src))
        
        for source in video.find_all('source'):
            src = source.get('src', '')
            if src:
                video_urls.append(urljoin(base_url, src))
    
    # 5. 其他JavaScript数据
    for script in script_tags:
        if script.string:
            patterns = [
                r'https?://[^"\']*\.(?:mp4|m3u8|m4v|mov|avi|webm)[^"\']*',
                r'src[:=]["\'](https?://[^"\']+)["\']',
                r'url[:=]["\'](https?://[^"\']+)["\']',
                r'cloudfront\.net[^"\']*\.(?:mp4|m3u8)',
                r'aws[^"\']*\.(?:mp4|m3u8)',
                r'https?://[^"\']*skilljar[^"\']*\.(?:mp4|m3u8)'
            ]
            
            for pattern in patterns:
                matches = re.findall(pattern, script.string, re.IGNORECASE)
                for match in matches:
                    if not match.startswith('http'):
                        match = 'https://' + match
                    video_urls.append(match)
    
    # 添加视频标题信息到URL（用于调试）
    if video_urls and video_title != "Unknown":
        video_urls = [f"{url}?title={video_title}" for url in video_urls]
    
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
        'retries': 3,  # 减少重试次数避免长时间等待
        'socket_timeout': 15,  # 缩短超时时间
        'merge_output_format': 'mp4',
        'http_headers': HEADERS,
        'ignoreerrors': True,  # 忽略错误继续下载其他视频
        'timeout': 30,  # 总超时时间
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
        error_msg = str(e)
        if "timed out" in error_msg or "timeout" in error_msg:
            print(f"⏰ 下载超时: {video_url}")
        elif "404" in error_msg or "Not Found" in error_msg:
            print(f"🔍 视频不存在: {video_url}")
        else:
            print(f"❌ 下载失败: {error_msg}")
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
    
    # 提取所有课程章节URL
    lesson_urls = extract_lesson_urls(html_content, course_url)
    
    if not lesson_urls:
        print("未找到课程章节链接，尝试直接提取视频...")
        # 回退到直接提取视频的方法
        video_urls = extract_video_urls_from_lesson(html_content, course_url)
        
        if not video_urls:
            print("未找到视频链接，建议手动分析...")
            print("\n建议手动分析方法:")
            print("1. 打开浏览器开发者工具 (F12)")
            print("2. 访问课程页面")
            print("3. 在网络(Network)标签页中筛选mp4/m3u8文件")
            print("4. 找到视频URL后，可以手动添加到下载列表中")
            
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
        
        # 下载视频
        download_videos(video_urls, output_path)
        return
    
    print(f"找到 {len(lesson_urls)} 个课程章节:")
    for i, url in enumerate(lesson_urls, 1):
        print(f"  {i}. {url}")
    
    # 保存课程章节列表
    lesson_list_path = os.path.join(output_path, "lesson_urls.txt")
    with open(lesson_list_path, 'w', encoding='utf-8') as f:
        for url in lesson_urls:
            f.write(f"{url}\n")
    print(f"课程章节列表已保存到: {lesson_list_path}")
    
    # 遍历每个课程章节，提取并下载视频
    all_video_urls = []
    
    for i, lesson_url in enumerate(lesson_urls, 1):
        print(f"\n处理第 {i}/{len(lesson_urls)} 个课程章节:")
        print(f"URL: {lesson_url}")
        
        # 获取课程章节页面内容
        lesson_html = get_page_content(lesson_url)
        if not lesson_html:
            print(f"❌ 无法获取课程章节页面: {lesson_url}")
            continue
        
        # 提取视频URL
        video_urls = extract_video_urls_from_lesson(lesson_html, lesson_url, i)
        
        if video_urls:
            print(f"  找到 {len(video_urls)} 个视频链接")
            for video_url in video_urls:
                if video_url not in all_video_urls:
                    all_video_urls.append(video_url)
                    print(f"    - {video_url}")
        else:
            print("  未找到视频链接")
            
        # 检查是否有视频处理中的消息
        if "video is still being processed" in lesson_html:
            print("  ⚠️  视频仍在处理中，可能需要等待或需要认证")
        
        # 添加延迟避免请求过于频繁
        time.sleep(1)
    
    if not all_video_urls:
        print("\n在所有课程章节中均未找到视频链接")
        return
    
    print(f"\n总共找到 {len(all_video_urls)} 个视频链接:")
    for i, url in enumerate(all_video_urls, 1):
        print(f"  {i}. {url}")
    
    # 保存视频URL列表
    video_list_path = os.path.join(output_path, "video_urls.txt")
    with open(video_list_path, 'w', encoding='utf-8') as f:
        for url in all_video_urls:
            f.write(f"{url}\n")
    print(f"视频URL列表已保存到: {video_list_path}")
    
    # 下载所有视频
    download_videos(all_video_urls, output_path)

def download_videos(video_urls, output_path):
    """下载视频列表"""
    print("\n开始自动下载...")
    
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
    
    # 提供关于受保护内容的建议
    if success_count == 0 and len(video_urls) > 0:
        print(f"\n{'='*60}")
        print("⚠️  重要提示：")
        print("所有视频下载失败，可能是因为：")
        print("1. 视频内容受保护，需要用户认证")
        print("2. 视频仍在处理中（显示'video is still being processed'）")
        print("3. 需要有效的用户会话或cookie")
        print("4. 视频URL需要动态生成或授权")
        print("\n建议手动访问课程页面检查视频访问权限")

def download_single_page_video(page_url, output_path="/Users/Daglas/Desktop/skilljar_videos"):
    """下载单个网页中的视频"""
    print(f"开始处理单个页面: {page_url}")
    
    # 获取页面内容
    html_content = get_page_content(page_url)
    if not html_content:
        print("无法获取页面内容")
        return
    
    # 保存HTML内容用于调试
    debug_html_path = os.path.join(output_path, "debug_single_page.html")
    os.makedirs(output_path, exist_ok=True)
    with open(debug_html_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    print(f"页面内容已保存到: {debug_html_path}")
    
    # 直接提取视频URL
    video_urls = extract_video_urls_from_lesson(html_content, page_url, 1)
    
    if not video_urls:
        print("未找到视频链接，尝试直接提取视频...")
        
        # 尝试其他提取方法
        # soup = BeautifulSoup(html_content, 'html.parser')  # 暂时注释掉未使用的变量
        
        # 检查是否有视频处理中的消息
        if "video is still being processed" in html_content:
            print("⚠️  视频仍在处理中，可能需要等待或需要认证")
        
        print("\n建议手动分析方法:")
        print("1. 打开浏览器开发者工具 (F12)")
        print("2. 访问页面")
        print("3. 在网络(Network)标签页中筛选mp4/m3u8文件")
        print("4. 找到视频URL后，可以手动添加到下载列表中")
        
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
    url_list_path = os.path.join(output_path, "single_page_video_urls.txt")
    with open(url_list_path, 'w', encoding='utf-8') as f:
        for url in video_urls:
            f.write(f"{url}\n")
    print(f"视频URL列表已保存到: {url_list_path}")
    
    # 下载视频
    download_videos(video_urls, output_path)

def main():
    """主函数"""
    # 默认输出目录
    output_path = "/Users/Daglas/Desktop/skilljar_videos"
    
    # 解析命令行参数
    if len(sys.argv) > 1:
        # 第一个参数可能是URL或输出路径
        first_arg = sys.argv[1]
        
        if first_arg.startswith('http'):
            # 第一个参数是URL
            target_url = first_arg
            
            # 检查是否有第二个参数（输出路径）
            if len(sys.argv) > 2:
                output_path = sys.argv[2]
        else:
            # 第一个参数是输出路径，使用默认URL
            output_path = first_arg
            target_url = "https://anthropic.skilljar.com/claude-code-in-action"
    else:
        # 没有参数，使用默认值
        target_url = "https://anthropic.skilljar.com/claude-code-in-action"
    
    print("Skilljar视频下载工具")
    print("=" * 50)
    print(f"目标URL: {target_url}")
    print(f"输出目录: {output_path}")
    print("=" * 50)
    
    # 判断是课程页面还是单个页面
    # 更可靠的检测方法：检查URL路径部分是否有数字ID
    parsed_url = urlparse(target_url)
    path_parts = parsed_url.path.strip('/').split('/')
    
    # 单个页面的特征：路径包含数字ID且不是课程主页
    is_single_page = (
        "/claude-code-in-action/" in target_url and
        len(path_parts) >= 2 and
        path_parts[-1].isdigit() and  # 最后一部分是数字
        path_parts[0] == "claude-code-in-action"
    )
    
    if is_single_page:
        # 单个课程页面
        print("检测到单个课程页面，开始下载单个视频...")
        download_single_page_video(target_url, output_path)
    else:
        # 课程主页
        print("检测到课程主页，开始下载整个课程...")
        download_skilljar_course(target_url, output_path)

if __name__ == "__main__":
    main()