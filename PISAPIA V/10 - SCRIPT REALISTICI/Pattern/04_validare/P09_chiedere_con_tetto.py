"""
P9 — Chiedere finché il dato è buono: ciclo di richiesta con un tetto ai
    tentativi

Catalogo dei pattern, Giorno 10 — capitolo 4, Validare
Teoria: TEORIA_GIORNO_10.md §4.3

IN SINTESI
Richiede un dato finché non è valido, entro un numero massimo di tentativi,
e restituisce il valore o un segnale di mancata acquisizione.

DESCRIZIONE
Il file fissa il tetto TENTATIVI_MASSIMI, il valore di ripiego NESSUN_VALORE
e l'intervallo dei colli. chiedi_intero() riceve una lista di risposte
simulate e i due estremi: scorre la fetta risposte[:TENTATIVI_MASSIMI],
stampa l'eco di ogni risposta, converte con int() in un try che sul
ValueError passa oltre con continue, e restituisce il primo valore
nell'intervallo; esauriti i tentativi stampa l'avviso e restituisce
NESSUN_VALORE. Il chiamante la prova su due serie: la prima registra 7
colli, la seconda esaurisce il tetto e non registra niente.

LO SCHEMA
La forma degli esercizi, con la tastiera vera: la firma riceve il testo
della domanda.

Lo schema sta qui sotto, subito dopo questa docstring, come blocco
commentato: è uno stampo, non un programma, e non ha output. Si copia nel
proprio script, si tolgono i commenti (Ctrl+/ in PyCharm, Cmd+/ su Mac) e si
cambiano solo le righe marcate # <-- adattare.

IN AZIONE
Il codice eseguibile di questo file è l'In azione: lanciatelo, e l'output
deve essere quello di ESEMPIO OUTPUT in fondo a questa docstring.

VARIANTI
- while True con un contatore dei tentativi e break, equivalente al for
  (Giorno 05 §13.2).

- converti_intero() di P8 al posto del try in linea: il ciclo resta.

ERRORI TIPICI
- Il while True senza tetto: chi non sa rispondere resta bloccato.

- Il continue dimenticato nel gestore (nel codice qui sotto):
  UnboundLocalError dentro la funzione, NameError fuori (Giorno 09 §4.6).

DA DOVE VIENE
Giorno 03 §3.4 · Giorno 05 §13.1, §13.2 · Giorno 06 §5.4 · Giorno 09 §4.6,
§8.7, §12.4

DOVE SI USA NEGLI ESERCIZI
10.7

ESEMPIO OUTPUT
Colli da spedire: zero
[ERRORE] Serve un numero intero, per esempio 7.
Colli da spedire: 0
[ERRORE] Ammessi da 1 a 50 colli.
Colli da spedire: 7
Registrati 7 colli.
Colli da spedire: tanti
[ERRORE] Serve un numero intero, per esempio 7.
Colli da spedire: 99
[ERRORE] Ammessi da 1 a 50 colli.
Colli da spedire: -1
[ERRORE] Ammessi da 1 a 50 colli.
[!] Troppi tentativi: la spedizione passa all'operatore.
Nessun valore registrato.
"""

# ==========================================================================
# LO SCHEMA — lo stampo da copiare. Non si esegue: è commentato.
# ==========================================================================
# TENTATIVI_MASSIMI = 3
# NESSUN_VALORE = -1
#
#
# def chiedi_intero(prompt, minimo, massimo):
#     """Chiede un intero fra minimo e massimo; oltre il tetto, NESSUN_VALORE."""
#     for tentativo in range(TENTATIVI_MASSIMI):
#         testo = input(prompt)
#         try:
#             valore = int(testo)
#         except ValueError:
#             print("[ERRORE] Serve un numero intero.")          # <-- adattare
#             continue
#         if minimo <= valore <= massimo:
#             return valore
#         print(f"[ERRORE] Ammessi da {minimo} a {massimo}.")    # <-- adattare
#     print("[!] Troppi tentativi.")                             # <-- adattare
#     return NESSUN_VALORE


# ==========================================================================
# IN AZIONE — lo schema su un caso del corso. Si esegue.
# ==========================================================================
TENTATIVI_MASSIMI = 3
NESSUN_VALORE = -1
COLLI_MINIMI = 1
COLLI_MASSIMI = 50


def chiedi_intero(risposte, minimo, massimo):
    """Restituisce la prima risposta intera nell'intervallo, o NESSUN_VALORE."""
    # La fetta [:TENTATIVI_MASSIMI] impone il tetto: le risposte oltre il
    # limite non vengono mai lette.
    for testo in risposte[:TENTATIVI_MASSIMI]:
        print(f"Colli da spedire: {testo}")
        try:
            valore = int(testo)
        except ValueError:
            print("[ERRORE] Serve un numero intero, per esempio 7.")
            continue
        if minimo <= valore <= massimo:
            return valore
        print(f"[ERRORE] Ammessi da {minimo} a {massimo} colli.")
    print("[!] Troppi tentativi: la spedizione passa all'operatore.")
    return NESSUN_VALORE


for risposte in [["zero", "0", "7"], ["tanti", "99", "-1", "5"]]:
    colli = chiedi_intero(risposte, COLLI_MINIMI, COLLI_MASSIMI)
    if colli == NESSUN_VALORE:
        print("Nessun valore registrato.")
    else:
        print(f"Registrati {colli} colli.")

# TRABOCCHETTO: senza il continue nel gestore, al primo "zero" il programma
#   arriverebbe al confronto con valore mai assegnato e si fermerebbe con
#   UnboundLocalError: cannot access local variable 'valore' where it is not
#   associated with a value.
