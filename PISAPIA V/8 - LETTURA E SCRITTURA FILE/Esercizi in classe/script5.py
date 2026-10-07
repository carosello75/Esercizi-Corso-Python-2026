from pathlib import Path

PERCORSO = Path("dati") / "spedizioni.txt"

with open(PERCORSO, "r", encoding="utf-8") as f:
    intestazione = f.readline()

print(intestazione)
