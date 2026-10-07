"""
P17 — Il contatore per categoria: dizionario e .get(k, 0) + 1

Catalogo dei pattern, Giorno 10 — capitolo 7, Accumulare e contare
Teoria: TEORIA_GIORNO_10.md §7.3

IN SINTESI
Conta le occorrenze di ogni categoria in un dizionario, creando la chiave
alla prima comparsa con .get(chiave, 0) + 1.

DESCRIZIONE
Il file dichiara le categorie attese in CATEGORIE e sette ticket grezzi in
TICKET. La funzione conta_per_chiave() riceve una sequenza di chiavi e
restituisce un dizionario di frequenze costruito con conteggi.get(chiave, 0)
+ 1, senza normalizzare né stampare. Il programma normalizza prima i ticket
con .strip().upper() in una nuova lista e li conta; poi scorre CATEGORIE e
stampa ogni conteggio con .get(categoria, 0), così anche PRENOTAZIONE
compare a 0. L'ultima riga conta i dati grezzi e ottiene 6 categorie.

LO SCHEMA
Lo schema sta qui sotto, subito dopo questa docstring, come blocco
commentato: è uno stampo, non un programma, e non ha output. Si copia nel
proprio script, si tolgono i commenti (Ctrl+/ in PyCharm, Cmd+/ su Mac) e si
cambiano solo le righe marcate # <-- adattare.

IN AZIONE
Il codice eseguibile di questo file è l'In azione: lanciatelo, e l'output
deve essere quello di ESEMPIO OUTPUT in fondo a questa docstring.

VARIANTI
- Categorie ricavate dai dati invece che dichiarate: si scorre .items() del
  dizionario, e compaiono anche le impreviste, ma non quelle a zero.

ERRORI TIPICI
- conteggi[chiave] += 1 su una chiave nuova: KeyError alla prima comparsa.

- Contare prima di normalizzare (nel codice qui sotto): due categorie al
  posto di una.

DA DOVE VIENE
Giorno 07 §10.2, §12.1, §12.2, §12.5 · Giorno 08 §10.4

DOVE SI USA NEGLI ESERCIZI
10.3, 10.5, 10.8, 10.9, casa_10.2

ERRORI TIPICI DELLA GIORNATA COLLEGATI (teoria, capitolo 14)
- E2 — Il contatore azzerato dentro il ciclo: la categoria che vale sempre 1

ESEMPIO OUTPUT
PRENOTAZIONE   0
REFERTO        3
PAGAMENTO      2
RECLAMO        1
ALTRO          1
6 categorie contando i dati grezzi
"""

# ==========================================================================
# LO SCHEMA — lo stampo da copiare. Non si esegue: è commentato.
# ==========================================================================
# def conta_per_chiave(chiavi):
#     """Restituisce il dizionario chiave -> quante volte compare."""
#     conteggi = {}
#     for chiave in chiavi:
#         # .get(chiave, 0) restituisce 0 per una chiave assente: la prima
#         # occorrenza crea la voce senza KeyError e senza un if separato.
#         conteggi[chiave] = conteggi.get(chiave, 0) + 1
#     return conteggi


# ==========================================================================
# IN AZIONE — lo schema su un caso del corso. Si esegue.
# ==========================================================================
CATEGORIE = ["PRENOTAZIONE", "REFERTO", "PAGAMENTO", "RECLAMO", "ALTRO"]
TICKET = ["REFERTO", "PAGAMENTO", "referto ", "ALTRO", "RECLAMO", "REFERTO",
          "Pagamento"]


def conta_per_chiave(chiavi):
    """Restituisce il dizionario chiave -> quante volte compare."""
    conteggi = {}
    for chiave in chiavi:
        conteggi[chiave] = conteggi.get(chiave, 0) + 1
    return conteggi


# 1. Normalizzazione prima del conteggio: conta_per_chiave() confronta le
#    chiavi alla lettera e non conosce maiuscole e spazi.
normalizzate = []
for categoria in TICKET:
    normalizzate.append(categoria.strip().upper())
conteggi = conta_per_chiave(normalizzate)
# 2. Iterazione sulle categorie dichiarate con .get(categoria, 0): escono
#    anche quelle a zero, nell'ordine fissato dalla costante.
for categoria in CATEGORIE:
    print(f"{categoria:<13}{conteggi.get(categoria, 0):>3}")
# TRABOCCHETTO: contare i dati grezzi. "referto " e "Pagamento" diventano
#   chiavi distinte, e i conteggi si ripartiscono senza nessun errore.
print(len(conta_per_chiave(TICKET)), "categorie contando i dati grezzi")
