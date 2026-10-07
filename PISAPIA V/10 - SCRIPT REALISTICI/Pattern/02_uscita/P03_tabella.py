"""
P3 — La tabella a larghezza fissa: intestazione, righe, separatori e il
    testo che sfonda

Catalogo dei pattern, Giorno 10 — capitolo 2, L'uscita: la pagina che si legge
Teoria: TEORIA_GIORNO_10.md §2.3

IN SINTESI
Stampa più record come tabella a colonne fisse, con intestazione, separatori
calcolati e testo troncato con lo slicing per non sfondare.

DESCRIZIONE
Il file tiene il listino LogiSud in LISTINO, una lista di tuple (zona,
descrizione, prezzo), e le larghezze in tre costanti, da cui calcola
LARGHEZZA_TABELLA. Stampa l'intestazione e un separatore lungo quanto la
tabella; poi un for con unpacking tronca ogni descrizione con la fetta
descrizione[:COL_DESCRIZIONE] e stampa la riga con il testo a sinistra e il
prezzo a destra, con due decimali. Dopo il separatore finale, la prova del
trabocchetto calcola che senza la fetta la riga ISOLE sarebbe di 41
caratteri invece di 30.

LO SCHEMA
Lo schema sta qui sotto, subito dopo questa docstring, come blocco
commentato: è uno stampo, non un programma, e non ha output. Si copia nel
proprio script, si tolgono i commenti (Ctrl+/ in PyCharm, Cmd+/ su Mac) e si
cambiano solo le righe marcate # <-- adattare.

IN AZIONE
Il codice eseguibile di questo file è l'In azione: lanciatelo, e l'output
deve essere quello di ESEMPIO OUTPUT in fondo a questa docstring.

VARIANTI
- Riga di totale sotto un secondo separatore, con l'etichetta larga quanto
  due colonne: f"{'TOTALE':<{COL_ZONA + COL_DESCRIZIONE}}".

- Troncamento dichiarato: tagliare a COL_DESCRIZIONE - 1 e aggiungere un
  punto.

ERRORI TIPICI
- Il testo lungo sposta tutta la riga (nel codice qui sotto): la larghezza è
  un minimo.

- Numeri allineati a sinistra: 14.00 sembra più piccolo di 8.50 (Giorno 03
  §9.3). E l'ultima colonna di testo a sinistra lascia spazi in coda (§9.6).

DA DOVE VIENE
Giorno 02 §9.3 · Giorno 03 §9.1, §9.3, §9.4, §9.5, §9.6, §9.7

DOVE SI USA NEGLI ESERCIZI
10.1, 10.9, 10.10, casa_10.3

ESEMPIO OUTPUT
ZONA    DESCRIZIONE     PREZZO
------------------------------
NORD    Nord Italia       8.50
CENTRO  Centro            7.00
SUD     Sud Italia        9.50
ISOLE   Isole maggio     14.00
------------------------------
Senza fetta la riga ISOLE sarebbe di 41 caratteri, non 30.
"""

# ==========================================================================
# LO SCHEMA — lo stampo da copiare. Non si esegue: è commentato.
# ==========================================================================
# COL_CHIAVE = 8                                       # <-- adattare
# COL_TESTO = 12                                       # <-- adattare
# COL_NUMERO = 10                                      # <-- adattare
# LARGHEZZA_TABELLA = COL_CHIAVE + COL_TESTO + COL_NUMERO
#
# righe = [("A", "testo", 1.0)]                        # <-- adattare
#
# print(f"{'CHIAVE':<{COL_CHIAVE}}{'TESTO':<{COL_TESTO}}{'NUMERO':>{COL_NUMERO}}")
# print("-" * LARGHEZZA_TABELLA)
# for chiave, testo, numero in righe:
#     # Lo slicing tronca alla larghezza della colonna; su un testo piu' corto
#     # restituisce la stringa intera, quindi e' sicuro su ogni valore.
#     print(f"{chiave:<{COL_CHIAVE}}{testo[:COL_TESTO]:<{COL_TESTO}}"
#           f"{numero:>{COL_NUMERO}.2f}")


# ==========================================================================
# IN AZIONE — lo schema su un caso del corso. Si esegue.
# ==========================================================================
LISTINO = [
    ("NORD", "Nord Italia", 8.50),
    ("CENTRO", "Centro", 7.00),
    ("SUD", "Sud Italia", 9.50),
    ("ISOLE", "Isole maggiori e minori", 14.00),
]
COL_ZONA = 8
COL_DESCRIZIONE = 12
COL_PREZZO = 10
# Larghezza derivata dalle colonne: modificando una costante, anche i
# separatori si adeguano senza altri interventi.
LARGHEZZA_TABELLA = COL_ZONA + COL_DESCRIZIONE + COL_PREZZO

print(f"{'ZONA':<{COL_ZONA}}{'DESCRIZIONE':<{COL_DESCRIZIONE}}"
      f"{'PREZZO':>{COL_PREZZO}}")
print("-" * LARGHEZZA_TABELLA)
for zona, descrizione, prezzo in LISTINO:
    # La descrizione piu' lunga ha 23 caratteri e la colonna 12: la fetta
    # [:COL_DESCRIZIONE] tronca a 12 e garantisce la larghezza della riga.
    breve = descrizione[:COL_DESCRIZIONE]
    print(f"{zona:<{COL_ZONA}}{breve:<{COL_DESCRIZIONE}}{prezzo:>{COL_PREZZO}.2f}")
print("-" * LARGHEZZA_TABELLA)
# TRABOCCHETTO: :<12 non tronca. La larghezza di formato e' un minimo, non
#   un massimo: senza la fetta, la riga ISOLE si allunga e il prezzo esce
#   di colonna.
lunghezza = COL_ZONA + len(LISTINO[3][1]) + COL_PREZZO
print(f"Senza fetta la riga ISOLE sarebbe di {lunghezza} caratteri, non "
      f"{LARGHEZZA_TABELLA}.")
