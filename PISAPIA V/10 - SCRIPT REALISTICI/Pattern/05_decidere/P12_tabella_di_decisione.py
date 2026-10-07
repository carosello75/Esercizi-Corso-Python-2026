"""
P12 — La tabella di decisione in un dizionario: .get(chiave, ripiego) al
    posto di dieci elif

Catalogo dei pattern, Giorno 10 — capitolo 5, Decidere
Teoria: TEORIA_GIORNO_10.md §5.3

IN SINTESI
Associa a ogni valore di una chiave un esito fisso tramite un dizionario,
con .get(chiave, ripiego) per i casi non previsti.

DESCRIZIONE
Il file definisce il dizionario UFFICI, che associa le categorie agli
uffici, il ripiego UFFICIO_RIPIEGO e cinque categorie grezze in TICKET. Un
for normalizza ogni categoria con .strip().upper() e ricava l'ufficio con
UFFICI.get(categoria, UFFICIO_RIPIEGO): le chiavi presenti danno l'ufficio
associato, mentre ALTRO e VACCINI, che non sono chiavi, finiscono al
Centralino. Ogni coppia esce incolonnata. In coda la prova del trabocchetto
passa a .get() la categoria non normalizzata, che finisce al Centralino
invece che alla Cassa, senza errori.

LO SCHEMA
Lo schema sta qui sotto, subito dopo questa docstring, come blocco
commentato: è uno stampo, non un programma, e non ha output. Si copia nel
proprio script, si tolgono i commenti (Ctrl+/ in PyCharm, Cmd+/ su Mac) e si
cambiano solo le righe marcate # <-- adattare.

IN AZIONE
Il codice eseguibile di questo file è l'In azione: lanciatelo, e l'output
deve essere quello di ESEMPIO OUTPUT in fondo a questa docstring.

VARIANTI
- La chiave assente è un'anomalia, non un caso da smistare? Allora if
  categoria not in UFFICI: e lo scarto con il motivo (Giorno 09 §8.5).

- Più valori per chiave: {"REFERTO": ("Archivio referti", 2)}, spacchettati
  dopo il .get().

ERRORI TIPICI
- UFFICI[categoria] su una chiave assente: KeyError (nel codice qui sotto).

- La chiave non normalizzata: il ripiego al posto dell'ufficio giusto, senza
  errori (nel codice qui sotto). Il più insidioso dei due, perché non si
  vede.

DA DOVE VIENE
Giorno 07 §10.1, §10.3, §11.1, §15.1 · Giorno 09 §8.5

DOVE SI USA NEGLI ESERCIZI
10.2, 10.3, 10.4, 10.8, casa_10.1, casa_10.4

ESEMPIO OUTPUT
REFERTO      -> Archivio referti
PAGAMENTO    -> Cassa
ALTRO        -> Centralino
VACCINI      -> Centralino
RECLAMO      -> URP
Senza normalizzare: Centralino
"""

# ==========================================================================
# LO SCHEMA — lo stampo da copiare. Non si esegue: è commentato.
# ==========================================================================
# TABELLA = {"VALORE_A": "esito A", "VALORE_B": "esito B"}   # <-- adattare
# RIPIEGO = "esito di tutti gli altri casi"                  # <-- adattare
#
#
# def decidi(chiave, tabella, ripiego):
#     """Restituisce il valore associato alla chiave normalizzata, o il ripiego."""
#     return tabella.get(chiave.strip().upper(), ripiego)


# ==========================================================================
# IN AZIONE — lo schema su un caso del corso. Si esegue.
# ==========================================================================
UFFICI = {"PRENOTAZIONE": "CUP", "REFERTO": "Archivio referti",
          "PAGAMENTO": "Cassa", "RECLAMO": "URP"}
UFFICIO_RIPIEGO = "Centralino"
TICKET = ["REFERTO", " pagamento", "ALTRO", "VACCINI", "reclamo "]

for grezza in TICKET:
    # 1. La chiave cercata va portata nella forma delle chiavi del dizionario
    #    (senza spazi, maiuscolo): il lookup confronta stringhe esatte.
    categoria = grezza.strip().upper()
    # 2. Per le chiavi assenti, come ALTRO e VACCINI, .get() restituisce il
    #    valore di ripiego invece di sollevare KeyError.
    ufficio = UFFICI.get(categoria, UFFICIO_RIPIEGO)
    print(f"{categoria:<13}-> {ufficio}")

# TRABOCCHETTO: senza normalizzare, " pagamento" non e' "PAGAMENTO" e va al
#   centralino in silenzio. Con UFFICI["VACCINI"] al posto di .get(), invece,
#   il programma si ferma con KeyError: 'VACCINI'.
print("Senza normalizzare:", UFFICI.get(" pagamento", UFFICIO_RIPIEGO))
