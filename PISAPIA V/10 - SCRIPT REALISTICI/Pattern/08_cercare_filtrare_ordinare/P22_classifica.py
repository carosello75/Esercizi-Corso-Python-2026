"""
P22 — La classifica: coppie (valore, nome), sort(reverse=True), i primi N

Catalogo dei pattern, Giorno 10 — capitolo 8, Cercare, filtrare, ordinare
Teoria: TEORIA_GIORNO_10.md §8.4

IN SINTESI
Costruisce coppie (valore, nome) da un dizionario, le ordina in senso
decrescente e restituisce le prime N come classifica.

DESCRIZIONE
Il file definisce il dizionario PUNTEGGI, da nome a punteggio, la costante
QUANTI_IN_CLASSIFICA e la funzione primi(), che riceve dizionario e numero
di posizioni, costruisce una lista di tuple (valore, chiave), la ordina sul
posto con sort(reverse=True) e restituisce la fetta coppie[:quanti]. Il
ciclo principale scorre il risultato con enumerate(..., 1), spacchetta ogni
coppia in punteggio, nome e stampa posizione, nome e punteggio incolonnati:
Verdi Luca 91, Ricci Paolo 88, Gallo Pietro 83.

LO SCHEMA
Lo schema sta qui sotto, subito dopo questa docstring, come blocco
commentato: è uno stampo, non un programma, e non ha output. Si copia nel
proprio script, si tolgono i commenti (Ctrl+/ in PyCharm, Cmd+/ su Mac) e si
cambiano solo le righe marcate # <-- adattare.

IN AZIONE
Il codice eseguibile di questo file è l'In azione: lanciatelo, e l'output
deve essere quello di ESEMPIO OUTPUT in fondo a questa docstring.

VARIANTI
Classifica crescente («i tre più lenti»): sort() senza reverse. Di conteggi
(P17) o di somme (P18): primi() senza cambiare una riga. Il solo primo:
max() sulle coppie (§7.2).

ERRORI TIPICI
- classifica = coppie.sort(reverse=True) → None, e la fetta si ferma con
  TypeError: 'NoneType' object is not subscriptable (Giorno 07 E4).

- Coppie scritte (nome, valore) → una classifica alfabetica che sembra vera.

DA DOVE VIENE
Giorno 07 §6.3, §8.1, §8.3, §8.4, §14.3, E4 · Giorno 08 §10.4

DOVE SI USA NEGLI ESERCIZI
10.4, 10.6, 10.8, 10.10, 10.11, casa_10.2, casa_10.4

ERRORI TIPICI DELLA GIORNATA COLLEGATI (teoria, capitolo 14)
- E6 — La parità nella classifica: reverse=True rovescia anche l'ordine dei
  nomi

ESEMPIO OUTPUT
1. Verdi Luca      91
2. Ricci Paolo     88
3. Gallo Pietro    83
"""

# ==========================================================================
# LO SCHEMA — lo stampo da copiare. Non si esegue: è commentato.
# ==========================================================================
# def primi(dizionario, quanti):
#     """Restituisce le prime coppie (valore, chiave), dalla piu' alta."""
#     coppie = []
#     for chiave, valore in dizionario.items():
#         # Valore come primo campo: le tuple si confrontano in ordine
#         # lessicografico, campo per campo (Giorno 07 §8.4).
#         coppie.append((valore, chiave))
#     # sort() modifica la lista sul posto e restituisce None: il suo
#     # risultato non va mai assegnato a una variabile.
#     coppie.sort(reverse=True)
#     return coppie[:quanti]


# ==========================================================================
# IN AZIONE — lo schema su un caso del corso. Si esegue.
# ==========================================================================
PUNTEGGI = {"Rossi Anna": 78, "Verdi Luca": 91, "Gallo Pietro": 83,
            "Ricci Paolo": 88, "Neri Sara": 64}
QUANTI_IN_CLASSIFICA = 3


def primi(dizionario, quanti):
    coppie = []
    for chiave, valore in dizionario.items():
        coppie.append((valore, chiave))
    coppie.sort(reverse=True)
    return coppie[:quanti]


# 1. enumerate con partenza 1 (Giorno 07 §6.3): la posizione stampata
#    coincide con il rango, non con l'indice della lista.
for posizione, coppia in enumerate(primi(PUNTEGGI, QUANTI_IN_CLASSIFICA), 1):
    # 2. Spacchettamento nell'ordine della tupla (valore, nome), lo stesso
    #    che primi() usa come criterio di ordinamento.
    punteggio, nome = coppia
    print(f"{posizione}. {nome:<14}{punteggio:>4}")

# TRABOCCHETTO: con coppie.append((chiave, valore)) l'ordine lo decide il
#   nome: in testa escono Verdi, Rossi e Ricci, l'alfabeto al contrario, con
#   i punteggi 91, 78, 88 che non scendono. Nessun errore.
