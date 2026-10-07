from pathlib import Path
from bs4 import BeautifulSoup

PERCORSO = Path("dati") / "pagina-1.html"

testo_html = PERCORSO.read_text()

pagina = BeautifulSoup(testo_html, 'html.parser')

prodotti = pagina.find_all("li", class_="prodotto")
print("class prodotto: ", len(prodotti))

esauriti = pagina.find_all("li", class_="esaurito")
print("class esauriti: ", len(esauriti), "->", esauriti[0].h2.get_text())

audio = pagina.find_all("li", attrs={"data-categoria": "AUDIO"})
print("data-categoria: ", len(audio))

for scheda in audio:
    print(" ", scheda.h2.get_text(), "\n")
