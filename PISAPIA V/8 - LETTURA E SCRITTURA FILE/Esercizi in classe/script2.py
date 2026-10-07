# with open(nome_file, r/w, encoding="utf-8") as f
from pathlib import Path

percorso = Path("dati") / "ticket.txt"

"""
with open(percorso, "w") as f:
    f.write("\n\nCiao Mondo\n")

with open(percorso, "r") as f:
    print(f.read())
"""

file = open(percorso, "a")
file.write("\n\nCiao Mondo senza with\n")
file.close()

# Mddalità

"""
Lettura: r
Scrittura
w -> scrittura da zero
a -> aggiunge in fondo
x -> creazione esclusiva
"""
