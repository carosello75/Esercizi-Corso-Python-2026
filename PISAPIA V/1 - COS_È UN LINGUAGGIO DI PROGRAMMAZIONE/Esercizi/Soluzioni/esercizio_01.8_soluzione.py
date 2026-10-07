"""
SOLUZIONE — Esercizio 01.8: Apertura conto corrente

Il documento è diviso in tre sezioni perché così lo legge il cliente:
chi sono, quanto mi costa, quanto ho. La divisione non è estetica: se
domani la banca aggiunge una voce di costo, si sa esattamente dove va.

Il listino sta tutto in costanti, i dati del cliente in variabili, e i
tre numeri che contano (canone annuo, totale primo anno, saldo) sono
calcolati e mai scritti a mano. Questa è la struttura standard del
capitolo 15 applicata per intero: docstring, costanti, main(), guard.
"""

CANONE_MENSILE = 3.50
MESI_ANNO = 12
IMPOSTA_BOLLO_ANNUA = 34.20
COSTO_CARTA_DEBITO = 12.00

RIGA_DOPPIA = "=================================================="
RIGA_SINGOLA = "--------------------------------------------------"
NOTA_FINALE = "Documento \"provvisorio\": fa fede la contabile dello sportello."


def main():
    """Stampa il riepilogo di apertura di un conto corrente."""
    intestatario = "Elena Marino"
    filiale = "Battipaglia - Agenzia 2"
    iban = "IT60X0542811101000000123456"
    prodotto = "Conto Base"
    versamento_iniziale = 1500.00

    # I tre conti della giornata. Nessuno di questi valori va scritto a
    # mano: il canone annuo dipende dal listino, il totale dipende dal
    # canone, il saldo dipende dal versamento.
    canone_annuo = CANONE_MENSILE * MESI_ANNO
    totale_primo_anno = canone_annuo + IMPOSTA_BOLLO_ANNUA + COSTO_CARTA_DEBITO
    saldo_disponibile = versamento_iniziale - CANONE_MENSILE

    print(RIGA_DOPPIA)
    print("BANCA MERIDIANA - APERTURA CONTO CORRENTE")
    print(RIGA_DOPPIA)

    # Sezione anagrafica: valori di testo, quindi si incollano con il +
    # e gli spazi li contiamo noi. Qui l'etichetta più lunga è
    # "Intestatario:" e la colonna dei valori parte dal 26esimo
    # carattere.
    print("Intestatario:            " + intestatario)
    print("Filiale:                 " + filiale)
    print("IBAN:                    " + iban)
    print("Prodotto:                " + prodotto)

    print(RIGA_SINGOLA)
    print("COSTI DEL PRIMO ANNO")

    # Trabocchetto 1: qui i valori sono numeri e si stampano con la
    # virgola. Nell'etichetta gli spazi sono UNO IN MENO rispetto alle
    # righe di sopra, perché print ne aggiunge già uno di suo. Se li
    # scrivete tutti, la colonna si sposta di un carattere e ve ne
    # accorgete solo guardando l'output con attenzione.
    print("Canone mensile:         ", CANONE_MENSILE)
    print("Canone annuo:           ", canone_annuo)
    print("Imposta di bollo:       ", IMPOSTA_BOLLO_ANNUA)
    print("Carta di debito:        ", COSTO_CARTA_DEBITO)
    print("Totale primo anno:      ", totale_primo_anno)

    print(RIGA_SINGOLA)
    print("MOVIMENTI DI APERTURA")
    print("Versamento iniziale:    ", versamento_iniziale)
    print("Addebito primo canone:  ", CANONE_MENSILE)
    print("Saldo disponibile:      ", saldo_disponibile)

    print(RIGA_DOPPIA)

    # Trabocchetto 2: gli importi escono come 42.0, 88.2 e 1496.5, non
    # come 42,00 euro. Non è un errore ed è inutile provare a
    # sistemarlo oggi: a Python gli zeri finali non interessano, e lo
    # strumento per dare la forma da documento (le f-string) arriva il
    # Giorno 02. Oggi il documento è corretto nei conti e brutto
    # nella forma, ed è esattamente il punto in cui dobbiamo essere.
    print()
    print(NOTA_FINALE)


if __name__ == "__main__":
    main()
