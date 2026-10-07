"""
SOLUZIONE — Esercizio 09.2: La media del turno, anche a turno vuoto

IL PROBLEMA
Tre guasti diversi sullo stesso calcolo. Il file del turno di notte non
esiste, e aprirlo solleva FileNotFoundError. Il file del turno vuoto esiste
ma non contiene punteggi: la media diventa una divisione per zero
(ZeroDivisionError), e il minimo e il massimo di una lista vuota non
esistono (ValueError). Il file del pomeriggio ha una riga scritta a
parole, "novanta", e int() la rifiuta con un altro ValueError.

LA STRATEGIA
Ogni calcolo scritto due volte, in due funzioni gemelle:
    leggi_con_if(percorso)     -> (punteggi, scartate)   salta con .isdecimal()
    leggi_con_try(percorso)    -> (punteggi, scartate)   try stretto su int()
    media_con_if(percorso)     -> (esito, letti, scartate)   exists(), len()
    media_con_try(percorso)    -> (esito, letti, scartate)   due try stretti
    estremi_con_if(percorso)   -> esito                  previene: exists(), len()
    estremi_con_try(percorso)  -> esito                  gestisce: due try stretti
Le funzioni con if chiamano solo funzioni con if, quelle con try solo
funzioni con try: ogni strada è completa dall'apertura del file al
risultato. Nessuna stampa: main() mette gli esiti uno accanto all'altro e
controlla se dicono la stessa cosa.

LA RISPOSTA ALLA DOMANDA SUL FILE CON "novanta"
Nella versione di partenza la lettura stava in UNA funzione condivisa,
senza difese: int("novanta") sollevava ValueError dentro tutte e due le
strade. Si fermava per prima la strada con if, solo perché main() la
chiama per prima; quella con try non ci arrivava nemmeno, e comunque non
l'avrebbe raccolto, perché il suo except aspettava FileNotFoundError
(Cap. 5.1: si raccoglie solo il tipo dichiarato). Per non fermare
nessuna delle due, la difesa va dove nasce l'errore: nella lettura, che
per questo è diventata due funzioni.

IL VERDETTO
Qui le due strade coincidono sempre. Per il turno vuoto l'if è più chiaro:
il caso è prevedibile, costa una riga e dice che cosa controlla (Cap.
8.4). Per il file assente il try ha un vantaggio che su questi dati non si
vede: regge anche se il file sparisce fra exists() e l'apertura (Cap. 9.2).
Per la riga sporca le due si equivalgono solo su questi dati: "-5" o
" 90" sono rifiutati da .isdecimal() e accettati da int() (Cap. 8.3).

LIMITI NOTI DI QUESTA SOLUZIONE
- Ogni file viene letto quattro volte: due strade per due calcoli. Su
  file da otto righe non conta; su un file grande si leggerebbe una volta
  sola per strada e si passerebbe la lista ai due calcoli.
- Un punteggio fuori scala (130) passa in tutte e due le strade: si
  controlla che sia un intero, non che stia fra 0 e 100.
- La riga scartata si conta, ma non si dice quale fosse.

Concetti di teoria: cap. 4.4 (FileNotFoundError catturato), cap. 5.1
(except ValueError), cap. 6.3 (ZeroDivisionError), cap. 8.3-8.4
(.isdecimal() contro int(), if contro except sulla media), Giorno 08
(Path, with open, lettura riga per riga), Giorno 06 (funzioni che
restituiscono una coppia).
"""

from pathlib import Path

# --- Costanti ---------------------------------------------------------------
FILE_TURNI = ("punteggi_turno.txt", "punteggi_vuoto.txt",
              "punteggi_notte.txt", "punteggi_pomeriggio.txt")
ESITO_ASSENTE = "file assente"
ESITO_VUOTO = "nessun dato"
LARGHEZZA = 70

# La cartella dei dati si ricava dalla posizione di QUESTO file, non dalla
# cartella da cui si lancia il programma: lanciato da PyCharm, dal
# terminale o dal collaudo, il percorso è sempre lo stesso (Giorno 08).
CARTELLA_DATI = Path(__file__).resolve().parent.parent / "dati"

# Il segnaposto per la colonna dei punteggi letti quando il file non c'è.
# È una stringa e non None apposta: vedi il trabocchetto in stampa_riga().
NESSUN_CONTEGGIO = "-"
RISPOSTA_SI = "sì"
RISPOSTA_NO = "no"


# --- La lettura, nelle due strade --------------------------------------------
def leggi_con_if(percorso):
    """Legge un punteggio per riga, saltando prima le righe non numeriche."""
    # Nessuna difesa sul file assente: se il file non c'è, open() solleva
    # FileNotFoundError e l'eccezione risale a chi ha chiamato. Il controllo
    # exists() lo fa il chiamante, che sa se l'assenza è un guaio o un caso
    # previsto (Cap. 12.2).
    punteggi = []
    scartate = 0
    with open(percorso, encoding="utf-8") as f:
        for riga in f:
            # .strip() toglie il "\n" di fine riga. Le righe vuote si
            # saltano senza contarle: un a capo in più non è un dato sporco.
            testo = riga.strip()
            if testo == "":
                continue
            # La prevenzione: si converte solo ciò che è fatto di cifre.
            # "novanta" non lo è, e viene contato fra le scartate.
            if not testo.isdecimal():
                scartate += 1
                continue
            punteggi.append(int(testo))
    return punteggi, scartate


def leggi_con_try(percorso):
    """Legge un punteggio per riga, raccogliendo le righe che int() rifiuta."""
    punteggi = []
    scartate = 0
    with open(percorso, encoding="utf-8") as f:
        for riga in f:
            testo = riga.strip()
            # Questo if non tocca né il file assente né il turno vuoto: toglie
            # le righe vuote, che non sono dati. Senza, int("") solleverebbe
            # un ValueError e un a capo in fondo al file conterebbe come riga
            # scartata.
            if testo == "":
                continue
            # Il try stretto, dentro il ciclo: una riga sbagliata si salta e
            # la lettura continua con la successiva (Cap. 9.6).
            #
            # TRABOCCHETTO: mettere il try FUORI dal for, attorno a tutto il
            #   ciclo. Il ValueError di "novanta" fa uscire dal ciclo intero:
            #   la lista si ferma a 88 e 73, e i tre punteggi dopo la riga
            #   sporca non vengono mai letti. Nessun errore a schermo: la
            #   riga del pomeriggio dice media 79.60 con if e media 80.50
            #   con try, e UGUALI "no". Se ne accorge solo il confronto fra
            #   le due strade, ed è il motivo per cui il programma lo fa.
            try:
                punteggi.append(int(testo))
            except ValueError:
                scartate += 1
    return punteggi, scartate


# --- La media, nelle due strade ----------------------------------------------
def media_con_if(percorso):
    """Media dei punteggi prevenendo: controlla prima, calcola poi."""
    # La difesa del Giorno 08: prima si guarda se il file c'è.
    #
    # TRABOCCHETTO: dimenticare questo controllo. I primi due file vanno
    #   bene e le loro righe escono; al terzo il programma si ferma con
    #   FileNotFoundError: [Errno 2] No such file or directory:
    #   seguito dal percorso COMPLETO del file sulla vostra macchina, fra
    #   apici. Sul computer del vicino quel percorso è diverso: è il motivo
    #   per cui nei messaggi all'utente si stampa solo .name (Cap. 9.1).
    if not percorso.exists():
        return ESITO_ASSENTE, NESSUN_CONTEGGIO, NESSUN_CONTEGGIO

    # La strada con if legge con la lettura con if: le righe sporche sono
    # già state tolte, qui arrivano solo interi.
    punteggi, scartate = leggi_con_if(percorso)

    # La difesa dei Giorni 05 e 07: prima di dividere, si guarda se c'è
    # qualcosa da dividere.
    #
    # TRABOCCHETTO: scrivere if punteggi == 0: al posto del controllo sulla
    #   lunghezza. Una lista vuota non è uguale al numero zero, il confronto
    #   è sempre False, e il secondo file arriva alla divisione e ferma il
    #   programma con
    #   ZeroDivisionError: division by zero
    #   dentro la funzione che doveva impedirlo.
    if len(punteggi) == 0:
        return ESITO_VUOTO, 0, scartate

    media = sum(punteggi) / len(punteggi)
    return f"media {media:.2f}", len(punteggi), scartate


def media_con_try(percorso):
    """Media dei punteggi gestendo: prova a calcolare, rimedia se fallisce."""
    # Due try stretti, uno per guasto. Il primo protegge solo la lettura,
    # il secondo solo la divisione: così ogni except sa esattamente che cosa
    # è successo e restituisce l'esito giusto (Cap. 4.5).
    try:
        punteggi, scartate = leggi_con_try(percorso)
    except FileNotFoundError:
        # TRABOCCHETTO: sostituire questo return con una stampa e basta.
        #   L'except finisce, il programma riprende dopo, arriva a
        #   len(punteggi) e si ferma con
        #   UnboundLocalError: cannot access local variable 'punteggi'
        #   where it is not associated with a value
        #   perché l'assegnazione nel try non è mai avvenuta (Cap. 4.6).
        return ESITO_ASSENTE, NESSUN_CONTEGGIO, NESSUN_CONTEGGIO

    # TRABOCCHETTO: calcolare la media su una riga PRIMA del try e mettere
    #   nel try solo la formattazione. Il try non vede niente di ciò che
    #   succede sopra di lui: il secondo file si ferma con
    #   ZeroDivisionError: division by zero
    #   esattamente come se il try non ci fosse. Un try protegge solo le
    #   righe che contiene (Cap. 4.2).
    try:
        media = sum(punteggi) / len(punteggi)
    except ZeroDivisionError:
        return ESITO_VUOTO, 0, scartate
    return f"media {media:.2f}", len(punteggi), scartate


# --- Minimo e massimo, nelle due strade --------------------------------------
def estremi_con_if(percorso):
    """Punteggio minimo e massimo prevenendo: stesso schema della media."""
    if not percorso.exists():
        return ESITO_ASSENTE
    # [0] prende il primo elemento della coppia, la lista: gli scarti li
    # conta già la media, e qui non servono.
    punteggi = leggi_con_if(percorso)[0]
    # Lo stesso controllo della media, per un motivo diverso: qui non c'è
    # nessuna divisione, ma min() e max() su una lista vuota non hanno
    # niente da restituire.
    if len(punteggi) == 0:
        return ESITO_VUOTO
    return f"min {min(punteggi)} max {max(punteggi)}"


def estremi_con_try(percorso):
    """Punteggio minimo e massimo gestendo: min() e max() dentro il try."""
    try:
        punteggi = leggi_con_try(percorso)[0]
    except FileNotFoundError:
        return ESITO_ASSENTE
    # Su una lista vuota max() non divide per zero: solleva
    #   ValueError: max() iterable argument is empty
    # Stesso guasto della media, eccezione diversa. Chi copiasse l'except
    # della media, ZeroDivisionError, non raccoglierebbe niente.
    #
    # TRABOCCHETTO: copiare anche qui except ZeroDivisionError. Il primo
    #   file passa, il secondo ferma il programma con
    #   ValueError: min() iterable argument is empty
    #   È min() e non max(), perché nella f-string min() viene chiamato per
    #   primo: si ferma sempre la prima cosa che incontra il guasto.
    try:
        return f"min {min(punteggi)} max {max(punteggi)}"
    except ValueError:
        return ESITO_VUOTO


# --- Stampa -----------------------------------------------------------------
def stampa_riga(nome_file, letti, esito_if, esito_try, uguali):
    """Stampa una riga della tabella, incolonnata come l'intestazione."""
    # TRABOCCHETTO: per il file assente, restituire None invece del
    #   segnaposto "-". None non protesta finché non incontra un formato:
    #   qui, con :>5, la riga del terzo file si ferma con
    #   TypeError: unsupported format string passed to NoneType.__format__
    #   Le prime due righe della tabella sono già uscite, la terza no
    #   (Cap. 6.2). Una stringa invece si incolonna con lo stesso formato
    #   di un numero.
    print(f"{nome_file:<24}{letti:>5}  {esito_if:<16}{esito_try:<16}{uguali}")


def stampa_etichetta(testo, valore):
    """Stampa 'testo ..... valore' con i puntini di riempimento."""
    puntini = "." * (22 - len(testo) - 1)
    print(f"{testo} {puntini} {valore}")


def risposta(uguali):
    """Trasforma il confronto vero/falso nella scritta della colonna."""
    if uguali:
        return RISPOSTA_SI
    return RISPOSTA_NO


def main():
    """Calcola media ed estremi di ogni turno nei due modi e li confronta."""
    print("=" * LARGHEZZA)
    print("POLIAMBULATORIO AURORA - Media del gradimento per turno")
    print("=" * LARGHEZZA)
    # L'intestazione usa gli stessi formati delle righe, con i titoli al
    # posto dei dati: le colonne restano sotto il loro titolo per
    # costruzione (Giorno 03, capitolo 9).
    stampa_riga("FILE", "LETTI", "CON IF", "CON TRY", "UGUALI")

    # Gli accumulatori per il riepilogo, come nei cicli del Giorno 05.
    concordi_media = 0
    file_letti = 0
    punteggi_letti = 0
    righe_scartate = 0
    # Gli estremi si stampano in una seconda tabella, dopo la prima: si
    # tengono da parte in una lista di tuple (Giorno 07) invece di
    # ricalcolarli.
    righe_estremi = []

    for nome_file in FILE_TURNI:
        percorso = CARTELLA_DATI / nome_file
        # Le due funzioni restituiscono una tupla di tre valori, che
        # l'unpacking del Giorno 03 divide in tre nomi.
        esito_if, letti, scartate = media_con_if(percorso)
        esito_try, letti_try, scartate_try = media_con_try(percorso)

        # L'accordo si confronta sull'esito E sui due conteggi: due strade
        # che dicessero "media 79.60" scartando righe diverse non sarebbero
        # d'accordo, anche se la scritta coincide.
        stesso_esito = (esito_if == esito_try and letti == letti_try
                        and scartate == scartate_try)
        if stesso_esito:
            concordi_media += 1

        # Il segnaposto "-" è una stringa: si sommano solo i conteggi veri.
        if letti != NESSUN_CONTEGGIO:
            file_letti += 1
            punteggi_letti += letti
            righe_scartate += scartate

        # Nella tabella va solo il nome del file, mai il percorso completo:
        # percorso.name è uguale su ogni macchina, percorso intero no.
        stampa_riga(percorso.name, letti, esito_if, esito_try,
                    risposta(stesso_esito))

        estremi_if = estremi_con_if(percorso)
        estremi_try = estremi_con_try(percorso)
        righe_estremi.append((percorso.name, letti, estremi_if, estremi_try))

    print("-" * LARGHEZZA)
    # Seconda tabella: stesse colonne, stessa funzione di stampa. Cambiano
    # solo i titoli delle due colonne centrali.
    stampa_riga("FILE", "LETTI", "MIN/MAX CON IF", "MIN/MAX CON TRY", "UGUALI")
    concordi_estremi = 0
    for nome_file, letti, estremi_if, estremi_try in righe_estremi:
        # Qui basta la scritta: il conteggio è lo stesso della prima tabella.
        if estremi_if == estremi_try:
            concordi_estremi += 1
        stampa_riga(nome_file, letti, estremi_if, estremi_try,
                    risposta(estremi_if == estremi_try))

    print("-" * LARGHEZZA)
    totale = len(FILE_TURNI)
    print(f"Media: le due strade concordano su {concordi_media} file su {totale}.")
    print(f"Min/max: le due strade concordano su {concordi_estremi} file su "
          f"{totale}.")
    stampa_etichetta("File letti", f"{file_letti} su {totale}")
    stampa_etichetta("Punteggi letti", punteggi_letti)
    stampa_etichetta("Righe scartate", righe_scartate)
    print("=" * LARGHEZZA)


if __name__ == "__main__":
    main()
