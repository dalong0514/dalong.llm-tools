#!/usr/bin/env python3
"""
htmltable2csv

读取 Markdown 文件中的 HTML 表格，提取所有表格数据，
以第一个表格的表头为准合并为一个 CSV 并写入输出文件。

Usage:
  python scripts/htmltable2csv.py \
    --input data/20251023html-table-dataA1.md \
    --output data/20251023csv-dataA1.csv

Notes / 说明:
- 只使用第一个表格的表头（项目需求表示表头一致）。
- CSV 输出包含 UTF-8 BOM（utf-8-sig），以便与参考文件兼容。
- 解析依赖 beautifulsoup4（在项目 pyproject/requirements 已包含）。
"""

from __future__ import annotations

import argparse
import csv
from pathlib import Path
from typing import Iterable, List, Tuple

from bs4 import BeautifulSoup


def parse_tables_from_markdown(md_text: str) -> List[List[List[str]]]:
    """Parse all HTML tables embedded in a Markdown document.

    Returns a list of tables, where each table is a list of rows,
    and each row is a list of cell strings.
    """
    soup = BeautifulSoup(md_text, "html.parser")
    tables = []
    for tbl in soup.find_all("table"):
        rows: List[List[str]] = []
        for tr in tbl.find_all("tr"):
            cells = tr.find_all(["th", "td"])  # header or data cells
            # Normalize cell text: strip surrounding whitespace; preserve inner newlines
            row = [c.get_text(separator="\n", strip=True) for c in cells]
            if row:  # skip empty rows
                rows.append(row)
        if rows:
            tables.append(rows)
    return tables


def merge_tables_with_first_header(tables: List[List[List[str]]]) -> Tuple[List[str], List[List[str]]]:
    """Merge multiple tables using the first table's header.

    - Uses the first row of the first table as the header.
    - Appends all subsequent rows from all tables.
    - If a row length mismatches the header, it is padded/truncated.
    """
    if not tables:
        return [], []

    header = tables[0][0]
    n_cols = len(header)

    merged_rows: List[List[str]] = []
    for i, table in enumerate(tables):
        # Skip the first row (header) for every table
        data_rows = table[1:]
        for row in data_rows:
            if len(row) < n_cols:
                # pad with empty strings to match header length
                padded = row + [""] * (n_cols - len(row))
                merged_rows.append(padded)
            elif len(row) > n_cols:
                # truncate extras if any
                merged_rows.append(row[:n_cols])
            else:
                merged_rows.append(row)

    return header, merged_rows


def write_csv(path: Path, header: List[str], rows: Iterable[List[str]]) -> None:
    """Write CSV with UTF-8 BOM, quoting as needed (including newlines)."""
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.writer(
            f,
            dialect="excel",
            lineterminator="\r\n",  # match typical Windows/Excel style as in reference
            quoting=csv.QUOTE_MINIMAL,
        )
        if header:
            writer.writerow(header)
        for row in rows:
            writer.writerow(row)


def main() -> None:
    parser = argparse.ArgumentParser(description="Extract HTML tables in Markdown to merged CSV.")
    parser.add_argument(
        "--input",
        default="data/20251023html-table-dataA1.md",
        type=str,
        help="Input Markdown file path containing HTML <table> blocks.",
    )
    parser.add_argument(
        "--output",
        default="data/20251023csv-dataA1.csv",
        type=str,
        help="Output CSV file path.",
    )
    args = parser.parse_args()

    input_path = Path(args.input)
    output_path = Path(args.output)

    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")

    md_text = input_path.read_text(encoding="utf-8")
    tables = parse_tables_from_markdown(md_text)
    if not tables:
        raise ValueError("No <table> found in input Markdown.")

    header, rows = merge_tables_with_first_header(tables)
    if not header:
        raise ValueError("Failed to detect header in the first table.")

    write_csv(output_path, header, rows)

    # Minimal, helpful console output
    print(f"Parsed tables: {len(tables)}")
    print(f"Rows written: {len(rows)} (header columns: {len(header)})")
    print(f"CSV saved to: {output_path}")


if __name__ == "__main__":
    main()

