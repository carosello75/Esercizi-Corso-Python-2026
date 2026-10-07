TENTATIVI_MASSIMI = 4
MIN = 1
MAX = 12


def chiedi_intero(risposte, minimo, massimo):
    print(risposte[:TENTATIVI_MASSIMI])
    for risposta in risposte[:TENTATIVI_MASSIMI]:
        print(f"Componente {risposta}")

        try:
            valore = int(risposta)
        except ValueError:
            print("[ERRORE] Serve un numero")
            continue

        if valore < minimo:
            print(f"Il valore iminimo ammesso è {minimo}")
        elif valore > massimo:
            print(f"Il valore massimo ammesso è {massimo}")
        else:
            return valore

    return -1


for risposta in [["tre", "4", "4", "otto"], ["24", "100", "due", "10"]]:
    valore = chiedi_intero(risposta, MIN, MAX)
    if valore == -1:
        print("Nessun valore registrato")
    else:
        print(f"Valore registrato: {valore}")
