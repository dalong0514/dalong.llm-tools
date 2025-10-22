# -*- coding: utf-8 -*-
"""
Fun-ASR transcription helper

封装：
- 本地文件上传至阿里云 OSS（基于环境变量配置）
- 通过 DashScope Fun-ASR 提交与等待转写
- 下载 transcription_url JSON 并抽取纯文本

环境变量：
- DASHSCOPE_API_KEY（或 BAILIAN_API_KEY 作为兜底）
- OSS_ENDPOINT（如 https://oss-cn-hangzhou.aliyuncs.com）
- OSS_BUCKET
- OSS_ACCESS_KEY_ID
- OSS_ACCESS_KEY_SECRET
- 可选：OSS_PREFIX（默认 uploads/）

依赖：dashscope、oss2、requests
"""
from __future__ import annotations

import os
import json
from pathlib import Path
from typing import Optional
from datetime import datetime
from urllib.parse import urlparse
from http import HTTPStatus

import requests

try:
    import dashscope
    from dashscope.audio.asr import Transcription
except Exception:  # pragma: no cover - optional import error surfaced at runtime
    dashscope = None
    Transcription = None

try:
    import oss2  # type: ignore
except Exception:  # pragma: no cover - optional import error surfaced at runtime
    oss2 = None


def _normalize_endpoint(ep: str) -> str:
    ep = (ep or '').strip()
    if not ep:
        return ep
    if ep.startswith('http://') or ep.startswith('https://'):
        return ep
    return f'https://{ep}'


def _extract_text_from_result_json(obj: dict) -> str:
    """Best-effort extraction of transcript text from Fun-ASR result JSON."""
    transcripts = obj.get('transcripts')
    if isinstance(transcripts, list) and transcripts:
        parts = []
        for item in transcripts:
            if isinstance(item, dict) and isinstance(item.get('text'), str):
                t = item['text'].strip()
                if t:
                    parts.append(t)
            elif isinstance(item, dict) and isinstance(item.get('sentences'), list):
                lines = []
                for s in item['sentences']:
                    if isinstance(s, dict) and isinstance(s.get('text'), str):
                        st = s['text'].strip()
                        if st:
                            lines.append(st)
                if lines:
                    parts.append('\n'.join(lines))
        if parts:
            return '\n'.join(parts)

    for key in ('text', 'transcript', 'transcription'):
        val = obj.get(key)
        if isinstance(val, str) and val.strip():
            return val.strip()

    # 递归兜底：跳过 words/word
    def scan(any_obj):
        if isinstance(any_obj, dict):
            for key in ('text', 'transcript', 'transcription'):
                val = any_obj.get(key)
                if isinstance(val, str) and val.strip():
                    return val.strip()
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


def _oss_upload_and_sign(
    file_path: Path,
    *,
    endpoint: str,
    bucket_name: str,
    access_key_id: str,
    access_key_secret: str,
    prefix: str = 'uploads/',
    expires: int = 24 * 3600,
    verbose: bool = True,
    http_fallback: bool = True,
) -> Optional[str]:
    """Upload a file to OSS and return a pre-signed GET URL."""
    if oss2 is None:
        print('缺少 oss2 依赖，请先安装：pip install oss2')
        return None

    endpoint = _normalize_endpoint(endpoint)

    def attempt(ep: str) -> str:
        auth = oss2.Auth(access_key_id, access_key_secret)
        bucket = oss2.Bucket(auth, ep, bucket_name)
        base = file_path.name
        ts = datetime.now().strftime('%Y%m%d/%H%M%S')
        key = f"{prefix.rstrip('/')}/{ts}-{base}"
        if verbose:
            print(f"OSS 上传: endpoint={ep}, bucket={bucket_name}, key={key}")
        bucket.put_object_from_file(key, str(file_path))
        signed_url = bucket.sign_url('GET', key, expires, slash_safe=True)
        return signed_url

    try:
        return attempt(endpoint)
    except Exception as e:
        print(f'上传 OSS 或生成签名链接失败: {e}')
        if http_fallback and endpoint.startswith('https://'):
            try:
                http_ep = 'http://' + endpoint[len('https://'):]
                print('尝试使用 http 端点重试一次（仅用于排障）...')
                return attempt(http_ep)
            except Exception as e2:
                print(f'http 重试仍失败: {e2}')
        return None


def funasr_transcribe_local_file(
    input_path: str | Path,
    output_dir: str | Path | None = None,
    *,
    model: str = 'fun-asr',
    signed_url_expires: int = 24 * 3600,
    oss_prefix: Optional[str] = None,
    http_fallback: bool = True,
    verbose: bool = True,
) -> Optional[str]:
    """Transcribe a local audio/video file via Aliyun Fun-ASR.

    输入：本地文件路径。函数会上传到 OSS，生成签名 URL，并调用 Fun-ASR。
    输出：写入 output_dir/<stem>.txt，并保存原始 JSON 至 <stem>_funasr.json。

    Returns the path to the .txt transcript on success; None on failure.
    """
    if Transcription is None or dashscope is None:
        print('缺少 dashscope 依赖，请先安装：pip install dashscope')
        return None

    src_path = Path(input_path)
    if not src_path.exists():
        print(f'本地文件不存在: {src_path}')
        return None

    # Resolve output directory (default to input file dir)
    out_dir = Path(output_dir) if output_dir else src_path.parent
    out_dir.mkdir(parents=True, exist_ok=True)
    stem = src_path.stem

    # Load API keys
    api_key = os.getenv('DASHSCOPE_API_KEY') or os.getenv('BAILIAN_API_KEY')
    if not api_key:
        print('缺少 API Key，请设置 DASHSCOPE_API_KEY 或 BAILIAN_API_KEY')
        return None
    dashscope.api_key = api_key

    # OSS config
    endpoint = os.getenv('OSS_ENDPOINT')
    bucket_name = os.getenv('OSS_BUCKET')
    access_key_id = os.getenv('OSS_ACCESS_KEY_ID')
    access_key_secret = os.getenv('OSS_ACCESS_KEY_SECRET')
    prefix = oss_prefix or os.getenv('OSS_PREFIX', 'uploads/')
    for name, val in (
        ('OSS_ENDPOINT', endpoint), ('OSS_BUCKET', bucket_name),
        ('OSS_ACCESS_KEY_ID', access_key_id), ('OSS_ACCESS_KEY_SECRET', access_key_secret)
    ):
        if not val:
            print(f'缺少必要的 OSS 配置：{name}')
            return None

    # Upload to OSS
    signed_url = _oss_upload_and_sign(
        src_path,
        endpoint=endpoint,
        bucket_name=bucket_name,
        access_key_id=access_key_id,
        access_key_secret=access_key_secret,
        prefix=prefix,
        expires=signed_url_expires,
        verbose=verbose,
        http_fallback=http_fallback,
    )
    if not signed_url:
        print('上传 OSS 失败，请检查配置与网络')
        return None

    # Call Fun-ASR
    try:
        task_resp = Transcription.async_call(model=model, file_urls=[signed_url], channel_id=[0])
        transcribe_resp = Transcription.wait(task=task_resp.output.task_id)
    except Exception as e:
        print(f'调用 Fun-ASR 失败: {e}')
        return None

    if getattr(transcribe_resp, 'status_code', None) != HTTPStatus.OK:
        print(f'Fun-ASR 返回异常状态: {getattr(transcribe_resp, "status_code", None)}')
        return None

    output = getattr(transcribe_resp, 'output', None) or {}
    results = output.get('results') or []
    texts = []
    json_path: Optional[Path] = None
    for item in results:
        if not isinstance(item, dict):
            continue
        if item.get('subtask_status') != 'SUCCEEDED':
            continue
        t_url = item.get('transcription_url')
        if not t_url:
            continue
        r = requests.get(t_url, timeout=60)
        r.raise_for_status()
        obj = r.json()
        # Save original result JSON
        json_path = out_dir / f'{stem}_funasr.json'
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(obj, f, ensure_ascii=False, indent=2)
        txt = _extract_text_from_result_json(obj)
        if txt:
            texts.append(txt)

    if not texts:
        # final fallback: try task output
        try:
            raw_obj = json.loads(json.dumps(output))
            t = _extract_text_from_result_json(raw_obj)
            if t:
                texts.append(t)
        except Exception:
            pass

    if not texts:
        print('未获取到有效的转写文本')
        return None

    txt_path = out_dir / f'{stem}.txt'
    with open(txt_path, 'w', encoding='utf-8') as f:
        f.write('\n\n'.join(texts))
    return str(txt_path)

