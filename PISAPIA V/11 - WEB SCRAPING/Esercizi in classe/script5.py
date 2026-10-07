from pathlib import Path
from bs4 import BeautifulSoup

PERCORSO = Path("dati") / "pagina-1.html"

testo_html = PERCORSO.read_text()

pagina = BeautifulSoup(testo_html, 'html.parser')

main = pagina.find("main")
SELETTORI = ["li.prodotto", ".nome", "li.esaurito"]

for selettore in SELETTORI:
    trovati = main.select(selettore)
    print(f"{selettore: <10} -> {len(trovati)} elementi")

try:
    testata = main.select_one("#testata")
    print(f"{testata:<10}")
except TypeError:
    print("Tag non presente")
