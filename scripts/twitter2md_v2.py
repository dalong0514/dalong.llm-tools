#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
处理最新Andrej Karpathy Twitter数据的脚本
将JSON格式的推文数据按年度分组并保存为markdown文件
"""

from __future__ import annotations

import os
import sys
import json
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List

# 将项目根目录加入模块搜索路径，便于复用src中的工具函数
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import src.utils as utils  # noqa: E402  pylint: disable=wrong-import-position

JsonDict = Dict[str, Any]


def load_tweets(json_file: Path) -> List[JsonDict]:
    """加载推文JSON数据"""
    with json_file.open('r', encoding='utf-8') as file:
        tweets: List[JsonDict] = json.load(file)
    return tweets


def parse_created_at(value: str | None) -> datetime | None:
    """解析Twitter的createdAt字段为datetime对象"""
    if not value:
        return None
    try:
        return datetime.strptime(value, "%a %b %d %H:%M:%S %z %Y")
    except ValueError:
        return None


def group_tweets_by_year(tweets: Iterable[JsonDict]) -> Dict[int, List[JsonDict]]:
    """按年度分组推文"""
    yearly_tweets: Dict[int, List[JsonDict]] = defaultdict(list)

    for tweet in tweets:
        created_at = parse_created_at(tweet.get('createdAt'))
        if created_at is None:
            continue
        yearly_tweets[created_at.year].append(tweet)

    return yearly_tweets


def build_interaction_note(tweet: JsonDict) -> str:
    """构建互动数据字符串，格式与旧数据保持一致"""
    fields = [
        ("Likes", 'likeCount'),
        ("Retweets", 'retweetCount'),
        ("Replies", 'replyCount'),
        ("Quotes", 'quoteCount'),
        ("Views", 'viewCount'),
        ("Bookmarks", 'bookmarkCount'),
        ("isReply", 'isReply'),
    ]
    parts: List[str] = []
    for label, key in fields:
        value = tweet.get(key)
        if isinstance(value, int):
            parts.append(f"{label}: {value:,}")
    return '; '.join(parts)


def format_tweet_content(tweet: JsonDict) -> str:
    """格式化单条推文内容"""
    title = tweet.get('text', '').strip()
    translated_content = tweet.get('tranlastedContent', '').strip()
    translated_content = utils.modify_text(translated_content)

    url = tweet.get('url', '')
    author = '@karpathy'
    # author = '@AndrewYNg'

    issued_date = ''
    created_at = parse_created_at(tweet.get('createdAt'))
    if created_at is not None:
        issued_date = created_at.astimezone(timezone.utc).strftime('%Y-%m-%d')

    note = tweet.get('note', '').strip()
    if not note:
        note = build_interaction_note(tweet)

    content_lines = [
        f"作者: {author}",
        f"时间: {issued_date}",
        f"链接: {url}",
    ]
    if note:
        content_lines.append(f"互动: {note}")
    content_lines.append('')
    content_lines.append(title)
    if translated_content:
        content_lines.append('')
        content_lines.append(translated_content)

    return '\n'.join(content_lines) + '\n'


def sort_key(tweet: JsonDict) -> datetime:
    """生成排序键，保证推文按时间顺序输出"""
    created_at = parse_created_at(tweet.get('createdAt'))
    if created_at is None:
        return datetime.min.replace(tzinfo=timezone.utc)
    return created_at.astimezone(timezone.utc)


def save_yearly_markdown(year: int, tweets: List[JsonDict], output_dir: Path) -> None:
    """保存年度推文到markdown文件"""
    filename = f"{year}Andrew_Ng_Twitter.md"
    filepath = output_dir / filename

    tweets.sort(key=sort_key)

    with filepath.open('w', encoding='utf-8') as file:
        file.write(f"# Andrej Karpathy Twitter {year}\n\n")
        file.write(f"本文件包含Andrej Karpathy在{year}年的所有推文。\n\n")
        file.write(f"总计推文数量: {len(tweets)}\n\n")

        for index, tweet in enumerate(tweets, start=1):
            file.write(f"\n### {index:03d}\n\n")
            content = format_tweet_content(tweet)
            file.write(content)

    print(f"已保存 {len(tweets)} 条推文到 {filename}")


def main() -> None:
    """主函数"""
    base_dir = Path(__file__).resolve().parent.parent
    json_file = base_dir / "data/TranslatedTwitterContentData.json"
    output_dir = base_dir / "data"
    output_dir.mkdir(parents=True, exist_ok=True)

    print("开始处理Andrej Karpathy Twitter数据...")
    print(f"正在加载 {json_file}...")

    tweets = load_tweets(json_file)
    print(f"总共加载了 {len(tweets)} 条推文")

    print("正在按年度分组推文...")
    yearly_tweets = group_tweets_by_year(tweets)

    print("按年度分组结果:")
    for year in sorted(yearly_tweets.keys()):
        print(f"  {year}年: {len(yearly_tweets[year])} 条推文")

    print("\n开始生成年度markdown文件...")
    for year in sorted(yearly_tweets.keys()):
        save_yearly_markdown(year, yearly_tweets[year], output_dir)

    print(f"\n处理完成！共生成 {len(yearly_tweets)} 个年度文件。")


if __name__ == "__main__":
    main()
