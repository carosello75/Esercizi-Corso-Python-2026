"""
P25 — Le cartelle di lavoro: DATI e OUTPUT accanto allo script, con
    Path(__file__)

Catalogo dei pattern, Giorno 10 — capitolo 10, Leggere dai file
Teoria: TEORIA_GIORNO_10.md §10.1

IN SINTESI
Ancora i percorsi dei file alla cartella dello script con
Path(__file__).resolve().parent e crea le cartelle di output prima di
scriverci.

DESCRIZIONE
Il file costruisce le costanti di percorso a partire da CARTELLA =
Path(__file__).resolve().parent: DATI, OUTPUT come sottocartella
output/preventivi, e i due file PERCORSO_LISTINO e PERCORSO_ASSENTE. Crea
DATI con exist_ok=True e OUTPUT anche con parents=True, poi scrive in
listino_zone.txt una riga di listino con write_text(). Non stampa percorsi
assoluti: mostra che CARTELLA è assoluta, che la cartella dei prodotti
esiste e, per ciascuno dei due file, nome, estensione da .suffix ed esito di
exists(), True per il listino e False per l'altro.

LO SCHEMA
Lo schema sta qui sotto, subito dopo questa docstring, come blocco
commentato: è uno stampo, non un programma, e non ha output. Si copia nel
proprio script, si tolgono i commenti (Ctrl+/ in PyCharm, Cmd+/ su Mac) e si
cambiano solo le righe marcate # <-- adattare.

IN AZIONE
Il codice eseguibile di questo file è l'In azione: lanciatelo, e l'output
deve essere quello di ESEMPIO OUTPUT in fondo a questa docstring.

VARIANTI
Lo script in una sottocartella e i dati una sopra, come negli esercizi di
oggi: Path(__file__).resolve().parent.parent / "dati" (a casa, tre .parent).
Una sottocartella per esercizio, OUTPUT / "promemoria".

ERRORI TIPICI
- Path("dati") / "ordini.txt", relativo → funziona solo lanciando dalla
  cartella giusta (Giorno 08 E1, qui E9).

- Il percorso intero nel messaggio → illeggibile e diverso su ogni macchina.

DA DOVE VIENE
Giorno 08 §7.1, §7.3, §7.4, §7.5, §8.1, §8.3 · Giorno 09 E9

DOVE SI USA NEGLI ESERCIZI
10.1, 10.5, 10.10

ERRORI TIPICI DELLA GIORNATA COLLEGATI (teoria, capitolo 14)
- E9 — Il percorso relativo che funziona solo da PyCharm

ESEMPIO OUTPUT
Cartella dello script assoluta? True
Cartella dei prodotti: preventivi True
listino_zone.txt      .txt  True
tariffe_vecchie.txt   .txt  False
"""

# ==========================================================================
# LO SCHEMA — lo stampo da copiare. Non si esegue: è commentato.
# ==========================================================================
# from pathlib import Path
#
# # Percorso assoluto della cartella dello script, indipendente dalla
# # directory di lavoro del processo (Giorno 08 §7.4).
# CARTELLA = Path(__file__).resolve().parent
# DATI = CARTELLA / "dati"  # <-- adattare: nomi delle cartelle
# OUTPUT = CARTELLA / "output"
# PERCORSO_INGRESSO = DATI / "ordini.txt"  # <-- adattare: i file del caso
#
# # Creazione idempotente: exist_ok=True tollera la cartella esistente,
# # parents=True crea anche i livelli intermedi mancanti.
# OUTPUT.mkdir(parents=True, exist_ok=True)
# if not PERCORSO_INGRESSO.exists():
#     # Messaggio con il solo .name: il percorso assoluto varia da macchina
#     # a macchina e rende il testo illeggibile (Giorno 09 E9).
#     print(f"[ERRORE] manca {PERCORSO_INGRESSO.name} nella cartella dati")


# ==========================================================================
# IN AZIONE — lo schema su un caso del corso. Si esegue.
# ==========================================================================
from pathlib import Path

CARTELLA = Path(__file__).resolve().parent
DATI = CARTELLA / "dati"
OUTPUT = CARTELLA / "output" / "preventivi"
PERCORSO_LISTINO = DATI / "listino_zone.txt"
PERCORSO_ASSENTE = DATI / "tariffe_vecchie.txt"

# 1. mkdir con exist_ok=True e' idempotente: dalla seconda esecuzione
#    trova le cartelle e non solleva FileExistsError.
DATI.mkdir(exist_ok=True)
OUTPUT.mkdir(parents=True, exist_ok=True)
PERCORSO_LISTINO.write_text("NORD;8.50\n", encoding="utf-8")

# 2. Il percorso assoluto si usa ma non si stampa: dipende dalla macchina
#    (/Users/ su Mac, C: su Windows) e l'output non sarebbe confrontabile
#    in collaudo. Si stampano solo proprieta' stabili.
print("Cartella dello script assoluta?", CARTELLA.is_absolute())
print("Cartella dei prodotti:", OUTPUT.name, OUTPUT.exists())
for percorso in [PERCORSO_LISTINO, PERCORSO_ASSENTE]:
    print(f"{percorso.name:<22}{percorso.suffix:<6}{percorso.exists()}")

# TRABOCCHETTO: senza parents=True, OUTPUT.mkdir() si ferma con
#   FileNotFoundError, perche' "output" non esiste ancora e mkdir crea un
#   livello solo. Dalla seconda esecuzione non succede piu': il difetto si
#   vede solo sulla macchina pulita di chi riceve lo script.
