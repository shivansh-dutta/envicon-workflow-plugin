#!/usr/bin/env python3
"""Query a LightRAG index built from EDR documents."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from lightrag import QueryParam

from _common import create_rag, finalize_rag, load_env, resolve_working_dir, run_async


async def query(project_path: Path, question: str, mode: str) -> str:
    load_env()
    working_dir = resolve_working_dir(project_path)
    if not working_dir.is_dir():
        raise SystemExit(
            f"No LightRAG index at {working_dir}. Run ingest.py first."
        )

    rag = None
    try:
        rag = await create_rag(working_dir)
        result = await rag.aquery(question, param=QueryParam(mode=mode))
        return result
    finally:
        await finalize_rag(rag)


def main() -> None:
    parser = argparse.ArgumentParser(description="Query EDR LightRAG index")
    parser.add_argument("project_path", type=Path, help="Path to Projects/<name>/")
    parser.add_argument("question", help="Natural-language query")
    parser.add_argument(
        "--mode",
        default="hybrid",
        choices=["naive", "local", "global", "hybrid", "mix"],
        help="LightRAG query mode (default: hybrid)",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Output JSON instead of plain text",
    )
    args = parser.parse_args()
    project_path = args.project_path.resolve()
    if not project_path.is_dir():
        print(f"Not a directory: {project_path}", file=sys.stderr)
        sys.exit(1)

    answer = run_async(query(project_path, args.question, args.mode))
    if args.json:
        print(json.dumps({"question": args.question, "answer": answer, "mode": args.mode}))
    else:
        print(answer)


if __name__ == "__main__":
    main()
