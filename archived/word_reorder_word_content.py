"""Reorder word extraction entries by originContent length.

按 originContent 字符长度降序重排 Word 内容数据。
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

BASE_DIR = Path(__file__).resolve().parent.parent
DEFAULT_INPUT = BASE_DIR / "data" / "TranslatedWordContentData.json"
DEFAULT_OUTPUT = BASE_DIR / "data" / "TranslatedWordContentDataReOrdered.json"

def load_word_content(path: Path) -> list[dict[str, Any]]:
    """Load word extraction entries from JSON (读取词条 JSON 数据)."""
    if not path.exists():
        raise FileNotFoundError(f"Input file not found: {path}")
    with path.open("r", encoding="utf-8") as file:
        data = json.load(file)
    if not isinstance(data, list):
        raise ValueError("Expected the source JSON to be a list of objects.")
    return data

def reorder_entries(entries: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Return entries sorted by descending originContent length (按原文长度排序)."""

    def origin_length(item: dict[str, Any]) -> int:
        origin = item.get("originContent", "")
        return len(origin if isinstance(origin, str) else str(origin))

    return sorted(entries, key=origin_length, reverse=True)

def write_entries(entries: list[dict[str, Any]], path: Path) -> None:
    """Write entries out to JSON (写入目标 JSON 文件)."""
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as file:
        json.dump(entries, file, ensure_ascii=False, indent=2)

def parse_args() -> argparse.Namespace:
    """Parse CLI arguments for the reorder script."""
    parser = argparse.ArgumentParser(
        description="Reorder word content entries in descending originContent length."
    )
    parser.add_argument(
        "--input",
        type=Path,
        default=DEFAULT_INPUT,
        help="Path to TranslatedWordContentData.json (输入文件路径)",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT,
        help="Path to save reordered JSON data (输出文件路径)",
    )
    return parser.parse_args()

def resolve_path(path: Path) -> Path:
    """Return absolute path, respecting cwd for relative values."""
    return path if path.is_absolute() else Path.cwd() / path

def main() -> None:
    """CLI entry point."""
    args = parse_args()
    input_path = resolve_path(args.input)
    output_path = resolve_path(args.output)
    entries = load_word_content(input_path)
    reordered = reorder_entries(entries)
    write_entries(reordered, output_path)

if __name__ == "__main__":
    main()
