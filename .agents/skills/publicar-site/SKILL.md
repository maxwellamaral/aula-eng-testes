---
name: publicar-site
description: Publica o estado local já aprovado deste repositório no site online por meio de auditoria, build, commit, push e verificação do deploy. Usar somente quando o usuário pedir explicitamente para publicar o site, atualizar o site online, fazer deploy ou enviar/publicar a versão atual; não usar para criar ou revisar conteúdo, executar apenas um build, inspecionar alterações ou interpretar mensagens como “material pronto”, “aula concluída” ou “pode seguir” como autorização para commit ou push.
---

# Publicar site

Publicar somente após autorização explícita. `AGENTS.md` permanece a autoridade operacional; esta Skill define como executar a publicação, não se o conteúdo pedagógico está pronto.

## Aplicar as travas de segurança

Antes de commit ou push, confirmar que o working tree contém apenas alterações relacionadas ao trabalho aprovado.

Ao encontrar arquivo inesperado, temporário, cache, artefato de build, arquivo pessoal, credencial, segredo, conteúdo potencialmente recuperável ou alteração sem relação comprovada com o trabalho:

1. interromper imediatamente;
2. não remover nem descartar o arquivo;
3. não incluí-lo no commit;
4. não prosseguir com build, commit ou push quando a auditoria exigir parada;
5. explicar o achado e aguardar decisão explícita.

Inspecionar padrões como `*.swp`, `*.swo`, `.venv/`, `__pycache__/`, temporários de editor e credenciais, sem tratar essa lista como exaustiva. Nunca executar `git reset --hard` ou `git clean -fd`.

## Auditar antes da publicação

1. Ler `AGENTS.md`, `.gitignore`, `_quarto.yml` e os workflows em `.github/workflows/`.
2. Executar:

   ```bash
   git status
   git status --short --untracked-files=all
   git diff --check
   ```

3. Inspecionar o diff versionado, alterações não staged e arquivos novos relevantes. Usar, quando necessário, operações de leitura como `git diff`, `git diff --staged` e `git ls-files`.
4. Relacionar cada alteração ao trabalho aprovado e procurar arquivos locais ou dados sensíveis.

Não executar `git add .` antes dessa auditoria. Não aproveitar a publicação para revisar ou melhorar aulas, laboratórios, specs, Skills, conteúdo ou navegação.

## Executar o build

Somente após uma auditoria limpa, executar:

```bash
uv run quarto render
```

Se o Quarto não for executado pelo ambiente `uv`, usar `quarto render`.

Se falhar, diagnosticar a causa. Corrigir apenas erro técnico evidente decorrente das alterações atuais, como sintaxe de configuração, Markdown inválido ou link quebrado por renomeação aprovada. Se a correção exigir decisão pedagógica, editorial ou estrutural, interromper e pedir orientação. Repetir o build somente após correção autorizada ou inequivocamente técnica.

## Conferir depois do build

Repetir:

```bash
git status
git status --short --untracked-files=all
git diff --check
```

Reinspecionar o diff final e procurar alterações ou artefatos produzidos pelo build. Interromper antes do commit se surgir algo inesperado.

## Confirmar destino Git

Identificar por comandos de leitura:

- branch atual;
- remotes configurados;
- upstream da branch ativa.

Publicar apenas na branch ativa e no upstream já configurado. Não trocar ou criar branch, alterar remote, inventar upstream, fazer merge ou rebase. Se o destino estiver ausente ou ambíguo, interromper e informar.

## Preparar e criar o commit

Prosseguir somente com autorização explícita, auditorias limpas, build válido e destino conhecido.

1. Selecionar conscientemente apenas os arquivos aprovados para staging; evitar `git add .`.
2. Conferir `git diff --staged`, seu resumo e `git diff --staged --check`.
3. Se houver item inesperado, removê-lo do staging apenas quando isso for inequivocamente seguro; diante de dúvida, interromper.
4. Usar a mensagem fornecida pelo usuário ou uma mensagem objetiva que descreva o conjunto, nunca mensagens vagas como `updates`, `fix` ou `changes`.
5. Não alterar commits anteriores nem o histórico.

## Enviar ao upstream

Após o commit, executar push normal para o upstream atual. Nunca usar `--force` ou `--force-with-lease`.

Se o push for rejeitado por divergência remota, não executar pull, merge ou rebase automaticamente. Interromper e relatar a situação.

## Verificar a publicação

Depois do push:

1. consultar os workflows existentes para identificar o mecanismo de publicação;
2. se GitHub Actions for usado e `gh` estiver instalado e autenticado, consultar somente o estado do workflow disparado;
3. informar nome, estado e conclusão quando disponíveis;
4. se `gh` não estiver disponível ou autenticado, informar a limitação sem tratar isso como falha do push;
5. informar a URL pública somente se ela puder ser confirmada pela configuração ou pelo GitHub; nunca inferi-la apenas do nome do repositório.

Não modificar workflows durante a verificação. Se o GitHub Pages estiver
configurado para GitHub Actions, mas não houver workflow de deploy, relatar a
ausência e interromper. Criar ou alterar esse workflow só é permitido quando o
usuário autorizar explicitamente a implementação da automação de deploy; nesse
caso, tratar a mudança como implementação, auditá-la, gerar o site, criar um
commit específico, fazer push e verificar a execução disparada.

## Encerrar

Executar `git status`. O ideal é terminar com working tree limpa. Se restarem alterações, listar e explicar por que não foram incluídas; não criar outro commit automaticamente.

Relatar de forma breve:

- resultado do build;
- branch e remote/upstream;
- arquivos incluídos;
- hash curto e mensagem do commit;
- resultado do push;
- workflow e status, quando verificáveis;
- URL pública, quando confirmável;
- estado final do working tree.

Não decidir publicar por conta própria, criar conteúdo, fazer revisão pedagógica, modificar outras Skills ou specs, remover arquivos inesperados, descartar mudanças locais, alterar histórico ou publicar algo que não possa ser relacionado ao trabalho aprovado.
