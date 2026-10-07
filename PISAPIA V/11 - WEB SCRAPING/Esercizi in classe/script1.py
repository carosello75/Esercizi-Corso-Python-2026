from pathlib import Path
from bs4 import BeautifulSoup


def titolo_pagina(testo_html):
    pagina = BeautifulSoup(testo_html, 'html.parser')
    return pagina.title.get_text()


pagina_HTML = "<html><head><title>Test HTML</title></head></html>"
titolo_pagina_ = titolo_pagina(pagina_HTML)
print(f"Titolo pagina da HTML statico: {titolo_pagina_}")

print("*" * 50)

PERCORSO = Path("dati") / "tariffe.html"
pagina_HTML_da_file = PERCORSO.read_text(encoding="utf-8")

for contenuto_html in [pagina_HTML, pagina_HTML_da_file]:
    titolo_da_stampare = titolo_pagina(contenuto_html)
    print(f"{type(contenuto_html)}: {titolo_da_stampare}\n")
