#!/usr/bin/env python3
"""Ingest EDR PDFs from a Phase 1 project Raw/ folder into LightRAG."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from pypdf import PdfReader

from _common import create_rag, finalize_rag, load_env, resolve_working_dir, run_async


def extract_pdf_text(pdf_path: Path) -> str:
    reader = PdfReader(str(pdf_path))
    pages = []
    for i, page in enumerate(reader.pages, start=1):
        text = page.extract_text() or ""
        if text.strip():
            pages.append(f"--- Page {i} ---\n{text}")
    return "\n\n".join(pages)


def find_pdfs(raw_dir: Path) -> list[Path]:
    if not raw_dir.is_dir():
        raise SystemExit(f"Raw/ directory not found: {raw_dir}")
    pdfs = sorted(raw_dir.glob("*.pdf"))
    if not pdfs:
        raise SystemExit(f"No PDF files found in {raw_dir}")
    return pdfs


async def ingest(project_path: Path) -> None:
    load_env()
    raw_dir = project_path / "Raw"
    working_dir = resolve_working_dir(project_path)
    pdfs = find_pdfs(raw_dir)

    print(f"Project: {project_path}")
    print(f"Index:   {working_dir}")
    print(f"PDFs:    {len(pdfs)}")

    rag = None
    try:
        rag = await create_rag(working_dir)
        for pdf in pdfs:
            print(f"Ingesting {pdf.name}...")
            text = extract_pdf_text(pdf)
            if not text.strip():
                print(f"  Skipped (no extractable text): {pdf.name}")
                continue
            doc_id = pdf.stem
            await rag.ainsert(text, ids=[doc_id])
            print(f"  Done ({len(text):,} chars)")
        print("Ingestion complete.")
    finally:
        await finalize_rag(rag)


def main() -> None:
    parser = argparse.ArgumentParser(description="Ingest EDR PDFs into LightRAG")
    parser.add_argument(
        "project_path",
        type=Path,
        help="Path to Projects/<name>/ folder",
    )
    args = parser.parse_args()
    project_path = args.project_path.resolve()
    if not project_path.is_dir():
        print(f"Not a directory: {project_path}", file=sys.stderr)
        sys.exit(1)
    run_async(ingest(project_path))


if __name__ == "__main__":
    main()
