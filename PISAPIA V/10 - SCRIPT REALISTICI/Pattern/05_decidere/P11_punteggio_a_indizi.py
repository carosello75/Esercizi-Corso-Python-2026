"""
P11 — Il punteggio a indizi: pesi in un dizionario, somma, confronto con la
    soglia

Catalogo dei pattern, Giorno 10 — capitolo 5, Decidere
Teoria: TEORIA_GIORNO_10.md §5.2

IN SINTESI
Somma i pesi degli indizi presenti in un testo, tenuti in un dizionario, e
confronta il punteggio ottenuto con una soglia.

DESCRIZIONE
Il file tiene in PAROLE_SPIA un dizionario parola-peso, con la soglia
SOGLIA_SPAM e quattro testi in MESSAGGI. La funzione punteggio() riceve
testo e dizionario, porta il testo in minuscolo, scorre le coppie con
.items() e somma all'accumulatore il peso di ogni parola trovata con in;
restituisce l'intero senza stampare. Il ciclo confronta ogni punteggio con
la soglia usando >= e stampa punti, esito e messaggio: il bando della
provincia prende 3 punti per la sottostringa vinci. Il secondo esempio
confronta in e .count() sullo stesso testo: 6 punti contro 12.

LO SCHEMA
Lo schema sta qui sotto, subito dopo questa docstring, come blocco
commentato: è uno stampo, non un programma, e non ha output. Si copia nel
proprio script, si tolgono i commenti (Ctrl+/ in PyCharm, Cmd+/ su Mac) e si
cambiano solo le righe marcate # <-- adattare.

IN AZIONE
Il codice eseguibile di questo file è l'In azione: lanciatelo, e l'output
deve essere quello di ESEMPIO OUTPUT in fondo a questa docstring.

VARIANTI
- Pesi e soglia letti da un file di configurazione (P27).

- Più livelli: il punteggio passa a fascia() di P10, con [(2, "BASSA"), (4,
  "MEDIA")] e "ALTA" per il resto.

ERRORI TIPICI
- in trova la sequenza, non la parola (nel codice qui sotto): vinci in
  provincia, rotto in dirotto. È un limite: si dichiara nella docstring.

- Il testo non normalizzato: un messaggio tutto in maiuscolo passa pulito.
  Il .lower() dentro la funzione chiude la porta.

DA DOVE VIENE
Giorno 04 §5.2, §14.3, §14.4, §14.5, §14.6 · Giorno 07 §10.1, §11.3 · Giorno
08 §10.5

CHICCA — .count() al posto di in: la parola ripetuta tre volte vale tre
volte. in risponde sì o no, quindi «gratis, gratis, gratis» vale quanto un
«gratis» solo. .count(), il metodo delle stringhe del Giorno 02 §10.4, dice
quante volte: moltiplicato per il peso, dà un punteggio che pesa le
ripetizioni. Il limite resta lo stesso: conta sequenze di caratteri.

DOVE SI USA NEGLI ESERCIZI
10.8

ERRORI TIPICI DELLA GIORNATA COLLEGATI (teoria, capitolo 14)
- E4 — in che trova una parola dentro un'altra: "rotto" in "dirotto"

ESEMPIO OUTPUT
 0 punti  ok    Le confermo l'appuntamento in sede
 3 punti  ok    Urgente: pratica di rimborso in scadenza
 9 punti  SPAM  Offerta imperdibile: clicca subito e ricevi un buono gratis
 3 punti  ok    Nuovo bando della provincia per i tirocini
Con in:    6 punti
Con count: 12 punti
'vinci' dentro 'provincia', contato: 1
"""

# ==========================================================================
# LO SCHEMA — lo stampo da copiare. Non si esegue: è commentato.
# ==========================================================================
# PESI = {"parola spia": 3, "altra parola": 2}         # <-- adattare
# SOGLIA = 5                                           # <-- adattare
#
#
# def punteggio(testo, pesi):
#     """Restituisce la somma dei pesi delle parole spia trovate nel testo."""
#     testo = testo.lower()
#     totale = 0
#     for parola, peso in pesi.items():
#         if parola in testo:
#             totale += peso
#     return totale
#
#
# # Soglia inclusiva: >= e non >, come nel Giorno 04; un punteggio pari
# # alla soglia e' gia' segnalato.
# segnalato = punteggio(testo, PESI) >= SOGLIA         # <-- adattare: il testo


# ==========================================================================
# IN AZIONE — lo schema su un caso del corso. Si esegue.
# ==========================================================================
PAROLE_SPIA = {"gratis": 3, "vinci": 3, "clicca subito": 4,
               "offerta imperdibile": 2, "urgente": 1, "credenziali": 4,
               "rimborso": 2}
SOGLIA_SPAM = 5
MESSAGGI = ["Le confermo l'appuntamento in sede",
            "Urgente: pratica di rimborso in scadenza",
            "Offerta imperdibile: clicca subito e ricevi un buono gratis",
            "Nuovo bando della provincia per i tirocini"]


def punteggio(testo, pesi):
    """Restituisce la somma dei pesi delle parole spia trovate nel testo."""
    # Normalizzazione interna alla funzione: il risultato non dipende dalle
    # maiuscole con cui il chiamante passa il testo.
    testo = testo.lower()
    totale = 0
    for parola, peso in pesi.items():
        if parola in testo:
            totale += peso
    return totale


for messaggio in MESSAGGI:
    punti = punteggio(messaggio, PAROLE_SPIA)
    if punti >= SOGLIA_SPAM:
        esito = "SPAM"
    else:
        esito = "ok"
    print(f"{punti:>2} punti  {esito:<4}  {messaggio}")

# TRABOCCHETTO: l'ultimo messaggio prende 3 punti senza contenere nessuna
#   parola spia. "vinci" sta dentro "pro-VINCI-a": in verifica la presenza
#   di una sottostringa, non di una parola (Giorno 04 §14.4). Qui resta
#   sotto soglia per caso, non per costruzione.


# ==========================================================================
# ANCORA IN AZIONE — l'esempio che la teoria aggiunge alla scheda.
# ==========================================================================
PESI = {"gratis": 3, "vinci": 3}
testo = "gratis! gratis! tutto gratis, vinci subito"

con_in = 0
con_count = 0
for parola, peso in PESI.items():
    if parola in testo:
        con_in += peso
    # count() restituisce il numero di occorrenze, 0 se assente: il prodotto
    # con il peso non richiede un if.
    con_count += testo.count(parola) * peso
print(f"Con in:    {con_in} punti")
print(f"Con count: {con_count} punti")
print(f"'vinci' dentro 'provincia', contato: {'provincia'.count('vinci')}")
