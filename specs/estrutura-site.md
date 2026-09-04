# Estrutura do site

## Organização

- Páginas institucionais: `index.qmd` e `about.qmd`.
- Catálogo de materiais: `docs/index.qmd`.
- Aula: `docs/<nn>-<tema>/`.
- Ativos estáticos: `assets/css/`, `assets/js/` e `assets/images/<nn>-<tema>/`.
- Saída gerada: `_site/`; nunca é editada manualmente.

## Uma aula

Uma aula reutilizável pela apostila contém:

```text
docs/<nn>-<tema>/
├── index.qmd       # título, contexto, links e include do conteúdo
├── _content.qmd    # conteúdo canônico incluído pela página e pela apostila
└── slides.qmd      # opcional, para apresentação presencial
```

Laboratórios ficam no mesmo diretório como `laboratorio.qmd`. Ao criar uma aula, atualize `docs/index.qmd`; atualize `docs/apostila.qmd` somente quando o conteúdo canônico deve integrar o PDF.

## Renderização

`_quarto.yml` é a configuração global. O projeto gera o site em `_site/`. Após uma renderização completa, execute `uv run python scripts/render_apostila.py` para gerar `docs/apostila.pdf` e copiá-la para `_site/docs/apostila.pdf`; o script não é acionado durante `quarto preview`.
