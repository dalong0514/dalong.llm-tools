# -*- coding:utf-8 -*-
"""Extract Word XML text nodes into a JSON dataset.

从 Word XML 中提取文本节点并导出 JSON 数据集。
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
from html import unescape
from pathlib import Path
from typing import Iterable, List, Sequence

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))

DATA_DIR = PROJECT_ROOT / "data"
DEFAULT_ORIGIN_XML = DATA_DIR / "OriginWord.xml"
DEFAULT_OUTPUT_JSON = DATA_DIR / "ExtractXMLContentData.json"

TEXT_PATTERN = re.compile(r"<w:t(?:\s[^>]*)?>(.*?)</w:t>", re.DOTALL)
ASCII_ALNUM_PATTERN = re.compile(r"^[A-Za-z0-9]+$")
NUMBER_PATTERN = re.compile(r"-?\d+(?:\.\d+)*$")
WHITESPACE_PATTERN = re.compile(r"\s+")
INLINE_PREFIX_TO_SKIP = "<w:titlePg/>"

TRANSLATION_KEY_ORIGIN = "originContent"
TRANSLATION_KEY_TRANSLATED = "tranlastedContent"


def extract_text_nodes(xml_text: str) -> List[str]:
    """Find candidate text nodes and normalize their contents."""
    matches = TEXT_PATTERN.findall(xml_text)
    texts: List[str] = []
    for raw_match in matches:
        text = unescape(raw_match.strip())
        if not text:
            continue
        if text.startswith(INLINE_PREFIX_TO_SKIP):
            continue
        texts.append(text)
    return texts


def is_ascii_alphanumeric(text: str) -> bool:
    """Return True when text is composed only of ASCII letters and digits."""
    normalized = WHITESPACE_PATTERN.sub("", text)
    if not normalized:
        return True
    return bool(ASCII_ALNUM_PATTERN.fullmatch(normalized))


def is_punctuation_char(char: str) -> bool:
    """Return True when char is a Unicode punctuation mark."""
    return bool(char) and unicodedata.category(char).startswith("P")


def is_pure_punctuation(text: str) -> bool:
    """Return True when text contains only punctuation (ignoring whitespace)."""
    compact = WHITESPACE_PATTERN.sub("", text)
    if not compact:
        return False
    return all(is_punctuation_char(char) for char in compact)


def is_letter_with_punctuation(text: str) -> bool:
    """Return True when text is letters plus punctuation without digits or spaces."""
    stripped = text.strip()
    if not stripped or any(char.isspace() for char in stripped):
        return False
    letters = 0
    punctuation = 0
    for char in stripped:
        if char.isalpha():
            letters += 1
        elif is_punctuation_char(char):
            punctuation += 1
        else:
            return False
    return letters > 0 and punctuation > 0


def should_exclude_text(text: str) -> bool:
    """Determine whether the text should be excluded from the final dataset."""
    stripped = text.strip()
    if not stripped:
        return True
    if is_ascii_alphanumeric(stripped):
        return True
    compact = WHITESPACE_PATTERN.sub("", stripped)
    if NUMBER_PATTERN.fullmatch(compact):
        return True
    if is_pure_punctuation(stripped):
        return True
    if is_letter_with_punctuation(stripped):
        return True
    return False


def filter_unique_texts(texts: Iterable[str]) -> List[str]:
    """Filter unwanted entries, enforce uniqueness, and sort by length descending."""
    seen: set[str] = set()
    filtered: List[str] = []
    for text in texts:
        if should_exclude_text(text):
            continue
        if text in seen:
            continue
        seen.add(text)
        filtered.append(text)
    filtered.sort(key=len, reverse=True)
    return filtered


def build_entries(texts: Sequence[str]) -> List[dict[str, str]]:
    """Convert texts to the JSON-friendly structure."""
    return [
        {
            TRANSLATION_KEY_ORIGIN: text,
            TRANSLATION_KEY_TRANSLATED: "",
        }
        for text in texts
    ]


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Extract <w:t> text nodes from a Word XML file and save them as JSON."
    )
    parser.add_argument(
        "--origin-xml",
        type=Path,
        default=DEFAULT_ORIGIN_XML,
        help="Path to the source Word XML file.",
    )
    parser.add_argument(
        "--output-json",
        type=Path,
        default=DEFAULT_OUTPUT_JSON,
        help="Path to write the extracted JSON data.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_arguments()
    xml_path: Path = args.origin_xml
    output_path: Path = args.output_json

    xml_text = xml_path.read_text(encoding="utf-8")
    texts = extract_text_nodes(xml_text)
    filtered_texts = filter_unique_texts(texts)
    entries = build_entries(filtered_texts)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(entries, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Extracted {len(entries)} entries into {output_path}")


if __name__ == "__main__":
    main()
