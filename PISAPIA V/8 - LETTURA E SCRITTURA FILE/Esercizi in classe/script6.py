from pathlib import Path

PERCORSO = Path("dati") / "presenze.txt"

with open(PERCORSO, "w", encoding="utf-8") as f:
    f.write("Piro\nRossano\nRossi\nVerdi")

with open(PERCORSO, "r", encoding="utf-8") as f:
    nome = input("Dammi nome da cercare: ").strip()
    for riga in f:
        riga_temp = riga.lower().rstrip("\n")
        print(riga_temp)
        if riga_temp == nome.lower():
            print(f"{nome} è presente")
