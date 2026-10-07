"""
SOLUZIONE — Esercizio 10.1: Le letture dei contatori

IL PROBLEMA
Otto righe, quattro campi ciascuna, e da ognuna tre numeri: il consumo, la
fascia, l'importo. A mano si fa, ma alla prossima bolletta si rifà da capo,
e alla terza si sbaglia una sottrazione. Il programma fa i conti sempre
nello stesso modo, e il giorno che cambia la tariffa si cambia una riga.

LA STRATEGIA: CARICA, CALCOLA, RIPORTA
    leggi_righe_utili(percorso, sep)   P6 + P25  file -> liste di campi puliti
    fascia(valore, soglie, oltre)      P10       numero -> etichetta
    media(valori)                      P15       lista non vuota -> float
    estremi(record, posizione)         P16       record minimo e massimo
    conta_per_chiave(chiavi)           P17       etichetta -> quante volte
    stampa_voce(etichetta, valore)     P2        "Etichetta ...... valore"
    calcola_utenze(righe)              specifica campi -> record completi
    stampa_tabella(utenze)             specifica P3, le colonne di QUESTO caso
    main()                             P1        il regista

COME SI RIUSA
Il file è diviso in zone con un riquadro di commento. La PARTE GENERALE
non sa niente di acqua e di utenze: riceve liste e numeri e restituisce
liste e numeri. La PARTE SPECIFICA sa che la riga ha quattro campi, che il
consumo è una differenza e che le colonne si chiamano UTENZA e FASCIA. Per
il gas si toccano solo le costanti in cima; per i furgoni anche
calcola_utenze() e le intestazioni di stampa_tabella().

LIMITI NOTI
- Il file si suppone pulito: una lettura scritta in lettere ferma il
  programma con ValueError. La validazione riga per riga è il pattern P24
  (esercizio 10.3), qui non serve e appesantirebbe il primo esercizio.
- Una lettura attuale minore della precedente dà un consumo negativo, che
  finisce in fascia BASE senza protestare: è la prima voce di SE HAI
  FINITO PRIMA.

Riprese dai giorni precedenti: lo scheletro con main() e la guardia
(Giorno 01 §13.3, Giorno 06 §13.1); la riga in campi con split() (Giorno 03
§7.2, Giorno 08 §9.1); le soglie in ordine crescente (Giorno 04 §6.1-6.5);
accumulatore e media (Giorno 05 §6.2-6.4); massimo e minimo con chi li
possiede (Giorno 05 §6.5, Giorno 06 §10.5); il contatore con .get()
(Giorno 07 §12.1); la cartella accanto allo script (Giorno 08 §7.1).
"""

from pathlib import Path

# ===== PERCORSI: uguali in tutti gli script della giornata ==================
# La cartella dei dati si calcola a partire da questo file, non dalla
# directory da cui lo lanciate: così il programma trova i dati sia da
# PyCharm sia dal terminale (Giorno 08 §7.1, pattern P25).
DATI = Path(__file__).resolve().parent.parent / "dati"

# ===== PARTE SPECIFICA (1 di 2): le costanti del caso =======================
# Tutto ciò che cambia passando dall'acqua al gas, o ai furgoni, sta qui.
FILE_LETTURE = "letture_contatori.txt"
SEPARATORE = ";"

# Le soglie come DATI e non come catena di elif: la funzione fascia() le
# scorre, e aggiungere una fascia vuol dire aggiungere una tupla. Ordine
# CRESCENTE obbligatorio (vedi il trabocchetto dentro fascia()).
SOGLIE_CONSUMO = [(50, "BASE"), (120, "MEDIA")]
FASCIA_OLTRE = "ALTA"
TARIFFA_M3 = 1.20
UNITA = "mc"

# ===== COSTANTI DI IMPAGINAZIONE: generali ==================================
LARGHEZZA = 60
LARGHEZZA_ETICHETTA = 28
SEGNO_BARRA = "#"


# ===== PARTE GENERALE: si riusa così com'è ==================================
# Nessuna funzione di questa zona nomina l'acqua, le utenze o i metri cubi.
# Se ne trovate una che lo fa, è finita nella zona sbagliata.

def leggi_righe_utili(percorso, separatore):
    """P6 + P25. Restituisce una lista di campi puliti per ogni riga utile.

    Salta le righe vuote e quelle che cominciano con # (commenti).
    """
    righe = []
    with open(percorso, encoding="utf-8") as f:
        for riga in f:
            pulita = riga.strip()
            # TRABOCCHETTO: togliere il controllo sul #. La riga di commento
            #   ha anche lei tre punti e virgola, quindi split() la divide
            #   docilmente in quattro campi e nessuno protesta qui. Il guasto
            #   arriva dopo, alla sottrazione, che converte per primo il
            #   quarto campo (quello a sinistra del meno):
            #   ValueError: invalid literal for int() with base 10:
            #   'lettura_attuale'
            #   Un commento in testa al file è normale: il programma deve
            #   saperlo ignorare, non fermarsi.
            if pulita == "" or pulita.startswith("#"):
                continue
            # Si pulisce ogni CAMPO, non solo la riga: " Rossi Anna " fra
            # due punti e virgola resterebbe con i suoi spazi (Giorno 03
            # §7.5, e il pattern P6).
            campi = []
            for campo in pulita.split(separatore):
                campi.append(campo.strip())
            righe.append(campi)
    return righe


def fascia(valore, soglie, oltre):
    """P10. Restituisce l'etichetta della prima soglia che contiene valore."""
    # La prima soglia che va bene vince, e la funzione esce subito con
    # return: le soglie successive non vengono nemmeno guardate. È la
    # stessa logica della catena if/elif del Giorno 04, scritta come dati.
    #
    # TRABOCCHETTO: scrivere < al posto di <=. Nessun errore, ma le due
    #   utenze sul bordo cambiano fascia in silenzio: VL-004 (50 mc) passa
    #   da BASE a MEDIA e VL-005 (120 mc) da MEDIA ad ALTA. Il conteggio
    #   per fascia diventa BASE 2, MEDIA 3, ALTA 3. Il regolamento dice
    #   "fino a 50": il bordo è incluso.
    #
    # TRABOCCHETTO: le soglie in ordine sbagliato, [(120, "MEDIA"),
    #   (50, "BASE")]. 48 è minore di 120, quindi prende MEDIA prima di
    #   arrivare a BASE: nessuna utenza risulta BASE, e il conteggio esce
    #   BASE 0, MEDIA 6, ALTA 2 (Giorno 04 §6.1).
    for limite, etichetta in soglie:
        if valore <= limite:
            return etichetta
    return oltre


def media(valori):
    """P15. Media aritmetica. Precondizione: valori non è vuota."""
    # Il controllo della lista vuota lo fa chi chiama, che sa che cosa
    # stampare in quel caso: la funzione fa un conto e basta (Giorno 09
    # §8.4, il turno vuoto).
    return sum(valori) / len(valori)


def estremi(record, posizione):
    """P16. Restituisce (record_minimo, record_massimo) sul campo indicato.

    Precondizione: record non è vuota.
    """
    # Si parte dal PRIMO record, non da zero: così il minimo e il massimo
    # sono sempre valori veri della lista, con il loro proprietario
    # attaccato (Giorno 05 §6.5).
    #
    # TRABOCCHETTO: partire da un record finto a consumo zero per il
    #   minimo. Nessun consumo è sotto zero, quindi il confronto < non
    #   scatta mai e il report dice che il consumo minimo è 0 mc,
    #   attribuito a un'utenza che nel file non esiste. Con il massimo lo
    #   stesso difetto si vedrebbe solo su valori tutti negativi, cioè mai
    #   in prova e una volta in produzione.
    minimo = record[0]
    massimo = record[0]
    for attuale in record[1:]:
        if attuale[posizione] < minimo[posizione]:
            minimo = attuale
        if attuale[posizione] > massimo[posizione]:
            massimo = attuale
    # Due valori restituiti insieme: chi chiama li spacchetta nell'ordine
    # scritto qui, minimo prima (Giorno 06 §10.5).
    return minimo, massimo


def conta_per_chiave(chiavi):
    """P17. Restituisce un dizionario chiave -> numero di occorrenze."""
    conteggi = {}
    for chiave in chiavi:
        # .get(chiave, 0) regge la prima volta che una chiave compare:
        # conteggi[chiave] += 1 si fermerebbe con KeyError (Giorno 07 §12.1).
        conteggi[chiave] = conteggi.get(chiave, 0) + 1
    return conteggi


def stampa_voce(etichetta, valore):
    """P2. Stampa 'Etichetta ........ valore' a larghezza fissa."""
    # Il carattere prima di < è il riempitivo: i puntini li mette Python,
    # e le righe restano allineate qualunque sia la lunghezza
    # dell'etichetta (Giorno 03 §9.7). Lo spazio aggiunto all'etichetta
    # separa la parola dal primo puntino.
    print(f"{etichetta + ' ':.<{LARGHEZZA_ETICHETTA}} {valore}")


# ===== PARTE SPECIFICA (2 di 2): calcoli, tabella e regista del caso ========

def calcola_utenze(righe):
    """Da liste di campi a record (codice, nome, consumo, fascia, importo)."""
    utenze = []
    for campi in righe:
        # L'unpacking documenta la riga meglio di campi[2]: quattro nomi
        # per quattro campi, nell'ordine scritto nel commento del file.
        codice, nome, precedente, attuale = campi
        # TRABOCCHETTO: invertire la sottrazione, precedente - attuale.
        #   Nessun errore: tutti i consumi escono negativi, cadono tutti in
        #   fascia BASE (ogni negativo è "fino a 50"), il totale dice -642 e
        #   l'importo -770.40. E il "consumo massimo" diventa VL-006 con
        #   -21, cioè l'utenza che consuma meno. Il contatore conta in
        #   avanti: la lettura nuova meno la vecchia.
        consumo = int(attuale) - int(precedente)
        # round(..., 2) sui soldi: 48 * 1.20 in binario è 57.599999...,
        # e sommando otto importi del genere l'errore si accumula. Lo
        # arrotondiamo dove nasce, al centesimo (Giorno 02 §7.4).
        importo = round(consumo * TARIFFA_M3, 2)
        etichetta = fascia(consumo, SOGLIE_CONSUMO, FASCIA_OLTRE)
        # Un record è una tupla: i cinque campi viaggiano insieme e nessuno
        # li modifica più dopo il calcolo (Giorno 07 §13).
        utenze.append((codice, nome, consumo, etichetta, importo))
    return utenze


def stampa_tabella(utenze):
    """P3. Tabella delle utenze con la riga di totale; restituisce i totali."""
    # Le larghezze sono scelte sul contenuto: il nome più lungo è
    # "Esposito Carla" (14) e sta nei 18 della colonna. I numeri a destra,
    # i testi a sinistra: è così che si confrontano a occhio (Giorno 03 §9.1).
    print(f"{'UTENZA':<8}{'INTESTATARIO':<18}{'CONSUMO':>8}  "
          f"{'FASCIA':<8}{'IMPORTO':>12}")
    totale_consumo = 0
    totale_importi = 0
    for codice, nome, consumo, etichetta, importo in utenze:
        print(f"{codice:<8}{nome:<18}{consumo:>8}  {etichetta:<8}{importo:>12.2f}")
        totale_consumo += consumo
        totale_importi += importo
    print("-" * LARGHEZZA)
    # La riga di totale usa le STESSE larghezze della tabella: 8 + 18 per
    # le due colonne di testo unite, 8 per il consumo, 2 + 8 vuoti per la
    # fascia, 12 per l'importo. Così i totali cadono sotto le loro colonne.
    print(f"{'TOTALE':<26}{totale_consumo:>8}  {'':<8}{totale_importi:>12.2f}")
    return totale_consumo, totale_importi


def main():
    """Carica le letture, calcola i consumi e stampa il report."""
    print("=" * LARGHEZZA)
    print("ACQUEDOTTO DI VILLANOVA - Consumi del periodo")
    print("=" * LARGHEZZA)

    # --- 1. Carica ---------------------------------------------------------
    percorso = DATI / FILE_LETTURE
    # Prevenzione, non gestione: se il file non c'è lo diciamo con parole
    # nostre e usciamo, invece di lasciare un traceback (Giorno 08 §8.1).
    # Si stampa .name e non il percorso intero, che cambia da macchina a
    # macchina.
    if not percorso.exists():
        print(f"[ERRORE] File non trovato: {percorso.name}")
        return
    righe = leggi_righe_utili(percorso, SEPARATORE)
    utenze = calcola_utenze(righe)
    print(f"File letto: {percorso.name} ({len(utenze)} utenze)")
    print("-" * LARGHEZZA)

    if len(utenze) == 0:
        # Senza questo ramo, media() dividerebbe per zero ed estremi()
        # cercherebbe utenze[0] in una lista vuota: meglio dirlo prima.
        print("[!] Nessuna utenza nel file: niente da calcolare.")
        print("=" * LARGHEZZA)
        return

    # --- 2. Tabella --------------------------------------------------------
    stampa_tabella(utenze)
    print("-" * LARGHEZZA)

    # --- 3. Media, massimo, minimo -----------------------------------------
    consumi = []
    for utenza in utenze:
        consumi.append(utenza[2])
    # TRABOCCHETTO: dividere per il numero di righe del FILE invece che per
    #   il numero di utenze. Le righe sono 9, commento compreso, e la media
    #   esce 71.33 invece di 80.25: nessun errore, solo un numero più
    #   basso del vero. Il denominatore è quante cose avete sommato, non
    #   quante righe avete letto.
    consumo_medio = media(consumi)
    stampa_voce("Consumo medio", f"{consumo_medio:.2f} {UNITA}")

    # 2 è la posizione del consumo nel record: estremi() è generale e
    # confronta il campo che le dite voi.
    minimo, massimo = estremi(utenze, 2)
    stampa_voce("Consumo massimo",
                f"{massimo[2]} {UNITA} ({massimo[0]} {massimo[1]})")
    stampa_voce("Consumo minimo",
                f"{minimo[2]} {UNITA} ({minimo[0]} {minimo[1]})")
    print("-" * LARGHEZZA)

    # --- 4. Utenze per fascia (requisito promosso) -------------------------
    etichette = []
    for utenza in utenze:
        etichette.append(utenza[3])
    conteggi = conta_per_chiave(etichette)
    # Le fasce si scorrono dalla COSTANTE, non dal dizionario dei conteggi:
    # così escono sempre nell'ordine BASE, MEDIA, ALTA, e una fascia senza
    # utenze compare con 0 invece di sparire dal report.
    fasce_ordinate = []
    for soglia in SOGLIE_CONSUMO:
        # soglia è la coppia (limite, etichetta): serve solo l'etichetta.
        fasce_ordinate.append(soglia[1])
    fasce_ordinate.append(FASCIA_OLTRE)
    print("UTENZE PER FASCIA")
    for etichetta in fasce_ordinate:
        quante = conteggi.get(etichetta, 0)
        print(f"{etichetta:<10}{quante:>3}  {SEGNO_BARRA * quante}")
    print("-" * LARGHEZZA)

    # --- 5. Sopra la media (requisito promosso) ----------------------------
    # Un filtro (P20 in piccolo): si tengono i codici, non i record, perché
    # la riga finale li elenca e basta.
    sopra = []
    for utenza in utenze:
        # > e non >=: "più della media". Su questi dati nessuno è
        # esattamente a 80.25, ma la regola va scritta com'è detta.
        if utenza[2] > consumo_medio:
            sopra.append(utenza[0])
    print(f"Sopra la media: {len(sopra)} utenze ({', '.join(sopra)})")
    print("=" * LARGHEZZA)


if __name__ == "__main__":
    main()
