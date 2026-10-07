LISTINO = {"NORD": 8.50, "CENTRO": 7.00, "SUD": 9.50, "ISOLE": 14.00}

for zona, peso_testo in [("NORD", "12.5"), ("ISOLE", "3"), ("SUD", "venti")]:
    try:
        peso = float(peso_testo)
    except ValueError:
        print(f"{zona}: {peso_testo} -> Peso non valido, riga scartata")
    else:
        costo = peso * LISTINO[zona]
        print(f"{zona}: {peso} -> Costo: {costo}")
    finally:
        print("Riga chiusa")

print("==" * 50)


def stampa_listino(zona):
    try:
        return LISTINO[zona]
    finally:
        print("Ricerca conclusa")


prezzo = stampa_listino("NORD")
print(prezzo)
