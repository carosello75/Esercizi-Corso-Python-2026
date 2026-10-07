candidature = [
    ("Bianchi Anna", 30, 78, "IDONEO"),
    ("Verdi Luca", 18, 50, "NON IDONEO"),
    ("Rossi Marco", 62, 98, "IDONEO"),
    ("Pero Giovani", 25, 20, "NON IDONEO"),
]

# for nome, eta, punteggio, esito in candidature:
#     print(f"{nome:<20}{eta:>5}{punteggio:>5} {esito}")
IDONEO = "IDONEO"
idonei = 0
somma = 0

for nome, eta, punteggio, esito in candidature:
    somma += punteggio
    if esito == IDONEO:
        idonei += 1

print(f"Idonei: {idonei} su {len(candidature)}")
print(f"La somma dei punteggi è: {somma}")
print(f"La media dei test è: {somma / len(candidature):.2f}")
