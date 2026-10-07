CATALOGO = ["Cuffie Bluetooth", "Tastiera meccanica", "Mouse verticale",
            "Monitor 27 pollici", "Webcam HD", "Hub USB-C"]
NUMERI = [1, 2, 3, 4]
print(f"Catalogo di partenza: {CATALOGO}, \nlunghezza: {len(CATALOGO)}")
print("=" * 50)

CATALOGO[3]
# numero tot di elementi
# print(len(CATALOGO))

# visualizzare un elemento con indice
# print(CATALOGO[len(CATALOGO) - 1])


# assegnazione per posizione "classica"
# CATALOGO[5] = "Tastiera wireless"
# print(CATALOGO)


# append -> aggiunge in fondo (sempre) un valore
# CATALOGO.append("Monitor 32 pollici")
# print(CATALOGO, len(CATALOGO))


# insert(i, valore) -> valore va alla posizione i e tutti gli altri scalano 1
# CATALOGO.insert(1, "Mouse Apple")
# print(CATALOGO, len(CATALOGO))

# remove(x) -> rimuove la PRIMA occorrenza del valore
# CATALOGO.remove("Tastiera meccanica")
# print(CATALOGO)

# pop() -> rimuovo l'ultimo
# pop(i) -> rimuovo quello alla posizione specificata con i

# CATALOGO.pop(2)
# print(CATALOGO)
