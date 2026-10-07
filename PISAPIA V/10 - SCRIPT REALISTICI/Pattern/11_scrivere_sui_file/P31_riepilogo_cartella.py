"""
P31 — Il riepilogo di una cartella: glob, sorted() e le righe di ogni file

Catalogo dei pattern, Giorno 10 — capitolo 11, Scrivere sui file
Teoria: TEORIA_GIORNO_10.md §11.4

IN SINTESI
Seleziona con glob i file di una cartella che rispondono a un modello di
nome, li ordina con sorted() e ne riassume il contenuto file per file.

DESCRIZIONE
Il file crea la cartella esportazioni nella cartella di lavoro e vi scrive,
in ordine non alfabetico, tre file .txt, uno dei quali vuoto, e una nota
note.md. righe_per_file() riceve cartella e modello di nome, scorre
sorted(cartella.glob(modello)), conta le righe di ogni file con
len(f.readlines()) dentro un with open e restituisce una lista di tuple
(nome, righe). Il ciclo principale, sul modello "*.txt", stampa nome e righe
incolonnati, aggiunge [!] vuoto ai file a zero righe, accumula il totale e
chiude con 3 file e 5 righe.

LO SCHEMA
Lo schema sta qui sotto, subito dopo questa docstring, come blocco
commentato: è uno stampo, non un programma, e non ha output. Si copia nel
proprio script, si tolgono i commenti (Ctrl+/ in PyCharm, Cmd+/ su Mac) e si
cambiano solo le righe marcate # <-- adattare.

IN AZIONE
Il codice eseguibile di questo file è l'In azione: lanciatelo, e l'output
deve essere quello di ESEMPIO OUTPUT in fondo a questa docstring.

VARIANTI
Il nome del file come dato: percorso.stem dà negozio_centro, e
.replace("negozio_", "") lascia centro. I file attesi contro i trovati: una
lista ATTESI confrontata con i nomi (P21) dice quale file non è arrivato,
che glob non può dire; il mancante si tratta con P33.

ERRORI TIPICI
- Elenco non ordinato → output diverso fra macchine.

- Modello troppo largo → entrano file che non sono dati.

DA DOVE VIENE
Giorno 08 §7.5, §13.1, §13.2, §13.4

DOVE SI USA NEGLI ESERCIZI
10.10

ESEMPIO OUTPUT
a.txt     3
b.txt     0  [!] vuoto
c.txt     2
File 3, righe in tutto 5
"""

# ==========================================================================
# LO SCHEMA — lo stampo da copiare. Non si esegue: è commentato.
# ==========================================================================
# def righe_per_file(cartella, modello):  # <-- adattare: cartella e modello
#     """Restituisce [(nome, righe), ...] dei file del modello, ordinata per nome."""
#     risultato = []
#     # sorted() rende l'ordine deterministico: glob restituisce i file
#     # nell'ordine del file system, che varia fra macchine.
#     for percorso in sorted(cartella.glob(modello)):
#         with open(percorso, encoding="utf-8") as f:
#             risultato.append((percorso.name, len(f.readlines())))
#     return risultato


# ==========================================================================
# IN AZIONE — lo schema su un caso del corso. Si esegue.
# ==========================================================================
from pathlib import Path

CARTELLA = Path("esportazioni")
CARTELLA.mkdir(exist_ok=True)
# 1. File creati in ordine non alfabetico: l'ordine dell'output deve
#    dipendere da sorted(), non dalla sequenza di creazione.
(CARTELLA / "c.txt").write_text("riga 1\nriga 2\n", encoding="utf-8")
(CARTELLA / "a.txt").write_text("riga 1\nriga 2\nriga 3\n", encoding="utf-8")
(CARTELLA / "b.txt").write_text("", encoding="utf-8")
(CARTELLA / "note.md").write_text("da non contare\n", encoding="utf-8")


def righe_per_file(cartella, modello):
    risultato = []
    for percorso in sorted(cartella.glob(modello)):
        with open(percorso, encoding="utf-8") as f:
            risultato.append((percorso.name, len(f.readlines())))
    return risultato


totale = 0
elenco = righe_per_file(CARTELLA, "*.txt")
for nome, righe in elenco:
    # 2. Un file a zero righe non solleva eccezioni ma va segnalato: e'
    #    spesso il sintomo di un'esportazione non riuscita.
    riga_report = f"{nome:<8}{righe:>3}"
    if righe == 0:
        riga_report += "  [!] vuoto"
    print(riga_report)
    totale += righe
print(f"File {len(elenco)}, righe in tutto {totale}")

# TRABOCCHETTO: senza sorted() l'ordine e' quello del disco, e su due
#   macchine esce diverso: stesso programma, due output, collaudo in DIFF.
#   Con "*" al posto di "*.txt" entra anche note.md: 4 file, 6 righe.
