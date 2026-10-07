"""
P19 — Cercare il primo che soddisfa: return nel ciclo e il «non trovato»

Catalogo dei pattern, Giorno 10 — capitolo 8, Cercare, filtrare, ordinare
Teoria: TEORIA_GIORNO_10.md §8.1

IN SINTESI
Scorre un elenco e restituisce il primo record che soddisfa la condizione,
oppure None se il ciclo arriva in fondo senza trovarlo.

DESCRIZIONE
Il file definisce LISTINO, una lista di tuple (codice, descrizione, prezzo),
e la funzione cerca_per_codice(), che riceve elenco e codice, normalizza il
codice con strip().upper() e restituisce il primo record che ha quel codice
in posizione 0, oppure None a ciclo esaurito. Un for la chiama su due
codici: ns-a03 preceduto da uno spazio e NS-Z99. Se il risultato è vero, il
record viene spacchettato e stampato come riga [OK] incolonnata; altrimenti
si stampa il codice ripulito con l'avviso «non a listino».

LO SCHEMA
Lo schema sta qui sotto, subito dopo questa docstring, come blocco
commentato: è uno stampo, non un programma, e non ha output. Si copia nel
proprio script, si tolgono i commenti (Ctrl+/ in PyCharm, Cmd+/ su Mac) e si
cambiano solo le righe marcate # <-- adattare.

IN AZIONE
Il codice eseguibile di questo file è l'In azione: lanciatelo, e l'output
deve essere quello di ESEMPIO OUTPUT in fondo a questa docstring.

VARIANTI
Fuori da una funzione, bandiera trovato = None e break (Giorno 05 §6.6,
§10.1); se basta sapere se c'è, in su una lista di codici; per il primo che
rispetta una condizione cambia solo l'if (record[2] > 30.00).

ERRORI TIPICI
- else: return None dentro il ciclo → trova solo il primo record
  dell'elenco.

- Il record spacchettato senza controllo → TypeError: cannot unpack
  non-iterable NoneType object su un codice assente.

DA DOVE VIENE
Giorno 05 §6.6, §10.1 · Giorno 06 §5.3, §6.3, E7 · Giorno 07 §5.1, §5.2,
§14.1

DOVE SI USA NEGLI ESERCIZI
10.7, 10.9, 10.12

ESEMPIO OUTPUT
[OK] NS-A03  Webcam HD           39.00
[!] NS-Z99: non a listino
"""

# ==========================================================================
# LO SCHEMA — lo stampo da copiare. Non si esegue: è commentato.
# ==========================================================================
# def cerca_per_codice(elenco, codice):
#     """Restituisce il primo record con quel codice, oppure None."""
#     # Normalizzazione dell'argomento (P4): il confronto con == e' esatto,
#     # quindi la chiave cercata deve avere la forma di quelle in elenco.
#     codice = codice.strip().upper()
#     for record in elenco:
#         if record[0] == codice:  # <-- adattare: il campo che fa da codice
#             # return anticipato: termina la funzione e quindi anche il ciclo.
#             return record
#     # Ripiego dopo il for: si raggiunge solo a ciclo esaurito, cioe'
#     # quando nessun record ha soddisfatto la condizione.
#     return None


# ==========================================================================
# IN AZIONE — lo schema su un caso del corso. Si esegue.
# ==========================================================================
LISTINO = [
    ("NS-A01", "Cuffie Bluetooth", 49.90),
    ("NS-A02", "Cavo HDMI 2 m", 9.90),
    ("NS-A03", "Webcam HD", 39.00),
    ("NS-A04", "Mouse senza fili", 19.50),
]


def cerca_per_codice(elenco, codice):
    codice = codice.strip().upper()
    for record in elenco:
        if record[0] == codice:
            return record
    return None


# 1. " ns-a03" ha uno spazio iniziale e le minuscole: lo strip().upper()
#    interno alla funzione lo riconduce alla chiave NS-A03.
for cercato in [" ns-a03", "NS-Z99"]:
    record = cerca_per_codice(LISTINO, cercato)
    # 2. None ha valore di verita' falso (Giorno 06 §6.3), una tupla non vuota
    #    vero: l'if separa trovato e non trovato senza confronti espliciti.
    if record:
        codice, descrizione, prezzo = record
        print(f"[OK] {codice}  {descrizione:<18}{prezzo:>7.2f}")
    else:
        print(f"[!] {cercato.strip()}: non a listino")

# TRABOCCHETTO: con un else: return None dentro il for, allineato all'if, la
#   funzione si arrende al primo giro. NS-A01 non e' NS-A03, e " ns-a03"
#   risulta "non a listino" pur essendo il terzo (Giorno 06 E7).
