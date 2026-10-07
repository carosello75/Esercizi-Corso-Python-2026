"""
P15 — Totale, conteggio e media, con il caso zero elementi

Catalogo dei pattern, Giorno 10 — capitolo 7, Accumulare e contare
Teoria: TEORIA_GIORNO_10.md §7.1

IN SINTESI
Accumula somma e conteggio di una serie di valori e ne calcola la media solo
dopo aver escluso il caso di zero elementi.

DESCRIZIONE
Il file parte dalla lista PUNTEGGI_TURNO e dalla costante SOGLIA_BUONO, e
definisce media(), che restituisce sum(valori) / len(valori) con la
precondizione di lista non vuota. Un for la applica a un turno pieno e a uno
vuoto: il turno vuoto, falso per if not turno, stampa che la media non è
calcolabile invece di dividere. Poi due accumulatori, somma e quanti,
inizializzati fuori dal ciclo, raccolgono solo i valori maggiori di 70:
escono 4 valori con media 83.75.

LO SCHEMA
Lo schema sta qui sotto, subito dopo questa docstring, come blocco
commentato: è uno stampo, non un programma, e non ha output. Si copia nel
proprio script, si tolgono i commenti (Ctrl+/ in PyCharm, Cmd+/ su Mac) e si
cambiano solo le righe marcate # <-- adattare.

IN AZIONE
Il codice eseguibile di questo file è l'In azione: lanciatelo, e l'output
deve essere quello di ESEMPIO OUTPUT in fondo a questa docstring.

VARIANTI
- if not valori: return 0.0 nella funzione: comodo, ma turno vuoto e turno a
  zero diventano indistinguibili.

ERRORI TIPICI
- L'accumulatore inizializzato dentro il ciclo si azzera a ogni giro.

- La divisione senza il caso zero: ZeroDivisionError, anche su una lista
  piena quando il filtro non lascia passare niente (nel codice qui sotto).

DA DOVE VIENE
Giorno 04 §11.2 · Giorno 05 §6.2, §6.3, §6.4 · Giorno 07 §9.1, §9.3 · Giorno
09 §8.4

DOVE SI USA NEGLI ESERCIZI
10.1, 10.4, 10.7, casa_10.1, casa_10.2, casa_10.4

ERRORI TIPICI DELLA GIORNATA COLLEGATI (teoria, capitolo 14)
- E2 — Il contatore azzerato dentro il ciclo: la categoria che vale sempre 1

ESEMPIO OUTPUT
Somma 596, valori 8, media 74.50
Nessun dato: media non calcolabile
Sopra 70: 4 valori, media 83.75
"""

# ==========================================================================
# LO SCHEMA — lo stampo da copiare. Non si esegue: è commentato.
# ==========================================================================
# def media(valori):
#     """Restituisce la media. Precondizione: la lista non e' vuota."""
#     return sum(valori) / len(valori)
#
#
# # Il caso della lista vuota lo gestisce il chiamante, prima della
# # divisione: media() ha la precondizione di lista non vuota.
# if valori:                                           # <-- adattare: la lista
#     print(f"Media: {media(valori):.2f}")
# else:
#     print("Nessun dato: media non calcolabile")      # <-- adattare


# ==========================================================================
# IN AZIONE — lo schema su un caso del corso. Si esegue.
# ==========================================================================
PUNTEGGI_TURNO = [72, 88, 65, 91, 70, 84, 59, 67]
SOGLIA_BUONO = 70


def media(valori):
    """Restituisce la media. Precondizione: la lista non e' vuota."""
    return sum(valori) / len(valori)


for turno in [PUNTEGGI_TURNO, []]:
    # 1. Una lista vuota ha valore di verita' falso (Giorno 04 §11.2): il
    #    caso zero si intercetta qui, prima di chiamare media().
    if not turno:
        print("Nessun dato: media non calcolabile")
        continue
    print(f"Somma {sum(turno)}, valori {len(turno)}, media {media(turno):.2f}")

# 2. Con un filtro sum() e len() non bastano: servono due accumulatori,
#    inizializzati fuori dal ciclo e aggiornati solo nel ramo filtrato.
somma = 0
quanti = 0
for valore in PUNTEGGI_TURNO:
    if valore > SOGLIA_BUONO:
        somma += valore
        quanti += 1
print(f"Sopra {SOGLIA_BUONO}: {quanti} valori, media {somma / quanti:.2f}")

# TRABOCCHETTO: il 70 sta sul bordo. Con >= entra anche lui: 5 valori e
#   media 81.00. E se nessun valore passasse il filtro, quanti resterebbe 0:
#   ZeroDivisionError: division by zero, sulla riga della print.
