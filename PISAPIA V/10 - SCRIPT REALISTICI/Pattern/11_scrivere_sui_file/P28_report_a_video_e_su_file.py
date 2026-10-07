"""
P28 — Il report composto una volta: lista di righe, a video e su file

Catalogo dei pattern, Giorno 10 — capitolo 11, Scrivere sui file
Teoria: TEORIA_GIORNO_10.md §11.1

IN SINTESI
Compone il report una sola volta come lista di stringhe e lo invia a video o
su file con la stessa funzione, cambiando solo la destinazione.

DESCRIZIONE
Il file definisce PRATICHE, le pratiche evase per ufficio, e
PERCORSO_REPORT. componi_report() riceve il dizionario e restituisce, senza
stampare, una lista di stringhe con il titolo, una riga incolonnata per
ufficio e il totale; stampa_righe() riceve le righe e un parametro file,
None per default, e le invia con print(riga, file=file). Le stesse righe
vanno prima a video, poi in report_pratiche.txt aperto in modalità "w".
Infine il file viene riletto con read_text().splitlines(): il programma
stampa 5 righe per ciascuna destinazione e il confronto fra le due liste,
True.

LO SCHEMA
Lo schema sta qui sotto, subito dopo questa docstring, come blocco
commentato: è uno stampo, non un programma, e non ha output. Si copia nel
proprio script, si tolgono i commenti (Ctrl+/ in PyCharm, Cmd+/ su Mac) e si
cambiano solo le righe marcate # <-- adattare.

IN AZIONE
Il codice eseguibile di questo file è l'In azione: lanciatelo, e l'output
deve essere quello di ESEMPIO OUTPUT in fondo a questa docstring.

VARIANTI
Tutto in una chiamata: "\n".join(righe) + "\n" passato a write_text(), con
l'a capo finale aggiunto a mano (Giorno 08 §6.4). Due larghezze: la
larghezza come parametro di componi_report().

ERRORI TIPICI
- file=f dimenticato → il report esce due volte a video, il file resta
  vuoto.

- Due codici di composizione, uno per il video e uno per il file → al primo
  ritocco l'archivio non è più quello che si è visto.

DA DOVE VIENE
Giorno 06 §8.1, §9.1 · Giorno 08 §6.1, §6.3, §6.4, §11.1, §11.2, §11.5

DOVE SI USA NEGLI ESERCIZI
10.5, 10.8, 10.9, 10.11, casa_10.1

ESEMPIO OUTPUT
PRATICHE EVASE PER UFFICIO
ANAGRAFE          42
TRIBUTI           18
EDILIZIA           9
Totale            69
Righe a video 5, righe nel file 5
File identico al video: True
"""

# ==========================================================================
# LO SCHEMA — lo stampo da copiare. Non si esegue: è commentato.
# ==========================================================================
# def componi_report(dati):  # <-- adattare: i dati che servono al report
#     """Restituisce le righe del report come lista di stringhe. Non stampa."""
#     righe = ["TITOLO DEL REPORT"]  # <-- adattare
#     for chiave, valore in dati.items():
#         righe.append(f"{chiave:<14}{valore:>10.2f}")  # <-- adattare: P2, P3
#     return righe
#
#
# def stampa_righe(righe, file=None):
#     """Manda le righe a video (file=None, il default di print) o sul file."""
#     for riga in righe:
#         print(riga, file=file)


# ==========================================================================
# IN AZIONE — lo schema su un caso del corso. Si esegue.
# ==========================================================================
from pathlib import Path

PRATICHE = {"ANAGRAFE": 42, "TRIBUTI": 18, "EDILIZIA": 9}
PERCORSO_REPORT = Path("report_pratiche.txt")


def componi_report(conteggi):
    righe = ["PRATICHE EVASE PER UFFICIO"]
    for ufficio, quante in conteggi.items():
        righe.append(f"{ufficio:<14}{quante:>6}")
    righe.append(f"{'Totale':<14}{sum(conteggi.values()):>6}")
    return righe


def stampa_righe(righe, file=None):
    for riga in righe:
        print(riga, file=file)


righe = componi_report(PRATICHE)
# 1. Prima destinazione: file=None, cioe' lo standard output.
stampa_righe(righe)
# 2. Seconda destinazione: lo stesso elenco di righe verso il file
#    aperto in "w", passato come argomento file.
with open(PERCORSO_REPORT, "w", encoding="utf-8") as f:
    stampa_righe(righe, file=f)
# 3. Verifica di andata e ritorno (Giorno 08 §11.5): il file riletto
#    con splitlines() deve coincidere riga per riga con la lista.
rilette = PERCORSO_REPORT.read_text(encoding="utf-8").splitlines()
print(f"Righe a video {len(righe)}, righe nel file {len(rilette)}")
print("File identico al video:", rilette == righe)

# TRABOCCHETTO: con f.write(riga) al posto di print(riga, file=file) le
#   cinque righe finiscono incollate su una sola: "righe nel file 1", e il
#   confronto dice False. write() non va a capo da sola (Giorno 08 §6.1).
