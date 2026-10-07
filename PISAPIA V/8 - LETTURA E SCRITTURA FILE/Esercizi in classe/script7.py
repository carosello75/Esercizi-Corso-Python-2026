from pathlib import Path

PERCORSO = Path("dati") / "anagrafiche.txt"
CERCATO = "barbato"

trovati = 0
with open(PERCORSO, "r") as f:
    for riga in f:
        riga = riga.rstrip("\n")
        if riga.strip() == "" or riga.startswith("#"):
            continue

        nome, cognome, email = riga.split(";")

        cognome_normalizzato = cognome.strip().lower()
        if cognome_normalizzato == CERCATO:
            trovati += 1
            print(f"{cognome_normalizzato} è stato trovato")
            print(f"{nome.strip().lower()} {email.strip().lower()}")
