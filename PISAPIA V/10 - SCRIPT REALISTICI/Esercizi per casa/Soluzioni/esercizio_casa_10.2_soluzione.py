"""
SOLUZIONE — Esercizio per casa 10.2: Il questionario di gradimento

IL PROBLEMA
Dodici risposte, un voto e un commento ciascuna, due righe sbagliate. La
direzione vuole tre cose: quanto piace ogni ambulatorio, come si
distribuiscono i voti, e di che cosa si lamenta chi dà 1 o 2.

LA STRATEGIA: SETTE PATTERN DEL CATALOGO
- P26 il caricatore e P6 la riga in campi: righe utili, numerate come le
  mostra l'editor, con i campi già puliti.
- P7 i quattro controlli, in ordine: presenza, forma, intervallo, valori
  ammessi. La variabile errore raccoglie il primo motivo trovato.
- P17 il contatore per categoria, usato QUATTRO volte con la stessa
  funzione: risposte per ambulatorio, soddisfatti per ambulatorio, voti
  per valore, parole per testo. È il punto dell'esercizio: un pezzo solo,
  quattro domande diverse.
- P18 la somma per chiave, per le medie per ambulatorio.
- P15 la media, con il caso zero gestito dal chiamante.
- P22 la classifica a coppie (valore, nome), due volte: ambulatori per
  media e parole per frequenza.

COME È DIVISO IL FILE
PARTE GENERALE: le funzioni del catalogo, con le firme della teoria; non
sanno che cosa sia un voto. PARTE SPECIFICA: costanti, validatore,
estrazione delle parole, main(). Per il gradimento di un corso di
formazione si riscrive la seconda e si copia la prima.

LIMITI NOTI DI QUESTA SOLUZIONE
- Le parole si contano così come sono scritte: "attesa" e "attese" sono
  due parole diverse. Ridurle alla stessa radice è un problema di
  linguistica, non di conteggio.
- Si tolgono le virgole e basta. Un commento con un punto o un punto
  esclamativo attaccato a una parola la conterebbe a parte ("lunga." e
  "lunga"): nel file non succede, in un questionario vero sì, e la cura è
  una catena di replace() in più (P4).
- Le parità nelle classifiche si risolvono con l'ordine alfabetico
  inverso: è l'effetto di sort(reverse=True) sulle coppie, e la traccia lo
  dichiara. Un ordine diverso a parità chiederebbe un secondo criterio.
"""

from pathlib import Path

# --- Costanti ------------------------------------------------------------
# Tre .parent: la soluzione sta un livello più in basso della traccia
# (P25, Giorno 08 §7.3).
CARTELLA_GIORNO = Path(__file__).resolve().parent.parent.parent
DATI = CARTELLA_GIORNO / "dati"
FILE_QUESTIONARIO = DATI / "questionario_gradimento.txt"

SEPARATORE = ";"
COMMENTO = "#"
CAMPI_ATTESI = 3
LARGHEZZA = 60
LARGHEZZA_BARRA = 40
LARGHEZZA_ETICHETTA = 27
SEGNO_BARRA = "#"
QUANTI_IN_CLASSIFICA = 3

AMBULATORI = ["CARDIOLOGIA", "DERMATOLOGIA", "ORTOPEDIA"]
VOTO_MINIMO = 1
VOTO_MASSIMO = 5
SODDISFATTO_DA = 4
INSODDISFATTO_FINO_A = 2
LETTERE_MINIME = 4
PER_CENTO = 100

TITOLO = "POLIAMBULATORIO AURORA - Questionario di gradimento"


# =========================================================================
# ===== PARTE GENERALE: si riusa così com'è ===============================
# =========================================================================

# P26 — Il caricatore: righe utili con il numero di riga dell'editor.
def carica_righe(percorso):
    """Restituisce [(numero_riga, campi), ...], senza righe vuote né commenti."""
    righe_utili = []
    with open(percorso, encoding="utf-8") as ingresso:
        # start=1: il numero che esce nei messaggi è quello che l'editor
        # mostra a sinistra (Giorno 08 §10.1).
        for numero, riga in enumerate(ingresso, start=1):
            testo = riga.strip()
            if testo == "" or testo.startswith(COMMENTO):
                continue
            # P6: ogni campo pulito uno per uno (Giorno 03 §7.5).
            campi = []
            for campo in testo.split(SEPARATORE):
                campi.append(campo.strip())
            righe_utili.append((numero, campi))
    return righe_utili


# P15 — La media, con una precondizione dichiarata.
def media(valori):
    """Media di una lista NON vuota: il controllo del caso zero è del chiamante."""
    return sum(valori) / len(valori)


# P17 — Il contatore per categoria.
def conta_per_chiave(chiavi):
    """Restituisce un dizionario chiave -> quante volte compare."""
    conteggi = {}
    for chiave in chiavi:
        # TRABOCCHETTO (P17, Giorno 07 §12.2): scritto conteggi[chiave] += 1
        #   il programma si ferma alla prima chiave nuova con
        #   KeyError: 'CARDIOLOGIA'. .get(chiave, 0) risponde 0 alle chiavi
        #   che il dizionario non ha ancora visto.
        conteggi[chiave] = conteggi.get(chiave, 0) + 1
    return conteggi


# P18 — La somma per chiave, da coppie (chiave, valore).
def somma_per_chiave(coppie):
    """Restituisce un dizionario chiave -> somma dei valori."""
    somme = {}
    for chiave, valore in coppie:
        somme[chiave] = somme.get(chiave, 0) + valore
    return somme


# P22 — La classifica: coppie (valore, chiave), ordine decrescente, i primi N.
def primi(dizionario, quanti):
    """Restituisce le prime `quanti` coppie (valore, chiave), valore decrescente."""
    coppie = []
    for chiave, valore in dizionario.items():
        # Il valore va PRIMA: le tuple si confrontano campo per campo, e il
        # primo campo decide l'ordine (Giorno 07 §8.3).
        # TRABOCCHETTO: con le coppie scritte (chiave, valore) la classifica
        #   ordina per nome, al contrario, e il programma non arriva nemmeno
        #   alle parole: si ferma già alla classifica per media con
        #   ValueError: Unknown format code 'f' for object of type 'str'
        #   perché al posto della media riceve 'ORTOPEDIA'. Fra le parole
        #   uscirebbero tempi, telefono, risponde, che compaiono una volta
        #   sola, e "attesa", che compare tre volte, sparirebbe.
        coppie.append((valore, chiave))
    # TRABOCCHETTO (E6): reverse=True rovescia l'ordine di TUTTA la tupla,
    #   quindi a parità di valore rovescia anche i nomi. "poca" e "lunga"
    #   valgono 2 tutte e due, ed esce prima "poca", perché p viene dopo l
    #   nell'alfabeto. Non è un errore del programma: è una regola da
    #   conoscere e da dichiarare, come fa la traccia.
    coppie.sort(reverse=True)
    return coppie[:quanti]


def riga_puntini(etichetta, valore):
    """P2 — 'Etichetta ........ valore', con i valori in colonna."""
    return f"{etichetta + ' ':.<{LARGHEZZA_ETICHETTA}} {valore}"


def barra(quota):
    """P18 — Una barra di '#' lunga quota * LARGHEZZA_BARRA."""
    # round() e non int(): con int() una quota piccola (0.02 * 40 = 0.8)
    # darebbe una barra vuota, e la categoria sembrerebbe assente.
    return SEGNO_BARRA * round(quota * LARGHEZZA_BARRA)


# =========================================================================
# ===== PARTE SPECIFICA: si cambia per un altro caso ======================
# =========================================================================

def valida_risposta(campi):
    """Restituisce ((ambulatorio, voto, commento), '') oppure (None, motivo)."""
    # Prima il conteggio dei campi, poi l'unpacking (P6).
    if len(campi) != CAMPI_ATTESI:
        return None, f"servono {CAMPI_ATTESI} campi, ne ha {len(campi)}"
    ambulatorio, testo_voto, commento = campi
    ambulatorio = ambulatorio.upper()

    # P7, i quattro controlli nell'ordine in cui ognuno protegge il
    # successivo. La catena di elif si ferma al primo che fallisce, e
    # l'utente legge un motivo solo: quello vero.
    # TRABOCCHETTO: mettete il controllo d'intervallo prima di quello di
    #   forma e il programma si ferma alla riga 9 con
    #   ValueError: invalid literal for int() with base 10: 'ottimo'.
    #   La riga 6 passa lo stesso ("6" è fatto di cifre): il difetto si
    #   vede solo quando arriva un voto scritto in lettere.
    errore = ""
    if ambulatorio == "":
        errore = "ambulatorio mancante"
    elif not testo_voto.isdecimal():
        errore = f"voto non numerico: '{testo_voto}'"
    elif not VOTO_MINIMO <= int(testo_voto) <= VOTO_MASSIMO:
        errore = f"voto fuori scala {VOTO_MINIMO}-{VOTO_MASSIMO}: {testo_voto}"
    elif ambulatorio not in AMBULATORI:
        errore = f"ambulatorio sconosciuto: {ambulatorio}"

    if errore:
        return None, errore
    return (ambulatorio, int(testo_voto), commento), ""


def parole_del_commento(commento):
    """Restituisce le parole di almeno LETTERE_MINIME lettere, in minuscolo."""
    # Minuscolo PRIMA di contare: "Attesa" a inizio frase e "attesa" in
    # fondo sono la stessa parola (P4).
    # TRABOCCHETTO: senza .lower() la classifica diventa lunga 2, Attesa 2,
    #   tempi 1. "attesa" si divide fra la forma maiuscola (2) e quella
    #   minuscola (1), e la lamentela più frequente del poliambulatorio
    #   scende al secondo posto.
    # TRABOCCHETTO: senza togliere le virgole, "lunga," della riga 8 è una
    #   parola diversa da "lunga": lunga scende a 1 e la classifica diventa
    #   attesa 3, poca 2, tempi 1.
    testo = commento.lower().replace(",", "")
    parole = []
    for parola in testo.split():
        if len(parola) >= LETTERE_MINIME:
            parole.append(parola)
    return parole


def quota(parte, totale):
    """Frazione parte / totale, oppure 0.0 se il totale è zero."""
    # Il caso zero di P15, detto una volta sola: nessuna percentuale del
    # programma può dividere per zero.
    if totale == 0:
        return 0.0
    return parte / totale


def stampa_tabella(conteggi, somme, soddisfatti, totale, somma_voti,
                   totale_soddisfatti):
    """Stampa la tabella per ambulatorio e la riga TUTTI."""
    print(f"{'AMBULATORIO':<14}{'RISPOSTE':>10}{'MEDIA':>8}{'SODDISFATTI':>16}")
    # Si scorre la COSTANTE, non il dizionario: l'ordine è fisso e un
    # ambulatorio senza risposte valide compare lo stesso, con i trattini.
    for ambulatorio in AMBULATORI:
        risposte = conteggi.get(ambulatorio, 0)
        if risposte == 0:
            print(f"{ambulatorio:<14}{risposte:>10}{'-':>8}{'-':>16}")
            continue
        media_voti = somme[ambulatorio] / risposte
        contenti = soddisfatti.get(ambulatorio, 0)
        rapporto = f"{contenti}/{risposte}"
        print(f"{ambulatorio:<14}{risposte:>10}{media_voti:>8.2f}"
              f"{rapporto:>8}{quota(contenti, risposte):>8.1%}")
    print("-" * LARGHEZZA)
    rapporto = f"{totale_soddisfatti}/{totale}"
    print(f"{'TUTTI':<14}{totale:>10}{quota(somma_voti, totale):>8.2f}"
          f"{rapporto:>8}{quota(totale_soddisfatti, totale):>8.1%}")


def main():
    """Legge il questionario e stampa il gradimento per ambulatorio."""
    print("=" * LARGHEZZA)
    print(TITOLO)
    print("=" * LARGHEZZA)

    # 1. CARICA, con il file che manca prevenuto (Giorno 08 §8.1).
    if not FILE_QUESTIONARIO.exists():
        print(f"[ERRORE] {FILE_QUESTIONARIO.name} non trovato nella cartella dati.")
        print("=" * LARGHEZZA)
        return
    righe = carica_righe(FILE_QUESTIONARIO)
    print(f"File letto: {FILE_QUESTIONARIO.name}")

    # 2. VALIDA: i buoni in una lista, gli scarti stampati con il motivo.
    risposte = []
    for numero, campi in righe:
        risposta, motivo = valida_risposta(campi)
        if risposta is None:
            print(f"[!] riga {numero:>2}  {motivo}")
            continue
        risposte.append(risposta)
    print(riga_puntini("Righe lette", len(righe)))
    print(riga_puntini("Risposte valide", len(risposte)))
    print(riga_puntini("Righe scartate", len(righe) - len(risposte)))
    print("-" * LARGHEZZA)

    # 3. ELABORA. Si preparano le liste che i pattern generali si
    #    aspettano: chiavi per P17, coppie per P18. Il lavoro specifico è
    #    solo questo, scegliere che cosa mettere nelle liste.
    ambulatori_risposte = []
    coppie_voti = []
    ambulatori_contenti = []
    voti = []
    commenti_negativi = []
    for ambulatorio, voto, commento in risposte:
        ambulatori_risposte.append(ambulatorio)
        coppie_voti.append((ambulatorio, voto))
        voti.append(voto)
        # TRABOCCHETTO: con > al posto di >= il voto 4 non conta più come
        #   soddisfatto. CARDIOLOGIA scende a 1/3 33.3%, DERMATOLOGIA a
        #   2/3 66.7%, TUTTI a 3/10 30.0% e il saldo di gradimento a
        #   +0.0 punti. Nessun errore: solo un poliambulatorio che sembra
        #   piacere a metà dei pazienti di prima.
        if voto >= SODDISFATTO_DA:
            ambulatori_contenti.append(ambulatorio)
        if voto <= INSODDISFATTO_FINO_A:
            commenti_negativi.append(commento)

    conteggi = conta_per_chiave(ambulatori_risposte)
    somme = somma_per_chiave(coppie_voti)
    soddisfatti = conta_per_chiave(ambulatori_contenti)
    totale = len(risposte)
    totale_soddisfatti = len(ambulatori_contenti)
    totale_insoddisfatti = len(commenti_negativi)

    # 4. RIPORTA: tabella per ambulatorio.
    # La media globale divide per le risposte VALIDE (10), non per le righe
    # lette (12): due righe scartate non hanno un voto da dividere, e
    # contarle al denominatore farebbe scendere la media TUTTI a 2.83.
    stampa_tabella(conteggi, somme, soddisfatti, totale, sum(voti),
                   totale_soddisfatti)
    print("-" * LARGHEZZA)

    # Requisito promosso: la classifica per media. P22 vuole un dizionario
    # chiave -> valore: lo si costruisce qui, per i soli ambulatori che
    # hanno risposte (il caso zero, ancora una volta).
    medie = {}
    for ambulatorio in conteggi:
        medie[ambulatorio] = somme[ambulatorio] / conteggi[ambulatorio]
    print("CLASSIFICA PER MEDIA")
    posizione = 1
    for valore, ambulatorio in primi(medie, QUANTI_IN_CLASSIFICA):
        print(f"{posizione}. {ambulatorio:<16}{valore:.2f}")
        posizione += 1
    print("-" * LARGHEZZA)

    # La distribuzione: P17 sui voti, poi un ciclo su TUTTA la scala, non
    # sul dizionario. Così un voto che nessuno ha dato compare con zero,
    # e la scala si legge intera.
    distribuzione = conta_per_chiave(voti)
    print("DISTRIBUZIONE DEI VOTI")
    for voto in range(VOTO_MINIMO, VOTO_MASSIMO + 1):
        quanti = distribuzione.get(voto, 0)
        print(f"voto {voto} {quanti:>4} {barra(quota(quanti, totale))}")
    print("-" * LARGHEZZA)

    # Requisito promosso: insoddisfatti e saldo. Il saldo è una differenza
    # fra due percentuali, quindi si esprime in punti, non in percento:
    # passare da 50% a 55% è +5 punti, non +10%.
    percento_contenti = quota(totale_soddisfatti, totale) * PER_CENTO
    percento_scontenti = quota(totale_insoddisfatti, totale) * PER_CENTO
    saldo = percento_contenti - percento_scontenti
    print(riga_puntini("Soddisfatti", f"{totale_soddisfatti} "
                       f"({quota(totale_soddisfatti, totale):.1%})"))
    print(riga_puntini("Insoddisfatti", f"{totale_insoddisfatti} "
                       f"({quota(totale_insoddisfatti, totale):.1%})"))
    # Il segno + esplicito (:+.1f) dice a colpo d'occhio da che parte pende
    # il gradimento.
    print(riga_puntini("Saldo di gradimento", f"{saldo:+.1f} punti"))
    print("-" * LARGHEZZA)

    # Le parole dei commenti negativi: estrarle è specifico, contarle e
    # classificarle è generale (P17 + P22, identici a sopra).
    parole = []
    for commento in commenti_negativi:
        for parola in parole_del_commento(commento):
            parole.append(parola)
    print(f"PAROLE NEI COMMENTI NEGATIVI ({len(commenti_negativi)} commenti)")
    posizione = 1
    for quante, parola in primi(conta_per_chiave(parole), QUANTI_IN_CLASSIFICA):
        print(f"{posizione}. {parola:<16}{quante}")
        posizione += 1
    print("=" * LARGHEZZA)


if __name__ == "__main__":
    main()
