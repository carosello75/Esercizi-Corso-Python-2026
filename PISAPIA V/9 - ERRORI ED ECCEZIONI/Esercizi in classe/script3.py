from pathlib import Path

percorso = Path("dati/report.txt")
QUANTITA = ["12", "4", "venti", "67"]

try:
    with open(percorso, "w") as f:
        print("Report ORDINI", file=f)
        for testo in QUANTITA:
            print(f"quantita: {int(testo)}", file=f)
            print(f"scritta la riga con il testo: {testo}")
except ValueError:
    print("Il programma si è bloccato!")

contenuto = percorso.read_text()
print(contenuto, end="")

righe_di_dati = len(contenuto.splitlines()) - 1

print(f"Report completato parzialmente: {righe_di_dati} righe su {len(QUANTITA)} caricate sul file")
