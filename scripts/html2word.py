#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""Convert HTML documents to Word (DOCX) using Pandoc with high fidelity."""

import argparse
import shutil
import subprocess
import sys
from pathlib import Path


def ensure_pandoc(executable: str) -> str:
    """Locate the Pandoc executable or raise an informative error."""
    pandoc_path = shutil.which(executable)
    if pandoc_path:
        return pandoc_path
    raise FileNotFoundError(
        f"未找到 Pandoc 可执行文件 '{executable}'。请先安装 Pandoc 并确保它在 PATH 中。"
    )


def normalize_output_path(output: Path, input_path: Path) -> Path:
    if output.suffix.lower() != ".docx":
        output = output.with_suffix(".docx")
    if not output.is_absolute():
        output = (input_path.parent / output).resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    return output


def build_resource_path(paths: list[Path]) -> str:
    # Pandoc expects PATH-like string for resource lookup.
    sep = ";" if sys.platform.startswith("win") else ":"
    return sep.join(str(p) for p in paths)


def convert_html_to_docx(
    html_path: Path,
    output_path: Path | None = None,
    reference_doc: Path | None = None,
    resource_paths: list[Path] | None = None,
    pandoc_bin: str = "pandoc",
    extra_args: list[str] | None = None,
) -> Path:
    pandoc_executable = ensure_pandoc(pandoc_bin)

    if not html_path.exists() or not html_path.is_file():
        raise FileNotFoundError(f"未找到输入文件: {html_path}")

    if output_path is None:
        output_path = html_path.with_suffix(".docx")
    output_path = normalize_output_path(output_path, html_path)

    resources = resource_paths or [html_path.parent]
    cmd = [
        pandoc_executable,
        str(html_path),
        "--from",
        "html+smart",
        "--to",
        "docx",
        "--standalone",
        "--output",
        str(output_path),
        "--resource-path",
        build_resource_path([p.resolve() for p in resources]),
    ]

    if reference_doc:
        cmd.extend(["--reference-doc", str(reference_doc.resolve())])

    if extra_args:
        cmd.extend(extra_args)

    try:
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as exc:
        raise RuntimeError(
            "Pandoc 转换失败，请检查输入文件与参数设置。"
        ) from exc

    return output_path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="使用 Pandoc 将 HTML 转换为高还原度的 Word (DOCX) 文件"
    )
    parser.add_argument("input", help="待转换的 HTML 文件路径")
    parser.add_argument(
        "-o",
        "--output",
        help="输出 DOCX 文件路径（可省略，默认为与输入同名）",
    )
    parser.add_argument(
        "--reference-doc",
        help="Pandoc reference DOCX，用于套用样式模板",
    )
    parser.add_argument(
        "--resource-path",
        action="append",
        dest="resource_paths",
        help="资源检索路径，可重复提供以定位图片等静态资源",
    )
    parser.add_argument(
        "--pandoc-bin",
        default="pandoc",
        help="Pandoc 可执行文件名称或路径，默认 pandoc",
    )
    parser.add_argument(
        "--extra-arg",
        dest="extra_args",
        action="append",
        help="透传额外的 Pandoc 参数，可重复使用",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    html_path = Path(args.input).expanduser().resolve()
    output_path = Path(args.output).expanduser() if args.output else None
    reference_doc = Path(args.reference_doc).expanduser().resolve() if args.reference_doc else None

    resource_paths = (
        [Path(p).expanduser().resolve() for p in args.resource_paths]
        if args.resource_paths
        else None
    )

    extra_args = args.extra_args or []

    try:
        result = convert_html_to_docx(
            html_path=html_path,
            output_path=output_path,
            reference_doc=reference_doc,
            resource_paths=resource_paths,
            pandoc_bin=args.pandoc_bin,
            extra_args=extra_args,
        )
    except Exception as exc:  # Surface friendly errors for CLI usage.
        print(f"转换失败: {exc}", file=sys.stderr)
        sys.exit(1)

    print(f"转换完成: {result}")


if __name__ == "__main__":
    main()
