"""
Convert an EPUB file into structured data and chapter-level Markdown files.

The script mirrors the parsing/cleaning logic from reader3.py: it extracts
metadata, TOC, spine content, and images, cleans HTML, saves images, pickles
the `Book` object, and writes one Markdown file per spine item.
"""

import os
import pickle
import re
import shutil
from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional
from urllib.parse import unquote

import ebooklib
from bs4 import BeautifulSoup, Comment, NavigableString
from ebooklib import epub

# --- Data structures ---


@dataclass
class ChapterContent:
    """
    Represents a physical file in the EPUB (Spine Item).
    A single file might contain multiple logical chapters (TOC entries).
    """

    id: str  # Internal ID (e.g., 'item_1')
    href: str  # Filename (e.g., 'part01.html')
    title: str  # Best guess title from file or TOC
    content: str  # Cleaned HTML with rewritten image paths
    text: str  # Plain text for search/LLM context
    order: int  # Linear reading order


@dataclass
class TOCEntry:
    """Represents a logical entry in the navigation sidebar."""

    title: str
    href: str  # original href (e.g., 'part01.html#chapter1')
    file_href: str  # just the filename (e.g., 'part01.html')
    anchor: str  # just the anchor (e.g., 'chapter1'), empty if none
    children: List["TOCEntry"] = field(default_factory=list)


@dataclass
class BookMetadata:
    """Metadata"""

    title: str
    language: str
    authors: List[str] = field(default_factory=list)
    description: Optional[str] = None
    publisher: Optional[str] = None
    date: Optional[str] = None
    identifiers: List[str] = field(default_factory=list)
    subjects: List[str] = field(default_factory=list)


@dataclass
class Book:
    """The Master Object to be pickled."""

    metadata: BookMetadata
    spine: List[ChapterContent]  # The actual content (linear files)
    toc: List[TOCEntry]  # The navigation tree
    images: Dict[str, str]  # Map: original_path -> local_path

    # Meta info
    source_file: str
    processed_at: str
    version: str = "3.0"


# --- Utilities ---


def clean_html_content(soup: BeautifulSoup) -> BeautifulSoup:
    """Strip dangerous/useless tags and comments."""
    for tag in soup(["script", "style", "iframe", "video", "nav", "form", "button"]):
        tag.decompose()

    for comment in soup.find_all(string=lambda text: isinstance(text, Comment)):
        comment.extract()

    for tag in soup.find_all("input"):
        tag.decompose()

    return soup


def extract_plain_text(soup: BeautifulSoup) -> str:
    """Extract clean text for LLM/Search usage."""
    text = soup.get_text(separator=" ")
    return " ".join(text.split())


def html_to_markdown(html: str) -> str:
    """
    Convert cleaned HTML into lightweight Markdown/plaintext.
    This is intentionally simple to avoid extra dependencies.
    """
    soup = BeautifulSoup(html, "html.parser")
    lines: List[str] = []

    def emit_blank():
        if lines and lines[-1] != "":
            lines.append("")

    def walk(node):
        if isinstance(node, Comment):
            return
        if isinstance(node, NavigableString):
            text = str(node).strip()
            if text:
                lines.append(text)
            return
        if not hasattr(node, "name") or node.name is None:
            return

        name = node.name.lower()

        if name in {"h1", "h2", "h3", "h4", "h5", "h6"}:
            level = int(name[1])
            heading = node.get_text(" ", strip=True)
            lines.append(f"{'#' * level} {heading}")
            emit_blank()
            return

        if name == "p":
            paragraph = node.get_text(" ", strip=True)
            if paragraph:
                lines.append(paragraph)
                emit_blank()
            return

        if name == "br":
            lines.append("")
            return

        if name in {"ul", "ol"}:
            for idx, li in enumerate(node.find_all("li", recursive=False)):
                bullet = "-" if name == "ul" else f"{idx + 1}."
                text = li.get_text(" ", strip=True)
                lines.append(f"{bullet} {text}")
            emit_blank()
            return

        if name == "blockquote":
            quote = node.get_text(" ", strip=True)
            if quote:
                lines.append(f"> {quote}")
                emit_blank()
            return

        if name in {"pre", "code"}:
            code_text = node.get_text("", strip=True)
            if code_text:
                lines.append("```")
                lines.append(code_text)
                lines.append("```")
                emit_blank()
            return

        if name == "img":
            src = node.get("src", "")
            alt = node.get("alt", "")
            if src:
                lines.append(f"![{alt}]({src})")
                emit_blank()
            return

        if name == "a":
            text = node.get_text(" ", strip=True)
            href = node.get("href", "")
            if text and href:
                lines.append(f"[{text}]({href})")
            elif text:
                lines.append(text)
            return

        for child in node.children:
            walk(child)

    for child in soup.body.children if soup.body else soup.children:
        walk(child)

    # Collapse consecutive blanks
    collapsed: List[str] = []
    for line in lines:
        if line.strip() == "":
            if collapsed and collapsed[-1] != "":
                collapsed.append("")
        else:
            collapsed.append(line)

    return "\n".join(collapsed).strip()


def parse_toc_recursive(toc_list: List[Any], depth: int = 0) -> List[TOCEntry]:
    """Recursively parses the TOC structure from ebooklib."""
    result: List[TOCEntry] = []

    for item in toc_list:
        if isinstance(item, tuple):
            section, children = item
            entry = TOCEntry(
                title=section.title,
                href=section.href,
                file_href=section.href.split("#")[0],
                anchor=section.href.split("#")[1] if "#" in section.href else "",
                children=parse_toc_recursive(children, depth + 1),
            )
            result.append(entry)
        elif isinstance(item, epub.Link):
            entry = TOCEntry(
                title=item.title,
                href=item.href,
                file_href=item.href.split("#")[0],
                anchor=item.href.split("#")[1] if "#" in item.href else "",
            )
            result.append(entry)
        elif isinstance(item, epub.Section):
            entry = TOCEntry(
                title=item.title,
                href=item.href,
                file_href=item.href.split("#")[0],
                anchor=item.href.split("#")[1] if "#" in item.href else "",
            )
            result.append(entry)

    return result


def get_fallback_toc(book_obj: epub.EpubBook) -> List[TOCEntry]:
    """If TOC is missing, build a flat one from the Spine."""
    toc: List[TOCEntry] = []
    for item in book_obj.get_items():
        if item.get_type() == ebooklib.ITEM_DOCUMENT:
            name = item.get_name()
            title = (
                name.replace(".html", "")
                .replace(".xhtml", "")
                .replace("_", " ")
                .title()
            )
            toc.append(TOCEntry(title=title, href=name, file_href=name, anchor=""))
    return toc


def extract_metadata_robust(book_obj: epub.EpubBook) -> BookMetadata:
    """Extracts metadata handling both single and list values."""

    def get_list(key: str) -> List[str]:
        data = book_obj.get_metadata("DC", key)
        return [x[0] for x in data] if data else []

    def get_one(key: str) -> Optional[str]:
        data = book_obj.get_metadata("DC", key)
        return data[0][0] if data else None

    return BookMetadata(
        title=get_one("title") or "Untitled",
        language=get_one("language") or "en",
        authors=get_list("creator"),
        description=get_one("description"),
        publisher=get_one("publisher"),
        date=get_one("date"),
        identifiers=get_list("identifier"),
        subjects=get_list("subject"),
    )


def collect_toc_title_map(
    entries: List[TOCEntry], mapping: Optional[Dict[str, str]] = None
) -> Dict[str, str]:
    """Flatten TOC into a filename -> title map for quick lookups."""
    mapping = mapping or {}
    for entry in entries:
        if entry.file_href and entry.file_href not in mapping:
            mapping[entry.file_href] = entry.title
        if entry.children:
            collect_toc_title_map(entry.children, mapping)
    return mapping


def safe_filename_from_title(title: str, index: int) -> str:
    """Create a filesystem-friendly filename fragment."""
    sanitized = "".join(
        c if c.isalnum() or c in "-_" else "-" for c in title.strip().lower()
    )
    sanitized = sanitized.strip("-") or f"section-{index}"
    return f"{index:03d}-{sanitized}.md"


_CHAPTER_TITLE_RE = re.compile(
    r"^\s*chapter\s+(?P<number>\d+)\b(?:\s*[:.\-–—]\s*)?(?P<rest>.*)$",
    re.IGNORECASE,
)
_CHAPTER_TITLE_ZH_RE = re.compile(
    r"^\s*第(?P<number>[0-9零〇一二三四五六七八九十百千两]+)\s*[章节回部篇]\s*(?:[:：.\-–—、]\s*)?(?P<rest>.*)$"
)
_CHINESE_NUMERAL_MAP = {
    "零": 0,
    "〇": 0,
    "一": 1,
    "二": 2,
    "两": 2,
    "三": 3,
    "四": 4,
    "五": 5,
    "六": 6,
    "七": 7,
    "八": 8,
    "九": 9,
}
_CHINESE_UNIT_MAP = {"十": 10, "百": 100, "千": 1000}


def _sanitize_title_fragment(text: str) -> str:
    sanitized = "".join(c if c.isalnum() or c in "-_" else "-" for c in text.lower())
    return sanitized.strip("-")


def _chinese_numeral_to_int(text: str) -> Optional[int]:
    if not text:
        return None
    if text.isdigit():
        return int(text)

    total = 0
    current = 0
    for char in text:
        if char in _CHINESE_NUMERAL_MAP:
            current = _CHINESE_NUMERAL_MAP[char]
        elif char in _CHINESE_UNIT_MAP:
            unit_value = _CHINESE_UNIT_MAP[char]
            if current == 0:
                current = 1
            total += current * unit_value
            current = 0
        else:
            return None
    total += current
    return total if total > 0 else None


def _build_chapter_filename(number: int, rest: str, epub_stem: str) -> str:
    sanitized_rest = _sanitize_title_fragment(rest.strip())
    if not sanitized_rest:
        sanitized_rest = f"chapter-{number}"
    chapter_code = f"{number:02d}01"
    return f"{epub_stem}{chapter_code}-{sanitized_rest}.md"


def safe_spine_markdown_filename(title: str, index: int, epub_stem: str) -> str:
    """
    Generate the Markdown filename for a spine item.

    - Default: keep the legacy `{index:03d}-<sanitized-title>.md` format.
    - For main chapters whose title starts with `chapter <n>` (case-insensitive),
      switch to: `<epub_stem>{n:02d}01-<sanitized-rest>.md`.

    Example:
        `007-chapter-1-scaling.md` -> `2025213The-Scaling-Era0101-scaling.md`
    """
    match = _CHAPTER_TITLE_RE.match(title)
    if match:
        return _build_chapter_filename(
            number=int(match.group("number")),
            rest=match.group("rest"),
            epub_stem=epub_stem,
        )

    zh_match = _CHAPTER_TITLE_ZH_RE.match(title)
    if zh_match:
        number = _chinese_numeral_to_int(zh_match.group("number"))
        if number is not None:
            return _build_chapter_filename(
                number=number,
                rest=zh_match.group("rest"),
                epub_stem=epub_stem,
            )

    return safe_filename_from_title(title, index)


# --- Main Conversion Logic ---


def process_epub(epub_path: str, output_dir: str) -> Book:
    # 1. Load Book
    print(f"Loading {epub_path}...")
    book = epub.read_epub(epub_path)

    # 2. Extract Metadata
    metadata = extract_metadata_robust(book)

    # 3. Prepare Output Directories
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)
    images_dir = os.path.join(output_dir, "images")
    os.makedirs(images_dir, exist_ok=True)

    # 4. Extract Images & Build Map
    print("Extracting images...")
    image_map: Dict[str, str] = {}  # Key: internal_path, Value: local_relative_path

    for item in book.get_items():
        if item.get_type() == ebooklib.ITEM_IMAGE:
            original_fname = os.path.basename(item.get_name())
            safe_fname = "".join(
                [c for c in original_fname if c.isalpha() or c.isdigit() or c in "._-"]
            ).strip()

            local_path = os.path.join(images_dir, safe_fname)
            with open(local_path, "wb") as f:
                f.write(item.get_content())

            rel_path = f"images/{safe_fname}"
            image_map[item.get_name()] = rel_path
            image_map[original_fname] = rel_path

    # 5. Process TOC
    print("Parsing Table of Contents...")
    toc_structure = parse_toc_recursive(book.toc)
    if not toc_structure:
        print("Warning: Empty TOC, building fallback from Spine...")
        toc_structure = get_fallback_toc(book)

    title_map = collect_toc_title_map(toc_structure)

    # 6. Process Content (Spine-based to preserve HTML validity)
    print("Processing chapters...")
    spine_chapters: List[ChapterContent] = []

    for i, spine_item in enumerate(book.spine):
        item_id, _ = spine_item
        item = book.get_item_with_id(item_id)

        if not item:
            continue

        if item.get_type() == ebooklib.ITEM_DOCUMENT:
            raw_content = item.get_content().decode("utf-8", errors="ignore")
            soup = BeautifulSoup(raw_content, "html.parser")

            # Fix Images
            for img in soup.find_all("img"):
                src = img.get("src", "")
                if not src:
                    continue

                src_decoded = unquote(src)
                filename = os.path.basename(src_decoded)

                if src_decoded in image_map:
                    img["src"] = image_map[src_decoded]
                elif filename in image_map:
                    img["src"] = image_map[filename]

            # Clean HTML
            soup = clean_html_content(soup)

            # Extract Body Content only
            body = soup.find("body")
            if body:
                final_html = "".join([str(x) for x in body.contents])
            else:
                final_html = str(soup)

            final_md = html_to_markdown(final_html)

            spine_chapters.append(
                ChapterContent(
                    id=item_id,
                    href=item.get_name(),
                    title=title_map.get(item.get_name(), f"Section {i + 1}"),
                    content=final_md,
                    text=extract_plain_text(soup),
                    order=i,
                )
            )

    # 7. Final Assembly
    final_book = Book(
        metadata=metadata,
        spine=spine_chapters,
        toc=toc_structure,
        images=image_map,
        source_file=os.path.basename(epub_path),
        processed_at=datetime.now().isoformat(),
    )

    return final_book


def save_to_pickle(book: Book, output_dir: str) -> str:
    p_path = os.path.join(output_dir, "book.pkl")
    with open(p_path, "wb") as f:
        pickle.dump(book, f)
    print(f"Saved structured data to {p_path}")
    return p_path


def save_chapter_markdown(book: Book, output_dir: str) -> List[str]:
    """
    Write each spine item to a standalone Markdown file.

    Additionally, write the entire book (all spine items) into a single `.txt`
    file for convenient full-book reading/LLM context.
    """
    os.makedirs(output_dir, exist_ok=True)
    markdown_paths: List[str] = []
    ordered_spine = sorted(book.spine, key=lambda c: c.order)
    epub_stem = os.path.splitext(book.source_file)[0]

    for chapter in ordered_spine:
        filename = safe_spine_markdown_filename(
            title=chapter.title,
            index=chapter.order + 1,
            epub_stem=epub_stem,
        )
        out_path = os.path.join(output_dir, filename)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(f"# {chapter.title}\n\n")
            f.write(f"<!-- href: {chapter.href} -->\n\n")
            f.write(chapter.content)
            f.write("\n")
        markdown_paths.append(out_path)
        print(f"Wrote {out_path}")

    book_txt_path = os.path.join(output_dir, "book.txt")
    book_lines: List[str] = [
        f"Title: {book.metadata.title}",
        f"Authors: {', '.join(book.metadata.authors) if book.metadata.authors else 'Unknown'}",
        f"Language: {book.metadata.language}",
        f"Source: {book.source_file}",
        f"Processed at: {book.processed_at}",
        "",
        "-----",
        "",
    ]

    for chapter in ordered_spine:
        book_lines.append(f"# {chapter.title}")
        book_lines.append(f"<!-- href: {chapter.href} -->")
        book_lines.append("")
        if chapter.content.strip():
            book_lines.append(chapter.content.strip())
        book_lines.append("")
        book_lines.append("-----")
        book_lines.append("")

    with open(book_txt_path, "w", encoding="utf-8") as f:
        f.write("\n".join(book_lines).rstrip() + "\n")
    print(f"Wrote {book_txt_path}")

    return markdown_paths


# --- CLI ---


def main():
    import sys

    if len(sys.argv) < 2:
        print("Usage: python scripts/epub2md.py <file.epub> [output_dir]")
        sys.exit(1)

    epub_file = sys.argv[1]
    if not os.path.exists(epub_file):
        print(f"File not found: {epub_file}")
        sys.exit(1)

    output_dir = (
        sys.argv[2] if len(sys.argv) > 2 else os.path.splitext(epub_file)[0] + "_data"
    )

    book_obj = process_epub(epub_file, output_dir)
    save_to_pickle(book_obj, output_dir)
    save_chapter_markdown(book_obj, output_dir)

    print("\n--- Summary ---")
    print(f"Title: {book_obj.metadata.title}")
    print(f"Authors: {', '.join(book_obj.metadata.authors)}")
    print(f"Physical Files (Spine): {len(book_obj.spine)}")
    print(f"TOC Root Items: {len(book_obj.toc)}")
    print(f"Images extracted: {len(book_obj.images)}")
    print(f"Output dir: {output_dir}")


if __name__ == "__main__":
    main()
