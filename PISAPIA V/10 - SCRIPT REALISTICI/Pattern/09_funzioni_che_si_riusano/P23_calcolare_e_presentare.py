"""
P23 — Calcolare e presentare: calcola_ restituisce, stampa_ stampa

Catalogo dei pattern, Giorno 10 — capitolo 9, Funzioni che si riusano
Teoria: TEORIA_GIORNO_10.md §9.1

IN SINTESI
Separa il calcolo dalla presentazione: la funzione calcola_ restituisce il
valore senza stamparlo, la funzione stampa_ lo formatta senza restituire
nulla.

DESCRIZIONE
Il file definisce LISTINO, la tariffa al chilo per zona, le richieste
(codice, zona, peso) in RICHIESTE e TETTO_SPESA. calcola_costo() riceve
peso, zona e listino e restituisce listino[zona] * peso senza stampare;
stampa_preventivo() riceve codice, zona, peso e costo e stampa la riga
incolonnata, senza restituire nulla. In main(), avviato dalla guardia if
__name__ == "__main__", ogni costo restituito viene stampato e sommato a
totale; dopo il ciclo si stampa il totale, 110.40, e, poiché supera il
tetto, un avviso con l'eccedenza di 10.40.

LO SCHEMA
Lo schema sta qui sotto, subito dopo questa docstring, come blocco
commentato: è uno stampo, non un programma, e non ha output. Si copia nel
proprio script, si tolgono i commenti (Ctrl+/ in PyCharm, Cmd+/ su Mac) e si
cambiano solo le righe marcate # <-- adattare.

IN AZIONE
Il codice eseguibile di questo file è l'In azione: lanciatelo, e l'output
deve essere quello di ESEMPIO OUTPUT in fondo a questa docstring.

VARIANTI
La funzione che restituisce la riga invece di stamparla
(componi_preventivo()), che main() manda a video e su file: è il ponte verso
P28. Costo e avviso restituiti insieme con il return multiplo (Giorno 06
§10.1).

ERRORI TIPICI
- print al posto di return → TypeError su NoneType lontano dalla causa.

- Argomenti nell'ordine sbagliato, calcola_costo(zona, peso, LISTINO) →
  KeyError: 7.2: il dizionario viene interrogato con il peso.

DA DOVE VIENE
Giorno 06 §5.1, §5.2, §6.2, §7.1, §7.2, §12.2, §14.2

DOVE SI USA NEGLI ESERCIZI
10.4, 10.6, casa_10.4

ESEMPIO OUTPUT
LS-0510  SUD       7.2 kg     68.40 euro
LS-0511  ISOLE     3.0 kg     42.00 euro
Totale preventivi: 110.40 euro
[!] tetto di 100.00 superato di 10.40
"""

# ==========================================================================
# LO SCHEMA — lo stampo da copiare. Non si esegue: è commentato.
# ==========================================================================
# def calcola_costo(peso, zona, listino):  # <-- adattare: nome e parametri
#     """Restituisce il numero. Non stampa niente."""
#     return listino[zona] * peso  # <-- adattare: la formula del caso
#
#
# def stampa_preventivo(codice, costo):  # <-- adattare
#     """Stampa il numero. Non calcola, non restituisce niente."""
#     print(f"{codice}  {costo:>10.2f} euro")  # <-- adattare: il formato (P2)
#
#
# # Il chiamante conserva il valore di ritorno in una variabile e lo
# # riusa senza ricalcolarlo: calcolo e presentazione restano separati.
# costo = calcola_costo(peso, zona, LISTINO)
# stampa_preventivo(codice, costo)


# ==========================================================================
# IN AZIONE — lo schema su un caso del corso. Si esegue.
# ==========================================================================
LISTINO = {"NORD": 8.50, "CENTRO": 7.00, "SUD": 9.50, "ISOLE": 14.00}
RICHIESTE = [("LS-0510", "SUD", 7.2), ("LS-0511", "ISOLE", 3.0)]
TETTO_SPESA = 100.00


def calcola_costo(peso, zona, listino):
    return listino[zona] * peso


def stampa_preventivo(codice, zona, peso, costo):
    print(f"{codice}  {zona:<7}{peso:>6.1f} kg{costo:>10.2f} euro")


def main():
    totale = 0.0
    for codice, zona, peso in RICHIESTE:
        # 1. Un solo valore di ritorno, tre usi: presentazione, accumulo nel
        #    totale, confronto con la soglia.
        costo = calcola_costo(peso, zona, LISTINO)
        stampa_preventivo(codice, zona, peso, costo)
        totale += costo
    print(f"Totale preventivi: {totale:.2f} euro")
    # 2. Il confronto opera sul float: la stringa prodotta dalla
    #    formattazione non e' confrontabile con TETTO_SPESA.
    if totale > TETTO_SPESA:
        eccedenza = totale - TETTO_SPESA
        print(f"[!] tetto di {TETTO_SPESA:.2f} superato di {eccedenza:.2f}")


if __name__ == "__main__":
    main()

# TRABOCCHETTO: con print(listino[zona] * peso) al posto del return, la
#   funzione stampa il costo nudo, 68.4, e restituisce None. Il programma si
#   ferma una riga dopo, dentro stampa_preventivo, con TypeError: unsupported
#   format string passed to NoneType.__format__ (Giorno 06 §6.2).
