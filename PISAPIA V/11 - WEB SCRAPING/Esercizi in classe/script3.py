from pathlib import Path
from bs4 import BeautifulSoup

PERCORSO = Path("dati") / "pagina-1.html"

testo_html = PERCORSO.read_text()

pagina = BeautifulSoup(testo_html, 'html.parser')

h2_element = pagina.nav
h2_elements = pagina.find_all("h2")

table_elements = pagina.find_all("table")
table_element = pagina.table  # pagina.find("table")

# Recupero di tutti gli span presenti nel secondo elemento dell'elenco puntano
li_elements = pagina.find_all("li")
secondo_li = li_elements[1]

span_elements = secondo_li.find_all("span", recursive=False)

print(span_elements)
