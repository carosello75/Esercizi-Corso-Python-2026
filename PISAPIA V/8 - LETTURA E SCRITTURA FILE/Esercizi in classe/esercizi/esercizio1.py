from pathlib import Path

PERCORSO = Path("../dati") / "spedizioni.txt"
CAMPI_ATTESI = 3
ZONE_AMMESSE = ["NORD", "CENTRO", "SUD", "ISOLE"]


def carica_spedizione(percorso):
    """
    Restituire la lista di tuple delle spedizioni (codice, zona, peso) e il numero delle scartate
    :param percorso:
    :return:
    """
    spedizioni = []
    spedizioni_scartate = []
    scartate = 0
    with open(percorso, "r") as f:
        for riga in f:
            riga = riga.rstrip("\n")
            if riga.strip() == "" or riga.startswith("#"):
                continue

            campi = riga.split(";")

            if len(campi) != CAMPI_ATTESI:
                scartate += 1
                continue

            codice = campi[0].strip()
            zona = campi[1].strip().upper()

            if zona not in ZONE_AMMESSE:
                scartate += 1
                continue

            peso_grezzo = campi[2]

            if peso_grezzo.isalpha():
                scartate += 1
                continue

            peso_normalizzato = float(peso_grezzo.strip().replace(",", "."))

            spedizioni.append((codice, zona, peso_normalizzato))

    return spedizioni, scartate


spedizioni, scartate = carica_spedizione(PERCORSO)
print(f"Spedizioni caricate correttamente: {spedizioni}")
print(f"Totale spedizioni: {len(spedizioni)}")
print(f"Numero di spedizioni scartate: {scartate}")
