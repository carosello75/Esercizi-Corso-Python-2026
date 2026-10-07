from pathlib import Path

PERCORSO = Path("dati") / "lettera_candidatura.txt"

with open(PERCORSO, "r", encoding="utf-8") as f:
    testo = f.read()

print(type(testo))
print(f"Contenuto del file:\n{testo}\n")
print(f"Conteggio dei caratteri: {len(testo)}\n")
print(f"Conteggio righe: {testo.count("\n")}\n")

parole = testo.split()
print(f"Stampa di tutte le parole: {parole}\n")
print(f"Conteggio delle parole: {len(parole)}\n")

print("=" * 50)

with open(PERCORSO, "r", encoding="utf-8") as f:
    righe = f.readlines()

for riga in righe:
    if riga != "\n":
        print(f"Riga: {riga}")

print(f"Lista righe: {righe}\n")
print(f"Conteggio righe: {len(righe)}\n")
print(f"Ultima riga: {righe[-1]}")
