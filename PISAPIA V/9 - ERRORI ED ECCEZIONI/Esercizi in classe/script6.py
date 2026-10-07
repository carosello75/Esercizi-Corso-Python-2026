ETA_PENSIONE = 67


def anni_alla_pensione(testo):
    try:
        eta = int(testo)
    except ValueError:
        print(f"{testo} non è un valore valido!")
        return

    return ETA_PENSIONE - eta


print(anni_alla_pensione("venti"))
