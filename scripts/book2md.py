"""
Split a Markdown book into chapter-level Markdown files and a full-book TXT.

The splitter uses Markdown headings as chapter boundaries, with optional
filters to avoid TOC headings and to match chapter-like titles.
"""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Iterable, List, Optional, Pattern, Tuple


HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")
FENCE_RE = re.compile(r"^(```|~~~)")

DEFAULT_CHAPTER_REGEX = (
    r"^(Chapter|Part|Preface|Copyright|Acknowledgments|Index)\b"
)
DEFAULT_TOC_MARKER = "Table of Contents"
DEFAULT_TOC_END_REGEX = r"^(Copyright|Preface)\b"


@dataclass
class Chapter:
    title: str
    content: str
    order: int


def safe_filename_from_title(title: str, index: int) -> str:
    """Create a filesystem-friendly filename fragment using ASCII only."""
    normalized = title.strip().lower()
    sanitized = re.sub(r"[^a-z0-9_-]+", "-", normalized)
    sanitized = sanitized.strip("-") or f"section-{index}"
    return f"{index:03d}-{sanitized}.md"


def detect_toc_start(lines: Iterable[str], marker: str) -> bool:
    """Return True if the TOC marker appears in the content."""
    marker_lower = marker.lower()
    return any(marker_lower in line.lower() for line in lines)


def find_toc_end_index(
    lines: List[str], toc_end_pattern: Pattern[str]
) -> Optional[int]:
    """Find the first heading index that marks the end of the TOC."""
    for idx, line in enumerate(lines):
        match = HEADING_RE.match(line.lstrip())
        if not match:
            continue
        title = match.group(2).strip()
        title = re.sub(r"\s+#+\s*$", "", title).strip()
        if toc_end_pattern.search(title):
            return idx
    return None


def split_markdown_by_chapter(
    lines: List[str],
    heading_level: int,
    chapter_pattern: Pattern[str],
    default_title: str,
    front_matter_title: str,
    skip_headings_before: int = 0,
) -> List[Chapter]:
    chapters: List[Chapter] = []
    preface_lines: List[str] = []
    current_title: Optional[str] = None
    current_lines: List[str] = []
    order = 0
    in_fence = False
    fence_marker = ""

    def flush_current() -> None:
        nonlocal order, current_title, current_lines
        if current_title is None:
            return
        content = "".join(current_lines).strip("\n")
        chapters.append(Chapter(title=current_title, content=content, order=order))
        order += 1
        current_lines = []

    for idx, line in enumerate(lines):
        stripped = line.lstrip()
        fence_match = FENCE_RE.match(stripped)
        if fence_match:
            marker = fence_match.group(1)
            if not in_fence:
                in_fence = True
                fence_marker = marker
            elif marker == fence_marker:
                in_fence = False
                fence_marker = ""

        if not in_fence and idx >= skip_headings_before:
            heading_match = HEADING_RE.match(stripped)
            if heading_match:
                level = len(heading_match.group(1))
                title = heading_match.group(2).strip()
                title = re.sub(r"\s+#+\s*$", "", title).strip()
                if level == heading_level and chapter_pattern.search(title):
                    if current_title is None:
                        preface_content = "".join(preface_lines).strip("\n")
                        if preface_content.strip():
                            chapters.append(
                                Chapter(
                                    title=front_matter_title,
                                    content=preface_content,
                                    order=order,
                                )
                            )
                            order += 1
                        preface_lines = []
                    else:
                        flush_current()

                    current_title = title
                    current_lines = []
                    continue

        if current_title is None:
            preface_lines.append(line)
        else:
            current_lines.append(line)

    if current_title is None:
        remaining = "".join(preface_lines).strip("\n")
        if remaining.strip():
            chapters.append(
                Chapter(title=default_title, content=remaining, order=order)
            )
    else:
        flush_current()

    return chapters


def save_chapters(chapters: List[Chapter], output_dir: Path) -> List[Path]:
    output_dir.mkdir(parents=True, exist_ok=True)
    outputs: List[Path] = []
    for idx, chapter in enumerate(chapters, start=1):
        filename = safe_filename_from_title(chapter.title, idx)
        out_path = output_dir / filename
        with out_path.open("w", encoding="utf-8") as handle:
            handle.write(f"# {chapter.title}\n\n")
            if chapter.content.strip():
                handle.write(chapter.content.strip("\n"))
                handle.write("\n")
        outputs.append(out_path)
    return outputs


def save_book_txt(
    chapters: List[Chapter], output_dir: Path, source_file: str
) -> Path:
    output_dir.mkdir(parents=True, exist_ok=True)
    book_txt_path = output_dir / "book.txt"
    lines: List[str] = [
        f"Source: {source_file}",
        f"Processed at: {datetime.now().isoformat()}",
        "",
        "-----",
        "",
    ]

    for chapter in chapters:
        lines.append(f"# {chapter.title}")
        lines.append("")
        if chapter.content.strip():
            lines.append(chapter.content.strip())
        lines.append("")
        lines.append("-----")
        lines.append("")

    book_txt_path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    return book_txt_path


def build_output_dir(input_path: Path, output_dir: Optional[Path]) -> Path:
    if output_dir:
        return output_dir
    base = input_path.with_suffix("")
    return base.with_name(f"{base.name}_data")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Split a Markdown book into chapter files and a TXT copy."
    )
    parser.add_argument("input_file", type=Path, help="Path to the Markdown book.")
    parser.add_argument(
        "output_dir",
        type=Path,
        nargs="?",
        default=None,
        help="Output directory for chapter files.",
    )
    parser.add_argument(
        "--heading-level",
        type=int,
        default=1,
        help="Heading level to treat as chapter boundaries.",
    )
    parser.add_argument(
        "--chapter-regex",
        type=str,
        default=DEFAULT_CHAPTER_REGEX,
        help="Regex for heading titles that should start a chapter.",
    )
    parser.add_argument(
        "--front-matter-title",
        type=str,
        default="Front Matter",
        help="Title for content before the first chapter.",
    )
    parser.add_argument(
        "--skip-toc",
        action=argparse.BooleanOptionalAction,
        default=True,
        help="Skip TOC headings when a TOC marker is detected.",
    )
    parser.add_argument(
        "--toc-marker",
        type=str,
        default=DEFAULT_TOC_MARKER,
        help="Marker text used to detect a TOC section.",
    )
    parser.add_argument(
        "--toc-end-regex",
        type=str,
        default=DEFAULT_TOC_END_REGEX,
        help="Regex for headings that mark the TOC end.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    input_path: Path = args.input_file
    if not input_path.exists():
        raise SystemExit(f"Input file not found: {input_path}")

    output_dir = build_output_dir(input_path, args.output_dir)
    content = input_path.read_text(encoding="utf-8", errors="ignore")
    lines = content.splitlines(keepends=True)

    chapter_pattern_text = args.chapter_regex or r".*"
    chapter_pattern = re.compile(chapter_pattern_text, re.IGNORECASE)
    toc_end_pattern = re.compile(args.toc_end_regex, re.IGNORECASE)

    skip_headings_before = 0
    if args.skip_toc and detect_toc_start(lines, args.toc_marker):
        toc_end_index = find_toc_end_index(lines, toc_end_pattern)
        if toc_end_index is not None:
            skip_headings_before = toc_end_index

    chapters = split_markdown_by_chapter(
        lines=lines,
        heading_level=args.heading_level,
        chapter_pattern=chapter_pattern,
        default_title=input_path.stem,
        front_matter_title=args.front_matter_title,
        skip_headings_before=skip_headings_before,
    )

    chapter_paths = save_chapters(chapters, output_dir)
    book_txt_path = save_book_txt(chapters, output_dir, input_path.name)

    print("\n--- Summary ---")
    print(f"Source: {input_path}")
    print(f"Chapters: {len(chapters)}")
    print(f"Chapter files: {len(chapter_paths)}")
    print(f"Book txt: {book_txt_path}")
    print(f"Output dir: {output_dir}")


if __name__ == "__main__":
    main()
