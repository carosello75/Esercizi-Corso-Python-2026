"""
P13 — La sentinella: leggere finché non arriva il segnale di fine

Catalogo dei pattern, Giorno 10 — capitolo 6, Ripetere
Teoria: TEORIA_GIORNO_10.md §6.1

IN SINTESI
Legge dati in quantità ignota finché non arriva il valore di fine, con una
lettura prima del ciclo e una in coda al corpo.

DESCRIZIONE
Il file fissa la costante SENTINELLA e simula la tastiera con la lista
RISPOSTE; la funzione leggi() riceve la lista e una posizione, stampa l'eco
e restituisce la risposta normalizzata con .strip().upper(). Una prima
lettura precede il while, che prosegue finché il codice letto è diverso
dalla sentinella: il corpo aggiunge il codice a codici con .append(),
incrementa posizione e rilegge in coda. La sentinella scritta come Fine con
spazi viene riconosciuta, e il programma stampa i 2 codici registrati e 1
risposta mai letta.

LO SCHEMA
La forma degli esercizi, con la tastiera vera.

Lo schema sta qui sotto, subito dopo questa docstring, come blocco
commentato: è uno stampo, non un programma, e non ha output. Si copia nel
proprio script, si tolgono i commenti (Ctrl+/ in PyCharm, Cmd+/ su Mac) e si
cambiano solo le righe marcate # <-- adattare.

IN AZIONE
Il codice eseguibile di questo file è l'In azione: lanciatelo, e l'output
deve essere quello di ESEMPIO OUTPUT in fondo a questa docstring.

VARIANTI
- while True con una lettura sola in testa e break sulla sentinella (Giorno
  05 §8.4).

- Da un file: readline() restituisce la stringa vuota a fine file, la
  sentinella che il disco vi dà gratis (Giorno 08 §4.4).

ERRORI TIPICI
- La sentinella confrontata prima della normalizzazione (nel codice qui
  sotto).

- La conversione prima del controllo: con codici numerici, int(testo)
  scritto prima del confronto si ferma sulla parola di chiusura con
  ValueError: invalid literal for int() with base 10: 'fine' (Giorno 05
  §9.5).

DA DOVE VIENE
Giorno 05 §8.4, §9.2, §9.3, §9.4, §9.5 · Giorno 08 §4.4

DOVE SI USA NEGLI ESERCIZI
10.9

ESEMPIO OUTPUT
Codice collo: ls01
Codice collo: LS02
Codice collo:   Fine
Codici registrati: 2 -> ['LS01', 'LS02']
Risposte mai lette: 1
"""

# ==========================================================================
# LO SCHEMA — lo stampo da copiare. Non si esegue: è commentato.
# ==========================================================================
# SENTINELLA = "FINE"                                  # <-- adattare
# PROMPT = "Codice (FINE per chiudere): "              # <-- adattare
#
# codici = []
# # Doppia lettura: la prima, fuori dal ciclo, inizializza la condizione
# # del while; la seconda, in coda al corpo, prepara il confronto seguente.
# testo = input(PROMPT).strip().upper()
# while testo != SENTINELLA:
#     codici.append(testo)                             # <-- adattare: il lavoro
#     testo = input(PROMPT).strip().upper()
# print(f"Letti {len(codici)} codici")


# ==========================================================================
# IN AZIONE — lo schema su un caso del corso. Si esegue.
# ==========================================================================
SENTINELLA = "FINE"
RISPOSTE = ["ls01", "LS02", "  Fine", "LS03"]


def leggi(risposte, posizione):
    """Simula la tastiera: stampa l'eco e restituisce la risposta normalizzata."""
    print(f"Codice collo: {risposte[posizione]}")
    return risposte[posizione].strip().upper()


codici = []
posizione = 0
# 1. Lettura iniziale fuori dal ciclo: la condizione del while viene
#    valutata su un valore gia' assegnato.
codice = leggi(RISPOSTE, posizione)
while codice != SENTINELLA:
    codici.append(codice)
    # 2. Rilettura in coda al corpo: il confronto successivo valuta il dato
    #    appena letto, non quello gia' elaborato.
    posizione += 1
    codice = leggi(RISPOSTE, posizione)
print(f"Codici registrati: {len(codici)} -> {codici}")
print(f"Risposte mai lette: {len(RISPOSTE) - posizione - 1}")

# TRABOCCHETTO: confrontando la risposta grezza, "  Fine" non e' "FINE": il
#   ciclo prosegue, legge LS03, e poi l'indice esce dalla lista con IndexError:
#   list index out of range. Alla tastiera vera il programma non si ferma.
