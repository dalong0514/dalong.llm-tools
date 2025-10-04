#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
处理Andrej Karpathy Twitter数据的脚本
将JSON格式的推文数据按年度分组并保存为markdown文件
"""

import json
from collections import defaultdict
from pathlib import Path

def load_tweets(json_file):
    """加载推文JSON数据"""
    with open(json_file, 'r', encoding='utf-8') as f:
        tweets = json.load(f)
    return tweets

def group_tweets_by_year(tweets):
    """按年度分组推文"""
    yearly_tweets = defaultdict(list)
    
    for tweet in tweets:
        # 提取发布年份
        if 'issued' in tweet and 'date-parts' in tweet['issued']:
            year = tweet['issued']['date-parts'][0][0]  # 获取年份
            yearly_tweets[year].append(tweet)
    
    return yearly_tweets

def format_tweet_content(tweet):
    """格式化单条推文内容"""
    # 提取推文内容
    title = tweet.get('title', '').strip()
    
    # 提取元数据
    url = tweet.get('URL', '')
    author = tweet.get('author', [{}])[0].get('family', '@karpathy')
    
    # 格式化时间
    issued_date = ''
    if 'issued' in tweet and 'date-parts' in tweet['issued']:
        date_parts = tweet['issued']['date-parts'][0]
        if len(date_parts) >= 3:
            issued_date = f"{date_parts[0]:04d}-{date_parts[1]:02d}-{date_parts[2]:02d}"
    
    # 提取互动数据
    note = tweet.get('note', '')
    
    # 构建markdown格式的推文内容
    content = f"**{title}**\n\n"
    content += f"- **作者**: {author}\n"
    content += f"- **时间**: {issued_date}\n"
    content += f"- **链接**: {url}\n"
    if note:
        content += f"- **互动**: {note}\n"
    
    return content

def save_yearly_markdown(year, tweets, output_dir: Path):
    """保存年度推文到markdown文件"""
    filename = f"{year}_andrej_karpathy_twitter.md"
    filepath = output_dir / filename
    
    # 按时间排序推文（最新在后）
    tweets.sort(key=lambda x: x['issued']['date-parts'][0] if 'issued' in x and 'date-parts' in x['issued'] else [0, 0, 0])
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(f"# Andrej Karpathy Twitter {year}\n\n")
        f.write(f"本文件包含Andrej Karpathy在{year}年的所有推文。\n\n")
        f.write(f"总计推文数量: {len(tweets)}\n\n")
        f.write("---\n\n")
        
        for i, tweet in enumerate(tweets):
            content = format_tweet_content(tweet)
            f.write(content)
            
            # 推文之间用 --- 分割
            if i < len(tweets) - 1:
                f.write("\n---\n\n")
    
    print(f"已保存 {len(tweets)} 条推文到 {filename}")

def main():
    """主函数"""
    # 文件路径
    base_dir = Path(__file__).resolve().parent.parent
    json_file = base_dir / "data/20250719dataset_twitter-scraper_2025-07-19_10-04-35-572_csl.json"
    output_dir = base_dir / "data"  # 保存到data目录
    output_dir.mkdir(parents=True, exist_ok=True)
    
    print("开始处理Andrej Karpathy Twitter数据...")
    
    # 加载推文数据
    print(f"正在加载 {json_file}...")
    tweets = load_tweets(json_file)
    print(f"总共加载了 {len(tweets)} 条推文")
    
    # 按年度分组
    print("正在按年度分组推文...")
    yearly_tweets = group_tweets_by_year(tweets)
    
    # 输出分组统计
    print(f"按年度分组结果:")
    for year in sorted(yearly_tweets.keys()):
        print(f"  {year}年: {len(yearly_tweets[year])} 条推文")
    
    # 为每年生成markdown文件
    print("\n开始生成年度markdown文件...")
    for year in sorted(yearly_tweets.keys()):
        save_yearly_markdown(year, yearly_tweets[year], output_dir)
    
    print(f"\n处理完成！共生成 {len(yearly_tweets)} 个年度文件。")

if __name__ == "__main__":
    main()
