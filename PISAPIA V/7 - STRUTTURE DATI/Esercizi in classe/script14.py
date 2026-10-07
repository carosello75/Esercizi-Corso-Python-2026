candidature = [
    ("Bianchi Anna", 30, 78, "IDONEO"),
    ("Verdi Luca", 18, 50, "NON IDONEO"),
    ("Rossi Marco", 62, 98, "IDONEO"),
    ("Pero Giovani", 25, 20, "NON IDONEO"),
]

coppie = []

for nome, eta, punteggio, esito in candidature:
    coppie.append((punteggio, nome))

coppie.sort()

print(coppie)

posizione = 0
for punteggio, nome in coppie[0:2]:
    posizione += 1
    print(f"{posizione}. {nome} - {punteggio}")
