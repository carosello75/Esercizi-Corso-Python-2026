# CATALOGO = ["Cuffie Bluetooth", "Tastiera meccanica", "Mouse verticale",
#            "Monitor 27 pollici", "Webcam HD", "Hub USB-C"]

# for prodotto in CATALOGO:
#    print("Prodotto:", prodotto)


lista = [130, 34, 42, 110, 120]

totale = 0
conta_sopra_cento = 0

for valore in lista:
    totale += valore
    if valore > 100:
        conta_sopra_cento += 1

print("Totale:", totale)
print("Sopra i cento:", conta_sopra_cento)
