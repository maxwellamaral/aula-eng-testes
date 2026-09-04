# Site de Verificação, Validação e Testes de Software

Repositório do material didático de **Verificação, Validação e Testes de Software (VVTS)**, do Bacharelado em Engenharia de Software — IFPB Campus João Pessoa. O site é construído com Quarto; exemplos e práticas usam Python 3.11+. As convenções operacionais e pedagógicas versionadas estão em `AGENTS.md` e `specs/`.

## Gerar uma nova aula com IA agêntica

Use a IA como colaboradora de autoria e implementação. Você define as decisões pedagógicas; o agente consulta as regras do repositório, cria o arquivo Quarto, atualiza a navegação quando necessário e valida a renderização.

### 1. Defina o que já está decidido

Antes de solicitar a aula, informe ao agente:

- número e título da aula;
- semana ou posição no cronograma;
- foco conceitual e objetivo de aprendizagem;
- conhecimentos que os estudantes já possuem e o que ainda não deve ser antecipado;
- relação com o *case*, laboratório ou projeto, quando houver;
- exemplo, atividade ou ferramenta que deve aparecer;
- regras de uso de IA, entrega ou avaliação, somente se já definidas.

Não é necessário especificar detalhes editoriais: o agente deve obtê-los em `AGENTS.md` e nas especificações pertinentes em `specs/`. Se uma escolha pedagógica importante ainda não estiver decidida, responda à pergunta do agente antes de pedir a implementação.

### 2. Faça o pedido

No diretório deste repositório, peça algo como:

```text
Crie a Aula 07 — Particionamento de equivalência.

Ela corresponde à semana 7 e deve preparar o laboratório de exercícios de caixa-preta.
O objetivo é que a turma derive classes de equivalência válidas e inválidas a partir de requisitos.
Use um pequeno exemplo em Python, sem introduzir Django, API ou valor-limite nesta aula.
Inclua uma atividade curta de classificação de entradas. Não há entrega nem avaliação definida.
```

Para criar aula e laboratório juntos, diga explicitamente que deseja um par e inclua a função prática do laboratório. O agente deve seguir `specs/padrao-aula.md` e `specs/padrao-laboratorio.md`.

### Continuidade pedagógica

Antes de criar ou revisar uma aula, leia `AGENTS.md`, `specs/projeto-pedagogico.md`, a aula anterior e os materiais já publicados. Use apenas as decisões curriculares disponíveis no repositório ou fornecidas pelo docente; não registre nem presuma informações acadêmicas que não estejam definidas.

### Slides são uma solicitação separada

Criar uma aula não implica criar slides. O site é o material completo e permanente de estudo; o deck só deve ser produzido quando houver pedido ou decisão pedagógica explícita do professor.

Ao solicitar slides, informe isso claramente junto da aula ou em um pedido posterior. O agente deve seguir `specs/padrao-slides.md`: construir uma narrativa própria para a condução presencial, com frames de função pedagógica definida, sem converter mecanicamente as seções da página da aula em slides. O deck precisa fornecer o apoio previsível à compreensão sem depender do site, de uma IDE ou de desenho obrigatório no quadro.

Exemplo de solicitação de slides:

```text
Leia AGENTS.md, specs/padrao-slides.md e o material da aula correspondente.

Crie a apresentação de slides para a Aula 02 — Introdução à Gestão da Qualidade de Produto
em docs/02-gestao-qualidade/slides.qmd.

Construa uma narrativa própria para condução presencial (com frames de abertura, contextualização,
problema/evidência, conceitos-chave, contraste de abordagens e síntese), sem converter
mecanicamente o texto da aula em slides. Utilize o formato Reveal.js nativo do Quarto,
mantenha o tema consistente com o site e priorize imagens vetoriais (SVG).

Ao concluir, atualize o link no material da aula, execute `uv run quarto render` e audite o deck alterado.
```

### 3. O que o agente deve fazer

Ao receber o pedido, o agente deve:

1. Ler `AGENTS.md` e as especificações pertinentes em `specs/`.
2. Conferir a continuidade com as páginas anteriores e materiais existentes; confirmar com o docente informações curriculares ausentes.
3. Pedir decisão ao professor apenas quando faltar uma definição pedagógica relevante.
4. Criar `docs/NN-tema/index.qmd` e `_content.qmd` no padrão da disciplina.
5. Explicar o conceito a partir de um problema ou evidência, com exemplos e atividades que apoiem o objetivo.
6. Introduzir Python e ferramentas da stack apenas quando forem necessários ao tema.
7. Atualizar `docs/index.qmd` e `docs/apostila.qmd` quando a estrutura de navegação ou a apostila exigir.
8. Renderizar o site e relatar os arquivos modificados e o resultado da validação.

O agente não deve inventar datas, pesos, critérios de nota, regras de entrega, política de IA, detalhes de *cases* ou decisões curriculares.

## Revisar antes de aceitar

Leia a aula gerada verificando principalmente:

- aderência ao objetivo e à semana do cronograma;
- precisão na distinção entre técnicas, níveis e tipos de teste;
- continuidade com o que a turma já estudou;
- exemplos executáveis e compatíveis com Python 3.11+;
- atividade viável e critérios observáveis, quando houver laboratório;
- clareza para leitura autônoma pelo estudante.

Você pode pedir: “revise esta aula conforme `specs/padrao-aula.md` e aplique apenas correções necessárias”. A revisão deve apontar problemas de conteúdo, progressão, acessibilidade, fontes e executabilidade antes de modificar os arquivos.

## Ambiente e validação

O fluxo esperado é:

```bash
uv sync
uv run quarto render
uv run python scripts/render_apostila.py
```

Execute `uv run pytest` quando houver testes. Para auditar slides, instale a dependência opcional e o navegador uma vez:

```bash
uv sync --group visual-audit
uv run playwright install chromium
uv run python scripts/audit_slides.py _site/docs/NN-tema/slides.html
```

O Quarto é uma dependência do sistema e deve estar disponível no `PATH`. A renderização completa também requer Java, Graphviz (`dot`) e PlantUML para os diagramas; o workflow de publicação instala esses componentes. Nunca edite `_site/` manualmente. Commits, push e publicação exigem solicitação explícita.

A apostila PDF é gerada pelo comando explícito `uv run python scripts/render_apostila.py` após a renderização. Ela só estará disponível para download público depois que a versão que a contém for publicada no site.

## Fontes de orientação

- `AGENTS.md`: regras operacionais, stack e limites de decisão.
- `specs/projeto-pedagogico.md`: decisões curriculares disponíveis e limites do repositório.
- `specs/padrao-aula.md`: formato e critérios de qualidade das aulas.
- `specs/padrao-laboratorio.md`: formato das práticas.
- `specs/padrao-slides.md`: narrativa e validação das apresentações.
- `specs/estrutura-site.md`: organização e navegação do site.
