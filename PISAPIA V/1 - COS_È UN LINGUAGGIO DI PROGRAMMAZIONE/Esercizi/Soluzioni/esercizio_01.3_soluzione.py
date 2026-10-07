"""
SOLUZIONE — Esercizio 01.3: Conto della spesa senza formattazione

Ogni passaggio del conto sta in una variabile con un nome: subtotale, iva,
totale, quota. Si potrebbe scrivere tutto in una riga sola, ma quando il
totale sbaglia non si capisce dove: con i passaggi separati si stampa un
pezzo alla volta e si trova l'errore in trenta secondi.

L'aliquota è una costante: compare in un punto solo e il giorno che
cambia si tocca una riga sola.
"""

ALIQUOTA_IVA = 0.22
RIGA = "------------------------------"


def main():
    """Calcola e stampa il riepilogo di un ordine di quattro articoli."""
    prezzo_tastiera = 89.00
    prezzo_mouse = 34.50
    prezzo_hub = 27.00
    prezzo_monitor = 219.00
    colleghi = 4

    # A destra dell'uguale c'è un calcolo: Python lo esegue e poi attacca
    # l'etichetta "subtotale" al risultato.
    subtotale = prezzo_tastiera + prezzo_mouse + prezzo_hub + prezzo_monitor

    # Le parentesi qui non servono: la moltiplicazione viene comunque
    # prima. Le mettiamo perché chi rilegge non deve fermarsi a pensarci.
    iva = (subtotale * ALIQUOTA_IVA)
    totale = subtotale + iva

    # Trabocchetto 1: la divisione in Python restituisce SEMPRE un numero
    # con la virgola, anche quando il conto viene esatto. Qui esce
    # 112.6975: quattro cifre decimali su una cifra in euro sono brutte
    # ma corrette. Arrotondare e incolonnare è materia del Giorno 02.
    quota_a_testa = totale / colleghi

    print("NovaStore - Riepilogo ordine")
    print(RIGA)

    # Trabocchetto 2: qui la virgola è obbligatoria. Scrivendo
    # "Tastiera meccanica " + prezzo_tastiera il programma si fermerebbe
    # con TypeError, perché il "+" non incolla un testo e un numero.
    print("Tastiera meccanica", prezzo_tastiera)
    print("Mouse verticale", prezzo_mouse)
    print("Hub USB-C", prezzo_hub)
    print("Monitor 27 pollici", prezzo_monitor)

    print(RIGA)
    print("Subtotale:", subtotale)
    print("IVA 22%:", iva)
    print("Totale:", totale)
    print("Quota a testa:", quota_a_testa)


if __name__ == "__main__":
    main()
