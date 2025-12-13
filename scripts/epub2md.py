"""
Convert an EPUB file into structured data and chapter-level Markdown files.

The script mirrors the parsing/cleaning logic from reader3.py: it extracts
metadata, TOC, spine content, and images, cleans HTML, saves images, pickles
the `Book` object, and writes one Markdown file per spine item.
"""

import os
import pickle
import shutil
from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional
from urllib.parse import unquote

import ebooklib
from bs4 import BeautifulSoup, Comment
from ebooklib import epub


# --- Data structures ---

@dataclass
class ChapterContent:
    """
    Represents a physical file in the EPUB (Spine Item).
    A single file might contain multiple logical chapters (TOC entries).
    """
    id: str           # Internal ID (e.g., 'item_1')
    href: str         # Filename (e.g., 'part01.html')
    title: str        # Best guess title from file or TOC
    content: str      # Cleaned HTML with rewritten image paths
    text: str         # Plain text for search/LLM context
    order: int        # Linear reading order


@dataclass
class TOCEntry:
    """Represents a logical entry in the navigation sidebar."""
    title: str
    href: str         # original href (e.g., 'part01.html#chapter1')
    file_href: str    # just the filename (e.g., 'part01.html')
    anchor: str       # just the anchor (e.g., 'chapter1'), empty if none
    children: List['TOCEntry'] = field(default_factory=list)


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
    toc: List[TOCEntry]          # The navigation tree
    images: Dict[str, str]       # Map: original_path -> local_path

    # Meta info
    source_file: str
    processed_at: str
    version: str = "3.0"


# --- Utilities ---

def clean_html_content(soup: BeautifulSoup) -> BeautifulSoup:
    """Strip dangerous/useless tags and comments."""
    for tag in soup(['script', 'style', 'iframe', 'video', 'nav', 'form', 'button']):
        tag.decompose()

    for comment in soup.find_all(string=lambda text: isinstance(text, Comment)):
        comment.extract()

    for tag in soup.find_all('input'):
        tag.decompose()

    return soup


def extract_plain_text(soup: BeautifulSoup) -> str:
    """Extract clean text for LLM/Search usage."""
    text = soup.get_text(separator=' ')
    return ' '.join(text.split())


def parse_toc_recursive(toc_list: List[Any], depth: int = 0) -> List[TOCEntry]:
    """Recursively parses the TOC structure from ebooklib."""
    result: List[TOCEntry] = []

    for item in toc_list:
        if isinstance(item, tuple):
            section, children = item
            entry = TOCEntry(
                title=section.title,
                href=section.href,
                file_href=section.href.split('#')[0],
                anchor=section.href.split('#')[1] if '#' in section.href else "",
                children=parse_toc_recursive(children, depth + 1)
            )
            result.append(entry)
        elif isinstance(item, epub.Link):
            entry = TOCEntry(
                title=item.title,
                href=item.href,
                file_href=item.href.split('#')[0],
                anchor=item.href.split('#')[1] if '#' in item.href else ""
            )
            result.append(entry)
        elif isinstance(item, epub.Section):
            entry = TOCEntry(
                title=item.title,
                href=item.href,
                file_href=item.href.split('#')[0],
                anchor=item.href.split('#')[1] if '#' in item.href else ""
            )
            result.append(entry)

    return result


def get_fallback_toc(book_obj: epub.EpubBook) -> List[TOCEntry]:
    """If TOC is missing, build a flat one from the Spine."""
    toc: List[TOCEntry] = []
    for item in book_obj.get_items():
        if item.get_type() == ebooklib.ITEM_DOCUMENT:
            name = item.get_name()
            title = name.replace('.html', '').replace('.xhtml', '').replace('_', ' ').title()
            toc.append(TOCEntry(title=title, href=name, file_href=name, anchor=""))
    return toc


def extract_metadata_robust(book_obj: epub.EpubBook) -> BookMetadata:
    """Extracts metadata handling both single and list values."""
    def get_list(key: str) -> List[str]:
        data = book_obj.get_metadata('DC', key)
        return [x[0] for x in data] if data else []

    def get_one(key: str) -> Optional[str]:
        data = book_obj.get_metadata('DC', key)
        return data[0][0] if data else None

    return BookMetadata(
        title=get_one('title') or "Untitled",
        language=get_one('language') or "en",
        authors=get_list('creator'),
        description=get_one('description'),
        publisher=get_one('publisher'),
        date=get_one('date'),
        identifiers=get_list('identifier'),
        subjects=get_list('subject')
    )


def collect_toc_title_map(entries: List[TOCEntry], mapping: Optional[Dict[str, str]] = None) -> Dict[str, str]:
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
    sanitized = "".join(c if c.isalnum() or c in "-_" else "-" for c in title.strip().lower())
    sanitized = sanitized.strip("-") or f"section-{index}"
    return f"{index:03d}-{sanitized}.md"


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
    images_dir = os.path.join(output_dir, 'images')
    os.makedirs(images_dir, exist_ok=True)

    # 4. Extract Images & Build Map
    print("Extracting images...")
    image_map: Dict[str, str] = {}  # Key: internal_path, Value: local_relative_path

    for item in book.get_items():
        if item.get_type() == ebooklib.ITEM_IMAGE:
            original_fname = os.path.basename(item.get_name())
            safe_fname = "".join([c for c in original_fname if c.isalpha() or c.isdigit() or c in '._-']).strip()

            local_path = os.path.join(images_dir, safe_fname)
            with open(local_path, 'wb') as f:
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
            raw_content = item.get_content().decode('utf-8', errors='ignore')
            soup = BeautifulSoup(raw_content, 'html.parser')

            # Fix Images
            for img in soup.find_all('img'):
                src = img.get('src', '')
                if not src:
                    continue

                src_decoded = unquote(src)
                filename = os.path.basename(src_decoded)

                if src_decoded in image_map:
                    img['src'] = image_map[src_decoded]
                elif filename in image_map:
                    img['src'] = image_map[filename]

            # Clean HTML
            soup = clean_html_content(soup)

            # Extract Body Content only
            body = soup.find('body')
            if body:
                final_html = "".join([str(x) for x in body.contents])
            else:
                final_html = str(soup)

            spine_chapters.append(
                ChapterContent(
                    id=item_id,
                    href=item.get_name(),
                    title=title_map.get(item.get_name(), f"Section {i + 1}"),
                    content=final_html,
                    text=extract_plain_text(soup),
                    order=i
                )
            )

    # 7. Final Assembly
    final_book = Book(
        metadata=metadata,
        spine=spine_chapters,
        toc=toc_structure,
        images=image_map,
        source_file=os.path.basename(epub_path),
        processed_at=datetime.now().isoformat()
    )

    return final_book


def save_to_pickle(book: Book, output_dir: str) -> str:
    p_path = os.path.join(output_dir, 'book.pkl')
    with open(p_path, 'wb') as f:
        pickle.dump(book, f)
    print(f"Saved structured data to {p_path}")
    return p_path


def save_chapter_markdown(book: Book, output_dir: str) -> List[str]:
    """Write each spine item to a standalone Markdown file."""
    markdown_paths: List[str] = []

    for chapter in book.spine:
        filename = safe_filename_from_title(chapter.title, chapter.order + 1)
        out_path = os.path.join(output_dir, filename)
        with open(out_path, 'w', encoding='utf-8') as f:
            f.write(f"# {chapter.title}\n\n")
            f.write(f"<!-- href: {chapter.href} -->\n\n")
            f.write(chapter.content)
            f.write("\n")
        markdown_paths.append(out_path)
        print(f"Wrote {out_path}")

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

    output_dir = sys.argv[2] if len(sys.argv) > 2 else os.path.splitext(epub_file)[0] + "_data"

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
