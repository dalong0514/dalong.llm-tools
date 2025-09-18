# -*- coding:utf-8 -*-
import argparse
import json
import sys
import time
from pathlib import Path
from typing import Any, Dict, List, Optional

from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))

from src.helper import get_api_key, get_base_url
from src.utils import extract_translation, modify_text, read_prompt_file

system_prompt = read_prompt_file("prompt_translate_ch2en")

api_key = get_api_key("deepseek")
base_url = get_base_url("deepseek")
model_name = "deepseek-chat"

model = ChatOpenAI(
    base_url=base_url,
    api_key=api_key,
    model_name=model_name,
)

PROMPT_TEMPLATE = ChatPromptTemplate(
    [
        ("system", system_prompt),
        ("user", "{content}"),
    ]
)

DATA_DIR = PROJECT_ROOT / "data"
EXTRACTED_DATA_PATH = DATA_DIR / "ExtractWordContentData.json"
TRANSLATED_DATA_PATH = DATA_DIR / "TranslatedWordContentData.json"
TRANSLATION_NOT_FOUND = extract_translation("")


def translate_once(llm: ChatOpenAI, origin_content: str, mode: str) -> Optional[str]:
    """Translate a single content string and post-process the result."""
    try:
        prompt = PROMPT_TEMPLATE.invoke({"content": origin_content})
        response = llm.invoke(prompt)
        response_text = response.content
        out_content = extract_translation(response_text)

        while out_content == TRANSLATION_NOT_FOUND:
            response = llm.invoke(prompt)
            response_text = response.content
            out_content = extract_translation(response_text)

        return modify_text(out_content)
    except Exception as exc:
        print(f"Error processing content: {exc}")
        if "429" in str(exc):
            print("Rate limit exceeded, waiting 30 seconds...")
            time.sleep(30)
            return translate_once(llm, origin_content, mode)
        return None


def load_source_entries(path: Path) -> List[Dict[str, Any]]:
    """Load translation entries from the source JSON file."""
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def translate_entries(entries: List[Dict[str, Any]], mode: str, llm: ChatOpenAI) -> List[Dict[str, Any]]:
    """Translate originContent values and update tranlastedContent in place."""
    total = len(entries)
    for index, entry in enumerate(entries, start=1):
        origin_content = entry.get("originContent", "")
        print(f"Processing item {index}/{total}")
        if not isinstance(origin_content, str) or not origin_content.strip():
            entry["tranlastedContent"] = ""
            continue

        translated_content = translate_once(llm, origin_content, mode)
        if translated_content is not None:
            entry["tranlastedContent"] = translated_content
    return entries


def translate(mode: str) -> None:
    entries = load_source_entries(EXTRACTED_DATA_PATH)
    updated_entries = translate_entries(entries, mode, model)
    with TRANSLATED_DATA_PATH.open("w", encoding="utf-8") as file:
        json.dump(updated_entries, file, ensure_ascii=False, indent=2)
    print(f"Translated data saved to {TRANSLATED_DATA_PATH}")


def parse_arguments() -> argparse.Namespace:
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description="Translate text")
    parser.add_argument(
        "--mode",
        type=str,
        default="zh",
        help="Translation mode",
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
