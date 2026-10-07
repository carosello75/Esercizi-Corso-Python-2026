"""
P16 — Massimo e minimo, e chi li possiede

Catalogo dei pattern, Giorno 10 — capitolo 7, Accumulare e contare
Teoria: TEORIA_GIORNO_10.md §7.2

IN SINTESI
Trova il massimo e il minimo di una serie insieme a chi li possiede,
partendo dal primo elemento e non da zero.

DESCRIZIONE
Il file parte da ORDINI, una lista di tuple (importo, codice), e definisce
minimo_e_massimo(), che riceve la lista non vuota, inizializza minimo e
massimo con il primo elemento, scorre coppie[1:] confrontando il solo primo
campo e restituisce le due coppie intere, senza stampare. Il chiamante
spacchetta il risultato in piu_basso e piu_alto e stampa codice e importo di
NS-1010 e NS-1008. Il secondo esempio applica max() e min() direttamente
alle tuple e mostra che a valore pari, 75, decide il secondo campo.

LO SCHEMA
Lo schema sta qui sotto, subito dopo questa docstring, come blocco
commentato: è uno stampo, non un programma, e non ha output. Si copia nel
proprio script, si tolgono i commenti (Ctrl+/ in PyCharm, Cmd+/ su Mac) e si
cambiano solo le righe marcate # <-- adattare.

IN AZIONE
Il codice eseguibile di questo file è l'In azione: lanciatelo, e l'output
deve essere quello di ESEMPIO OUTPUT in fondo a questa docstring.

VARIANTI
- max() e min() direttamente sulle coppie: vedi la chicca qui sotto.

ERRORI TIPICI
- Il minimo inizializzato a 0 non scende mai (nel codice qui sotto); il
  massimo a 0 sbaglia su valori tutti negativi. Si parte dal primo elemento.

DA DOVE VIENE
Giorno 05 §6.5 · Giorno 06 §10.1, §10.5 · Giorno 07 §9.1, §9.2

CHICCA — max() su coppie: il vincitore arriva con il nome attaccato. Due
tuple si confrontano campo per campo, da sinistra: prima gli importi, e solo
a importo pari i codici. max() e min() su coppie (valore, nome)
restituiscono la coppia intera, senza cicli. A punteggio pari decide il
nome, in ordine alfabetico: è la parità a sorpresa delle classifiche di P22.

DOVE SI USA NEGLI ESERCIZI
10.1, 10.4, casa_10.4

ESEMPIO OUTPUT
Ordine più alto:  NS-1010  278.90
Ordine più basso: NS-1008   27.00
(278.9, 'NS-1010')
(27.0, 'NS-1008')
(75, 'Greco Lorenzo')
"""

# ==========================================================================
# LO SCHEMA — lo stampo da copiare. Non si esegue: è commentato.
# ==========================================================================
# coppie = [(3.5, "A"), (7.0, "B")]                    # <-- adattare: (valore, chi)
# # Inizializzazione sul primo elemento, non su 0: il risultato e' corretto
# # per qualunque segno dei valori.
# minimo = coppie[0]
# massimo = coppie[0]
# for coppia in coppie[1:]:
#     # Il confronto usa il primo campo; si memorizza la coppia intera, cosi'
#     # il valore estremo resta associato al suo proprietario.
#     if coppia[0] < minimo[0]:
#         minimo = coppia
#     if coppia[0] > massimo[0]:
#         massimo = coppia


# ==========================================================================
# IN AZIONE — lo schema su un caso del corso. Si esegue.
# ==========================================================================
ORDINI = [(99.80, "NS-1001"), (219.00, "NS-1004"), (27.00, "NS-1008"),
          (278.90, "NS-1010"), (61.50, "NS-1003")]


def minimo_e_massimo(coppie):
    """Restituisce (coppia minima, coppia massima). Precondizione: non vuota."""
    # TRABOCCHETTO: minimo = 0 al posto di coppie[0]. Qui minimo deve essere
    #   una coppia: al primo confronto minimo[0] si ferma con
    #   TypeError: 'int' object is not subscriptable. Su una lista di soli
    #   importi lo stesso 0 non darebbe errori: il minimo non scenderebbe
    #   mai, perche' nessun importo e' minore di zero, e uscirebbe 0.
    minimo = coppie[0]
    massimo = coppie[0]
    for coppia in coppie[1:]:
        # coppia[0] e' l'importo, chiave del confronto; si assegna la coppia
        # intera per non perdere il codice dell'ordine.
        if coppia[0] < minimo[0]:
            minimo = coppia
        if coppia[0] > massimo[0]:
            massimo = coppia
    return minimo, massimo


# La funzione restituisce una tupla di due coppie, spacchettata in due
# nomi (Giorno 06 §10.1).
piu_basso, piu_alto = minimo_e_massimo(ORDINI)
print(f"Ordine più alto:  {piu_alto[1]} {piu_alto[0]:>7.2f}")
print(f"Ordine più basso: {piu_basso[1]} {piu_basso[0]:>7.2f}")


# ==========================================================================
# ANCORA IN AZIONE — l'esempio che la teoria aggiunge alla scheda.
# ==========================================================================
ORDINI = [(99.80, "NS-1001"), (278.90, "NS-1010"), (27.00, "NS-1008")]
print(max(ORDINI))
print(min(ORDINI))
# Le tuple si confrontano in ordine lessicografico: a valore pari decide
# il secondo campo, e "Greco" viene dopo "Bruno".
print(max([(75, "Bruno Dario"), (75, "Greco Lorenzo")]))
