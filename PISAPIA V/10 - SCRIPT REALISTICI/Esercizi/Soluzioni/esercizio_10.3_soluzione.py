"""
SOLUZIONE — Esercizio 10.3: Le note spese del trimestre

IL PROBLEMA
Dodici note, scritte a mano da un consulente: importi con la virgola, una
categoria in minuscolo, una riga vuota lasciata per sbaglio, una nota senza
descrizione, una categoria che non esiste. Due domande diverse sullo stesso
file: QUANTO si è speso (tutto il presentato, per categoria) e QUANTO si
rimborsa (ogni nota fino al suo tetto). La seconda non si ricava dalla
prima: una categoria può stare sotto il tetto in media e sforarlo con una
nota sola.

LA STRATEGIA: CARICA, VALIDA, AGGREGA, RIPORTA
    conta_righe(percorso)          P26  quante righe ha il file, vuote comprese
    carica_righe(percorso)         P26  [(numero_riga, campi), ...] utili
    normalizza_codice(testo)       P4   " vitto " -> "VITTO"
    converti_importo(testo)        P5   "85,40" -> 85.4, oppure ValueError
    conta_per_chiave(chiavi)       P17  categoria -> numero di note
    somma_per_chiave(coppie)       P18  categoria -> importo
    barra(quota)                   P18  0.447 -> "##################"
    stampa_voce(etichetta, valore) P2
    valida_nota(campi, tetti)      P24  specifica: (record, "") o (None, motivo)
    main()                         P20  partiziona in buone e scarti, poi riporta

COME SI RIUSA
La PARTE GENERALE legge righe, converte importi, conta e somma per chiave:
non sa che cosa sia una nota spese. La PARTE SPECIFICA sa quali sono i
quattro campi, quali categorie esistono (le chiavi di TETTI) e che cosa
vuol dire "sopra il tetto". Per gli acquisti di un ufficio contro il budget
si cambiano TETTI, valida_nota() e i titoli delle colonne.

LIMITI NOTI
- Il codice della nota non si controlla: due note SP04 passerebbero
  entrambe. I doppioni sono il pattern P21, qui fuori perimetro.
- Il tetto è per singola nota. Un tetto sul totale della categoria è la
  seconda voce di SE HAI FINITO PRIMA.

Riprese dai giorni precedenti: il numero all'italiana (Giorno 02 §7.3,
Giorno 03 §5.4); split e unpacking dopo il controllo dei campi (Giorno 03
§7.3-7.4, Giorno 08 §9.2); il contatore e la somma per chiave con .get()
(Giorno 07 §12.1-12.4); la funzione che restituisce record oppure motivo
(Giorno 06 §10.1-10.2, Giorno 08 §9.4); la riga di numero dell'editor e
l'invariante dei conteggi (Giorno 08 §5.3, Giorno 09 §14.4); la quota con
:.1% e la barra (Giorno 02 §13.3, Giorno 07 §14.2).
"""

from pathlib import Path

# ===== PERCORSI: uguali in tutti gli script della giornata ==================
DATI = Path(__file__).resolve().parent.parent / "dati"

# ===== PARTE SPECIFICA (1 di 2): le costanti del caso =======================
FILE_NOTE = "note_spese.txt"
SEPARATORE = ";"
NUMERO_CAMPI = 4
# Le chiavi di TETTI sono ANCHE l'elenco delle categorie ammesse e l'ordine
# in cui escono nel report: un dizionario solo fa tre lavori, e aggiungere
# una categoria vuol dire aggiungere una riga qui.
TETTI = {"VIAGGIO": 200.00, "VITTO": 30.00, "ALLOGGIO": 120.00,
         "MATERIALE": 50.00}
TITOLO = "TALENTHUB - Note spese del trimestre"

# ===== COSTANTI DI IMPAGINAZIONE: generali ==================================
LARGHEZZA = 60
LARGHEZZA_BARRA = 40
LARGHEZZA_ETICHETTA = 28
SEGNO_BARRA = "#"


# ===== PARTE GENERALE: si riusa così com'è ==================================

def conta_righe(percorso):
    """P26. Numero di righe del file, vuote comprese."""
    quante = 0
    with open(percorso, encoding="utf-8") as f:
        # La variabile del ciclo non serve: si conta e basta. Anche la riga
        # vuota è una riga, ed è proprio quella che vogliamo contare.
        for riga in f:
            quante += 1
    return quante


def carica_righe(percorso):
    """P26. Restituisce [(numero_riga, campi), ...] per le sole righe utili.

    Il numero è quello che mostra l'editor; le righe vuote e quelle che
    cominciano con # si saltano ma si contano. Ogni campo è ripulito dagli
    spazi ai bordi.
    """
    righe = []
    with open(percorso, encoding="utf-8") as f:
        # TRABOCCHETTO: contare le righe con un contatore proprio,
        #   incrementato solo sulle righe utili. La riga vuota (la 6) non
        #   viene contata e da lì in poi ogni numero è indietro di uno: il
        #   report dice "riga 6 scartata: importo non numerico: 'trenta'", e
        #   chi apre l'editor alla riga 6 trova una riga vuota. enumerate()
        #   conta TUTTE le righe, dalla prima, come l'editor (Giorno 08 §5.3).
        for numero, riga in enumerate(f, start=1):
            pulita = riga.strip()
            if pulita == "" or pulita.startswith("#"):
                continue
            campi = []
            for campo in pulita.split(SEPARATORE):
                campi.append(campo.strip())
            righe.append((numero, campi))
    return righe


def normalizza_codice(testo):
    """P4. Toglie gli spazi ai bordi e porta in maiuscolo."""
    return testo.strip().upper()


def converti_importo(testo):
    """P5. Da testo (anche con la virgola) a float; solleva ValueError."""
    pulito = testo.strip()
    # TRABOCCHETTO: passare il testo a float() senza la riparazione della
    #   virgola. float("85,40") solleva ValueError, e con lui TUTTE le
    #   note, perché nel file ogni importo ha la virgola. Il report dice
    #   Note buone ................. 0
    #   Note scartate .............. 12
    #   e nessuna categoria. Il dato non è sbagliato: è scritto
    #   all'italiana, e va riparato, non rifiutato (Giorno 03 §5.4).
    if "," in pulito:
        pulito = pulito.replace(".", "").replace(",", ".")
    try:
        return float(pulito)
    except ValueError:
        raise ValueError(f"importo non numerico: '{testo}'")


def conta_per_chiave(chiavi):
    """P17. Restituisce un dizionario chiave -> numero di occorrenze."""
    conteggi = {}
    for chiave in chiavi:
        conteggi[chiave] = conteggi.get(chiave, 0) + 1
    return conteggi


def somma_per_chiave(coppie):
    """P18. Da coppie (chiave, importo) a un dizionario chiave -> somma."""
    somme = {}
    for chiave, importo in coppie:
        # TRABOCCHETTO: lasciare l'importo stringa, cioè saltare la
        #   conversione nel validatore. Qui non ci si arriva: il programma
        #   si ferma prima, nel validatore stesso, al controllo importo <= 0:
        #   TypeError: '<=' not supported between instances of 'str' and 'int'
        #   Senza quel controllo si fermerebbe in main(), a totale += importo,
        #   ancora prima di questa somma. Il difetto nasce nel validatore:
        #   un record deve uscire dalla validazione con i tipi giusti.
        somme[chiave] = somme.get(chiave, 0) + importo
    return somme


def barra(quota):
    """P18. Una barra di # proporzionale alla quota (fra 0 e 1)."""
    # round() e non int(): int() tronca, e ogni barra perde un segno.
    #
    # TRABOCCHETTO: int(quota * LARGHEZZA_BARRA). Nessun errore, ma le
    #   barre escono di 10, 6, 17 e 4 segni invece di 11, 7, 18 e 5. E una
    #   categoria al 2% (0.02 x 40 = 0.8) sparirebbe del tutto: int(0.8)
    #   vale 0, round(0.8) vale 1. Arrotondare è la regola onesta.
    return SEGNO_BARRA * round(quota * LARGHEZZA_BARRA)


def stampa_voce(etichetta, valore):
    """P2. Stampa 'Etichetta ........ valore' a larghezza fissa."""
    print(f"{etichetta + ' ':.<{LARGHEZZA_ETICHETTA}} {valore}")


# ===== PARTE SPECIFICA (2 di 2): il validatore, il report e il regista ======

def valida_nota(campi, tetti):
    """P24. Restituisce ((codice, categoria, importo, descrizione), "")
    oppure (None, motivo). Non stampa niente.
    """
    # L'ordine dei controlli è una decisione: prima quanti campi ci sono
    # (senza, l'unpacking si ferma), poi la categoria, poi l'importo. Una
    # riga con due difetti viene scartata per il primo, sempre lo stesso.
    if len(campi) != NUMERO_CAMPI:
        return None, f"servono {NUMERO_CAMPI} campi, ne ha {len(campi)}"

    codice, categoria, testo_importo, descrizione = campi

    # TRABOCCHETTO: dimenticare la normalizzazione della categoria. "VITTO"
    #   passa, "vitto" no: SP03 e SP12 vengono scartate con
    #   categoria non ammessa: 'vitto'
    #   le note buone scendono a 7 e VITTO resta con una nota sola, 38.00.
    #   Due note regolari respinte per una lettera maiuscola.
    categoria = normalizza_codice(categoria)
    if categoria not in tetti:
        return None, f"categoria non ammessa: '{categoria}'"

    # Il try sta QUI e abbraccia una riga: la conversione. La funzione
    # generale solleva, il validatore traduce l'eccezione in un motivo, e il
    # ciclo del main() non vede mai un'eccezione (Giorno 09 §12.3).
    try:
        importo = converti_importo(testo_importo)
    except ValueError as e:
        return None, str(e)
    if importo <= 0:
        return None, f"importo non positivo: {importo:.2f}"

    return (codice, categoria, importo, descrizione), ""


def stampa_per_categoria(conteggi, somme, totale):
    """Tabella per categoria nell'ordine di TETTI, con quota e barra."""
    print(f"{'CATEGORIA':<10}{'NOTE':>5}{'IMPORTO':>11}{'QUOTA':>8}")
    for categoria in TETTI:
        note = conteggi.get(categoria, 0)
        importo = somme.get(categoria, 0)
        # La quota si calcola QUI, a totale completo. Dentro il ciclo di
        # lettura il totale sarebbe parziale e le quote sommerebbero ben
        # oltre il 100% (Giorno 07 §12.4).
        quota = importo / totale
        # :.1% moltiplica da solo per 100 e aggiunge il simbolo: gli si
        # passa la FRAZIONE, 0.447, non 44.7 (Giorno 02 §13.3).
        print(f"{categoria:<10}{note:>5}{importo:>11.2f}{quota:>8.1%}  "
              f"{barra(quota)}")


def main():
    """Carica le note, le valida, aggrega e stampa il rimborso."""
    print("=" * LARGHEZZA)
    print(TITOLO)
    print("=" * LARGHEZZA)

    percorso = DATI / FILE_NOTE
    if not percorso.exists():
        print(f"[ERRORE] File non trovato: {percorso.name}")
        return
    print(f"File letto: {percorso.name}")

    # --- 1. Carica ---------------------------------------------------------
    righe_file = conta_righe(percorso)
    righe = carica_righe(percorso)

    # --- 2. Valida: le buone da una parte, gli scarti con il motivo --------
    # Il pattern P20: due liste, nessuna riga persa. Lo scarto si stampa
    # subito, con il numero dell'editor, così chi corregge sa dove andare.
    buone = []
    scartate = 0
    for numero, campi in righe:
        record, motivo = valida_nota(campi, TETTI)
        if record is None:
            scartate += 1
            print(f"[!] riga {numero} scartata: {motivo}")
        else:
            buone.append(record)
    print("-" * LARGHEZZA)

    stampa_voce("Righe del file", righe_file)
    stampa_voce("Righe vuote", righe_file - len(righe))
    stampa_voce("Note buone", len(buone))
    stampa_voce("Note scartate", scartate)
    print("-" * LARGHEZZA)

    if len(buone) == 0:
        # Senza note buone il totale è zero e ogni quota dividerebbe per
        # zero: si dice e si chiude, invece di fermarsi con un traceback.
        print("[!] Nessuna nota valida: niente da rimborsare.")
        print("=" * LARGHEZZA)
        return

    # --- 3. Aggrega (requisito promosso: quota e barra) --------------------
    categorie = []
    coppie = []
    totale = 0
    for codice, categoria, importo, descrizione in buone:
        categorie.append(categoria)
        coppie.append((categoria, importo))
        totale += importo
    stampa_per_categoria(conta_per_chiave(categorie), somma_per_chiave(coppie),
                         totale)
    print("-" * LARGHEZZA)

    # --- 4. Il tetto, nota per nota (requisito promosso) -------------------
    print("NOTE SOPRA IL TETTO")
    eccedenze = 0
    for codice, categoria, importo, descrizione in buone:
        # Qui le quadre sono lecite: la categoria è già passata dal
        # validatore, quindi è di sicuro una chiave di TETTI.
        tetto = TETTI[categoria]
        # TRABOCCHETTO: >= al posto di >. SP12, VITTO 30.00, è esattamente
        #   sul tetto e comparirebbe nell'elenco con "eccedenza 0.00": il
        #   totale non cambia, ma l'amministrazione vede tre note sopra il
        #   tetto invece di due e ne contesta una regolare. "Fino a 30"
        #   comprende 30.
        if importo > tetto:
            eccedenza = importo - tetto
            eccedenze += eccedenza
            print(f"{codice:<6}{categoria:<12}{importo:>9.2f}  tetto "
                  f"{tetto:>7.2f}  eccedenza {eccedenza:>7.2f}")
    print("-" * LARGHEZZA)

    # --- 5. Il conto finale ------------------------------------------------
    stampa_voce("Totale presentato", f"{totale:.2f}")
    stampa_voce("Eccedenze", f"{eccedenze:.2f}")
    stampa_voce("Rimborsabile", f"{totale - eccedenze:.2f}")
    print("-" * LARGHEZZA)

    # --- 6. L'invariante ---------------------------------------------------
    # assert controlla il PROGRAMMA: se scatta, una riga si è persa per
    # strada fra la lettura e la partizione, e il difetto è nel codice, non
    # nel file (Giorno 09 §14.4).
    utili = len(righe)
    assert utili == len(buone) + scartate, (
        f"righe utili {utili}, ma buone + scartate fa {len(buone) + scartate}"
    )
    print(f"[OK] {utili} righe utili = {len(buone)} buone + {scartate} scartate")
    print("=" * LARGHEZZA)


if __name__ == "__main__":
    main()
