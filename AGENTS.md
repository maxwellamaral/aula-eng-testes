# Instruções do projeto

Este repositório contém o material didático da disciplina **Verificação, Validação e Testes de Software (VVTS)**. O site é gerado com Quarto e publicado a partir de `_site/`.

## Fontes de verdade

- Configuração e navegação global: `_quarto.yml`.
- Catálogo de materiais: `docs/index.qmd`.
- Cada aula: `docs/<nn>-<tema>/index.qmd` e, quando aplicável, `_content.qmd`.
- Apresentações: `docs/<nn>-<tema>/slides.qmd`.
- Laboratórios: `docs/<nn>-<tema>/laboratorio.qmd`.
- Apostila: `docs/apostila.qmd`, que inclui os fragmentos `_content.qmd`.
- Referências bibliográficas: `docs/references.bib`.
- Estilos e comportamento: `assets/`.

Leia as especificações relevantes em `specs/` antes de criar ou alterar material didático.

## Limites de decisão

Não invente cronograma, datas, notas, critérios de avaliação, regras de entrega, política de IA, casos, fontes ou decisões curriculares. Peça confirmação ao docente quando essas informações forem necessárias e não estiverem no repositório.

Não edite `_site/`, `.quarto/`, PDFs gerados ou outros artefatos de build. Não faça commit, push ou publicação sem solicitação explícita.

## Convenções de conteúdo

- Preserve o conteúdo canônico da aula em `_content.qmd` quando ele também integrar a apostila.
- Mantenha `index.qmd` como página de contexto, navegação e inclusão do conteúdo canônico.
- Slides são uma entrega independente: devem ter narrativa própria para aula presencial, não uma cópia linear da página.
- Use fontes verificáveis e registre-as em `docs/references.bib` quando citadas.
- Mantenha imagens em `assets/images/<nn>-<tema>/` e links relativos compatíveis com o site publicado.

## Ambiente e validação

```bash
uv sync
uv run quarto render
uv run python scripts/render_apostila.py
```

Execute `uv run pytest` quando houver testes. Para a auditoria visual de slides, instale o grupo opcional e o navegador uma vez:

```bash
uv sync --group visual-audit
uv run playwright install chromium
uv run python scripts/audit_slides.py _site/docs/<nn>-<tema>/slides.html
```

O Quarto, Java, Graphviz (`dot`) e PlantUML são dependências do sistema e devem estar disponíveis no `PATH` para uma renderização completa. O workflow de publicação instala esses componentes no Linux.

Confira o `git status` após alterações. A renderização deve terminar sem erros e a apostila deve existir em `_site/docs/apostila.pdf`.
