# -*- coding:utf-8 -*-
"""Replace Word XML content using translated strings.

使用翻译后的内容替换 Word XML 字符串。"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Dict, Iterable, List, Tuple

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))

DATA_DIR = PROJECT_ROOT / "data"
DEFAULT_ORIGIN_XML = DATA_DIR / "OriginWord.xml"
DEFAULT_TRANSLATIONS_JSON = DATA_DIR / "TranslatedWordContentData.json"
DEFAULT_OUTPUT_XML = DATA_DIR / "TranslatedWord.xml"

TRANSLATION_KEY_ORIGIN = "originContent"
TRANSLATION_KEY_VALUE = "tranlastedContent"


def load_translations(path: Path) -> List[Dict[str, str]]:
    """Load translation entries from JSON and normalize contents.

    读取 JSON 翻译数据并规范化内容。

    Args:
        path: Path to the JSON file containing translation entries.

    Returns:
        A list of dictionaries with normalized origin and translated strings.
    """
    with path.open("r", encoding="utf-8") as file:
        raw_data = json.load(file)

    if not isinstance(raw_data, list):
        raise ValueError("Translation data must be a list of objects.")

    translations: List[Dict[str, str]] = []
    for index, item in enumerate(raw_data, start=1):
        if not isinstance(item, dict):
            continue
        origin = item.get(TRANSLATION_KEY_ORIGIN, "")
        translated = item.get(TRANSLATION_KEY_VALUE, "")
        if not isinstance(origin, str) or not origin:
            continue
        if not isinstance(translated, str):
            translated = "" if translated is None else str(translated)
        translations.append({
            TRANSLATION_KEY_ORIGIN: origin,
            TRANSLATION_KEY_VALUE: translated,
        })
    return translations


def apply_translations(xml_text: str, translations: Iterable[Dict[str, str]]) -> Tuple[str, int, int]:
    """Apply translations to the XML content.

    Args:
        xml_text: The original XML content.
        translations: Iterable of translation entries.

    Returns:
        Tuple containing updated XML text, matched entry count, and total replacements.
    """
    matched_entries = 0
    total_replacements = 0
    updated_text = xml_text

    for entry in translations:
        origin = entry.get(TRANSLATION_KEY_ORIGIN, "")
        translated = entry.get(TRANSLATION_KEY_VALUE, "")
        if not origin:
            continue
        occurrences = updated_text.count(origin)
        if occurrences:
            updated_text = updated_text.replace(origin, translated)
            matched_entries += 1
            total_replacements += occurrences
    return updated_text, matched_entries, total_replacements


def replace_content(origin_xml: Path, translations_json: Path, output_xml: Path) -> Tuple[int, int]:
    """Load files, apply replacements, and write the result.

    Returns:
        Tuple of matched entry count and total replacements applied.
    """
    xml_text = origin_xml.read_text(encoding="utf-8")
    translations = load_translations(translations_json)
    updated_text, matched_entries, total_replacements = apply_translations(xml_text, translations)
    output_xml.write_text(updated_text, encoding="utf-8")
    return matched_entries, total_replacements


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Replace Word XML content using translated values.")
    parser.add_argument(
        "--origin-xml",
        type=Path,
        default=DEFAULT_ORIGIN_XML,
        help="Path to the original Word XML file.",
    )
    parser.add_argument(
        "--translations-json",
        type=Path,
        default=DEFAULT_TRANSLATIONS_JSON,
        help="Path to the JSON file containing translations.",
    )
    parser.add_argument(
        "--output-xml",
        type=Path,
        default=DEFAULT_OUTPUT_XML,
        help="Path to write the translated Word XML.",
    )
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    matched_entries, total_replacements = replace_content(
        origin_xml=args.origin_xml,
        translations_json=args.translations_json,
        output_xml=args.output_xml,
    )
    print(
        f"Replacements complete. Entries matched: {matched_entries}, total occurrences replaced: {total_replacements}."
    )


if __name__ == "__main__":
    main()
