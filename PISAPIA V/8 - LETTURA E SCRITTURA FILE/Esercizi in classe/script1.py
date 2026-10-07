from pathlib import Path

percorso = Path("dati") / "ticket.txt"

print(percorso)
if percorso.is_file():
    print("File trovato: ", percorso.name)
else:
    print("File non trovato")
