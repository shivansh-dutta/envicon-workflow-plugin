"""Shared helpers for Envicon LightRAG wrappers."""

from __future__ import annotations

import asyncio
import os
from pathlib import Path

from dotenv import load_dotenv


def load_env() -> None:
    load_dotenv()


def resolve_working_dir(project_path: Path) -> Path:
    return project_path / ".lightrag"


def require_api_key() -> str:
    key = os.getenv("OPENAI_API_KEY", "").strip()
    if not key:
        raise SystemExit(
            "OPENAI_API_KEY is required for LightRAG embeddings and LLM. "
            "Set it in .env or your environment."
        )
    return key


async def create_rag(working_dir: Path):
    from lightrag import LightRAG
    from lightrag.kg.shared_storage import initialize_pipeline_status
    from lightrag.llm.openai import gpt_4o_mini_complete, openai_embed

    require_api_key()
    working_dir.mkdir(parents=True, exist_ok=True)

    rag = LightRAG(
        working_dir=str(working_dir),
        embedding_func=openai_embed,
        llm_model_func=gpt_4o_mini_complete,
    )
    await rag.initialize_storages()
    await initialize_pipeline_status()
    return rag


async def finalize_rag(rag) -> None:
    if rag is not None:
        await rag.finalize_storages()


def run_async(coro):
    return asyncio.run(coro)
