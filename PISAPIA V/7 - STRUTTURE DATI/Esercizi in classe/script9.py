# {chiave: valore, ..., chiaveN: valoreM}

prezzi = {"Cuffie": 50.99, "Mouse": 20.99, "Tastiera meccanica": 69.99}

totale = prezzi["Mouse"] + prezzi["Cuffie"] + prezzi["Tastiera meccanica"]

# print(f"Il totale è: {totale:.2f}")


print(prezzi.get("Smartphone", 56.4))

print(prezzi)
