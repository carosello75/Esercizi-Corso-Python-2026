"""
SOLUZIONE — Esercizio per casa 10.4: Dallo schema al caso nuovo, gli
interventi di manutenzione

IL PROBLEMA
Tre squadre di manutenzione, dodici interventi, un tempo previsto per ogni
quartiere. La domanda è quella dei corrieri di 10.4: chi chiude entro il
previsto? Il punto dell'esercizio non è il report, che 10.4 sa già fare: è
arrivarci cambiando il MENO possibile.

PATTERN SCELTI (quali e perché, una riga ciascuno)
- P26  il file ha intestazione e righe da numerare come l'editor
- P6   ogni riga è delimitata da ';' e va spezzata e ripulita campo per campo
- P12  a ogni quartiere corrispondono ore previste fisse: tabella in un
       dizionario, non una catena di elif
- P18  tre grandezze per chiave nello stesso giro: interventi, ore, fuori
       tempo
- P15  media delle ore per squadra, con il totale sotto
- P16  lo sforamento più grande, e soprattutto DI CHI è
- P22  la classifica per puntualità, a coppie (percentuale, chiave)
- P23  calcolo e stampa separati: le funzioni restituiscono, una sola
       stampa_report() stampa, due volte

RIGHE CAMBIATE RISPETTO A 10.4
Parte specifica, riscritta:
  1. FILE_CONSEGNE -> FILE_INTERVENTI, con il nome del nuovo file di dati
  2. GIORNI_PREVISTI -> ORE_PREVISTE, con i tre quartieri e le loro ore
  3. valida_consegna() -> valida_intervento(): stessi controlli, nomi dei
     campi e testo dei motivi diversi ("ore", "quartiere")
  4. TITOLO e i dizionari TESTI_*: intestazioni di colonna e titoli dei
     blocchi ("SQUADRA", "ORE" al posto di "CORRIERE", "GIORNI")
  5. main(): i nomi delle variabili e le frasi finali
Aggiunto, perché la traccia lo chiede e 10.4 non lo aveva:
  6. il report per quartiere: in main() si ricompongono i record con il
     quartiere al posto della squadra, e si chiamano LE STESSE funzioni
  7. interventi_sul_bordo(): nuova, sta nella parte specifica. Se servisse
     anche a 10.4, salirebbe nella parte generale senza modifiche
NON cambiato, copiato identico:
  carica_righe(), aggrega_per_chiave(), classifica_puntualita(),
  massimo_scostamento(), stampa_report(), riga_puntini() e le costanti di
  formato (SEPARATORE, COMMENTO, LARGHEZZA, PER_CENTO).
  Il record ha la stessa forma nei due esercizi, (codice, chiave, zona,
  valore): in 10.4 (spedizione, corriere, zona, giorni), qui (intervento,
  squadra, quartiere, ore). È QUESTO che rende la parte generale
  copiabile: le funzioni non sanno che cosa c'è dentro i quattro campi,
  sanno solo in che posizione sta ciascuno.

LIMITI NOTI DI QUESTA SOLUZIONE
- Le ore sono intere. Un intervento di 2 ore e mezza richiederebbe P5 nel
  validatore, e la parte generale reggerebbe senza modifiche: sommare e
  confrontare float funziona come con gli interi.
- La parità nella classifica per quartiere (PERIFERIA e MARINA, 66.7%) la
  risolve l'ordine alfabetico inverso: è E6, dichiarato nella traccia.
"""

from pathlib import Path

# --- Costanti di formato: identiche a 10.4 --------------------------------
SEPARATORE = ";"
COMMENTO = "#"
LARGHEZZA = 60
LARGHEZZA_ETICHETTA = 27
PER_CENTO = 100

# --- Costanti del caso: PARTE SPECIFICA -----------------------------------
# Tre .parent: la soluzione sta un livello più in basso della traccia
# (P25, Giorno 08 §7.3).
CARTELLA_GIORNO = Path(__file__).resolve().parent.parent.parent
DATI = CARTELLA_GIORNO / "dati"
FILE_INTERVENTI = DATI / "interventi_manutenzione.csv"  # <-- adattato

CAMPI_ATTESI = 4
# TRABOCCHETTO (E1): è la riga che si dimentica copiando lo schema. Con i
#   GIORNI_PREVISTI dei corrieri lasciati al loro posto, PERIFERIA e MARINA
#   non esistono: i validi scendono da 10 a 4, otto righe su dodici
#   finiscono scartate, sette con "quartiere sconosciuto", e il report esce
#   ordinato e sbagliato. Nessun errore: un report di un altro caso.
ORE_PREVISTE = {"CENTRO": 3, "PERIFERIA": 4, "MARINA": 5}  # <-- adattato

TITOLO = "COMUNE DI VILLANOVA - Interventi di manutenzione"  # <-- adattato
TESTI_SQUADRA = {  # <-- adattato
    "titolo": "PER SQUADRA",
    "chiave": "SQUADRA",
    "unita": "ORE",
    "quota": "ENTRO I TEMPI",
    "classifica": "Classifica per puntualità:",
}
TESTI_QUARTIERE = {  # <-- aggiunto
    "titolo": "PER QUARTIERE",
    "chiave": "QUARTIERE",
    "unita": "ORE",
    "quota": "ENTRO I TEMPI",
    "classifica": "Classifica per puntualità:",
}


# =========================================================================
# ===== PARTE GENERALE: si riusa così com'è (copiata da 10.4) =============
# =========================================================================

# P26 — Il caricatore di un file con intestazione.
def carica_righe(percorso):
    """Restituisce [(numero_riga, campi), ...] per le righe dopo l'intestazione."""
    righe_utili = []
    with open(percorso, encoding="utf-8") as ingresso:
        # L'intestazione si legge a mano e si butta; il conteggio riparte
        # da 2, così il numero combacia con quello dell'editor (Giorno 08
        # §9.5).
        ingresso.readline()
        for numero, riga in enumerate(ingresso, start=2):
            testo = riga.strip()
            if testo == "" or testo.startswith(COMMENTO):
                continue
            campi = []
            for campo in testo.split(SEPARATORE):
                campi.append(campo.strip())
            righe_utili.append((numero, campi))
    return righe_utili


# P18 — Tre grandezze per chiave nello stesso giro, restituite insieme.
def aggrega_per_chiave(record, previsti):
    """Da record (codice, chiave, zona, valore): conteggi, totali, fuori_tempo."""
    conteggi = {}
    totali = {}
    fuori_tempo = {}
    for codice, chiave, zona, valore in record:
        conteggi[chiave] = conteggi.get(chiave, 0) + 1
        totali[chiave] = totali.get(chiave, 0) + valore
        # La chiave entra in fuori_tempo SEMPRE, con zero, anche se non
        # andrà mai fuori tempo.
        # TRABOCCHETTO: la tentazione è contare con .get() solo dentro l'if
        #   qui sotto. Allora una chiave senza ritardi non entra mai nel
        #   dizionario, e classifica_puntualita() si ferma con
        #   KeyError: 'SQUADRA_A'. È la squadra MIGLIORE a far cadere il
        #   programma, proprio perché non ha ritardi.
        fuori_tempo[chiave] = fuori_tempo.get(chiave, 0)
        # TRABOCCHETTO (E3): con >= al posto di > gli interventi chiusi
        #   esattamente nelle ore previste diventano fuori tempo. Nessun
        #   errore: SQUADRA_A scende da 100.0% a 50.0%, SQUADRA_B da 75.0%
        #   a 50.0%, il totale da 70.0% a 40.0%, e a parità SQUADRA_B passa
        #   davanti a SQUADRA_A in classifica.
        if valore > previsti[zona]:
            fuori_tempo[chiave] += 1
    # Tre valori restituiti insieme: chi chiama li spacchetta nello stesso
    # ordine (Giorno 06 §10.3).
    return conteggi, totali, fuori_tempo


# P22 — La classifica per puntualità.
def classifica_puntualita(conteggi, fuori_tempo):
    """Restituisce [(percentuale, chiave), ...] in ordine decrescente."""
    coppie = []
    for chiave in conteggi:
        puntuali = conteggi[chiave] - fuori_tempo[chiave]
        percentuale = puntuali / conteggi[chiave] * PER_CENTO
        # TRABOCCHETTO: con la coppia scritta (chiave, percentuale) la
        #   classifica ordina per nome, e stampa_report() si ferma con
        #   ValueError: Unknown format code 'f' for object of type 'str',
        #   perché al posto della percentuale riceve 'SQUADRA_C'.
        coppie.append((percentuale, chiave))
    # TRABOCCHETTO (E6): reverse=True rovescia l'ordine di tutta la tupla.
    #   Nel report per quartiere PERIFERIA e MARINA valgono entrambe 66.7%,
    #   e PERIFERIA esce prima perché P viene dopo M nell'alfabeto. Non è
    #   un errore: è la regola della classifica a coppie, da dichiarare.
    coppie.sort(reverse=True)
    return coppie


# P16 — Il massimo, con il suo proprietario.
def massimo_scostamento(record, previsti):
    """Restituisce (scostamento, codice, chiave, zona, valore) del massimo, o None."""
    # None come valore di partenza, e non 0: con 0 il massimo non sarebbe
    # mai "nessuno", anche su un file in cui tutti sono in anticipo
    # (Giorno 05 §6.5).
    migliore = None
    for codice, chiave, zona, valore in record:
        scostamento = valore - previsti[zona]
        if migliore is None or scostamento > migliore[0]:
            migliore = (scostamento, codice, chiave, zona, valore)
    return migliore


def riga_puntini(etichetta, valore):
    """P2 — 'Etichetta ........ valore', con i valori in colonna."""
    return f"{etichetta + ' ':.<{LARGHEZZA_ETICHETTA}} {valore}"


# P23 — La stampa: riceve numeri già calcolati, non calcola niente di suo
# se non le medie e le quote di riga.
def stampa_report(conteggi, totali, fuori_tempo, classifica, testi):
    """Stampa tabella, totali e classifica con le etichette di `testi`."""
    print(testi["titolo"])
    print(f"{testi['chiave']:<14}{'N.':>5}{testi['unita']:>6}{'MEDIA':>8}"
          f"{'FUORI':>7}{testi['quota']:>15}")
    for chiave in conteggi:
        numero = conteggi[chiave]
        # P15: media per riga. numero non è mai zero, perché la chiave è
        # nel dizionario proprio perché c'è almeno un record.
        # TRABOCCHETTO: con // al posto di / la media perde i decimali
        #   senza errori: SQUADRA_A esce 3.00 invece di 3.25, SQUADRA_C
        #   5.00 invece di 5.50. Il formato .2f aggiunge gli zeri, e il
        #   numero sembra perfino più preciso.
        media = totali[chiave] / numero
        entro = (numero - fuori_tempo[chiave]) / numero * PER_CENTO
        print(f"{chiave:<14}{numero:>5}{totali[chiave]:>6}{media:>8.2f}"
              f"{fuori_tempo[chiave]:>7}{entro:>14.1f}%")
    numero_totale = sum(conteggi.values())
    somma_totale = sum(totali.values())
    fuori_totale = sum(fuori_tempo.values())
    if numero_totale > 0:
        media_totale = somma_totale / numero_totale
        entro_totale = (numero_totale - fuori_totale) / numero_totale * PER_CENTO
        print(f"{'TOTALE':<14}{numero_totale:>5}{somma_totale:>6}"
              f"{media_totale:>8.2f}{fuori_totale:>7}{entro_totale:>14.1f}%")
    print(testi["classifica"])
    posizione = 1
    for coppia in classifica:
        percentuale, chiave = coppia
        print(f"{posizione:>3}. {chiave:<14}{percentuale:>6.1f}%")
        posizione += 1


# =========================================================================
# ===== PARTE SPECIFICA: si cambia per un altro caso ======================
# =========================================================================

def valida_intervento(campi, ore_previste):  # <-- adattato da valida_consegna
    """Restituisce ((intervento, squadra, quartiere, ore), '') o (None, motivo)."""
    # Stessi controlli di valida_consegna(), nello stesso ordine: numero
    # dei campi, valori ammessi, forma. Cambiano i nomi e le frasi.
    if len(campi) != CAMPI_ATTESI:
        return None, f"servono {CAMPI_ATTESI} campi, ne ha {len(campi)}"
    intervento, squadra, quartiere, testo_ore = campi
    intervento = intervento.upper()
    squadra = squadra.upper()
    quartiere = quartiere.upper()
    # P12: il quartiere deve stare nella tabella. Con in, e non con .get():
    # un quartiere sconosciuto è uno scarto da spiegare, non un ripiego.
    if quartiere not in ore_previste:
        return None, f"quartiere sconosciuto: {quartiere}"
    # .isdecimal() prima di int(): la prevenzione del Giorno 04 §13.2
    # basta, perché le ore sono intere e senza segno.
    if not testo_ore.isdecimal():
        return None, f"ore non numeriche: '{testo_ore}'"
    return (intervento, squadra, quartiere, int(testo_ore)), ""


def interventi_sul_bordo(record, previsti):  # <-- aggiunto
    """Restituisce i codici dei record con valore uguale al previsto."""
    # Sono i casi che la scelta fra > e >= sposta da una parte all'altra:
    # stamparli rende visibile la decisione presa, invece di nasconderla.
    codici = []
    for codice, chiave, zona, valore in record:
        if valore == previsti[zona]:
            codici.append(codice)
    return codici


def main():
    """Report degli interventi per squadra e per quartiere."""
    print("=" * LARGHEZZA)
    print(TITOLO)
    print("=" * LARGHEZZA)

    # 1. CARICA.
    if not FILE_INTERVENTI.exists():
        print(f"[ERRORE] {FILE_INTERVENTI.name} non trovato nella cartella dati.")
        print("=" * LARGHEZZA)
        return
    righe = carica_righe(FILE_INTERVENTI)
    print(f"File letto: {FILE_INTERVENTI.name}")

    # 2. VALIDA: i buoni in una lista di record a quattro campi, gli scarti
    #    stampati con il numero di riga dell'editor.
    interventi = []
    for numero, campi in righe:
        intervento, motivo = valida_intervento(campi, ORE_PREVISTE)
        if intervento is None:
            print(f"[!] riga {numero:>2}  {motivo}")
            continue
        interventi.append(intervento)
    print(riga_puntini("Righe di dati", len(righe)))
    print(riga_puntini("Interventi validi", len(interventi)))
    print(riga_puntini("Righe scartate", len(righe) - len(interventi)))
    print("-" * LARGHEZZA)

    # 3. ELABORA e RIPORTA per squadra: le stesse tre chiamate di 10.4.
    conteggi, totali, fuori_tempo = aggrega_per_chiave(interventi, ORE_PREVISTE)
    classifica = classifica_puntualita(conteggi, fuori_tempo)
    stampa_report(conteggi, totali, fuori_tempo, classifica, TESTI_SQUADRA)
    print("-" * LARGHEZZA)

    # 4. Requisito promosso: lo stesso report per QUARTIERE, senza funzioni
    #    nuove. aggrega_per_chiave() raggruppa per il secondo campo e
    #    confronta con il terzo: basta mettere il quartiere in tutti e due.
    #    È l'adattamento nella sua forma più pura: i dati si piegano alla
    #    funzione, la funzione non si tocca.
    per_quartiere = []
    for codice, squadra, quartiere, ore in interventi:
        per_quartiere.append((codice, quartiere, quartiere, ore))
    conteggi_q, totali_q, fuori_q = aggrega_per_chiave(per_quartiere, ORE_PREVISTE)
    classifica_q = classifica_puntualita(conteggi_q, fuori_q)
    stampa_report(conteggi_q, totali_q, fuori_q, classifica_q, TESTI_QUARTIERE)
    print("-" * LARGHEZZA)

    # 5. Il massimo con il suo proprietario (P16) e i casi sul bordo.
    peggiore = massimo_scostamento(interventi, ORE_PREVISTE)
    if peggiore is not None:
        scostamento, codice, squadra, quartiere, ore = peggiore
        print(f"Sforamento massimo: {scostamento:+} ore, {codice} ({squadra}, "
              f"{quartiere}: {ore} contro {ORE_PREVISTE[quartiere]})")
    # Requisito promosso: i casi sul bordo, in ordine di file.
    sul_bordo = interventi_sul_bordo(interventi, ORE_PREVISTE)
    print(f"Sul bordo (ore = previste): {', '.join(sul_bordo)}")
    print("=" * LARGHEZZA)


if __name__ == "__main__":
    main()
