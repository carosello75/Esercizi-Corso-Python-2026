"""
SOLUZIONE — Esercizio 04.4: Riparare la cassa

La strategia è la validazione preventiva: si controlla il testo PRIMA
di convertirlo, così la conversione non può fallire. È la prima linea
di difesa e con gli strumenti di oggi è anche l'unica.

I controlli sono divisi in due gruppi. Prima quelli sulla forma del
dato (è un numero? è una risposta ammessa?), che si fanno sul testo.
Poi quelli sul merito (è un numero sensato?), che hanno bisogno del
valore convertito. Il messaggio d'errore viene messo da parte in una
variabile e stampato in un punto solo: così la coda del programma è
identica in tutti i casi, e aggiungere un controllo costa due righe.

La tessera fedeltà non aggiunge un secondo calcolo: aggiunge una
percentuale, che senza tessera vale zero. Un calcolo solo, e lo
scontrino dice sempre la percentuale che ha davvero applicato.
"""

ALIQUOTA_IVA = 0.22
SCONTO_TESSERA = 0.05
NESSUNO_SCONTO = 0.00
QUANTITA_MASSIMA = 100

# Le due sole risposte ammesse alla domanda sulla tessera. Stanno in
# costante perché compaiono tre volte: nei due confronti del controllo
# e nel confronto che decide lo sconto.
RISPOSTA_SI = "si"
RISPOSTA_NO = "no"

LARGHEZZA_SCONTRINO = 50
RIGA_DOPPIA = "=" * LARGHEZZA_SCONTRINO
RIGA_SINGOLA = "-" * LARGHEZZA_SCONTRINO


def main():
    """Calcola lo scontrino solo se i quattro dati inseriti sono validi."""
    # 1. Lettura: tutto arriva come testo e resta testo. Niente int() e
    #    niente float() in questa parte del programma, per scelta.
    #    .replace(",", ".") normalizza la virgola decimale italiana,
    #    .strip() toglie gli spazi che la cassiera non vede.
    testo_prezzo = input("Prezzo unitario in euro: ").strip()
    testo_prezzo = testo_prezzo.replace(",", ".")
    testo_quantita = input("Quantità: ").strip()
    risposta_tessera = input("Tessera fedeltà? (si/no): ").strip().lower()
    testo_contanti = input("Contanti ricevuti in euro: ").strip()
    testo_contanti = testo_contanti.replace(",", ".")

    # TRABOCCHETTO: .isdecimal() dice di no a qualunque cosa non sia
    #   solo cifre, e il punto decimale è "qualunque cosa". Il trucco è
    #   toglierne uno solo — il terzo argomento di replace è il numero
    #   massimo di sostituzioni — e guardare cosa resta:
    #     "12.90"    ->  "1290"     (str)  solo cifre: era un numero
    #     "12.9.0"   ->  "129.0"    (str)  resta un punto: rifiutato
    #   Le due variabili non servono ai calcoli: servono solo a essere
    #   interrogate. Il dato su cui si calcola resta testo_prezzo.
    cifre_prezzo = testo_prezzo.replace(".", "", 1)
    cifre_contanti = testo_contanti.replace(".", "", 1)

    # 2. La variabile che raccoglie l'esito dei controlli. Parte vuota,
    #    cioè "nessun errore finora", e vuota resta se tutto va bene.
    errore = ""

    print(RIGA_DOPPIA)
    print("NOVASTORE - CASSA")
    print(RIGA_DOPPIA)

    # TRABOCCHETTO: il controllo sulla tessera nega un elenco di valori
    #   ammessi, e negare un OPPURE ribalta l'operatore. La risposta è
    #   buona se vale si OPPURE no; quindi è cattiva se non vale si E
    #   non vale no. Chi scrive
    #       elif risposta_tessera != RISPOSTA_SI or risposta_tessera != RISPOSTA_NO:
    #   ottiene una condizione sempre vera — "si" è diverso da "no" —
    #   e la cassa rifiuta ogni scontrino, anche quelli giusti.
    if not cifre_prezzo.isdecimal():
        errore = "Il prezzo deve essere un numero, per esempio 12,90."
    elif not testo_quantita.isdecimal():
        errore = "La quantità deve essere un numero intero, senza decimali."
    elif risposta_tessera != RISPOSTA_SI and risposta_tessera != RISPOSTA_NO:
        errore = "La tessera va indicata con si oppure no, per esteso."
    elif not cifre_contanti.isdecimal():
        errore = "I contanti devono essere un numero, per esempio 50,00."
    else:
        # TRABOCCHETTO: la conversione sta qui dentro, non in cima al
        #   programma. Chi converte subito e valida dopo ha già perso:
        #   il programma si ferma sulla riga di float() e il controllo
        #   scritto tre righe più sotto non viene mai eseguito.
        #   L'ordine non è uno stile, è la differenza fra un messaggio
        #   d'errore e un crash davanti al cliente.
        prezzo = float(testo_prezzo)
        quantita = int(testo_quantita)
        contanti = float(testo_contanti)

        # 3. La tessera decide una percentuale, non un calcolo a parte.
        #    Senza tessera la percentuale è zero, la moltiplicazione dà
        #    zero e lo scontrino resta identico nella forma.
        #      risposta_tessera  ->  "si"   (str)
        #      ha_tessera        ->  True   (bool)
        ha_tessera = risposta_tessera == RISPOSTA_SI
        if ha_tessera:
            percentuale_applicata = SCONTO_TESSERA
        else:
            percentuale_applicata = NESSUNO_SCONTO

        # 4. I calcoli, nell'ordine in cui li fa la legge: lo sconto
        #    abbassa l'imponibile, e l'IVA si applica su quello che
        #    resta. Invertire i due passaggi cambia il totale.
        imponibile = prezzo * quantita
        sconto_tessera = imponibile * percentuale_applicata
        imponibile_netto = imponibile - sconto_tessera
        iva = imponibile_netto * ALIQUOTA_IVA
        totale = imponibile_netto + iva
        resto = contanti - totale

        # 5. I controlli di merito: qui i dati sono già numeri, e la
        #    domanda non è più "è un numero?" ma "è un numero che alla
        #    cassa ha senso?". Il confronto == 0 sulla quantità basta
        #    perché .isdecimal() ha già escluso i negativi: "-5" non è
        #    fatto di sole cifre e non è arrivato fin qui.
        if prezzo <= 0:
            errore = "Il prezzo deve essere maggiore di zero."
        elif quantita == 0:
            errore = "La quantità deve essere almeno 1 pezzo."
        elif quantita > QUANTITA_MASSIMA:
            errore = f"Massimo {QUANTITA_MASSIMA} pezzi per scontrino."
        elif contanti < totale:
            errore = f"Contanti insufficienti: servono {totale:.2f} euro."
        else:
            # Le due etichette si costruiscono dalle percentuali che il
            # programma ha usato davvero: se domani l'aliquota cambia,
            # o se la tessera non c'è, cambia anche quello che si legge
            # sullo scontrino, senza toccare due punti diversi.
            etichetta_sconto = f"Sconto tessera {percentuale_applicata:.0%}:"
            etichetta_iva = f"IVA {ALIQUOTA_IVA:.0%}:"
            print(f"{'Prezzo unitario:':<20}{prezzo:>5.2f} euro")
            print(f"{'Quantità:':<20}{quantita:>5}")
            print(f"{'Imponibile:':<20}{imponibile:>5.2f} euro")
            print(f"{etichetta_sconto:<20}{sconto_tessera:>5.2f} euro")
            print(f"{'Imponibile netto:':<20}{imponibile_netto:>5.2f} euro")
            print(f"{etichetta_iva:<20}{iva:>5.2f} euro")
            print(RIGA_SINGOLA)
            print(f"{'Totale:':<20}{totale:>5.2f} euro")
            print(f"{'Contanti:':<20}{contanti:>5.2f} euro")
            print(f"{'Resto:':<20}{resto:>5.2f} euro")
            print("Scontrino emesso. Grazie e arrivederci.")

    # 6. Un solo punto di uscita per gli errori. `if errore:` è vero
    #    quando la stringa non è vuota: è il valore di verità del
    #    capitolo 11, e qui evita di scrivere otto volte le stesse due
    #    righe, una per ogni controllo.
    if errore:
        print(f"[ERRORE] {errore}")
        print("Nessuno scontrino emesso. Ripetere l'operazione.")

    print(RIGA_DOPPIA)


if __name__ == "__main__":
    main()
