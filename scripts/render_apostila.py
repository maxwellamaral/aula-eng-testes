#!/usr/bin/env python3
"""Renderiza a apostila Typst e a publica na saída estática do Quarto."""

from __future__ import annotations

import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
APOSTILA = ROOT / "docs" / "apostila.qmd"
INCLUDE_PATTERN = re.compile(r"\{\{<\s*include\s+([^\s}]+)")


def validate_includes() -> None:
    for include_path in INCLUDE_PATTERN.findall(APOSTILA.read_text(encoding="utf-8")):
        source = APOSTILA.parent / include_path
        if not source.is_file():
            raise FileNotFoundError(f"Include ausente na apostila: {source.relative_to(ROOT)}")


def main() -> int:
    if not APOSTILA.is_file():
        print("Apostila não gerada: docs/apostila.qmd não encontrado.", file=sys.stderr)
        return 1

    try:
        validate_includes()
    except FileNotFoundError as error:
        print(f"Apostila não gerada: {error}", file=sys.stderr)
        return 1

    subprocess.run(
        ["quarto", "render", "docs/apostila.qmd", "--to", "typst"],
        cwd=ROOT,
        check=True,
    )

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
