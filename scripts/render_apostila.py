#!/usr/bin/env python3
"""Renderiza a apostila Typst e a publica na saída estática do Quarto."""

from __future__ import annotations

import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
APOSTILA = ROOT / "docs" / "apostila.qmd"
INCLUDE_PATTERN = re.compile(r"\{\{<\s*include\s+([^\s}]+)")
CACHE_LOCK_MARKER = "database is locked"
STAGING_IGNORE = shutil.ignore_patterns(
    ".git",
    ".quarto",
    ".venv",
    "_site",
    ".env",
    "*.local",
    "resources",
    "scratch",
    "__pycache__",
    "apostila.pdf",
    "*_files",
    "*.quarto_ipynb",
)


def validate_includes() -> None:
    for include_path in INCLUDE_PATTERN.findall(APOSTILA.read_text(encoding="utf-8")):
        source = APOSTILA.parent / include_path
        if not source.is_file():
            raise FileNotFoundError(f"Include ausente na apostila: {source.relative_to(ROOT)}")


def render_typst(root: Path) -> None:
    result = subprocess.run(
        ["quarto", "render", "docs/apostila.qmd", "--to", "typst"],
        cwd=root,
        text=True,
        capture_output=True,
    )
    if result.returncode == 0:
        print(result.stdout, end="")
        return

    print(result.stdout, end="", file=sys.stderr)
    print(result.stderr, end="", file=sys.stderr)
    raise subprocess.CalledProcessError(
        result.returncode,
        result.args,
        output=result.stdout,
        stderr=result.stderr,
    )


def render_with_staging_fallback() -> None:
    try:
        render_typst(ROOT)
        return
    except subprocess.CalledProcessError as error:
        error_output = f"{error.output or ''}\n{error.stderr or ''}".lower()
        if CACHE_LOCK_MARKER not in error_output:
            raise

    print(
        "Cache Quarto bloqueado no diretório de trabalho; "
        "renderizando a apostila em uma cópia temporária.",
        file=sys.stderr,
    )
    with tempfile.TemporaryDirectory(prefix="vvts-apostila-") as temporary_dir:
        staging_root = Path(temporary_dir) / ROOT.name
        shutil.copytree(ROOT, staging_root, ignore=STAGING_IGNORE)
        render_typst(staging_root)

        staged_pdf = staging_root / "docs" / "apostila.pdf"
        if not staged_pdf.is_file():
            raise FileNotFoundError("Apostila não gerada: renderização temporária não produziu PDF.")
        shutil.copy2(staged_pdf, APOSTILA.with_suffix(".pdf"))


def main() -> int:
    if not APOSTILA.is_file():
        print("Apostila não gerada: docs/apostila.qmd não encontrado.", file=sys.stderr)
        return 1

    try:
        validate_includes()
    except FileNotFoundError as error:
        print(f"Apostila não gerada: {error}", file=sys.stderr)
        return 1

    render_with_staging_fallback()

    generated_pdf = APOSTILA.with_suffix(".pdf")
    if not generated_pdf.is_file():
        print("Apostila não gerada: Quarto não produziu docs/apostila.pdf.", file=sys.stderr)
        return 1

    output_pdf = ROOT / "_site" / "docs" / "apostila.pdf"
    output_pdf.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(generated_pdf, output_pdf)
    print(f"Apostila gerada: {output_pdf.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
