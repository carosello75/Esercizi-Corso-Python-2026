"""
P18 — Aggregare per chiave: somma, quota percentuale e barra

Catalogo dei pattern, Giorno 10 — capitolo 7, Accumulare e contare
Teoria: TEORIA_GIORNO_10.md §7.4

IN SINTESI
Somma gli importi per chiave in un dizionario e, a totale noto, ricava per
ogni chiave la quota percentuale e una barra proporzionale.

DESCRIZIONE
Il file definisce LARGHEZZA_BARRA, la lista ORDINI di coppie (categoria,
importo) e la funzione somma_per_chiave(), che riceve le coppie e
restituisce un dizionario categoria-somma, accumulato con somme.get(chiave,
0) + importo. Dopo la chiamata, il totale si calcola con
sum(somme.values()); un ciclo su items() ricava per ogni categoria la quota
sul totale e una barra di # lunga round(quota * LARGHEZZA_BARRA), e stampa
categoria, importo, percentuale e barra incolonnati. L'ultima riga stampa il
totale, 1457.60.

LO SCHEMA
somma_per_chiave() è il contatore di P17 con + importo.

Lo schema sta qui sotto, subito dopo questa docstring, come blocco
commentato: è uno stampo, non un programma, e non ha output. Si copia nel
proprio script, si tolgono i commenti (Ctrl+/ in PyCharm, Cmd+/ su Mac) e si
cambiano solo le righe marcate # <-- adattare.

IN AZIONE
Il codice eseguibile di questo file è l'In azione: lanciatelo, e l'output
deve essere quello di ESEMPIO OUTPUT in fondo a questa docstring.

VARIANTI
- Più dizionari nello stesso giro (importo, ordini): dal rapporto, la media.

ERRORI TIPICI
- La quota calcolata dentro il ciclo di accumulo: totale parziale, e la
  prima categoria risulta al 100%.

- La barra con int() (nel codice qui sotto); una barra vuota lascia spazi in
  coda.

DA DOVE VIENE
Giorno 02 §13.3 · Giorno 03 §10.5 · Giorno 07 §12.3, §12.4, §14.2

DOVE SI USA NEGLI ESERCIZI
10.3, 10.4, 10.10, 10.11, casa_10.2, casa_10.3, casa_10.4

ESEMPIO OUTPUT
AUDIO         299.40  20.5%  ########
INFORMATICA   383.00  26.3%  ###########
ACCESSORI     157.50  10.8%  ####
VIDEO         617.70  42.4%  #################
TOTALE       1457.60
"""

# ==========================================================================
# LO SCHEMA — lo stampo da copiare. Non si esegue: è commentato.
# ==========================================================================
# LARGHEZZA_BARRA = 40
# somme = somma_per_chiave(coppie)                     # <-- adattare: le coppie
# # Totale calcolato ad accumulo concluso: la quota e' un rapporto
# # sull'insieme completo delle somme, non su un totale parziale.
# totale = sum(somme.values())
# for chiave, importo in somme.items():
#     quota = importo / totale
#     barra = "#" * round(quota * LARGHEZZA_BARRA)
#     print(f"{chiave:<12}{importo:>8.2f}{quota:>7.1%}  {barra}")    # <-- adattare


# ==========================================================================
# IN AZIONE — lo schema su un caso del corso. Si esegue.
# ==========================================================================
LARGHEZZA_BARRA = 40
ORDINI = [("AUDIO", 99.80), ("INFORMATICA", 89.00), ("ACCESSORI", 61.50),
          ("VIDEO", 219.00), ("AUDIO", 49.90), ("VIDEO", 119.80),
          ("INFORMATICA", 178.00), ("ACCESSORI", 27.00), ("AUDIO", 149.70),
          ("VIDEO", 278.90), ("ACCESSORI", 69.00), ("INFORMATICA", 116.00)]


def somma_per_chiave(coppie):
    """Restituisce il dizionario chiave -> somma, da coppie (chiave, importo)."""
    somme = {}
    for chiave, importo in coppie:
        # Accumulatore per chiave: get(chiave, 0) gestisce la prima
        # occorrenza, poi si somma l'importo invece di contare (P17).
        somme[chiave] = somme.get(chiave, 0) + importo
    return somme


somme = somma_per_chiave(ORDINI)
# 1. Totale calcolato fuori dal ciclo di accumulo: dentro, ogni quota
#    sarebbe riferita a un totale parziale.
totale = sum(somme.values())
for categoria, importo in somme.items():
    quota = importo / totale
    # 2. round() e non int(): la lunghezza della barra arrotonda al valore
    #    piu' vicino invece di troncare, come fa la quota stampata accanto.
    barra = "#" * round(quota * LARGHEZZA_BARRA)
    print(f"{categoria:<12}{importo:>8.2f}{quota:>7.1%}  {barra}")
print(f"{'TOTALE':<12}{totale:>8.2f}")

# TRABOCCHETTO: int() tronca la parte decimale. INFORMATICA scenderebbe a 10
#   cancelletti, VIDEO a 16, e sotto il 2,5% una categoria non ne avrebbe
#   nemmeno uno: barra vuota, nessuna eccezione.
