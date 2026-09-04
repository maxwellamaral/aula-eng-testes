---
name: registrar-memoria-projeto
description: Registra a proveniência de uma sessão e consolida somente decisões duráveis e pendências do projeto na memória persistente via Hermes remoto. Use após mudanças relevantes de conteúdo, estrutura, workflow ou publicação quando o projeto exigir atualização de memória; não use para alterações triviais, nem para registrar credenciais, segredos ou arquivos temporários.
---

# Registrar memória do projeto

Use esta skill ao concluir uma tarefa que produza contexto durável para o projeto. O WSL é consumidor da memória; o servidor Hermes é o compilador principal.

## Pré-condições

1. Leia o `AGENTS.md` do repositório, `knowledge/index.md` e somente as notas relevantes em `knowledge/projects` ou `knowledge/research`.
2. Não edite `raw/daily` manualmente. Não copie, imprima ou registre chaves privadas, tokens, cookies, `.env` ou arquivos temporários.
3. Registre apenas decisões estáveis, fatos do projeto, mudanças relevantes e pendências. Se não houver informação durável nova, não crie uma sessão de memória.

## Configuração SSH do Hermes

Use a chave já configurada na máquina; nunca a inclua no repositório. Os valores deste projeto são:

```bash
MEMORY_SSH_HOST=100.118.79.48
MEMORY_SSH_PORT=41930
MEMORY_SSH_USER=root
MEMORY_SSH_KEY=/home/max/.ssh/id_ed25519
MEMORY_KNOWN_HOSTS=/mnt/c/users/max/.ssh/known_hosts
MEMORY_VAULT='/root/obsidian.new/10 - Vaults/ai-memory'
```

Verifique a permissão da chave (`chmod 600` se necessário) e use o arquivo de hosts conhecido. Não use `StrictHostKeyChecking=no`. O Hermes deve ser executado a partir do diretório pai do vault, não de `.memory`, para que encontre `.memory/agents.md` corretamente.

Modelo de conexão (substitua apenas o comando remoto, sem revelar a chave):

```bash
ssh -p 41930 -i /home/max/.ssh/id_ed25519 \
  -o IdentitiesOnly=yes \
  -o UserKnownHostsFile=/mnt/c/users/max/.ssh/known_hosts \
  -o BatchMode=yes root@100.118.79.48 'cd "/root/obsidian.new/10 - Vaults/ai-memory" && comando'
```

## Fluxo oficial

1. Obtenha o identificador da sessão Hermes que contém o trabalho concluído:

   ```bash
   ssh -p 41930 -i /home/max/.ssh/id_ed25519 -o IdentitiesOnly=yes \
     -o UserKnownHostsFile=/mnt/c/users/max/.ssh/known_hosts -o BatchMode=yes \
     root@100.118.79.48 \
     'cd "/root/obsidian.new/10 - Vaults/ai-memory" && hermes sessions list --source cli --limit 20'
   ```

   Se necessário, use `hermes sessions export --session-id ID --redact --yes` para confirmar o conteúdo, sem incluir segredos.

2. Crie a proveniência com o script oficial, usando a data local da sessão:

   ```bash
   ssh -p 41930 -i /home/max/.ssh/id_ed25519 -o IdentitiesOnly=yes \
     -o UserKnownHostsFile=/mnt/c/users/max/.ssh/known_hosts -o BatchMode=yes \
     root@100.118.79.48 \
     'cd "/root/obsidian.new/10 - Vaults/ai-memory" && \
      python3 .memory/scripts/summarize.py --session-id ID_DA_SESSAO'
   ```

3. Consolide a proveniência no conhecimento canônico:

   ```bash
   ssh -p 41930 -i /home/max/.ssh/id_ed25519 -o IdentitiesOnly=yes \
     -o UserKnownHostsFile=/mnt/c/users/max/.ssh/known_hosts -o BatchMode=yes \
     root@100.118.79.48 \
     'cd "/root/obsidian.new/10 - Vaults/ai-memory" && \
      python3 .memory/scripts/flush.py --date AAAA-MM-DD --force'
   ```

   O `flush.py` deve atualizar somente notas canônicas pertinentes, normalmente `knowledge/projects/aula-vvts.md` e índices relacionados. Não faça essa consolidação editando `knowledge` manualmente.

4. Verifique o resultado remotamente, sem retornar conteúdo sensível:

   ```bash
   ssh -p 41930 -i /home/max/.ssh/id_ed25519 -o IdentitiesOnly=yes \
     -o UserKnownHostsFile=/mnt/c/users/max/.ssh/known_hosts -o BatchMode=yes \
     root@100.118.79.48 \
     'cd "/root/obsidian.new/10 - Vaults/ai-memory" && \
      git diff -- .memory/knowledge/projects/aula-vvts.md .memory/knowledge/index.md'
   ```

   Confirme que a nota do projeto contém a decisão ou pendência, que a proveniência foi criada em `raw/daily`, e que nenhum segredo foi incluído. Se a sessão não for encontrada, o SSH falhar ou o compilador não atualizar a nota, pare e relate o bloqueio; não substitua o fluxo por edição manual de `raw`.

## Relato ao concluir

Informe a data, o identificador da sessão (sem conteúdo sensível), o arquivo de proveniência, as notas canônicas alteradas e eventuais pendências. Não inclua a chave, sua impressão digital completa, tokens, cookies ou transcrições desnecessárias.
