# Gabarito pedagógico — Laboratório 04: Mini-RTF guiada

**Uso interno do docente.** Este documento acompanha `docs/04-verificacao-estatica/laboratorio.qmd` e a planilha `docs/04-verificacao-estatica/ficha-inspecao-lab04.xlsx`. Não deve ser publicado no site. O cenário de biblioteca é fictício e serve apenas para praticar a revisão estática.

## Finalidade didática

O laboratório não cobra uma única solução de código. A pessoa estudante deve percorrer a mini-RTF da preparação ao acompanhamento das correções. Ao final, espera-se que ela:

- confira a prontidão do pacote e registre a preparação individual;
- compare o requisito, os critérios de aceitação e o código;
- diferencie uma divergência observável de uma lacuna que requer esclarecimento;
- aplique as seis perguntas NASA selecionadas, preservando a origem e a adaptação de cada uma;
- use linguagem centrada no artefato, e não na pessoa autora;
- registre localização, evidência, impacto a investigar e encaminhamento;
- mantenha a reunião voltada à identificação e ao registro dos problemas;
- separe a situação de cada descoberta da decisão global sobre o artefato;
- acompanhe o retrabalho, verifique as correções e indique se é necessária uma nova revisão.

Aceite formulações equivalentes quando estiverem ancoradas em R-01, CA-01 a CA-04, nas perguntas NASA selecionadas ou em um trecho identificável da função. A quantidade de itens encontrados não substitui a qualidade das evidências.

## Como usar este gabarito

As respostas abaixo orientam a discussão, mas não formam uma chave rígida. Há três limites importantes:

1. uma divergência só pode ser confirmada quando há base de referência suficiente;
2. uma lacuna não autoriza o grupo a inventar uma regra de negócio;
3. a correção acontece depois da reunião e precisa ser verificada por alguém que não realizou o retrabalho.

Se a prática for individual, trate-a como inspeção guiada. Não a apresente como revisão por pares.

---

## Artefato revisado

### Base de referência

- **R-01:** renovação por até duas vezes; sem reserva ativa de outra pessoa; sem atraso; motivo informado quando houver recusa.
- **CA-01:** após duas renovações concluídas, nova tentativa é recusada.
- **CA-02:** reserva ativa da própria pessoa não bloqueia.
- **CA-03:** reserva ativa de outra pessoa bloqueia.
- **CA-04:** atraso bloqueia e o motivo é informado.

### Código sob inspeção

```python
MAX_RENOVACOES = 2


def pode_renovar(renovacoes: int, ha_reserva: bool, atraso_dias: int) -> bool:
    if renovacoes > MAX_RENOVACOES:
        return False
    if ha_reserva:
        return False
    return atraso_dias <= 0
```

---

## Preparação da mini-RTF

Na aba **Preparação**, o grupo deve identificar o artefato e sua versão, registrar o escopo e indicar R-01 e CA-01 a CA-04 como base de referência. O pacote está pronto quando contém:

- o requisito e os quatro critérios de aceitação;
- o trecho da função `pode_renovar`;
- o recorte com as seis perguntas NASA;
- a agenda, os participantes e os papéis da revisão.

Se faltar um desses elementos, a condição de entrada adequada é interromper a revisão e devolver o pacote para complementação. Não aceite um registro de preparação preenchido retroativamente apenas para cumprir a planilha.

Em grupos com menos de quatro integrantes, uma pessoa pode acumular papéis, desde que isso fique registrado. A pessoa responsável pelo acompanhamento deve estar identificada antes do encerramento da reunião.

---

## Prática A — respostas orientadoras para a inspeção de requisitos

O requisito e os critérios já especificam com clareza o limite de duas renovações e a diferença entre reserva própria e reserva de outra pessoa. Portanto, não trate como ambiguidade a expressão “até duas vezes” isoladamente: CA-01 fixa a interpretação operacional.

Duas questões adequadas para a preparação individual são:

| ID sugerido | Localização | Tipo | Evidência | Encaminhamento esperado |
|---|---|---|---|---|
| RQ-01 | R-01 e CA-04 | Omissão de contrato de resposta | R-01 e CA-04 exigem informar o motivo, mas não definem a forma dessa informação: retorno estruturado, mensagem, código de motivo ou outro contrato. | Esclarecimento com quem define a interface ou requisito. Não inventar o formato. |
| RQ-02 | R-01 / critérios | Omissão de domínio de entrada | A base não define o tratamento para `renovacoes` negativo, nem explicita a origem ou validação desse dado. | Esclarecimento; documentar se a validação pertence a outra camada ou ao domínio da função. |

Outras questões aceitáveis, desde que bem justificadas:

- o significado operacional de “reserva ativa” e a fonte de verdade para identificar a pessoa que fez a reserva;
- como informar o motivo quando **mais de uma** condição de bloqueio ocorre simultaneamente;
- se `atraso_dias = 0` é sempre equivalente a “não está em atraso” no domínio adotado.

Não classificar como descoberta confirmada, sem outra evidência:

- uma multa, categoria especial de item, regra de férias ou política real de biblioteca;
- o canal exato da mensagem de recusa;
- uma terceira regra de negócio não fornecida no laboratório.

### Respostas orientadoras para o recorte NASA

A aba **Recorte NASA** preserva o checklist, a seção, o número e o texto de origem. Os campos de resposta, evidência, aplicabilidade e descoberta vinculada foram criados para a atividade; não são colunas originais da NASA.

| ID didático | Leitura aceitável | Evidência esperada | Possível vínculo |
|---|---|---|---|
| NASA-RQ-01 — PAT-003, Clareza, pergunta 3 | **Atende em parte.** O limite e as condições principais são compreensíveis quando R-01 é lido com CA-01 a CA-04. Ainda pode ser necessário esclarecer termos do domínio, como “reserva ativa”, se não houver definição externa. | Citar R-01 e os critérios que retiram a dúvida sobre “até duas vezes” e sobre a autoria da reserva. | RQ adicional apenas se a pessoa apontar um termo realmente indefinido. |
| NASA-RQ-02 — PAT-003, Completude, pergunta 1 | **Não atende integralmente.** A exigência de informar o motivo não define o contrato de resposta, e o domínio de alguns dados de entrada não está documentado. | Relacionar R-01/CA-04 ao retorno `bool` e registrar a ausência de regra para valores negativos de `renovacoes`. | I-03 e I-04. |
| NASA-RQ-03 — PAT-013, Uso de dados, pergunta 1 | **Não atende integralmente no recorte adaptado.** Faltam limites explícitos para `renovacoes`, e `ha_reserva` não representa quem fez a reserva. | Comparar a assinatura da função com CA-02 e CA-03; apontar o domínio não definido de `renovacoes`. | I-02 e I-04. |
| NASA-RQ-04 — PAT-013, Testabilidade, pergunta 2 | **Atende em parte.** Os critérios tornam as principais condições testáveis, mas o motivo da recusa não tem forma observável definida. | Citar CA-01 a CA-04 e explicar por que o contrato de resposta impede verificar toda a exigência de R-01. | I-03. |
| NASA-CD-01 — PAT-017, Funcionalidade, pergunta 1 | **Aplicável, sem divergência obrigatória.** A função tem o propósito geral de decidir se a renovação é permitida. O problema do retorno não deve ser forçado como violação de finalidade única. | Relacionar o nome e o fluxo da função à decisão de renovação. Uma resposta diferente precisa de justificativa no artefato. | Nenhum vínculo obrigatório. |
| NASA-CD-02 — PAT-017, Lógica, pergunta 10 | **Não atende integralmente.** A condição de fronteira usa `>` onde CA-01 exige bloquear a tentativa quando já ocorreram duas renovações. | Mostrar o percurso do cenário B e compará-lo com CA-01. | I-01. |

PAT-017 foi escrito para inspeção de código C. NASA-CD-01 usa uma pergunta independente da linguagem. Em NASA-CD-02, “árvores `if-else`” foi generalizado como “estruturas condicionais”, a referência a `switch` foi retirada e o exame das condições de fronteira ficou explícito. Essas mudanças precisam permanecer registradas na planilha.

---

## Prática B — teste de mesa esperado

O teste de mesa percorre a função na ordem das condições, sem executá-la.

| Cenário | Percurso das condições | Retorno previsto pelo código | Resultado segundo a base de referência | Leitura pedagógica |
|---|---|---|---|---|
| A: `renovacoes=1`, `ha_reserva=False`, `atraso_dias=0` | `1 > 2` é falso; reserva é falsa; `0 <= 0` é verdadeiro. | `True` | renovação permitida | Não há divergência observável nesse cenário. |
| B: `renovacoes=2`, `ha_reserva=False`, `atraso_dias=0` | `2 > 2` é falso; reserva é falsa; `0 <= 0` é verdadeiro. | `True` | renovação recusada por CA-01 | Divergência confirmada no limite: a função permite uma terceira tentativa. |
| C: `renovacoes=0`, `ha_reserva=True`, `atraso_dias=0` | `0 > 2` é falso; a condição de reserva é verdadeira e encerra o fluxo. | `False` | depende de quem fez a reserva | O valor booleano não permite representar CA-02 e CA-03. O cenário precisa ser separado em “reserva própria” e “reserva de outra pessoa”. |
| D: `renovacoes=0`, `ha_reserva=False`, `atraso_dias=1` | As duas primeiras condições são falsas; `1 <= 0` é falso. | `False` | renovação recusada por CA-04 | A decisão booleana é compatível com a recusa, mas a função não fornece o motivo exigido. |
| E: `renovacoes=-1`, `ha_reserva=False`, `atraso_dias=0` | `-1 > 2` é falso; reserva é falsa; `0 <= 0` é verdadeiro. | `True` | não definido | O código produz um resultado, mas a base não define o domínio nem o tratamento desse valor. Registrar a lacuna sem pressupor que a entrada é inválida. |

### Respostas às perguntas de inspeção

1. **Divergência de limite:** cenário B. `renovacoes > MAX_RENOVACOES` só recusa a partir de 3; ao receber 2, a função permite a nova renovação. Como `renovacoes` representa as renovações já concluídas, a condição precisa impedir a próxima tentativa após a segunda. A descoberta deve ser registrada, não corrigida durante a RTF.
2. **Reserva:** não. `ha_reserva` só indica que existe alguma reserva; não identifica a pessoa responsável. A implementação não consegue diferenciar CA-02 de CA-03.
3. **Motivo da recusa:** não. O retorno `bool` expressa somente permissão ou recusa. R-01 e CA-04 requerem uma informação adicional; o formato dessa informação não está definido pela base e deve ser esclarecido.
4. **Valor negativo:** a função retorna `True`, pois nenhuma condição bloqueia esse valor. Como o requisito não define o domínio válido, a conclusão correta é uma lacuna de especificação ou contrato, não uma regra nova proposta como fato.
5. **Classificação:** B é uma divergência confirmada entre código e CA-01. A impossibilidade de distinguir a origem da reserva é uma inconsistência entre a informação disponível na assinatura e CA-02/CA-03. O motivo da recusa é uma omissão de capacidade da interface frente a R-01/CA-04. O valor negativo exige esclarecimento do requisito/contrato.

---

## Registro consolidado — exemplo de resposta

| ID | Origem e referência da pergunta | Localização | Tipo | Evidência e base de referência | Impacto a investigar | Severidade didática | Encaminhamento | Situação inicial |
|---|---|---|---|---|---|---|---|---|
| I-01 | teste de mesa; NASA-CD-02 | `pode_renovar`, condição `renovacoes > MAX_RENOVACOES` | inconsistência | Para `renovacoes=2`, a função retorna `True`; CA-01 exige recusar nova tentativa após duas renovações concluídas. | Pode permitir uma terceira renovação. | alta | Corrigir a regra depois da reunião e verificar contra CA-01. | aberta |
| I-02 | NASA-RQ-03; pergunta complementar sobre reserva | assinatura `ha_reserva: bool` | inconsistência / informação insuficiente | CA-02 permite reserva da própria pessoa; CA-03 bloqueia reserva de outra pessoa. O booleano não informa a autoria da reserva. | Pode bloquear uma renovação permitida ou impedir a implementação dos critérios. | alta | Rever o contrato de dados e corrigir a representação da reserva. | aberta |
| I-03 | NASA-RQ-02 e NASA-RQ-04 | retorno `-> bool` | omissão | R-01 e CA-04 exigem informar o motivo da recusa; o retorno representa apenas permissão ou recusa. | A interface pode deixar de cumprir a exigência de comunicação. | alta | Esclarecer o contrato de resposta, corrigi-lo depois da reunião e verificar os motivos de recusa. | aberta |
| I-04 | NASA-RQ-02 e NASA-RQ-03 | domínio de `renovacoes` | omissão | O cenário E produz `True`, mas R-01 e os critérios não definem o domínio nem o tratamento de valores negativos. | O comportamento para uma entrada fora do domínio documentado permanece indefinido. | média ou a justificar | Esclarecer a regra de validade e a camada responsável pela validação. | aberta |

O laboratório pede pelo menos três itens. I-01, I-02 e I-03 formam o núcleo esperado. I-04 é uma descoberta adicional válida quando aparece como lacuna, sem classificar antecipadamente `renovacoes = -1` como dado inválido. Outros itens podem ser aceitos se tiverem localização, evidência e referência verificáveis.

---

## Prática C — condução da mini RTF

### Distribuição de papéis

- **Pessoa produtora:** apresenta R-01, CA-01 a CA-04 e a função, mas não tenta justificar nem corrigir os itens na reunião.
- **Moderação:** confirma que o escopo é apenas o artefato do laboratório; controla a agenda; interrompe discussões sobre solução detalhada.
- **Revisores:** apresentam as questões preparadas individualmente, com referência explícita ao artefato ou ao recorte NASA.
- **Pessoa registradora:** mantém a tabela de descobertas visível e registra apenas itens com localização e evidência.

O percurso deve seguir uma ordem conhecida: R-01, critérios de aceitação e função. A reunião identifica, consolida e encaminha problemas. Discussões sobre a solução detalhada ficam para o retrabalho.

### Decisão esperada

A decisão mais coerente com o conjunto I-01, I-02 e I-03 é **rejeitar por erros graves, exigir retrabalho e realizar uma nova revisão**. I-01 contradiz CA-01; I-02 impede distinguir CA-02 de CA-03; I-03 impede cumprir integralmente R-01 e CA-04.

As opções da planilha devem conservar o sentido destas três decisões:

1. aceitar sem modificações;
2. aceitar provisoriamente, condicionado a correções secundárias;
3. rejeitar por erros graves e exigir nova revisão.

Uma escolha diferente da terceira opção precisa explicar por que as divergências não bloqueiam o aceite. Não confunda essa decisão com a situação de I-01, I-02, I-03 ou I-04. A decisão vale para o artefato; cada descoberta segue seu próprio fluxo.

### Intervenções pedagógicas úteis

- Se alguém propor imediatamente uma nova assinatura ou um `enum` de motivos, pergunte: **“A base já aprovou essa solução ou ela é uma proposta para depois da revisão?”**
- Se o grupo chamar `ha_reserva=True` de falha, pergunte: **“O produto foi executado? O que temos: falha observada, defeito no artefato ou lacuna de especificação?”**
- Se alguém disser que “o autor errou”, peça reescrita centrada no trecho e no critério.
- Se o grupo classificar todas as questões como defeitos de código, retome I-04 para distinguir uma lacuna de requisito de uma divergência confirmada.

---

## Retrabalho e evidências esperadas

O gabarito não fixa uma única implementação. A correção é aceitável quando atualiza o contrato do artefato, resolve as descobertas encaminhadas e mantém rastreabilidade com a versão anterior.

### I-01 — condição de fronteira

Uma correção direta é substituir:

```python
if renovacoes > MAX_RENOVACOES:
```

por:

```python
if renovacoes >= MAX_RENOVACOES:
```

A evidência deve mostrar o trecho corrigido e a versão do artefato. A verificação refaz o cenário B e confirma a recusa da tentativa após duas renovações concluídas.

### I-02 — autoria da reserva

A interface corrigida precisa representar se a reserva ativa pertence à própria pessoa ou a outra pessoa. São aceitáveis, por exemplo, um parâmetro com esse significado explícito, um identificador de autoria ou um tipo que represente os estados pertinentes. A escolha deve estar documentada; trocar apenas o nome de `ha_reserva` sem mudar a informação disponível não resolve a descoberta.

A verificação precisa cobrir dois casos antes indistinguíveis:

- reserva ativa da própria pessoa: não bloqueia, conforme CA-02;
- reserva ativa de outra pessoa: bloqueia, conforme CA-03.

### I-03 — motivo da recusa

O contrato corrigido precisa carregar a decisão e o motivo quando houver recusa. Uma tupla, um objeto de resultado, um código ou outro formato podem funcionar, mas a escolha deve ser aprovada e registrada antes da alteração. Não aceite como evidência apenas uma mensagem escrita dentro da função se ela não puder chegar à parte do sistema responsável por informar a pessoa usuária.

A verificação deve observar pelo menos:

- motivo de limite de renovações, relacionado a CA-01;
- motivo de reserva feita por outra pessoa, relacionado a CA-03;
- motivo de atraso, relacionado a CA-04;
- ausência de motivo de recusa quando a renovação for permitida, conforme o contrato escolhido.

### I-04 — domínio de `renovacoes`

Este item não tem correção automática. Primeiro é preciso decidir e documentar o domínio válido e quem o valida. Se a decisão atribuir a validação a outra camada, a evidência deve identificar esse contrato. Se a função passar a validar o valor, a evidência deve mostrar a regra aprovada e seu tratamento. O item pode permanecer pendente em um relatório intermediário, mas a prática não deve ser considerada encerrada enquanto faltar essa decisão.

### Exemplo de artefato corrigido

O trecho abaixo serve para discutir o acompanhamento. Ele pressupõe duas decisões didáticas: a função recebe diretamente a informação sobre reserva feita por outra pessoa e retorna um código de motivo. Não apresente essas escolhas como se já constassem de R-01.

```python
MAX_RENOVACOES = 2


def pode_renovar(
    renovacoes: int,
    ha_reserva_de_outra_pessoa: bool,
    atraso_dias: int,
) -> tuple[bool, str | None]:
    if renovacoes >= MAX_RENOVACOES:
        return False, "limite_de_renovacoes"
    if ha_reserva_de_outra_pessoa:
        return False, "reserva_de_outra_pessoa"
    if atraso_dias > 0:
        return False, "item_em_atraso"
    return True, None
```

Esse exemplo resolve I-01, I-02 e I-03 sob as decisões declaradas. Ele não resolve I-04, pois o domínio de `renovacoes` continua dependendo de esclarecimento.

---

## Acompanhamento e eventual nova revisão

Na aba **Decisão e acompanhamento**, cada descoberta encaminhada deve ter responsável pelo retrabalho, correção ou versão, evidência, pessoa verificadora, resultado da verificação e situação final. Quem verifica não deve ser a mesma pessoa que realizou o retrabalho. Na prática individual, a verificação fica para um colega ou para o docente em um momento posterior.

| ID | Resultado de verificação esperado | Situação coerente |
|---|---|---|
| I-01 | O cenário B passa a ser recusado e a evidência aponta para CA-01. | resolvida, se a condição corrigida estiver registrada; reaberta, se o limite continuar incorreto |
| I-02 | Casos de reserva própria e de outra pessoa produzem decisões distintas conforme CA-02 e CA-03. | resolvida, se o contrato representar a autoria; reaberta, se persistir apenas um booleano sem esse significado |
| I-03 | Toda recusa relevante fornece um motivo observável segundo o contrato aprovado. | resolvida, se o motivo chegar à interface consumidora; pendente ou reaberta, se o contrato continuar indefinido ou incompleto |
| I-04 | Há decisão documentada sobre o domínio e a camada de validação. | resolvida ou descartada com justificativa, se houver decisão; pendente em relatório intermediário, se faltar esclarecimento |

Como a decisão esperada rejeita a versão inicial por erros graves, o grupo deve registrar a nova revisão da versão corrigida. Uma nova revisão não é apenas marcar uma célula: ela deve identificar a versão examinada, o resultado global e as pendências remanescentes. Um relatório intermediário pode registrar itens pendentes; o processo só termina quando todos estiverem resolvidos ou descartados com justificativa.

---

## Critérios para leitura do resultado

Considere que a prática atingiu o objetivo quando o grupo:

- registrou a solicitação, a prontidão do pacote, a distribuição e os papéis;
- respondeu às seis perguntas NASA com checklist, seção, número, aplicabilidade, evidência e adaptação quando existente;
- preencheu o teste de mesa sem executar a função;
- apontou I-01 com relação explícita a CA-01;
- percebeu que CA-02 e CA-03 não são representáveis com `ha_reserva: bool`;
- registrou a exigência de motivo como questão de contrato, sem inventar sua forma;
- usou linguagem centrada em artefatos;
- registrou a decisão global separadamente da situação das descobertas;
- realizou o retrabalho depois da reunião, preservando o registro original;
- anexou ou descreveu evidências das correções;
- verificou cada correção e registrou itens resolvidos, reabertos, pendentes ou descartados;
- realizou ou justificou a nova revisão exigida pela decisão global.

O número de descobertas não deve ser usado isoladamente como nota ou indicador de aprendizagem. Uma descoberta bem evidenciada vale mais pedagogicamente do que uma lista extensa de suposições. O preenchimento mecânico da planilha também não basta: os registros precisam formar uma sequência verificável entre pergunta, descoberta, correção e verificação.

## Síntese esperada no relatório

O relatório final deve informar:

- o artefato, a versão, o escopo e a base de referência;
- os participantes e os papéis assumidos;
- as descobertas consolidadas e suas evidências;
- a decisão global tomada depois da reunião;
- as correções realizadas, quem as verificou e o resultado;
- a versão e o resultado da nova revisão, quando exigida;
- as pendências que permaneceram abertas.

Não considere concluído um relatório que pare na lista inicial de descobertas.

## Referência de apoio

- Pressman, Roger S.; Maxim, Bruce R. *Engenharia de software: uma abordagem profissional*. 8. ed. AMGH, 2016. Capítulo 20, especialmente as orientações sobre revisões técnicas formais, registro e acompanhamento.
- NASA, PAT-003, PAT-013 e PAT-017, nos seis itens selecionados e identificados no roteiro. As listas funcionam como apoio prático; não substituem o método de revisão adotado na aula.
