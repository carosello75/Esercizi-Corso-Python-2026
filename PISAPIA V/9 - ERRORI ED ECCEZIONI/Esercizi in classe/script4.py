def converti(testo):
    return int(testo)


def carica(righe):
    numeri = []
    for riga in righe:
        numeri.append(converti(riga))
    return numeri


def media(righe):
    numeri = carica(righe)
    return sum(numeri) / len(righe)


try:
    print(f"Calcola media: {media(["22", "33", "quattro"])}")
except ValueError:
    print("Errore!!!")

print("fai altre cose ")
