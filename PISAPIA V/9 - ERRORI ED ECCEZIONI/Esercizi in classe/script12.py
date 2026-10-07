def fascia_isee(isee):
    fascia = 4
    if isee < 0:
        raise ValueError(f"ISEE negativo {isee} non è permesso; deve essere un valore >= 0")
    if isee <= 8000:
        fascia = 1
    elif isee <= 16000:
        fascia = 2
    elif isee <= 28000:
        fascia = 3

    return fascia


for isee in [7500, -200]:
    fascia = fascia_isee(isee)
    print(f"Fascia: {fascia}")
