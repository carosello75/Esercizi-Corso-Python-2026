"""
SOLUZIONE — Esercizio per casa 10.1: Il listino aggiornato

IL PROBLEMA
Dieci righe di listino con i prezzi all'italiana, un aumento diverso per
categoria, una categoria che non ha aumento e una riga illeggibile. Serve
il nuovo listino nello stesso formato del vecchio, così il prossimo
aumento si fa con lo stesso programma, rileggendo il file che esce oggi.

LA STRATEGIA: SETTE PATTERN DEL CATALOGO
- P26 il caricatore: righe utili con il numero dell'editor, commenti e
  righe vuote saltati. Non sa niente di prezzi: si riusa così com'è.
- P6 la riga in campi, P4 la normalizzazione della categoria.
- P5 il numero all'italiana, in andata (converti_importo) e in ritorno
  (formato_italiano): il file che esce deve rientrare nel caricatore.
- P12 la tabella di decisione: il dizionario AUMENTI dice di quanto sale
  ogni categoria. Qui con in, non con .get(): vedi il TRABOCCHETTO.
- P15 totale, conteggio e media, con il caso zero articoli.
- P28 il report composto una volta come lista di righe: la stessa
  stampa_righe() lo manda a video o su file.

COME È DIVISO IL FILE
Due zone, separate da un riquadro. La PARTE GENERALE contiene i pezzi del
catalogo con le firme della teoria: si copiano in un altro programma senza
toccarli. La PARTE SPECIFICA contiene ciò che sa di NovaStore: costanti,
validatore, composizione della tabella e del file, main(). Per un altro
caso si riscrive solo la seconda.

LIMITI NOTI DI QUESTA SOLUZIONE
- converti_importo() accetta anche "1e3" e "nan", perché li accetta
  float(). Un listino scritto da una persona non li contiene; un listino
  generato da un altro programma potrebbe, e allora serve un controllo di
  forma in più (P7).
- L'aumento si arrotonda articolo per articolo, come fa una cassa. Il
  totale nuovo è quindi la somma dei prezzi arrotondati, non il totale
  vecchio per un fattore medio: sono due numeri diversi, ed è giusto così.
- La riga scartata non finisce nel nuovo listino: senza un prezzo leggibile
  non c'è niente da aumentare. Va corretta a mano nel file di partenza.
"""

from pathlib import Path

# --- Costanti ------------------------------------------------------------
# La soluzione sta in esercizi_casa/soluzioni/, un livello più in basso
# della traccia: servono TRE .parent per arrivare a giorno_10/ (P25,
# Giorno 08 §7.3). Il .resolve() rende il percorso indipendente dalla
# cartella da cui si lancia il programma.
CARTELLA_GIORNO = Path(__file__).resolve().parent.parent.parent
DATI = CARTELLA_GIORNO / "dati"
OUTPUT = CARTELLA_GIORNO / "output"
FILE_LISTINO = DATI / "listino_novastore.txt"
FILE_AGGIORNATO = OUTPUT / "listino_aggiornato.txt"

SEPARATORE = ";"
COMMENTO = "#"
CAMPI_ATTESI = 4
LARGHEZZA = 60
LARGHEZZA_ETICHETTA = 27

# Larghezze delle colonne della tabella: la somma fa LARGHEZZA (P3).
COLONNA_CODICE = 8
COLONNA_DESCRIZIONE = 20
COLONNA_CATEGORIA = 14
COLONNA_PREZZO = 9

# Percentuali di aumento per categoria. È la tabella di decisione del P12:
# a ogni categoria corrisponde un numero fisso.
AUMENTI = {"AUDIO": 3, "VIDEO": 5, "ACCESSORI": 10, "INFORMATICA": 2}
CENTESIMI = 2
PER_CENTO = 100

INTESTAZIONE_FILE = "# NovaStore - codice;descrizione;categoria;prezzo"
TITOLO = "NOVASTORE - Listino aggiornato"
SEGNO_INVARIATO = " [!]"


# =========================================================================
# ===== PARTE GENERALE: si riusa così com'è ===============================
# =========================================================================

# P4 — Normalizzare un codice: spazi ai bordi via, tutto maiuscolo.
# È il primo gesto prima di ogni confronto con una chiave di dizionario
# (Giorno 03 §5.2): " audio" e "AUDIO" devono essere la stessa categoria.
def normalizza_codice(testo):
    """Restituisce il testo senza spazi ai bordi e in maiuscolo."""
    return testo.strip().upper()


# P5 — Il numero scritto all'italiana, in andata.
def converti_importo(testo):
    """Converte '1.250,00', '12,50' o '12.50' in float, o solleva ValueError."""
    pulito = testo.strip()
    # La regola dello schema: SOLO se c'è la virgola i punti sono migliaia.
    # TRABOCCHETTO: togliete i punti sempre, anche senza virgola, e "12.50"
    #   diventa 1250.0 senza nessun errore. In questo file non si vede,
    #   perché tutti i prezzi hanno la virgola; si vede il giorno in cui
    #   rileggete un listino scritto con il punto, e un cavo da 9.90 esce a
    #   990.00.
    if "," in pulito:
        pulito = pulito.replace(".", "").replace(",", ".")
    # Il try è stretto a una riga sola, la conversione (P8, Giorno 09
    # §8.3): tutto ciò che sta sopra non può sollevare, tutto ciò che sta
    # sotto è un altro mestiere.
    try:
        return float(pulito)
    except ValueError:
        raise ValueError(f"importo non numerico: '{testo.strip()}'")


# P5 — Il numero scritto all'italiana, al ritorno.
def formato_italiano(importo):
    """Restituisce l'importo con due decimali e la virgola: 51.4 -> '51,40'."""
    # Prima si formatta con il punto (f-string del Giorno 02 §13.2), poi
    # si scambia il simbolo: l'ordine conta, perché il formato .2f produce
    # sempre il punto.
    return f"{importo:.2f}".replace(".", ",")


# P26 — Il caricatore: righe utili con il numero di riga dell'editor.
def carica_righe(percorso):
    """Restituisce [(numero_riga, campi), ...], senza righe vuote né commenti."""
    righe_utili = []
    with open(percorso, encoding="utf-8") as ingresso:
        # TRABOCCHETTO: con enumerate(ingresso) senza start=1 la numerazione
        #   parte da 0 e ogni messaggio indica la riga PRIMA di quella vera:
        #   la categoria senza aumento esce come "riga  8", e chi apre
        #   l'editor alla riga 8 trova la tastiera meccanica, che è giusta.
        for numero, riga in enumerate(ingresso, start=1):
            testo = riga.strip()
            if testo == "" or testo.startswith(COMMENTO):
                continue
            # P6: si pulisce OGNI campo, non la riga intera. strip() sulla
            # riga toglie gli spazi ai bordi della riga, non quelli attorno
            # ai punti e virgola (Giorno 03 §7.5).
            campi = []
            for campo in testo.split(SEPARATORE):
                campi.append(campo.strip())
            righe_utili.append((numero, campi))
    return righe_utili


# P15 — La media, con una precondizione dichiarata.
def media(valori):
    """Media di una lista NON vuota: il controllo del caso zero è del chiamante."""
    return sum(valori) / len(valori)


# P28 — Mandare una lista di righe a video o su file, con lo stesso codice.
def stampa_righe(righe, file=None):
    """Stampa le righe a video (file=None) o dentro un file già aperto."""
    # print(..., file=None) scrive sullo schermo: è il valore predefinito
    # di print() stesso (Giorno 08 §6.3). Per questo una sola funzione
    # basta per le due destinazioni, e il report a video e quello su file
    # non possono divergere.
    for riga in righe:
        print(riga, file=file)


def riga_puntini(etichetta, valore):
    """P2 — 'Etichetta ........ valore', con i valori in colonna."""
    # Il carattere prima di < riempie lo spazio: niente puntini contati a
    # mano (Giorno 03 §9.7).
    return f"{etichetta + ' ':.<{LARGHEZZA_ETICHETTA}} {valore}"


# =========================================================================
# ===== PARTE SPECIFICA: si cambia per un altro caso ======================
# =========================================================================

def valida_articolo(campi):
    """Restituisce ((codice, descrizione, categoria, prezzo), '') o (None, motivo)."""
    # Prima il numero dei campi, POI l'unpacking: con tre campi l'unpacking
    # si fermerebbe con un ValueError il cui testo cambia fra le versioni
    # di Python. Il nostro messaggio dice quanti campi ci sono.
    if len(campi) != CAMPI_ATTESI:
        return None, f"servono {CAMPI_ATTESI} campi, ne ha {len(campi)}"
    codice, descrizione, categoria, testo_prezzo = campi
    codice = normalizza_codice(codice)
    categoria = normalizza_codice(categoria)
    try:
        prezzo = converti_importo(testo_prezzo)
    except ValueError as errore:
        # Il messaggio lo ha già scritto converti_importo(): qui si limita
        # a trasformare l'eccezione in un motivo di scarto (forma P24).
        return None, str(errore)
    return (codice, descrizione, categoria, prezzo), ""


def nuovo_prezzo(prezzo, percentuale):
    """Applica l'aumento percentuale e arrotonda ai centesimi."""
    # TRABOCCHETTO: scritto prezzo * (1 + percentuale), senza dividere per
    #   100, un aumento del 5% diventa un aumento del 500%: il monitor da
    #   159.00 esce a 954.00. Nessun errore, solo un listino che nessuno
    #   firmerebbe.
    return round(prezzo * (1 + percentuale / PER_CENTO), CENTESIMI)


def componi_tabella(articoli):
    """Restituisce le righe della tabella vecchio/nuovo, con i totali."""
    righe = []
    righe.append(
        f"{'CODICE':<{COLONNA_CODICE}}{'DESCRIZIONE':<{COLONNA_DESCRIZIONE}}"
        f"{'CATEGORIA':<{COLONNA_CATEGORIA}}{'VECCHIO':>{COLONNA_PREZZO}}"
        f"{'NUOVO':>{COLONNA_PREZZO}}"
    )
    totale_vecchio = 0.0
    totale_nuovo = 0.0
    for codice, descrizione, categoria, vecchio, nuovo, aumentato in articoli:
        # Il segno [!] sta in coda, fuori dalle colonne: la tabella resta
        # allineata e l'occhio trova subito la riga anomala.
        segno = "" if aumentato else SEGNO_INVARIATO
        # Lo slicing tronca la descrizione che sfonderebbe la colonna (P3,
        # Giorno 03 §9.7); qui nessuna la supera, ma il giorno che arriva
        # "Monitor 27 pollici curvo" la tabella non si deforma.
        righe.append(
            f"{codice:<{COLONNA_CODICE}}"
            f"{descrizione[:COLONNA_DESCRIZIONE - 1]:<{COLONNA_DESCRIZIONE}}"
            f"{categoria:<{COLONNA_CATEGORIA}}{vecchio:>{COLONNA_PREZZO}.2f}"
            f"{nuovo:>{COLONNA_PREZZO}.2f}{segno}"
        )
        totale_vecchio += vecchio
        totale_nuovo += nuovo
    righe.append("-" * LARGHEZZA)
    etichetta = "TOTALE"
    larghezza_etichetta = COLONNA_CODICE + COLONNA_DESCRIZIONE + COLONNA_CATEGORIA
    righe.append(
        f"{etichetta:<{larghezza_etichetta}}{totale_vecchio:>{COLONNA_PREZZO}.2f}"
        f"{totale_nuovo:>{COLONNA_PREZZO}.2f}"
    )
    return righe


def componi_listino(articoli):
    """Restituisce le righe del nuovo listino, nel formato del file di partenza."""
    righe = [INTESTAZIONE_FILE]
    for codice, descrizione, categoria, vecchio, nuovo, aumentato in articoli:
        # Il prezzo torna con la virgola: il file che esce deve poter
        # rientrare in questo stesso programma al prossimo aumento.
        righe.append(
            f"{codice}{SEPARATORE}{descrizione}{SEPARATORE}{categoria}"
            f"{SEPARATORE}{formato_italiano(nuovo)}"
        )
    return righe


def totale_del_file(percorso):
    """Rilegge un listino con il caricatore e restituisce la somma dei prezzi."""
    # Stesso caricatore e stesso convertitore dell'andata: se il file
    # scritto non rientra, il difetto è nella scrittura, e si vede qui.
    totale = 0.0
    for numero, campi in carica_righe(percorso):
        totale += converti_importo(campi[-1])
    return totale


def main():
    """Carica il listino, applica gli aumenti, scrive il nuovo listino."""
    print("=" * LARGHEZZA)
    print(TITOLO)
    print("=" * LARGHEZZA)

    # 1. CARICA. Il file che manca si previene con exists(), come nel
    #    Giorno 08 §8.1: il messaggio dice il nome, non il percorso intero,
    #    che cambia da una macchina all'altra.
    if not FILE_LISTINO.exists():
        print(f"[ERRORE] {FILE_LISTINO.name} non trovato nella cartella dati.")
        print("=" * LARGHEZZA)
        return
    righe = carica_righe(FILE_LISTINO)
    print(f"File letto: {FILE_LISTINO.name}")

    # 2. VALIDA ed ELABORA, nello stesso giro.
    articoli = []
    scartate = 0
    percentuali_applicate = []
    for numero, campi in righe:
        articolo, motivo = valida_articolo(campi)
        if articolo is None:
            print(f"[!] riga {numero:>2}  scartata: {motivo}")
            scartate += 1
            continue
        codice, descrizione, categoria, prezzo = articolo
        # P12 con in, non con .get(): la categoria senza aumento è una
        # notizia da dare, non un caso da coprire in silenzio.
        # TRABOCCHETTO: con AUMENTI.get(categoria, 0) il programma non si
        #   ferma e la chiavetta resta a 12.90, come deve. Ma sparisce il
        #   [!], l'articolo viene contato fra gli aumentati (9 invece di 8)
        #   e l'aumento medio applicato scende da 5.0% a 4.4%, perché uno
        #   zero entra nella media. Il totale non cambia: nessun conto lo
        #   segnala.
        if categoria in AUMENTI:
            percentuale = AUMENTI[categoria]
            nuovo = nuovo_prezzo(prezzo, percentuale)
            percentuali_applicate.append(percentuale)
            aumentato = True
        else:
            print(f"[!] riga {numero:>2}  {codice}: categoria {categoria} "
                  "senza aumento, prezzo invariato")
            nuovo = prezzo
            aumentato = False
        articoli.append((codice, descrizione, categoria, prezzo, nuovo, aumentato))
    print("-" * LARGHEZZA)

    # P15, il caso zero: se tutte le righe sono state scartate non c'è una
    # tabella da stampare e le medie dividerebbero per zero.
    if not articoli:
        print("[ERRORE] Nessun articolo valido: listino non aggiornato.")
        print("=" * LARGHEZZA)
        return

    # 3. RIPORTA a video: la tabella composta una volta (P28).
    stampa_righe(componi_tabella(articoli))
    print("-" * LARGHEZZA)

    vecchi = []
    nuovi = []
    for codice, descrizione, categoria, vecchio, nuovo, aumentato in articoli:
        vecchi.append(vecchio)
        nuovi.append(nuovo)
    totale_vecchio = sum(vecchi)
    totale_nuovo = sum(nuovi)
    aumento = totale_nuovo - totale_vecchio
    # TRABOCCHETTO: lo specificatore % moltiplica già per 100 (Giorno 03
    #   §9.2). Passategli aumento / totale_vecchio * 100 e la riga dice
    #   "20.19 euro (376.6%)": un aumento di venti euro su cinquecento
    #   presentato come un listino quadruplicato.
    quota_aumento = aumento / totale_vecchio

    print(riga_puntini("Righe lette", len(righe)))
    print(riga_puntini("Articoli aumentati", len(percentuali_applicate)))
    print(riga_puntini("Articoli invariati",
                       len(articoli) - len(percentuali_applicate)))
    print(riga_puntini("Righe scartate", scartate))
    print(riga_puntini("Aumento complessivo",
                       f"{aumento:.2f} euro ({quota_aumento:.1%})"))
    print(riga_puntini("Prezzo medio vecchio", f"{media(vecchi):.2f}"))
    print(riga_puntini("Prezzo medio nuovo", f"{media(nuovi):.2f}"))

    # Requisito promosso: l'aumento MEDIO APPLICATO. È la media delle
    # percentuali (3, 3, 5, 5, 10, 10, 2, 2 -> 5.0%), e non coincide con
    # l'aumento complessivo (3.8%) perché quella è una media pesata dai
    # prezzi: il 10% degli accessori si applica a oggetti da pochi euro, il
    # 2% dell'informatica a una tastiera da 89. Due numeri veri, che
    # rispondono a due domande diverse: "quanto abbiamo aumentato, in
    # media, le etichette?" e "quanto costa in più il listino?".
    if percentuali_applicate:
        media_applicata = media(percentuali_applicate)
        print(riga_puntini(
            "Aumento medio applicato",
            f"{media_applicata:.1f}% (su {len(percentuali_applicate)} articoli)",
        ))
    print("-" * LARGHEZZA)

    # 4. SCRIVI il nuovo listino. La modalità "w" è la ripartenza pulita:
    #    a ogni esecuzione il file si riscrive da capo.
    # TRABOCCHETTO: con "a" al posto di "w" la prima esecuzione è perfetta,
    #   la seconda no: il file ha 20 righe invece di 10 (l'intestazione due
    #   volte, gli articoli due volte), e la verifica qui sotto rilegge
    #   1112.58 contro 556.29 e stampa [ERRORE].
    OUTPUT.mkdir(parents=True, exist_ok=True)
    with open(FILE_AGGIORNATO, "w", encoding="utf-8") as uscita:
        stampa_righe(componi_listino(articoli), file=uscita)
    righe_scritte = FILE_AGGIORNATO.read_text(encoding="utf-8").splitlines()
    print(f"File scritto: {FILE_AGGIORNATO.name} ({len(righe_scritte)} righe)")

    # Requisito promosso: la verifica di andata e ritorno. Si confrontano
    # i due totali arrotondati ai centesimi: fra due float il confronto
    # con == è fragile, fra due importi al centesimo no (Giorno 02 §7.4).
    totale_riletto = totale_del_file(FILE_AGGIORNATO)
    if round(totale_riletto, CENTESIMI) == round(totale_nuovo, CENTESIMI):
        print(f"[OK] totale riletto {totale_riletto:.2f} = "
              f"totale nuovo {totale_nuovo:.2f}")
    else:
        print(f"[ERRORE] totale riletto {totale_riletto:.2f} diverso da "
              f"totale nuovo {totale_nuovo:.2f}")
    print("=" * LARGHEZZA)


if __name__ == "__main__":
    main()
