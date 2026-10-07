"""
P1 — Lo scheletro dello script: docstring, costanti, funzioni, main() e
    guardia

Catalogo dei pattern, Giorno 10 — capitolo 2, L'uscita: la pagina che si legge
Teoria: TEORIA_GIORNO_10.md §2.1

IN SINTESI
Ordina uno script in docstring, costanti, funzioni e un main() di regia,
avviato solo dalla guardia __name__.

DESCRIZIONE
Il file definisce le costanti NEGOZIO e ACQUISTI, una lista di tuple
(articolo, quantita, prezzo), e la funzione totale_riga(), che riceve
quantità e prezzo e restituisce il loro prodotto senza stampare. main()
stampa l'intestazione, inizializza l'accumulatore totale a 0.0 e, in un for
con unpacking, calcola l'importo di ogni riga, lo somma e lo stampa
incolonnato; chiude con la riga TOTALE di 109.70, allineata agli importi. La
chiamata a main() sta sotto la guardia if __name__ == "__main__":, quindi
parte solo quando il file è eseguito direttamente.

LO SCHEMA
Lo schema sta qui sotto, subito dopo questa docstring, come blocco
commentato: è uno stampo, non un programma, e non ha output. Si copia nel
proprio script, si tolgono i commenti (Ctrl+/ in PyCharm, Cmd+/ su Mac) e si
cambiano solo le righe marcate # <-- adattare.

IN AZIONE
Il codice eseguibile di questo file è l'In azione: lanciatelo, e l'output
deve essere quello di ESEMPIO OUTPUT in fondo a questa docstring.

VARIANTI
- Costanti calcolate da altre costanti: FATTORE_IVA = 1 + ALIQUOTA_IVA / 100
  (Giorno 02 §14.3).

- main() che chiama carica(), calcola() e stampa(): la forma di P34.

ERRORI TIPICI
- return quantita * 49.90: un numero magico, da cercare in tutto il file il
  giorno che il prezzo cambia.

- La chiamata al livello del modulo scritta sopra il def: NameError: name
  'totale_riga' is not defined. Python legge dall'alto (Giorno 06 §3.4).

DA DOVE VIENE
Giorno 01 §13.3, §13.5, §15.1 · Giorno 02 §14.2 · Giorno 06 §1.3, §3.4,
§3.5, §13.1

DOVE SI USA NEGLI ESERCIZI
10.1, 10.2

ESEMPIO OUTPUT
--- NovaStore ---
2 x Cuffie Bluetooth   99.80
1 x Cavo HDMI 2 m       9.90
TOTALE                109.70
"""

# ==========================================================================
# LO SCHEMA — lo stampo da copiare. Non si esegue: è commentato.
# ==========================================================================
# """Che cosa fa lo script, da dove prende i dati, che cosa produce."""
#
# VALORE_DI_PROVA = 3                                  # <-- adattare
# FATTORE = 1.22                                       # <-- adattare
#
#
# def calcola(valore):                                 # <-- adattare
#     """Restituisce il risultato del calcolo: non stampa niente."""
#     return valore * FATTORE
#
#
# def main():
#     """Il regista: chiama le funzioni in ordine, i conti li fanno loro."""
#     risultato = calcola(VALORE_DI_PROVA)
#     print(f"Risultato: {risultato:.2f}")             # <-- adattare
#
#
# if __name__ == "__main__":
#     main()


# ==========================================================================
# IN AZIONE — lo schema su un caso del corso. Si esegue.
# ==========================================================================
"""Scontrino NovaStore: righe dell'acquisto e totale."""

NEGOZIO = "NovaStore"
ACQUISTI = [("Cuffie Bluetooth", 2, 49.90), ("Cavo HDMI 2 m", 1, 9.90)]


def totale_riga(quantita, prezzo):
    """Restituisce l'importo di una riga: quantita' per prezzo unitario."""
    return quantita * prezzo


def main():
    """Stampa le righe dello scontrino e il totale."""
    print(f"--- {NEGOZIO} ---")
    totale = 0.0
    for articolo, quantita, prezzo in ACQUISTI:
        importo = totale_riga(quantita, prezzo)
        totale += importo
        print(f"{quantita} x {articolo:<17}{importo:>7.2f}")
    # 21 = 4 (il prefisso "2 x ", con quantita' a una cifra) + 17 (colonna
    # articolo): l'etichetta del totale occupa la stessa larghezza, cosi'
    # l'importo resta in colonna.
    print(f"{'TOTALE':<21}{totale:>7.2f}")


# TRABOCCHETTO: senza la guardia, main() verrebbe eseguito anche quando un
#   altro script importa da questo modulo solo totale_riga(): l'import
#   produrrebbe come side effect lo scontrino, dentro un programma altrui.
if __name__ == "__main__":
    main()
