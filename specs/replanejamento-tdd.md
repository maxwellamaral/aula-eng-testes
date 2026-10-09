# Replanejamento dos encontros restantes: TDD integrado

## Status e alcance

O docente aprovou esta reorganização na conversa de planejamento do projeto. Ela orienta os oito encontros restantes de quatro horas, incluindo apresentações. A numeração 06–13 identifica a nova sequência de encontros, não uma equivalência individual com as antigas semanas 06–17.

O planejamento inicial permanece registrado em `docs/00-apresentacao/slides.qmd`, especialmente na seção "Conteúdo Programático (17 Semanas)". Esta especificação substitui a sequência inicial apenas nos pontos descritos aqui. Não altera a ementa, as convenções editoriais nem estabelece novas regras de avaliação.

A reorganização antecipa TDD e integra as competências de elaboração e avaliação de testes ao desenvolvimento incremental. Não autoriza eliminar conteúdos por não fazerem parte dos exemplos de Percival.

## Situação da disciplina e pendências

- Restam oito encontros de quatro horas; parte desse tempo será usada para apresentações, devolutivas e síntese, não apenas para conteúdo novo.
- A N1 já ocorreu em formato diferente do catálogo inicial.
- A N2 está em andamento, com entrega parcial de verificação estática de requisitos do BVapp.
- A composição da N3, datas, prazos, pesos e critérios de avaliação não foram definidos nesta reorganização.
- A duração e distribuição das apresentações parciais e devolutivas da N2 ainda precisam de definição docente. O último encontro está reservado às apresentações e à síntese.

Não converter evidências de aprendizagem em obrigações de entrega ou critérios de nota sem autorização. Não deduzir regras atuais de avaliação a partir da Aula 00 quando divergirem do relato docente.

## Decisões sobre a demonstração e os projetos

1. A demonstração comum usa a Feature **24258**, "2.1. Inclusão de novos painéis solares", da Epic **24189**, "2. Gestão de Painéis Solares". As subseções **2.1.1.1–2.1.1.9** são a referência de requisitos; o incremento de cada encontro cobre somente parte desse escopo.
2. **Cooperado é obrigatório no contrato didático**, por decisão docente. Registrar explicitamente a divergência entre a opcionalidade de CA01 e a exigência de vínculo da US 24495. Não modificar silenciosamente o backlog nem atribuir ao documento original a decisão didática.
3. A aplicação didática será construída em repositório novo e isolado. Não copiar comportamentos implementados no backend existente nem apresentar caracterização de código existente como TDD de uma implementação nova.
4. Usar **Python, Django e Selenium**, com gestão do ambiente e das dependências por **`uv`**. Começar com `unittest` e os recursos de teste do Django, sem introduzir `pytest` na primeira aula da aplicação didática. Isso não altera o uso de `pytest` para validar este repositório de materiais.
5. O docente pretende preparar o ambiente com um script quando o laboratório for elaborado. Não reservar encontro anterior para instalação. Versões, comandos e funcionamento deverão ser definidos e verificados nessa etapa; não alegar agora que o ambiente está pronto.
6. Os grupos aplicam o método a comportamentos pequenos de suas próprias Epics, também em projetos didáticos iniciados do zero. Não exigir que todos implementem o cadastro de painéis da demonstração.
7. Não inventar limites, estados, combinações de regras ou critérios ausentes dos requisitos. Lacunas e divergências devem permanecer explícitas.

## Referências e abordagem

- **Percival:** condução prática do teste funcional externo, dos testes internos, dos pequenos passos e da refatoração. A primeira aula parte dos conceitos dos capítulos 1–4 do PDF fornecido; persistência entra no encontro seguinte. O livro não substitui a ementa pela sua sequência de capítulos.
- **Pressman e Maxim:** fundamentação de verificação e validação, estratégias de teste, desenvolvimento incremental, regressão e TDD.
- **Marco Túlio Valente:** fundamentação do ciclo vermelho–verde–refatorar, testabilidade, design e técnicas de teste.

Verificar as passagens nas fontes antes de citá-las. Distinguir páginas físicas do PDF e páginas impressas, quando diferentes. Registrar referências em `docs/references.bib` e identificar sínteses didáticas próprias sem atribuí-las aos autores.

Classificar os testes pelo alcance efetivamente exercitado e pela informação usada para elaborar os casos. Não tratar ferramenta, automação, caixa-preta/caixa-branca, nível de teste e prática de desenvolvimento como categorias equivalentes. Não presumir que todo teste interno executado pelo Django seja uma unidade isolada.

## Sequência aprovada

| Encontro | Eixo teórico | Demonstração e prática previstas |
|---|---|---|
| 06 — Introdução ao TDD | Teste como especificação executável; asserção e oráculo; falha esperada; vermelho–verde–refatorar; ciclos externo e interno; V&V | Repositório novo; primeiro teste com Selenium; testes internos com Django; página inicial de inclusão de painel |
| 07 — Entrada, persistência e integração | Componentes e integração; preparação e isolamento de dados; persistência; regressão | Submeter e salvar um painel associado a um Cooperado; verificar o resultado e a independência dos testes |
| 08 — Projeto de casos por caixa-preta | Particionamento de equivalência; valor-limite; casos positivos e negativos; rastreabilidade | Desenvolver validações por TDD, incluindo ausência de Cooperado; usar limites somente quando definidos nos requisitos |
| 09 — Regras combinadas e comportamento | Tabelas de decisão; transição de estados; combinação de condições; suficiência dos cenários | Selecionar requisitos das Epics que tenham combinações ou estados reais, sem inventá-los para encaixar a técnica |
| 10 — Teste estrutural e qualidade da suíte | Caixa-branca; cobertura de comandos e decisões; caminhos básicos; complexidade ciclomática; mutação | Inspecionar o código produzido; identificar lacunas; acrescentar testes justificados; interpretar cobertura e mutantes |
| 11 — Sistema, aceitação e risco | Alcance; cenários de sistema e aceitação; limites de testes end-to-end; priorização por risco; sistemas críticos | Consolidar fluxos e evidências; discutir sistemas críticos com fontes próprias, sem classificar automaticamente o BVapp como crítico |
| 12 — Automação e consolidação | Regressão automatizada; CI/CD; ambiente reproduzível; documentação de testes e evidências | Executar a suíte em pipeline e analisar falhas; usar Docker como apoio, sem transformar a aula em administração de infraestrutura |
| 13 — Apresentações e síntese | Argumentação baseada em evidências; limites da conformidade; revisão das competências | Apresentações, discussão dos resultados e síntese; não reservar conteúdo novo para este encontro |

Esta tabela define progressão pedagógica, não datas ou uma distribuição fechada de minutos. Os encontros anteriores ao último também deverão acomodar apresentações parciais e devolutivas conforme definição docente.

## Rastreabilidade curricular

As evidências abaixo orientam aprendizagem e preparação dos materiais. Não são, por si, regras de entrega ou avaliação.

| Competência do planejamento inicial | Encontros | Tratamento teórico previsto | Prática prevista | Evidência de aprendizagem |
|---|---|---|---|---|
| V&V e relação com requisitos | 06–13 | Contrato, comportamento esperado e limites da conformidade | Relacionar critérios a testes e resultados | Explicação do requisito, do teste e de suas limitações |
| TDD e persistência (antigas semanas 12–13) | 06–08, retomado nos seguintes | Ciclos externo/interno, refatoração e regressão | Construção incremental do projeto novo | Falha pelo motivo esperado, aprovação após implementação e execução após refatoração |
| Particionamento e valor-limite (antigas semanas 6–9) | 08 | Seleção e justificativa de entradas | Derivar casos dos requisitos revisados | Partições e limites justificados, sem regras inventadas |
| Decisão e estados (antigas semanas 6–9) | 09 | Condições, ações, estados e transições | Aplicar técnicas onde os requisitos permitirem | Tabela ou modelo rastreável e cenários correspondentes |
| Caixa-branca e mutação (antigas semanas 10–11) | 10 | Estrutura, caminhos, cobertura e força da suíte | Inspeção, medição e experimentos com mutantes | Lacunas analisadas e novos testes justificados |
| Sistema, aceitação e sistemas críticos (bloco final original) | 11 e síntese no 13 | Escopo, risco e limites da evidência | Fluxos completos e análise fundamentada de criticidade | Critérios cobertos/pendentes e riscos explicitados |
| CI/CD e Docker (antigas semanas 14–17) | 12 | Automação e reprodução do ambiente | Execução de regressão em pipeline | Resultado de execução e diagnóstico das falhas |
| Defesa dos resultados (bloco final original) | 13 e momentos parciais a definir | Argumentação técnica | Apresentar e discutir evidências | Distinção entre resultados observados, pendências e conclusões |

Durante a redação, associar essas competências a seções reais do texto canônico. Só depois das autorizações correspondentes, associá-las às ações e aos instrumentos de laboratório. Não marcar como executada uma prática apenas porque foi planejada.

## Recorte e materiais da Aula 06

Título de trabalho: **Introdução ao TDD: do requisito ao primeiro comportamento web**.

O primeiro incremento é uma página inicial de inclusão de painel solar, acessível pelo navegador, com a entrada de Cooperado indicada como obrigatória e os campos do recorte escolhido. Mostrar um campo ou sua indicação visual não prova a aplicação da regra: rejeição de cadastro sem Cooperado e persistência do vínculo ficam para os próximos incrementos. Não declarar a Feature concluída ao final da Aula 06.

O texto canônico deve abordar:

1. problema, contrato didático e relação com a verificação estática da N2;
2. teste antes do código, caso de teste, oráculo e asserção;
3. interpretação de falhas esperadas e distinção de falhas de infraestrutura;
4. ciclos externo e interno e pequenos passos;
5. alcance, base de elaboração e finalidade dos testes da demonstração;
6. refatoração, regressão e limites das evidências;
7. questões de revisão e leituras localizadas.

Preservar `_content.qmd` como conteúdo canônico e `index.qmd` como contexto e inclusão. Os slides terão narrativa própria de demonstração, não uma cópia linear do texto. O laboratório terá ações, entradas, evidências e critérios de avanço. Um guia docente, quando autorizado, deverá acompanhar o laboratório e sua sequência ensaiada.

## Ordem de produção e limites de autorização

1. Registrar este replanejamento e as instruções de precedência aos agentes.
2. Preparar primeiro o texto canônico da Aula 06 conforme as especificações relevantes.
3. Aguardar revisão manual do docente.
4. Gerar slides somente após nova instrução explícita do docente.
5. Gerar laboratório somente após nova instrução explícita do docente. Preparação do script de ambiente e da aplicação didática pertence à etapa autorizada correspondente.

Não antecipar slides, laboratório, guia docente, script ou aplicação de demonstração. Não reescrever agora a Aula 00: sua atualização requer autorização específica, deve preservar o planejamento inicial como histórico e apontar para a sequência vigente.

## Isolamento e publicação

A branch dos materiais é `replanejamento/tdd-integrado`. O repositório novo da aplicação didática é um artefato separado; criar a branch dos materiais não equivale a criar a aplicação.

Preservar alterações locais preexistentes. A aprovação deste plano não autoriza commit, push, merge, publicação ou alteração de artefatos gerados. Não renderizar sem autorização explícita. Submeter o texto à revisão docente antes de qualquer integração na `main`.
