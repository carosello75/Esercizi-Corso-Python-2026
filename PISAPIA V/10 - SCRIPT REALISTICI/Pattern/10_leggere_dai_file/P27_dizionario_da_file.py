"""
P27 — Il dizionario di riferimento da file: listino ; o configurazione JSON
    con i default

Catalogo dei pattern, Giorno 10 — capitolo 10, Leggere dai file
Teoria: TEORIA_GIORNO_10.md §10.3

IN SINTESI
Carica da file un dizionario di riferimento, da righe CHIAVE;valore o da
JSON, completando con i valori di default le chiavi assenti.

DESCRIZIONE
Il file definisce DEFAULT e crea con write_text() due file nella cartella di
lavoro: listino_zone.txt, righe ZONA;prezzo con una zona in minuscolo fra
spazi, e config.json con la sola chiave quanti_in_classifica.
carica_listino() legge il listino riga per riga, spezza su ; e restituisce
un dizionario con chiavi in maiuscolo e prezzi convertiti con float();
carica_configurazione() legge il JSON con json.load e restituisce, per ogni
chiave di DEFAULT, il valore del file oppure quello di default. Il programma
stampa il listino, il costo di due chili al SUD, 19.0, e la configurazione
completata.

LO SCHEMA
Lo schema sta qui sotto, subito dopo questa docstring, come blocco
commentato: è uno stampo, non un programma, e non ha output. Si copia nel
proprio script, si tolgono i commenti (Ctrl+/ in PyCharm, Cmd+/ su Mac) e si
cambiano solo le righe marcate # <-- adattare.

IN AZIONE
Il codice eseguibile di questo file è l'In azione: lanciatelo, e l'output
deve essere quello di ESEMPIO OUTPUT in fondo a questa docstring.

VARIANTI
Il file CHIAVE=valore del Giorno 08 §10.5: stesso caricatore con split("=").
Un JSON annidato ({"posti": {"CARDIOLOGIA": 8}}) si legge con due accessi in
fila, configurazione["posti"]["CARDIOLOGIA"].

ERRORI TIPICI
- Chiave non normalizzata al caricamento → KeyError: 'SUD' alla prima
  ricerca.

- Una riga vuota nel file → ValueError: not enough values to unpack
  (expected 2, got 1): se il file può averne, serve il salto di P26.

DA DOVE VIENE
Giorno 06 §8.1, §8.4 · Giorno 07 §11.1 · Giorno 08 §10.3, §10.5, §12.2 ·
Giorno 09 §9.5

DOVE SI USA NEGLI ESERCIZI
10.6, 10.8, 10.11, 10.12

ESEMPIO OUTPUT
{'NORD': 8.5, 'CENTRO': 7.0, 'SUD': 9.5, 'ISOLE': 14.0}
Due chili al SUD: 19.0
{'soglia_urgenza': 5, 'quanti_in_classifica': 10}
"""

# ==========================================================================
# LO SCHEMA — lo stampo da copiare. Non si esegue: è commentato.
# ==========================================================================
# import json
#
#
# def carica_listino(percorso):
#     """Da righe CHIAVE;valore a dizionario {chiave: float}."""
#     listino = {}
#     with open(percorso, encoding="utf-8") as f:
#         for riga in f:
#             chiave, valore = riga.rstrip("\n").split(";")
#             # Chiave normalizzata e valore convertito con float(): la lettura da
#             # file produce sempre str, e il tipo va ristabilito al caricamento.
#             listino[chiave.strip().upper()] = float(valore)  # <-- adattare
#     return listino
#
#
# def carica_configurazione(percorso, default):
#     """Legge un JSON e completa con i default le chiavi che mancano."""
#     with open(percorso, encoding="utf-8") as f:
#         letta = json.load(f)
#     configurazione = {}
#     # Iterazione sui default, non sul file: l'insieme delle chiavi lo fissa
#     # il programma, get() sceglie il valore del file quando c'e'.
#     for chiave, valore in default.items():
#         configurazione[chiave] = letta.get(chiave, valore)
#     return configurazione


# ==========================================================================
# IN AZIONE — lo schema su un caso del corso. Si esegue.
# ==========================================================================
import json
from pathlib import Path

DEFAULT = {"soglia_urgenza": 5, "quanti_in_classifica": 3}
Path("listino_zone.txt").write_text(
    "NORD;8.50\nCENTRO;7.00\n sud ;9.50\nISOLE;14.00\n", encoding="utf-8"
)
# 1. JSON parziale: dichiara una sola delle due chiavi attese, l'altra
#    dovra' arrivare dai default.
Path("config.json").write_text('{"quanti_in_classifica": 10}', encoding="utf-8")


def carica_listino(percorso):
    listino = {}
    with open(percorso, encoding="utf-8") as f:
        for riga in f:
            chiave, valore = riga.rstrip("\n").split(";")
            listino[chiave.strip().upper()] = float(valore)
    return listino


def carica_configurazione(percorso, default):
    with open(percorso, encoding="utf-8") as f:
        letta = json.load(f)
    configurazione = {}
    for chiave, valore in default.items():
        configurazione[chiave] = letta.get(chiave, valore)
    return configurazione


# 2. Normalizzazione applicata al caricamento: " sud " e' diventata la
#    chiave SUD, e le ricerche usano la forma canonica in maiuscolo.
listino = carica_listino("listino_zone.txt")
print(listino)
print("Due chili al SUD:", listino["SUD"] * 2)
print(carica_configurazione("config.json", DEFAULT))

# TRABOCCHETTO: senza float() il prezzo resta testo, e "9.50" * 2 non da'
#   errore: da' "9.509.50", la stringa ripetuta due volte (Giorno 02). Il
#   numero sbagliato arriva nel report, e nessuno l'ha visto partire.
