from pathlib import Path

CARTELLA_DATI = Path("dati")

for nome_file in ["ordini.txt", "report.txt"]:
    percorso = CARTELLA_DATI / nome_file
    try:
        with open(percorso, "r") as f:
            righe = f.readlines()
        print(f"{percorso.name}: {len(righe)}")
    except FileNotFoundError:
        print(f"{percorso.name} non trovato")

print("Il programma prosegue...")
