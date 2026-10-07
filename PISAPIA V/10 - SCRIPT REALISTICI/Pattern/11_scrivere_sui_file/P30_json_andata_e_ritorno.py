"""
P30 — JSON andata e ritorno: carica, modifica, salva in output/

Catalogo dei pattern, Giorno 10 — capitolo 11, Scrivere sui file
Teoria: TEORIA_GIORNO_10.md §11.3

IN SINTESI
Carica uno stato da file JSON, lo modifica in memoria e lo salva in output/,
lasciando intatto il file di partenza.

DESCRIZIONE
Il file crea rubrica.json con tre nomi e definisce OUTPUT come cartella
output relativa. carica_json() riceve un percorso e restituisce il contenuto
deserializzato con json.load; salva_json() apre il percorso in "w" e scrive
con json.dump, indent=2 ed ensure_ascii=False. Il programma crea output/,
carica la rubrica, accoda un nome con append(), la salva in
output/rubrica.json e la rilegge: stampa 3 contatti nel file di partenza e 4
in quello salvato, con l'ultimo nome. Il secondo esempio serializza lo
stesso dizionario con e senza ensure_ascii=False, confronta le lunghezze, 50
e 35 caratteri, e stampa il file leggibile.

LO SCHEMA
Lo schema sta qui sotto, subito dopo questa docstring, come blocco
commentato: è uno stampo, non un programma, e non ha output. Si copia nel
proprio script, si tolgono i commenti (Ctrl+/ in PyCharm, Cmd+/ su Mac) e si
cambiano solo le righe marcate # <-- adattare.

IN AZIONE
Il codice eseguibile di questo file è l'In azione: lanciatelo, e l'output
deve essere quello di ESEMPIO OUTPUT in fondo a questa docstring.

VARIANTI
Un dizionario di dizionari al posto della lista (le giacenze per codice): le
due funzioni restano identiche, cambia la modifica. json.dumps() e
json.loads() quando il JSON sta in una stringa (Giorno 08 §12.4).

ERRORI TIPICI
- La chiave intera che torna stringa (Giorno 08 §12.3): {1: "A"} riletto è
  {"1": "A"}, e dati[1] dà KeyError: 1. La tupla torna lista.

- ensure_ascii=False senza encoding="utf-8" nell'open → su Windows il file
  esce in un'altra codifica (Giorno 08 §12.2).

DA DOVE VIENE
Giorno 08 §12.1, §12.2, §12.3, §12.4, §12.7 · Giorno 09 §9.4

DOVE SI USA NEGLI ESERCIZI
10.7, 10.11, 10.12, casa_10.3

ESEMPIO OUTPUT
Contatti di partenza: 3
Contatti salvati: 4 - ultimo: Nocera Nicolò
predefinito.json   50 caratteri, stesso dizionario: True
leggibile.json     35 caratteri, stesso dizionario: True
{"nome": "Nicolò", "città": "Salò"}
"""

# ==========================================================================
# LO SCHEMA — lo stampo da copiare. Non si esegue: è commentato.
# ==========================================================================
# import json
#
#
# def carica_json(percorso):
#     """Restituisce il contenuto del file JSON: una lista o un dizionario."""
#     with open(percorso, encoding="utf-8") as f:
#         return json.load(f)
#
#
# def salva_json(percorso, dati):
#     """Scrive i dati in JSON leggibile: rientri di 2, lettere accentate vere."""
#     # Destinazione in output/, distinta dalla sorgente in dati/: salvare
#     # sopra l'originale rende il programma non idempotente.
#     with open(percorso, "w", encoding="utf-8") as f:
#         json.dump(dati, f, indent=2, ensure_ascii=False)


# ==========================================================================
# IN AZIONE — lo schema su un caso del corso. Si esegue.
# ==========================================================================
import json
from pathlib import Path

PARTENZA = Path("rubrica.json")
OUTPUT = Path("output")
PARTENZA.write_text('["Serra Marta", "Motta Luca", "Greco Anna"]', encoding="utf-8")


def carica_json(percorso):
    with open(percorso, encoding="utf-8") as f:
        return json.load(f)


def salva_json(percorso, dati):
    with open(percorso, "w", encoding="utf-8") as f:
        json.dump(dati, f, indent=2, ensure_ascii=False)


# 1. Carica, modifica in memoria, salva in output/: la sorgente non viene
#    mai riscritta, quindi ogni esecuzione riparte dagli stessi dati.
OUTPUT.mkdir(exist_ok=True)
rubrica = carica_json(PARTENZA)
rubrica.append("Nocera Nicolò")
salva_json(OUTPUT / "rubrica.json", rubrica)
# 2. Rilettura del file appena serializzato (Giorno 08 §11.5): permette
#    di controllare che il disco contenga lo stato in memoria.
riletta = carica_json(OUTPUT / "rubrica.json")
print("Contatti di partenza:", len(carica_json(PARTENZA)))
print("Contatti salvati:", len(riletta), "- ultimo:", riletta[-1])

# TRABOCCHETTO: in un programma vero, salvando sopra PARTENZA invece che in
#   output/, ogni lancio riparte dal file del lancio prima: 4 contatti, poi
#   5, poi 6, con Nocera ripetuto. Nessun errore, e l'originale e' perso.


# ==========================================================================
# ANCORA IN AZIONE — l'esempio che la teoria aggiunge alla scheda.
# ==========================================================================
import json
from pathlib import Path

CONTATTO = {"nome": "Nicolò", "città": "Salò"}

# 1. Stesso dizionario serializzato due volte: ensure_ascii al valore
#    predefinito, True, e poi a False.
Path("predefinito.json").write_text(json.dumps(CONTATTO), encoding="utf-8")
Path("leggibile.json").write_text(
    json.dumps(CONTATTO, ensure_ascii=False), encoding="utf-8"
)
for nome_file in ["predefinito.json", "leggibile.json"]:
    testo = Path(nome_file).read_text(encoding="utf-8")
    # 2. La deserializzazione restituisce lo stesso dizionario: cambia solo
    #    la rappresentazione su disco, e con essa la lunghezza.
    uguale = json.loads(testo) == CONTATTO
    print(f"{nome_file:<18}{len(testo):>3} caratteri, stesso dizionario: {uguale}")
print(Path("leggibile.json").read_text(encoding="utf-8"))
