# -*- coding:utf-8 -*-
import argparse
import json
import sys
import time
from pathlib import Path
from typing import Any, Dict, List, Optional

from google import genai
from google.genai import types

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))

from src.helper import get_api_key
import src.utils as utils

system_prompt = utils.read_prompt_file("prompt_translate_ch2en")
api_key = get_api_key("google")
client = genai.Client(api_key=api_key)
model_name = "gemini-2.5-flash"

DATA_DIR = PROJECT_ROOT / "data"
EXTRACTED_DATA_PATH = DATA_DIR / "ExtractWordContentData.json"
TRANSLATED_DATA_PATH = DATA_DIR / "TranslatedWordContentData.json"
TEMP_TRANSLATED_DATA_PATH = DATA_DIR / "TempTranslatedWordContentData.json"
TRANSLATION_NOT_FOUND = utils.extract_translation("")


def translate_once(origin_content: str, mode: str) -> Optional[str]:
    """Translate a single content string and post-process the result."""
    try:
        response = client.models.generate_content(
            model=model_name,
            contents=origin_content,
            config=types.GenerateContentConfig(
                system_instruction=system_prompt,
                thinking_config=types.ThinkingConfig(thinking_budget=512),
            ),
        )
        response_text = response.text if hasattr(response, "text") else str(response)
        out_content = utils.extract_translation(response_text)

        while out_content == TRANSLATION_NOT_FOUND:
            response = client.models.generate_content(
                model=model_name,
                contents=origin_content,
                config=types.GenerateContentConfig(
                    system_instruction=system_prompt,
                    thinking_config=types.ThinkingConfig(thinking_budget=512),
                ),
            )
            response_text = response.text if hasattr(response, "text") else str(response)
            out_content = utils.extract_translation(response_text)

        return out_content
    
    except Exception as e:
        print(f"Error processing content: {e}")
        if "429" in str(e):
            print("Rate limit exceeded, waiting 30 seconds...")
            time.sleep(30)
            return translate_once(origin_content, mode)
        return None


def load_source_entries(path: Path) -> List[Dict[str, Any]]:
    """Load translation entries from the source JSON file."""
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)

def save_entries(path: Path, entries: List[Dict[str, Any]]) -> None:
    """Persist translation entries to the specified JSON path."""
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as file:
        json.dump(entries, file, ensure_ascii=False, indent=2)



def translate_entries(entries: List[Dict[str, Any]], mode: str) -> List[Dict[str, Any]]:
    """Translate originContent values and update tranlastedContent in place."""
    total = len(entries)
    for index, entry in enumerate(entries, start=1):
        origin_content = entry.get("originContent", "")
        print(f"Processing item {index}/{total}")
        if not isinstance(origin_content, str) or not origin_content.strip():
            entry["tranlastedContent"] = ""
            save_entries(TEMP_TRANSLATED_DATA_PATH, entries)
            continue

        translated_content = translate_once(origin_content, mode)
        if translated_content is not None:
            entry["tranlastedContent"] = translated_content
        save_entries(TEMP_TRANSLATED_DATA_PATH, entries)
    return entries


def translate(mode: str) -> None:
    entries = load_source_entries(EXTRACTED_DATA_PATH)
    updated_entries = translate_entries(entries, mode)
    save_entries(TRANSLATED_DATA_PATH, updated_entries)
    print(f"Translated data saved to {TRANSLATED_DATA_PATH}")


def parse_arguments() -> argparse.Namespace:
    """解析命令行参数"""
    parser = argparse.ArgumentParser(description="翻译文本")
    parser.add_argument(
        "--mode",
        type=str,
        default="zh",
        help="处理模式",
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_arguments()
    start_time = time.time()
    print("waiting...\n")
    translate(args.mode)
    elapsed_time = time.time() - start_time
    if elapsed_time < 60:
        print(f"Time Used: {elapsed_time:.2f} seconds")
    else:
        print(f"Time Used: {elapsed_time/60:.2f} minutes")
