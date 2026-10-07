LISTINO = {"NORD": 8.50, "SUD": 9.50, "ISOLE": 14.00}

# keys() -> tutte le chiavi
# print(LISTINO.keys())

# values() -> tutti i valori
# print(LISTINO.values())

# items()
# print(LISTINO.items())

# for zona, prezzo in LISTINO.items():
#     print(f"{zona}: {prezzo}")


# LISTINO["CENTRO"] = 7.8
# LISTINO["NORD"] = 100
# print(LISTINO)


del LISTINO["NORD"]

print(LISTINO)
