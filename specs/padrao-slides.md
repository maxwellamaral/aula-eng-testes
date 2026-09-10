# Padrão de slides

Slides são apoio à condução presencial e não devem replicar a página da aula seção por seção. Cada deck deve usar Reveal.js e `assets/css/slides.css`.

## Narrativa mínima

Organize a apresentação com frames de abertura, contextualização, problema ou evidência, conceitos-chave, exemplo ou contraste, atividade quando necessária e síntese. O deck deve permitir compreensão básica sem depender de uma IDE ou desenho obrigatório no quadro.

## Critérios visuais

- Um objetivo principal por slide.
- Texto, imagens e diagramas precisam caber no viewport de 1280×720.
- Imagens devem ter fonte local ou URL estável, tamanho útil e legenda quando necessário.
- Inclua link para o material escrito da aula.
- Represente fluxos, processos e sequências como diagrama (por exemplo, Mermaid `flowchart`), nunca como diagrama ASCII dentro de um bloco de código (` ```text `). Um bloco de código sinaliza "código-fonte" para quem assiste, não um processo.
- Dentro do corpo de um slide (`## `), nunca use um heading de nível igual ou inferior ao `slide-level` do documento (por padrão, nível 1, `# `). O Reveal.js trata esse heading como início de um **slide novo**, partindo o conteúdo ao meio e deixando o slide original incompleto. Para destacar uma frase de impacto dentro do slide, use ênfase (`**texto**`) ou um heading de nível superior ao `slide-level` (por exemplo, `### `), nunca `#`.

## Revisão após a criação

Toda criação ou alteração de um deck exige as duas etapas abaixo, nesta ordem. Nenhuma delas substitui a outra.

1. **Auditoria automatizada.** Renderize o deck e execute `scripts/audit_slides.py` sobre o HTML gerado. Essa auditoria confirma apenas carregamento, dimensões, visibilidade e contenção de **imagens (`<img>`)**. Ela não verifica diagramas Mermaid/SVG, tabelas, listas ou estouro de texto.
2. **Inspeção humana slide a slide.** Abra o HTML renderizado no navegador e percorra **cada slide individualmente** (não apenas uma amostra), verificando em cada um:
   - se todo o conteúdo esperado está presente (texto, figura, quadro, tabela, link);
   - se nada está cortado nas bordas ou no rodapé do slide (sinal de que o conteúdo excede a altura do viewport — nesse caso, reduza texto ou divida o slide em dois);
   - se diagramas de fluxo/processo aparecem como diagrama, não como texto ASCII em bloco de código;
   - se cada slide corresponde a um único heading de nível `slide-level` e não foi partido involuntariamente por um heading de nível inferior mal utilizado no corpo do texto.

Corrija os problemas encontrados, renderize novamente e repita as duas etapas antes de considerar o deck pronto.
