# -*- coding: utf-8 -*-
import json
import time
from datetime import datetime
import os

def parse_twitter_timestamp(timestamp_str):
    """解析Twitter时间戳格式"""
    try:
        # 新格式：2023-01-24T20:14:00.000Z
        dt = datetime.fromisoformat(timestamp_str.replace('Z', '+00:00'))
        return {
            "date-parts": [[dt.year, dt.month, dt.day]]
        }
    except ValueError:
        return None

def extract_author_from_url(url):
    """从Twitter URL中提取作者信息"""
    try:
        # URL格式：https://x.com/username/status/... 或 https://twitter.com/username/status/...
        parts = url.split('/')
        if len(parts) >= 4 and ('x.com' in url or 'twitter.com' in url):
            username = parts[3]
            return {
                "family": f"@{username}",
                "given": ""
            }
    except:
        pass
    return {
        "family": "Twitter User",
        "given": ""
    }

def convert_tweet_to_csl(tweet):
    """将单条推文转换为CSL JSON格式"""
    
    # 基本CSL条目结构
    csl_item = {
        "type": "post-weblog",  # 使用博客文章类型，最接近社交媒体帖子
        "id": tweet.get("id", ""),
        "title": tweet.get("text", "").strip(),  # 使用新格式的 text 字段
        "URL": tweet.get("url", ""),
        "container-title": "Twitter",
        "genre": "Tweet"
    }
    
    # 添加作者信息
    author = extract_author_from_url(tweet.get("url", ""))
    if author:
        csl_item["author"] = [author]
    
    # 添加发布日期 - 使用新格式的 timestamp 字段
    if tweet.get("timestamp"):
        issued_date = parse_twitter_timestamp(tweet["timestamp"])
        if issued_date:
            csl_item["issued"] = issued_date
    
    # 添加访问日期（当前日期）
    now = datetime.now()
    csl_item["accessed"] = {
        "date-parts": [[now.year, now.month, now.day]]
    }
    
    # 添加统计信息作为note - 使用新格式的字段
    stats = []
    if tweet.get("likes"):
        stats.append(f"Likes: {tweet['likes']:,}")
    if tweet.get("retweets"):
        stats.append(f"Retweets: {tweet['retweets']:,}")
    if tweet.get("replies"):
        stats.append(f"Replies: {tweet['replies']:,}")
    if tweet.get("quotes"):
        stats.append(f"Quotes: {tweet['quotes']:,}")
    
    if stats:
        csl_item["note"] = "; ".join(stats)
    
    # 添加媒体信息到abstract
    additional_info = []
    if tweet.get("images"):
        media_count = len(tweet["images"])
        additional_info.append(f"Contains {media_count} image(s)")
    
    if additional_info:
        csl_item["abstract"] = "; ".join(additional_info)
    
    return csl_item

def convert_twitter_to_csl():
    """主转换函数"""
    input_file = "/Users/Daglas/dalong.github/dalong.llm-tools/working/dataset_twitter-scraper_2025-07-19_10-04-35-572.json"
    
    # 检查输入文件是否存在
    if not os.path.exists(input_file):
        print(f"错误：找不到输入文件 {input_file}")
        return
    
    print(f"正在读取文件: {input_file}")
    
    try:
        # 读取Twitter数据
        with open(input_file, 'r', encoding='utf-8') as f:
            twitter_data = json.load(f)
        
        print(f"成功读取 {len(twitter_data)} 条推文")
        
        # 转换为CSL JSON格式
        csl_data = []
        for i, tweet in enumerate(twitter_data):
            try:
                csl_item = convert_tweet_to_csl(tweet)
                csl_data.append(csl_item)
                if (i + 1) % 100 == 0:
                    print(f"已处理 {i + 1}/{len(twitter_data)} 条推文")
            except Exception as e:
                print(f"处理第 {i + 1} 条推文时出错: {e}")
                continue
        
        # 生成输出文件名
        output_file = input_file.replace('.json', '_csl.json')
        
        # 保存CSL JSON数据
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(csl_data, f, ensure_ascii=False, indent=2)
        
        print(f"\n转换完成！")
        print(f"输入文件: {input_file}")
        print(f"输出文件: {output_file}")
        print(f"成功转换 {len(csl_data)} 条推文为CSL JSON格式")
        
        # 显示一些统计信息
        print(f"\n文件大小:")
        print(f"输入文件: {os.path.getsize(input_file) / (1024*1024):.2f} MB")
        print(f"输出文件: {os.path.getsize(output_file) / (1024*1024):.2f} MB")
        
    except json.JSONDecodeError as e:
        print(f"JSON解析错误: {e}")
    except Exception as e:
        print(f"处理过程中出现错误: {e}")

if __name__ == '__main__':
    start_time = time.time()
    print('开始转换Twitter数据为CSL JSON格式...\n')
    convert_twitter_to_csl()
    end_time = time.time()
    # 改进时间显示
    elapsed_time = end_time - start_time
    if elapsed_time < 60:
        print(f'\n处理时间: {elapsed_time:.2f} 秒')
    else:
        print(f'\n处理时间: {elapsed_time/60:.2f} 分钟')