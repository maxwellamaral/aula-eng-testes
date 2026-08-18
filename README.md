# Site de Verificação, Validação e Testes de Software

Repositório do material didático de **Verificação, Validação e Testes de Software (VVTS)**, do Bacharelado em Engenharia de Software — IFPB Campus João Pessoa. O site será construído com Quarto; exemplos e práticas usam Python 3.11+ e a stack definida em `AGENTS.md`.

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

Não é necessário especificar detalhes editoriais: o agente deve obtê-los em `AGENTS.md` e nas specs. Se uma escolha pedagógica importante ainda não estiver decidida, responda à pergunta do agente antes de pedir a implementação.

### 2. Faça o pedido

No diretório deste repositório, peça algo como:

```text
Crie a Aula 07 — Particionamento de equivalência.

Ela corresponde à semana 7 e deve preparar o laboratório de exercícios de caixa-preta.
O objetivo é que a turma derive classes de equivalência válidas e inválidas a partir de requisitos.
Use um pequeno exemplo em Python, sem introduzir Django, API ou valor-limite nesta aula.
Inclua uma atividade curta de classificação de entradas. Não há entrega nem avaliação definida.
```

Para criar aula e laboratório juntos, diga explicitamente que deseja um par e inclua a função prática do laboratório. O agente usará a skill local `criar-par-aula-laboratorio`.

### Exemplo com memória persistente

Para manter a continuidade entre as aulas e registrar decisões duráveis, inclua a consulta e a consolidação da memória no pedido:

```text
Antes de criar a nova aula, consulte minha memória persistente, especialmente
knowledge/projects/aula-vvts.md, e as instruções do repositório.

Quero criar a Aula 02 — Fundamentos de Engenharia de Testes.

Ela corresponde à semana 2. O foco é diferenciar erro, defeito e falha, além de
apresentar verificação estática, validação e testes dinâmicos. A aula deve
conectar requisitos às evidências de qualidade, sem antecipar técnicas de
caixa-preta ou caixa-branca.

Não haverá entrega nem avaliação. Crie a página no padrão atual do projeto,
atualize o índice das aulas se necessário e execute `quarto render`.

Ao concluir, registre a sessão pelo fluxo de memória: crie a proveniência em
raw/daily via Hermes e consolide somente as decisões estáveis e pendências em
knowledge/projects/aula-vvts.md. Não registre credenciais ou arquivos
temporários.
```

O Hermes é responsável por registrar a proveniência em `raw/daily/` e atualizar
a nota canônica do projeto. Não edite `raw/daily/` manualmente neste WSL.

### Slides são uma solicitação separada

Criar uma aula não implica criar slides. O site é o material completo e permanente de estudo; o deck só deve ser produzido quando houver pedido ou decisão pedagógica explícita do professor.

Ao solicitar slides, informe isso claramente junto da aula ou em um pedido posterior. O agente deve seguir `specs/padrao-slides.md`: construir uma narrativa própria para a condução presencial, com frames de função pedagógica definida, sem converter mecanicamente as seções da página da aula em slides. O deck precisa fornecer o apoio previsível à compreensão sem depender do site, de uma IDE ou de desenho obrigatório no quadro.

### 3. O que o agente deve fazer

Ao receber o pedido, o agente deve:

1. Ler `AGENTS.md` e as specs pertinentes em `specs/`.
2. Conferir a continuidade com o cronograma, páginas anteriores e materiais existentes.
3. Pedir decisão ao professor apenas quando faltar uma definição pedagógica relevante.
4. Criar `docs/aulas/aula-XX-assunto.qmd` no padrão da disciplina.
5. Explicar o conceito a partir de um problema ou evidência, com exemplos e atividades que apoiem o objetivo.
6. Introduzir Python e ferramentas da stack apenas quando forem necessários ao tema.
7. Atualizar índice e `_quarto.yml` somente se a estrutura de navegação exigir.
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

Você pode pedir: “revise esta aula conforme `specs/padrao-aula.md` e aplique apenas correções necessárias”. A skill `revisar-material-didatico` faz essa revisão sem alterar arquivos, salvo quando a implementação for explicitamente solicitada.

## Ambiente e validação

Quando o projeto Quarto estiver inicializado, o fluxo esperado é:

```bash
uv sync
uv run pytest
uv run quarto render
```

Se o Quarto estiver instalado fora do ambiente `uv`, use `quarto render`. Nunca edite `_site/` manualmente. Commits, push e publicação exigem solicitação explícita.

A apostila PDF é gerada durante a renderização. Ela só estará disponível para download público depois que a versão que a contém for publicada no site.

## Fontes de orientação

- `AGENTS.md`: regras operacionais, stack e limites de decisão.
- `specs/projeto-pedagogico.md`: ementa, objetivos e cronograma.
- `specs/padrao-aula.md`: formato e critérios de qualidade das aulas.
- `specs/padrao-laboratorio.md`: formato das práticas.
- `specs/estrutura-site.md`: organização e navegação do site.
