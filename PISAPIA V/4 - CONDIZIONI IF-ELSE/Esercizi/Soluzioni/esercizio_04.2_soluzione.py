"""
SOLUZIONE — Esercizio 04.2: Sconto a soglie

La catena di `elif` è scritta dalla soglia più alta alla più bassa.
Non è una preferenza estetica: con l'ordine opposto la prima
condizione cattura tutti e le altre non vengono mai raggiunte, ed è
esattamente l'errore che ha prodotto i quaranta scontrini sbagliati.

I rami non stampano niente: assegnano quattro variabili. Stampare
dentro i rami sembra più corto, ma poi il formato dello scontrino
finisce scritto in quattro punti diversi e cambiarlo diventa un lavoro.

Due delle quattro variabili servono solo alla riga finale, quella che
dice quanto manca per salire di fascia. Nella fascia più alta non c'è
niente da dire, e il modo in cui il programma se lo ricorda è la parte
che vale la pena guardare.
"""

# Le soglie della campagna: il tariffario del punto vendita, non una
# scelta di chi programma. Quando la campagna cambia si toccano queste
# righe, e la catena di decisioni più sotto resta identica.
SOGLIA_BRONZO = 50.00
SOGLIA_ARGENTO = 100.00
SOGLIA_ORO = 200.00

# Le percentuali stanno come frazioni, non come numeri interi: 0.05 è
# già pronto per la moltiplicazione, e il formato :.0% lo rimette in
# percentuale al momento della stampa.
SCONTO_BASE = 0.00
SCONTO_BRONZO = 0.05
SCONTO_ARGENTO = 0.10
SCONTO_ORO = 0.15

# I due valori che dicono "sopra di te non c'è niente". La fascia più
# alta li assegna al posto del nome e della soglia successiva: sono
# dati dichiarati assenti, non dimenticanze.
NESSUNA_FASCIA_SOPRA = ""
NESSUNA_SOGLIA_SOPRA = 0.00

LARGHEZZA_SCONTRINO = 50
RIGA_DOPPIA = "=" * LARGHEZZA_SCONTRINO
RIGA_SINGOLA = "-" * LARGHEZZA_SCONTRINO


def main():
    """Applica lo sconto per fasce di spesa e stampa lo scontrino."""
    # 1. Lettura e normalizzazione: alla cassa il totale si digita con
    #    la virgola. .replace() restituisce una stringa nuova, quindi
    #    il dato originale resta disponibile se servisse ristamparlo.
    testo_spesa = input("Totale della spesa in euro: ").strip()
    testo_normalizzato = testo_spesa.replace(",", ".")

    # 2. Conversione: è l'unico punto in cui il programma può fermarsi.
    #      testo_spesa         ->  "137,50"  (str)
    #      testo_normalizzato  ->  "137.50"  (str)
    #      spesa               ->   137.5    (float)
    spesa = float(testo_normalizzato)

    # 3. La decisione: quattro fasce, quattro rami, nessuna stampa.
    #
    # TRABOCCHETTO: la catena si legge dall'alto e si ferma al primo
    #   ramo vero. Se il primo controllo fosse >= SOGLIA_BRONZO, una
    #   spesa di 250 euro entrerebbe lì dentro e prenderebbe il 5%: gli
    #   altri rami non verrebbero nemmeno guardati. Dal più stringente
    #   al meno stringente, sempre.
    #
    # TRABOCCHETTO: ogni ramo assegna TUTTE e quattro le variabili,
    #   anche quelle che nel suo caso non diranno niente. Un ramo che
    #   ne salta una funziona finché nessuno legge quella variabile, e
    #   il giorno in cui qualcuno la legge il programma si ferma con
    #   NameError: name 'fascia_prossima' is not defined, cioè con il
    #   nome di una variabile in faccia a chi aveva solo fatto la
    #   spesa. È il motivo per cui l'else finale non è facoltativo.
    if spesa >= SOGLIA_ORO:
        fascia = "ORO"
        sconto = SCONTO_ORO
        fascia_prossima = NESSUNA_FASCIA_SOPRA
        soglia_prossima = NESSUNA_SOGLIA_SOPRA
    elif spesa >= SOGLIA_ARGENTO:
        fascia = "ARGENTO"
        sconto = SCONTO_ARGENTO
        fascia_prossima = "ORO"
        soglia_prossima = SOGLIA_ORO
    elif spesa >= SOGLIA_BRONZO:
        fascia = "BRONZO"
        sconto = SCONTO_BRONZO
        fascia_prossima = "ARGENTO"
        soglia_prossima = SOGLIA_ARGENTO
    else:
        fascia = "BASE"
        sconto = SCONTO_BASE
        fascia_prossima = "BRONZO"
        soglia_prossima = SOGLIA_BRONZO

    # TRABOCCHETTO: il risparmio si calcola sulla spesa, non sul totale
    #   già scontato. Chi scrive da_pagare = spesa - spesa * sconto
    #   ottiene lo stesso numero da pagare, ma poi non ha più il
    #   risparmio da stampare e finisce per ricalcolarlo una seconda
    #   volta, con il rischio di usare una percentuale diversa.
    risparmio = spesa * sconto
    da_pagare = spesa - risparmio

    # 4. La stampa, da un punto solo. La larghezza 19 dell'etichetta e
    #    la larghezza 7 del numero tengono in colonna gli importi senza
    #    che nessuno debba contare gli spazi a mano.
    print(RIGA_DOPPIA)
    print("NOVASTORE - CASSA")
    print(RIGA_DOPPIA)
    print(f"{'Spesa:':<19}{spesa:>7.2f} euro")
    print(f"{'Fascia:':<19}{fascia}")
    print(f"{'Sconto applicato:':<19}{sconto:.0%}")
    print(RIGA_SINGOLA)
    print(f"{'Risparmio:':<19}{risparmio:>7.2f} euro")
    print(f"{'Totale da pagare:':<19}{da_pagare:>7.2f} euro")

    # 5. L'unica parte condizionale dello scontrino. `if fascia_prossima:`
    #    è il valore di verità del capitolo 11: una stringa vuota vale
    #    falso, qualunque altra stringa vale vero. Sulla fascia ORO il
    #    nome è vuoto, quindi queste tre righe non vengono eseguite e
    #    la sottrazione non viene nemmeno tentata: sarebbe un numero
    #    negativo da stampare a un cliente che ha già speso il massimo.
    if fascia_prossima:
        mancante = soglia_prossima - spesa
        print(RIGA_SINGOLA)
        print(f"Alla fascia {fascia_prossima} mancano {mancante:.2f} euro.")

    print(RIGA_DOPPIA)


if __name__ == "__main__":
    main()
