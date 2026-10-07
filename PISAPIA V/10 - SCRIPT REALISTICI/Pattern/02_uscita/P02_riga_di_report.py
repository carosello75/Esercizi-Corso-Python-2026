"""
P2 — La riga di report: etichetta, valore, larghezza e decimali in una
    f-string

Catalogo dei pattern, Giorno 10 — capitolo 2, L'uscita: la pagina che si legge
Teoria: TEORIA_GIORNO_10.md §2.2

IN SINTESI
Formatta etichetta e valore in una f-string con larghezza, allineamento e
decimali fissi, perché le righe successive si incolonnino.

DESCRIZIONE
Il file fissa in costanti i dati del riepilogo (RICEVUTE, EVASE,
DIRITTI_INCASSATI) e le larghezze COLONNA_TESTO e COLONNA_NUMERO, richiamate
nelle f-string con graffe annidate. Stampa i due interi allineati a destra,
la quota EVASE / RICEVUTE con lo specificatore .1% e l'importo con ,.2f, che
produce 1,234.50 con il separatore delle migliaia all'inglese. L'ultima riga
applica .1% al valore già moltiplicato per 100 e stampa 7578.1% senza
errori. Il secondo esempio scorre RIEPILOGO e allinea le etichette con il
riempitivo di puntini :.<24.

LO SCHEMA
Lo schema sta qui sotto, subito dopo questa docstring, come blocco
commentato: è uno stampo, non un programma, e non ha output. Si copia nel
proprio script, si tolgono i commenti (Ctrl+/ in PyCharm, Cmd+/ su Mac) e si
cambiano solo le righe marcate # <-- adattare.

IN AZIONE
Il codice eseguibile di questo file è l'In azione: lanciatelo, e l'output
deve essere quello di ESEMPIO OUTPUT in fondo a questa docstring.

VARIANTI
- :>10.2f sulla colonna dei soldi: il punto decimale sta sempre in colonna.

- Il numero è già una percentuale? f"{75.8:.1f}%", simbolo scritto a mano.

ERRORI TIPICI
- .1% sul numero già moltiplicato: 7578.1% (nel codice qui sotto).

- :, mette la virgola delle migliaia all'inglese, 1,234.50: è la convenzione
  di Python. In un report per l'ufficio va convertito (P5).

DA DOVE VIENE
Giorno 01 §10.2 · Giorno 02 §13.1, §13.2, §13.3 · Giorno 03 §8.4, §9.2

CHICCA — I puntini che riempiono: f"{etichetta:.<24}". Il carattere subito
prima di < è il riempitivo: al posto degli spazi, Python mette quello. Così
escono le righe «Righe lette ........ 16» dei report di oggi, senza contare
un puntino a mano (Giorno 03 §9.7).

DOVE SI USA NEGLI ESERCIZI
10.1, 10.2

ESEMPIO OUTPUT
Pratiche ricevute          128
Pratiche evase              97
Quota evasa              75.8%
Diritti incassati     1,234.50
Quota sbagliata        7578.1%
Righe lette ............  16
Righe buone ............  13
Righe scartate .........   3
"""

# ==========================================================================
# LO SCHEMA — lo stampo da copiare. Non si esegue: è commentato.
# ==========================================================================
# COLONNA_TESTO = 20                                   # <-- adattare
# COLONNA_NUMERO = 10                                  # <-- adattare
#
# etichetta = "Pratiche evase"                         # <-- adattare
# valore = 97                                          # <-- adattare
# parte, intero = 97, 128                              # <-- adattare
#
# # Etichetta allineata a sinistra, valore a destra, larghezze da costanti:
# # righe consecutive formattate cosi' condividono le stesse colonne.
# print(f"{etichetta:<{COLONNA_TESTO}}{valore:>{COLONNA_NUMERO}}")
# # Lo specificatore .1% si aspetta la frazione: moltiplica per 100 e
# # aggiunge il simbolo, quindi riceve parte / intero, non il prodotto.
# print(f"{'Quota':<{COLONNA_TESTO}}{parte / intero:>{COLONNA_NUMERO}.1%}")


# ==========================================================================
# IN AZIONE — lo schema su un caso del corso. Si esegue.
# ==========================================================================
RICEVUTE = 128
EVASE = 97
DIRITTI_INCASSATI = 1234.5
COLONNA_TESTO = 20
COLONNA_NUMERO = 10

# 1. Interi: allineamento a destra con :>, nessuno specificatore decimale.
print(f"{'Pratiche ricevute':<{COLONNA_TESTO}}{RICEVUTE:>{COLONNA_NUMERO}}")
print(f"{'Pratiche evase':<{COLONNA_TESTO}}{EVASE:>{COLONNA_NUMERO}}")
# 2. Quota: la divisione produce la frazione 0.7578125, che .1% converte
#    in percentuale con un decimale.
quota = EVASE / RICEVUTE
print(f"{'Quota evasa':<{COLONNA_TESTO}}{quota:>{COLONNA_NUMERO}.1%}")
# 3. Importi: .2f fissa due decimali e , inserisce il separatore delle
#    migliaia, secondo la convenzione inglese.
print(f"{'Diritti incassati':<{COLONNA_TESTO}}"
      f"{DIRITTI_INCASSATI:>{COLONNA_NUMERO},.2f}")
# TRABOCCHETTO: .1% applicato a un valore gia' moltiplicato per 100 lo
#   moltiplica di nuovo: 75.78 al posto di 0.7578 stampa 7578.1%, senza
#   alcuna eccezione.
print(f"{'Quota sbagliata':<{COLONNA_TESTO}}{quota * 100:>{COLONNA_NUMERO}.1%}")


# ==========================================================================
# ANCORA IN AZIONE — l'esempio che la teoria aggiunge alla scheda.
# ==========================================================================
RIEPILOGO = [("Righe lette", 16), ("Righe buone", 13), ("Righe scartate", 3)]

for etichetta, numero in RIEPILOGO:
    # Lo spazio si concatena prima: il riempitivo . copre solo la parte
    # rimanente fino alla larghezza 24.
    print(f"{etichetta + ' ':.<24} {numero:>3}")
