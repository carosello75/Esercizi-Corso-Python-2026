"""
P33 — Il file che manca o non si legge: un except per causa e un ripiego

Catalogo dei pattern, Giorno 10 — capitolo 12, Gli errori previsti
Teoria: TEORIA_GIORNO_10.md §12.2

IN SINTESI
Legge un file intercettando ogni causa d'errore prevista con un except
dedicato e, dove possibile, ripiega su una seconda lettura o su un default.

DESCRIZIONE
Il file crea nella cartella di lavoro anagrafe_vecchia.txt, codificato in
latin-1, e config.json, con una virgola mancante; tariffe.txt invece non
esiste. leggi_testo() riceve un percorso e restituisce il testo letto in
UTF-8; su FileNotFoundError stampa l'errore e restituisce la stringa vuota,
su UnicodeDecodeError avvisa e rilegge in latin-1. Un ciclo la applica a
tariffe.txt e anagrafe_vecchia.txt e stampa la lunghezza del testo, 0 e 11
caratteri. Infine json.loads() analizza il testo di config.json dentro un
try: il JSONDecodeError viene stampato con riga e messaggio, e la
configurazione diventa un dizionario vuoto.

LO SCHEMA
Lo schema sta qui sotto, subito dopo questa docstring, come blocco
commentato: è uno stampo, non un programma, e non ha output. Si copia nel
proprio script, si tolgono i commenti (Ctrl+/ in PyCharm, Cmd+/ su Mac) e si
cambiano solo le righe marcate # <-- adattare.

IN AZIONE
Il codice eseguibile di questo file è l'In azione: lanciatelo, e l'output
deve essere quello di ESEMPIO OUTPUT in fondo a questa docstring.

VARIANTI
Path.exists() prima di aprire, per il messaggio, e il try comunque, per la
garanzia (Giorno 09 §9.2). Sulla configurazione rotta, invece di {}, i
default di P27: il programma lavora con i valori di sempre, e lo dice.

ERRORI TIPICI
- print(e) di un FileNotFoundError → il percorso intero nel messaggio,
  Giorno 09 E9.

- Il ripiego silenzioso, riletto in latin-1 senza dirlo → chi manda il file
  non saprà mai che il suo gestionale usa la codifica sbagliata.

DA DOVE VIENE
Giorno 01 §14.2 · Giorno 08 §8.1, §8.2 · Giorno 09 §3.3, §7.2, §7.3, §8.8,
§9.1, §9.2, §9.3, §9.4

DOVE SI USA NEGLI ESERCIZI
10.10

ESEMPIO OUTPUT
[ERRORE] manca tariffe.txt: chiedetelo a chi lo invia
    tariffe.txt: 0 caratteri
[!] anagrafe_vecchia.txt non è in utf-8: riletto in latin-1
    anagrafe_vecchia.txt: 11 caratteri
[ERRORE] config.json alla riga 3: Expecting ',' delimiter
Arrivato in fondo. Configurazione: {}
"""

# ==========================================================================
# LO SCHEMA — lo stampo da copiare. Non si esegue: è commentato.
# ==========================================================================
# def leggi_testo(percorso):
#     """Restituisce il testo del file, oppure "" se non c'e'. Mai un traceback."""
#     try:
#         return percorso.read_text(encoding="utf-8")
#     # Un except per classe d'eccezione, dalla piu' specifica alla piu'
#     # generale: vince la prima clausola compatibile (Giorno 09 §7.2).
#     except FileNotFoundError:
#         print(f"[ERRORE] manca {percorso.name}: chiedetelo a chi lo invia")
#     except UnicodeDecodeError:
#         # Ripiego dichiarato: seconda decodifica in latin-1, che accetta
#         # qualunque sequenza di byte. Il messaggio rende visibile il ripiego.
#         print(f"[!] {percorso.name} non è in utf-8: riletto in latin-1")
#         return percorso.read_text(encoding="latin-1")  # <-- adattare
#     return ""


# ==========================================================================
# IN AZIONE — lo schema su un caso del corso. Si esegue.
# ==========================================================================
import json
from pathlib import Path

# 1. Tre casi di prova: file assente, file codificato in latin-1,
#    JSON sintatticamente non valido per una virgola mancante.
Path("anagrafe_vecchia.txt").write_text("Città;Salò\n", encoding="latin-1")
Path("config.json").write_text(
    '{\n  "soglia": 5\n  "righe": 3\n}\n', encoding="utf-8"
)


def leggi_testo(percorso):
    try:
        return percorso.read_text(encoding="utf-8")
    except FileNotFoundError:
        print(f"[ERRORE] manca {percorso.name}: chiedetelo a chi lo invia")
    except UnicodeDecodeError:
        print(f"[!] {percorso.name} non è in utf-8: riletto in latin-1")
        return percorso.read_text(encoding="latin-1")
    return ""


for nome in ["tariffe.txt", "anagrafe_vecchia.txt"]:
    testo = leggi_testo(Path(nome))
    print(f"    {nome}: {len(testo)} caratteri")

# 2. La lettura come testo riesce: l'errore e' sintattico e lo solleva
#    json.loads() come JSONDecodeError, con riga e messaggio.
try:
    configurazione = json.loads(leggi_testo(Path("config.json")))
except json.JSONDecodeError as e:
    print(f"[ERRORE] config.json alla riga {e.lineno}: {e.msg}")
    configurazione = {}
print("Arrivato in fondo. Configurazione:", configurazione)

# TRABOCCHETTO: un except OSError scritto SOPRA except FileNotFoundError
#   prende anche il file mancante, perche' FileNotFoundError e' sua figlia:
#   il messaggio specifico non si stampa mai, e nessuno ve lo segnala.
