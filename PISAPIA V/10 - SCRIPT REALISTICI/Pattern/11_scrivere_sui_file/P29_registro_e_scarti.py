"""
P29 — Il registro e il file degli scarti: modalità a e ripartenza pulita

Catalogo dei pattern, Giorno 10 — capitolo 11, Scrivere sui file
Teoria: TEORIA_GIORNO_10.md §11.2

IN SINTESI
Svuota il registro all'avvio e vi accoda una riga per evento in modalità
"a", così che il file descriva solo l'ultima esecuzione.

DESCRIZIONE
Il file definisce PERCORSO_REGISTRO, cioè registro_pesi.log nella cartella
di lavoro, e le righe codice;peso di RIGHE. apri_registro() svuota il file
scrivendo una stringa vuota; registra() lo apre in modalità "a" e accoda una
riga NNN | LIVELLO | messaggio. esegui() chiama apri_registro(), scorre
enumerate(RIGHE, 1), registra come SCARTO ogni peso che non supera
isdecimal() e chiude con un evento INFO numerato 0. Il programma lancia
esegui() due volte, legge il registro dopo ciascuna, stampa il secondo
contenuto e il confronto fra i due, True.

LO SCHEMA
Lo schema sta qui sotto, subito dopo questa docstring, come blocco
commentato: è uno stampo, non un programma, e non ha output. Si copia nel
proprio script, si tolgono i commenti (Ctrl+/ in PyCharm, Cmd+/ su Mac) e si
cambiano solo le righe marcate # <-- adattare.

IN AZIONE
Il codice eseguibile di questo file è l'In azione: lanciatelo, e l'output
deve essere quello di ESEMPIO OUTPUT in fondo a questa docstring.

VARIANTI
Il file degli scarti riga;motivo;contenuto, aperto in "w" una volta con
l'intestazione e riletto poi con P26 per correggere riga per riga. Lo
storico di più esecuzioni si fa con un registro per esecuzione, con nomi
diversi, non con un file che cresce.

ERRORI TIPICI
- "a" senza ripartenza → il registro cresce a ogni lancio: E8.

- apri_registro() dentro il ciclo → ogni giro svuota il file: restano
  l'ultimo scarto (004) e la riga di fine, lo scarto 002 sparisce. E il
  confronto fra due esecuzioni dice comunque True: il registro è stabile,
  solo che è sbagliato.

DA DOVE VIENE
Giorno 08 §6.5, §11.3, §11.4 · Giorno 09 §15.1, §15.2, §15.3

DOVE SI USA NEGLI ESERCIZI
10.5, 10.7, 10.11, 10.12

ERRORI TIPICI DELLA GIORNATA COLLEGATI (teoria, capitolo 14)
- E8 — Il file in output/ che cresce a ogni lancio: "a" senza ripartenza
  pulita

ESEMPIO OUTPUT
002 | SCARTO | peso non numerico: 'venti'
004 | SCARTO | peso non numerico: ''
000 | INFO   | fine: 4 righe lette
Due esecuzioni, stesso registro: True
"""

# ==========================================================================
# LO SCHEMA — lo stampo da copiare. Non si esegue: è commentato.
# ==========================================================================
# def apri_registro(percorso):
#     """Ripartenza pulita: svuota il registro all'avvio del programma."""
#     # write_text equivale a un'apertura in "w": crea il file o lo tronca a
#     # lunghezza zero. E' la ripartenza pulita del registro.
#     percorso.write_text("", encoding="utf-8")
#
#
# def registra(percorso, numero, livello, messaggio):
#     """Accoda una riga NNN | LIVELLO | messaggio. Livelli: INFO, SCARTO, ERRORE."""
#     with open(percorso, "a", encoding="utf-8") as f:
#         f.write(f"{numero:03d} | {livello:<6} | {messaggio}\n")


# ==========================================================================
# IN AZIONE — lo schema su un caso del corso. Si esegue.
# ==========================================================================
from pathlib import Path

PERCORSO_REGISTRO = Path("registro_pesi.log")
RIGHE = ["LS-0901;12.5", "LS-0902;venti", "LS-0903;7.2", "LS-0904;"]


def apri_registro(percorso):
    percorso.write_text("", encoding="utf-8")


def registra(percorso, numero, livello, messaggio):
    with open(percorso, "a", encoding="utf-8") as f:
        f.write(f"{numero:03d} | {livello:<6} | {messaggio}\n")


def esegui():
    apri_registro(PERCORSO_REGISTRO)
    for numero, riga in enumerate(RIGHE, 1):
        peso = riga.split(";")[1]
        if not peso.replace(".", "", 1).isdecimal():
            # 1. Il numero registrato e' quello della riga d'origine: rende lo
            #    scarto rintracciabile nel file di partenza.
            motivo = f"peso non numerico: '{peso}'"
            registra(PERCORSO_REGISTRO, numero, "SCARTO", motivo)
    # 2. Numero convenzionale 0 per gli eventi del programma, che non
    #    corrispondono a nessuna riga del file d'ingresso.
    registra(PERCORSO_REGISTRO, 0, "INFO", f"fine: {len(RIGHE)} righe lette")


esegui()
prima = PERCORSO_REGISTRO.read_text(encoding="utf-8")
esegui()
dopo = PERCORSO_REGISTRO.read_text(encoding="utf-8")
print(dopo, end="")
print("Due esecuzioni, stesso registro:", prima == dopo)

# TRABOCCHETTO: togliete apri_registro() e alla seconda esecuzione il
#   registro ha sei righe, con 002 e 004 due volte ciascuna. Nessun errore,
#   e il confronto dice False: e' E8.
