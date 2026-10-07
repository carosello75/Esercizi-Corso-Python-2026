from pathlib import Path

percorso = Path("ordini.txt")
righe = ["12", "8", "15", "20", "5", "9", "venti", "11", "7", "14"]

totale = 0
with open(percorso, "r") as f:
    for indice, riga in enumerate(f):
        quantita = int(riga.strip())
        totale += quantita
        print(quantita, totale)
