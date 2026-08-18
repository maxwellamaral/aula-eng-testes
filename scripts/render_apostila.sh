#!/usr/bin/env bash

set -euo pipefail

# O Quarto executa os scripts de pós-render também ao iniciar e atualizar o
# preview. Nesse contexto, o processo pai contém o subcomando `preview`.
# A apostila é gerada somente por `quarto render` (inclusive no deploy).
if ps -o args= -p "$PPID" | grep -Eq '(^|[[:space:]])preview([[:space:]]|$)'; then
  printf 'Apostila não gerada durante o preview local.\n'
  exit 0
fi

[[ -f docs/apostila.qmd ]] || exit 0

while IFS= read -r include_path; do
  if [[ ! -f "docs/${include_path}" ]]; then
    printf 'Apostila não gerada: include ausente em docs/%s\n' "${include_path}" >&2
    exit 0
  fi
done < <(sed -nE 's/.*include[[:space:]]+([^[:space:]}]+).*/\1/p' docs/apostila.qmd)

quarto render docs/apostila.qmd --to typst

mkdir -p _site/docs
cp docs/apostila.pdf _site/docs/apostila.pdf
