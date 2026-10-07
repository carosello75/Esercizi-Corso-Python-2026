SCHEDA = ("li", "",
          [("h2", "Cuffie", [("b", "Testo", [])]),
           ("span", "50 €", []),
           ("a", "Vedi Scheda", [])])

CATALOGO = ("ul", "Creazione UL", [SCHEDA])

nome_ul, testo_ul, figli_ul = CATALOGO

for nome_li, testo_li, figli_li in figli_ul:
    print(f"{nome_ul} -> {nome_li} -> Figlio diretto")
    for nome_foglia, testo_foglia, figli_foglia in figli_li:
        print(f"{nome_ul} -> {nome_li} -> {nome_foglia}")
