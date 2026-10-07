COLORI = ["BIANCO", "VERDE", "GIALLO", "ROSSO"]
print("Il colore più grave è:", COLORI[-1])

accessi = ["VERDE", "VERDE", "ROSSO", "GIALLO", "ROSSO"]
conteggi = {}

for colore in accessi:
    conteggi[colore] = conteggi.get(colore, 0) + 1

print(conteggi)

for colore in COLORI:
    print(f"{colore:<8}{conteggi.get(colore, 0)}")
