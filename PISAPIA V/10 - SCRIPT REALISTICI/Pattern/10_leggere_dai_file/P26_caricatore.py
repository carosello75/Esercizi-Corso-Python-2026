"""
P26 — Il caricatore: da file delimitato a lista di righe numerate, e il
    numero di riga dell'editor

Catalogo dei pattern, Giorno 10 — capitolo 10, Leggere dai file
Teoria: TEORIA_GIORNO_10.md §10.2

IN SINTESI
Legge un file delimitato e restituisce le righe utili come coppie (numero di
riga, campi puliti), saltando righe vuote e commenti.

DESCRIZIONE
Il file crea con write_text() il file spedizioni_lotto.txt, con un commento,
una riga vuota e due righe malformate. La funzione carica_righe() riceve il
percorso, lo apre con with open in UTF-8, numera le righe con enumerate(f,
1), salta con continue vuote e commenti, spezza su SEPARATORE applicando
strip() a ogni campo e restituisce una lista di tuple (numero, campi). Il
ciclo finale stampa ogni riga con il suo numero, senza la 1 e la 4. Il
secondo esempio crea ordini_settimana.csv, consuma l'intestazione con
readline(), numera con enumerate(f, start=2) e segnala la quantità non
numerica alla riga 3.

LO SCHEMA
Lo schema sta qui sotto, subito dopo questa docstring, come blocco
commentato: è uno stampo, non un programma, e non ha output. Si copia nel
proprio script, si tolgono i commenti (Ctrl+/ in PyCharm, Cmd+/ su Mac) e si
cambiano solo le righe marcate # <-- adattare.

IN AZIONE
Il codice eseguibile di questo file è l'In azione: lanciatelo, e l'output
deve essere quello di ESEMPIO OUTPUT in fondo a questa docstring.

VARIANTI
csv.reader(f, delimiter=";") con newline="" al posto dello split, quando un
campo può contenere il separatore fra virgolette (Giorno 08 §9.6); il
conteggio delle righe vuote saltate, per l'invariante di P32.

ERRORI TIPICI
- enumerate(f) senza il secondo argomento → numeri da 0: ogni scarto indica
  la riga sopra quella giusta.

- La riga pulita e i campi no → " sud " resta con gli spazi e non combacia
  con nessuna zona.

DA DOVE VIENE
Giorno 07 §6.3, §14.1 · Giorno 08 §4.3, §5.2, §5.3, §9.5, §10.1 · Giorno 09
§9.6

DOVE SI USA NEGLI ESERCIZI
10.3, 10.4, 10.6, 10.8, 10.11, casa_10.1, casa_10.2, casa_10.3, casa_10.4

ESEMPIO OUTPUT
riga 2: ['LS-0701', 'NORD', '12.5']
riga 3: ['LS-0702', 'sud', '7.2']
riga 5: ['LS-0703', 'ISOLE', '3.0']
riga 6: ['LS-0704', 'CENTRO']
riga 7: ['LS-0705', 'NORD', 'venti']
riga 3: campo quantita non numerico: 'due'
Colonne: ['codice', 'categoria', 'quantita']
"""

# ==========================================================================
# LO SCHEMA — lo stampo da copiare. Non si esegue: è commentato.
# ==========================================================================
# SEPARATORE = ";"  # <-- adattare
#
#
# def carica_righe(percorso):
#     """Restituisce [(numero_riga, campi), ...] delle righe utili del file."""
#     righe = []
#     with open(percorso, encoding="utf-8") as f:
#         # Numerazione a base 1 assegnata da enumerate prima di ogni filtro:
#         # il numero resta quello dell'editor anche dopo le righe saltate.
#         for numero, riga in enumerate(f, 1):
#             riga = riga.rstrip("\n")
#             if riga.strip() == "" or riga.startswith("#"):  # <-- adattare
#                 continue
#             # strip() per campo (P6): gli spazi attorno al separatore stanno
#             # dentro i campi, e uno strip() sulla riga non li raggiunge.
#             campi = []
#             for campo in riga.split(SEPARATORE):
#                 campi.append(campo.strip())
#             righe.append((numero, campi))
#     return righe


# ==========================================================================
# IN AZIONE — lo schema su un caso del corso. Si esegue.
# ==========================================================================
from pathlib import Path

SEPARATORE = ";"
PERCORSO = Path("spedizioni_lotto.txt")
PERCORSO.write_text(
    "# lotto del mattino, magazzino SUD\n"
    "LS-0701;NORD;12.5\n"
    "LS-0702; sud ;7.2\n"
    "\n"
    "LS-0703;ISOLE;3.0\n"
    "LS-0704;CENTRO\n"
    "LS-0705;NORD;venti\n",
    encoding="utf-8",
)


def carica_righe(percorso):
    righe = []
    with open(percorso, encoding="utf-8") as f:
        for numero, riga in enumerate(f, 1):
            riga = riga.rstrip("\n")
            if riga.strip() == "" or riga.startswith("#"):
                continue
            campi = []
            for campo in riga.split(SEPARATORE):
                campi.append(campo.strip())
            righe.append((numero, campi))
    return righe


# 1. Nessuna validazione nel caricatore: le righe 6 e 7, malformate,
#    passano intatte al validatore (P24).
# 2. I numeri 1 (commento) e 4 (vuota) mancano: la numerazione non viene
#    compattata e resta allineata al file.
for numero, campi in carica_righe(PERCORSO):
    print(f"riga {numero}: {campi}")

# TRABOCCHETTO: con un contatore numero += 1 scritto dopo il continue, al
#   posto di enumerate, LS-0704 diventa la riga 4: chi apre l'editor alla
#   riga 4 trova la riga vuota, e corregge la riga sbagliata.


# ==========================================================================
# ANCORA IN AZIONE — l'esempio che la teoria aggiunge alla scheda.
# ==========================================================================
from pathlib import Path

PERCORSO = Path("ordini_settimana.csv")
PERCORSO.write_text(
    "codice;categoria;quantita\n"
    "NS-1001;AUDIO;2\n"
    "NS-1002;VIDEO;due\n",
    encoding="utf-8",
)

with open(PERCORSO, encoding="utf-8") as f:
    # 1. readline() consuma l'intestazione prima del ciclo: il for riprende
    #    dalla riga successiva (Giorno 08 §9.5).
    colonne = f.readline().rstrip("\n").split(";")
    # 2. start=2 compensa la riga gia' consumata: il numero stampato
    #    coincide con quello dell'editor.
    for numero, riga in enumerate(f, start=2):
        campi = riga.rstrip("\n").split(";")
        if not campi[2].isdecimal():
            print(f"riga {numero}: campo {colonne[2]} non numerico: '{campi[2]}'")
print("Colonne:", colonne)
