"""
P21 — Doppioni e confronto fra due elenchi: la lista dei già visti e in

Catalogo dei pattern, Giorno 10 — capitolo 8, Cercare, filtrare, ordinare
Teoria: TEORIA_GIORNO_10.md §8.3

IN SINTESI
Elimina i doppioni di un elenco mantenendo l'ordine d'arrivo e confronta due
elenchi per unione, intersezione e differenza con l'operatore in.

DESCRIZIONE
Il file definisce due elenchi di indirizzi, NEGOZIO e ONLINE, e la funzione
senza_doppioni(), che riceve una lista, normalizza ogni voce con
strip().lower() e restituisce una lista nuova con ogni voce una sola volta,
nell'ordine d'arrivo. Sui due elenchi ripuliti, l'unione si costruisce dalla
copia negozio[:] accodando le voci online assenti; un secondo ciclo smista
le voci del negozio fra in_comune e solo_negozio con l'operatore in, e
solo_online si ottiene per sottrazione. Le tre print() mostrano 4 iscritti,
l'indirizzo in comune e le due differenze.

LO SCHEMA
Lo schema sta qui sotto, subito dopo questa docstring, come blocco
commentato: è uno stampo, non un programma, e non ha output. Si copia nel
proprio script, si tolgono i commenti (Ctrl+/ in PyCharm, Cmd+/ su Mac) e si
cambiano solo le righe marcate # <-- adattare.

IN AZIONE
Il codice eseguibile di questo file è l'In azione: lanciatelo, e l'output
deve essere quello di ESEMPIO OUTPUT in fondo a questa docstring.

VARIANTI
Un dizionario al posto della lista dei visti quando serve anche quante volte
una voce torna (P17); il doppione rifiutato durante la lettura con il motivo
già registrato, cioè la lista dei visti dentro un controllo P20.

ERRORI TIPICI
- .remove() di una voce che non c'è → ValueError: list.remove(x): x not in
  list. Prima si chiede con in.

- Le voci ripetute contate come voci diverse → quote oltre il 100%: E5.

DA DOVE VIENE
Giorno 07 §4.1, §5.1, §7.3, §11.2 · Giorno 08 §5.4

DOVE SI USA NEGLI ESERCIZI
10.6, 10.9

ERRORI TIPICI DELLA GIORNATA COLLEGATI (teoria, capitolo 14)
- E5 — Il doppione contato due volte: la percentuale oltre il 100%

ESEMPIO OUTPUT
Iscritti senza doppioni: 4
In comune: ['bianchi@mail.it']
Solo negozio: ['rossi@mail.it', 'verdi@mail.it'], solo online: 1
"""

# ==========================================================================
# LO SCHEMA — lo stampo da copiare. Non si esegue: è commentato.
# ==========================================================================
# def senza_doppioni(elenco):
#     """Restituisce una lista nuova: ogni voce una volta, nell'ordine d'arrivo."""
#     visti = []
#     for voce in elenco:
#         voce = voce.strip().lower()  # <-- adattare: la normalizzazione del caso
#         # Test di appartenenza con in sulla lista dei visti (Giorno 07 §5.1):
#         # la voce si accoda solo alla sua prima occorrenza normalizzata.
#         if voce not in visti:
#             visti.append(voce)
#     return visti


# ==========================================================================
# IN AZIONE — lo schema su un caso del corso. Si esegue.
# ==========================================================================
NEGOZIO = ["rossi@mail.it", "BIANCHI@mail.it ", "verdi@mail.it"]
ONLINE = ["bianchi@mail.it", "neri@mail.it"]


def senza_doppioni(elenco):
    visti = []
    for voce in elenco:
        voce = voce.strip().lower()
        if voce not in visti:
            visti.append(voce)
    return visti


negozio = senza_doppioni(NEGOZIO)
online = senza_doppioni(ONLINE)
# 1. Unione su una copia per fetta (Giorno 07 §7.3): un'assegnazione
#    semplice creerebbe un alias, e gli append modificherebbero negozio.
unione = negozio[:]
for email in online:
    if email not in unione:
        unione.append(email)
# 2. Intersezione e differenza in un'unica scansione: ogni voce di
#    negozio cade in esattamente una delle due liste.
in_comune = []
solo_negozio = []
for email in negozio:
    if email in online:
        in_comune.append(email)
    else:
        solo_negozio.append(email)
# 3. Differenza per sottrazione: corretta solo perche' entrambi gli
#    elenchi sono gia' privi di doppioni.
solo_online = len(online) - len(in_comune)

print(f"Iscritti senza doppioni: {len(unione)}")
print(f"In comune: {in_comune}")
print(f"Solo negozio: {solo_negozio}, solo online: {solo_online}")

# TRABOCCHETTO: senza .strip().lower() "BIANCHI@mail.it " e "bianchi@mail.it"
#   sono due persone: iscritti 5, in comune [], e Bianchi riceve la newsletter
#   due volte. Nessun errore, solo un conto sbagliato di uno.
