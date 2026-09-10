#let article(
  title: none,
  subtitle: none,
  authors: none,
  keywords: (),
  date: none,
  abstract-title: none,
  abstract: none,
  thanks: none,
  cols: 1,
  lang: "pt",
  region: "BR",
  font: none,
  fontsize: 10.5pt,
  title-size: 2em,
  subtitle-size: 1.25em,
  heading-family: none,
  heading-weight: "bold",
  heading-style: "normal",
  heading-color: black,
  heading-line-height: 0.65em,
  mathfont: none,
  codefont: none,
  linestretch: 1.1,
  sectionnumbering: none,
  linkcolor: "#0284c7",
  citecolor: "#0369a1",
  filecolor: "#0284c7",
  toc: false,
  toc_title: "Sumário",
  toc_depth: 3,
  toc_indent: 1.5em,
  doc,
) = {
  // Document metadata
  set document(title: if title != none { title } else { "Apostila VVTS" })
  if authors != none and authors != () {
    set document(author: if authors != none and authors != () { authors.map(a => content-to-string(a.name)).join(", ") } else { "Prof. Me. Maxwell Anderson Ielpo do Amaral" })
  }

  // Base typography and paragraph formatting
  set text(
    lang: lang,
    region: region,
    size: fontsize,
  )
  set par(
    justify: true,
    leading: linestretch * 0.65em,
  )
  show math.equation: set text(font: mathfont) if mathfont != none

  // Links styling
  show link: set text(fill: rgb(linkcolor))
  show ref: set text(fill: rgb(citecolor))

  // Headings base numbering
  set heading(numbering: sectionnumbering)

  // Headings page breaks and styling: level 1 always on new page
  show heading.where(level: 1): it => {
    pagebreak(weak: true)
    v(1.8em)
    text(fill: rgb("#0f172a"), weight: "bold")[#it]
    v(1em)
  }

  show heading.where(level: 2): it => {
    v(1.2em)
    text(fill: rgb("#1e293b"), weight: "bold")[#it]
    v(0.6em)
  }

  show heading.where(level: 3): it => {
    v(1em)
    text(fill: rgb("#334155"), weight: "bold")[#it]
    v(0.4em)
  }

  // Page setup: A4, header and footer
  set page(
    paper: "a4",
    margin: (x: 2.5cm, top: 2.5cm, bottom: 2.5cm),
    footer: context {
      let page_num = counter(page).get().first()
      if page_num > 1 {
        align(center)[
          #text(size: 9pt, fill: rgb("#64748b"))[#page_num]
        ]
      }
    },
  )

  // ==========================================
  // CAPA (Página 1: dedicada, sem cabeçalho/rodapé)
  // ==========================================
  {
    set page(
      header: none,
      footer: none,
      margin: (x: 2.8cm, top: 3.2cm, bottom: 2.8cm),
    )

    // Topo Institucional
    align(center)[
      #text(size: 11pt, weight: "bold", fill: rgb("#0f172a"))[
        INSTITUTO FEDERAL DE EDUCAÇÃO, CIÊNCIA E TECNOLOGIA DA PARAÍBA
      ] \
      #v(0.35em)
      #text(size: 9.5pt, weight: "medium", fill: rgb("#334155"))[
        CAMPUS JOÃO PESSOA • DIRETORIA DE ENSINO SUPERIOR
      ] \
      #v(0.25em)
      #text(size: 9.5pt, weight: "medium", fill: rgb("#334155"))[
        UNIDADE ACADÊMICA DE GESTÃO E TECNOLOGIA DA INFORMAÇÃO
      ] \
      #v(0.25em)
      #text(size: 9.5pt, weight: "medium", fill: rgb("#0284c7"))[
        CURSO DE BACHARELADO EM ENGENHARIA DE SOFTWARE
      ]
      #v(1.2em)
      #line(length: 75%, stroke: 1.5pt + rgb("#0284c7"))
    ]

    // Bloco Central do Título
    align(center + horizon)[
      #block(
        stroke: (left: 4pt + rgb("#0284c7")),
        inset: (left: 1.5em, y: 1.4em, right: 1em),
        fill: rgb("#f8fafc"),
        radius: (right: 6pt),
        width: 100%,
      )[
        #align(left)[
          #text(size: 10.5pt, weight: "bold", fill: rgb("#0284c7"))[
            APOSTILA DIDÁTICA INTEGRADA
          ]
          #v(0.7em)
          #text(size: 22pt, weight: "bold", fill: rgb("#0f172a"))[
            #if title != none { title } else [Verificação, Validação e Testes de Software]
          ]
          #if subtitle != none {
            v(0.9em)
            text(size: 12.5pt, weight: "medium", fill: rgb("#475569"))[#subtitle]
          }
        ]
      ]
    ]

    // Rodapé da Capa
    align(center + bottom)[
      #block(width: 100%)[
        #text(size: 11pt, weight: "bold", fill: rgb("#0f172a"))[
          #if authors != none and authors != () {
            authors.map(a => if type(a) == dictionary { a.name } else { str(a) }).join(", ")
          } else [
            Prof. Me. Maxwell Anderson Ielpo do Amaral
          ]
        ] \
        #v(0.3em)
        #text(size: 9.5pt, fill: rgb("#64748b"))[
          maxwell.amaral\@ifpb.edu.br
        ] \
        #v(2.5em)
        #text(size: 10pt, weight: "medium", fill: rgb("#334155"))[
          João Pessoa — PB \
          #if date != none { date } else [2026]
        ]
      ]
    ]
  }

  pagebreak()

  // ==========================================
  // SUMÁRIO (Inicia em nova página)
  // ==========================================
  if toc {
    pagebreak(weak: true)
    
    heading(level: 1, numbering: none, outlined: false)[
      #if toc_title != none { toc_title } else [Sumário]
    ]
    v(1.5em)

    outline(
      title: none,
      depth: toc_depth,
      indent: toc_indent,
    )

    pagebreak()
  }

  // Conteúdo principal
  doc
}

#set table(
  inset: 6pt,
  stroke: none,
)
