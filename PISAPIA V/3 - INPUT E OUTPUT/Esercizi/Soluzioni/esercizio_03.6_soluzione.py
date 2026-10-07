"""
SOLUZIONE — Esercizio 03.6: Disposizione di bonifico

Sei campi raccolti in tre gruppi (ordinante, beneficiario, operazione) e
un riquadro costruito con una regola sola: cornice di 50 cancelletti,
contenuto interno largo 46, perché 1 + 1 + 46 + 1 + 1 fa 50.

Il mascheramento dell'IBAN è fatto con lo slicing del Giorno 02 e con
costanti, non con numeri scritti dentro le parentesi quadre: il giorno
che si decide di mostrare sei cifre invece di quattro si cambia una riga.

Il programma assume un IBAN italiano di 27 caratteri e un importo scritto
senza separatore delle migliaia.
"""

CORNICE = "#" * 50
BANCA = "BANCA MERIDIANA - DISPOSIZIONE DI BONIFICO"
COMMISSIONE_BONIFICO = 1.50
IBAN_LUNGHEZZA = 27
PRIMI_VISIBILI = 4
ULTIMI_VISIBILI = 4
NOTA = "Disposizione registrata. Conservare la contabile."


def main():
    """Raccoglie una disposizione di bonifico e stampa il riquadro."""
    ordinante = input("Ordinante (nome e cognome): ").strip().title()
    beneficiario_grezzo = input("Beneficiario (nome o ragione sociale): ")
    beneficiario = beneficiario_grezzo.strip().title()

    # Trabocchetto 1: l'IBAN si scrive a gruppi di quattro perché così si
    # legge, ma va archiviato compatto. Prima .replace(" ", ""), poi
    # .upper(): al contrario funzionerebbe lo stesso, ma la lunghezza
    # calcolata sotto dipende dall'aver tolto gli spazi, quindi quella
    # pulizia non è facoltativa.
    iban_grezzo = input("IBAN beneficiario: ")
    iban = iban_grezzo.strip().replace(" ", "").upper()

    importo_grezzo = input("Importo in euro (senza separatore migliaia): ")
    importo = float(importo_grezzo.strip().replace(",", "."))

    causale = input("Causale: ").strip()
    data_valuta = input("Data valuta (gg/mm/aaaa): ").strip()

    # Trabocchetto 2: le posizioni dello slicing non si scrivono a mano.
    # iban[23:27] funziona finché l'IBAN è italiano; con una costante e
    # una sottrazione il codice dice cosa sta facendo e si adatta se
    # domani si decide di mostrare sei cifre invece di quattro.
    inizio = iban[0:PRIMI_VISIBILI]
    fine = iban[IBAN_LUNGHEZZA - ULTIMI_VISIBILI:IBAN_LUNGHEZZA]
    nascosti = IBAN_LUNGHEZZA - PRIMI_VISIBILI - ULTIMI_VISIBILI
    iban_mascherato = inizio + "*" * nascosti + fine

    totale_addebito = importo + COMMISSIONE_BONIFICO

    riga_ordinante = f"{'Ordinante:':<16}{ordinante}"
    riga_beneficiario = f"{'Beneficiario:':<16}{beneficiario}"
    riga_iban = f"{'IBAN:':<16}{iban_mascherato}"
    riga_causale = f"{'Causale:':<16}{causale}"
    riga_data = f"{'Data valuta:':<16}{data_valuta}"
    riga_importo = f"{'Importo:':<16}{importo:>12.2f} euro"
    riga_commissione = f"{'Commissione:':<16}{COMMISSIONE_BONIFICO:>12.2f} euro"
    riga_totale = f"{'TOTALE ADDEBITO:':<16}{totale_addebito:>12.2f} euro"

    print()
    print(CORNICE)
    print(f"# {BANCA:<46} #")
    print(CORNICE)
    print(f"# {riga_ordinante:<46} #")
    print(f"# {riga_beneficiario:<46} #")
    print(f"# {riga_iban:<46} #")
    print(f"# {riga_causale:<46} #")
    print(f"# {riga_data:<46} #")
    print(CORNICE)
    print(f"# {riga_importo:<46} #")
    print(f"# {riga_commissione:<46} #")
    print(f"# {riga_totale:<46} #")
    print(CORNICE)
    print(NOTA)


if __name__ == "__main__":
    main()
