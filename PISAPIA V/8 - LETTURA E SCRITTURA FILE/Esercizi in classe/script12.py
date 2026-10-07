from pathlib import Path

# with open("scontrino.txt", "r") as f:
#     print(f.read())

cartella_script_assoluta = Path(__file__).resolve().parent
percorso_relativo = Path("dati") / "ticket.txt"

print(cartella_script_assoluta.is_absolute())
print(percorso_relativo.is_absolute())

print("name:", percorso_relativo.name)
print("stem:", percorso_relativo.stem)
print("suffix:", percorso_relativo.suffix)
print("parent:", percorso_relativo.parent)

esiste = percorso_relativo.exists()
print("Esiste?", esiste)
