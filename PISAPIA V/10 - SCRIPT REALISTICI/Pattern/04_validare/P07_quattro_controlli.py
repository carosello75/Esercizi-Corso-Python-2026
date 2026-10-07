"""
P7 — I quattro controlli: presenza, forma, intervallo, valori ammessi, e la
    variabile errore

Catalogo dei pattern, Giorno 10 — capitolo 4, Validare
Teoria: TEORIA_GIORNO_10.md §4.1

IN SINTESI
Valida un dato digitato con quattro controlli in cascata (presenza, forma,
intervallo, valori ammessi) e conserva il motivo del rifiuto.

DESCRIZIONE
Il file fissa in costanti l'intervallo d'età ETA_MINIMA-ETA_MASSIMA e la
lista SEDI_AMMESSE, e in PROVE cinque coppie età-sede come le digiterebbe un
candidato. Per ogni coppia normalizza i due testi, inizializza errore a
stringa vuota e lo valorizza con il primo controllo fallito di una catena
if/elif: presenza, forma con .isdecimal(), intervallo con il confronto
concatenato, sede con not in. Un unico if errore finale stampa il rifiuto
con il motivo oppure l'accettazione: passa una sola prova, il candidato di
34 anni.

LO SCHEMA
Lo schema sta qui sotto, subito dopo questa docstring, come blocco
commentato: è uno stampo, non un programma, e non ha output. Si copia nel
proprio script, si tolgono i commenti (Ctrl+/ in PyCharm, Cmd+/ su Mac) e si
cambiano solo le righe marcate # <-- adattare.

IN AZIONE
Il codice eseguibile di questo file è l'In azione: lanciatelo, e l'output
deve essere quello di ESEMPIO OUTPUT in fondo a questa docstring.

VARIANTI
- Due controlli soli: la guardia con il cortocircuito, if testo.isdecimal()
  and int(testo) >= MINIMO: (Giorno 04 §9.2).

- Tutti i difetti in una volta: if separati invece di elif, e i motivi in
  una lista. Utile nei moduli lunghi, dove il ping-pong stanca.

ERRORI TIPICI
- L'intervallo prima della forma: ValueError su int() (nel codice qui
  sotto).

- Il messaggio generico «dato non valido»: il candidato non sa quale campo
  correggere, né come.

DA DOVE VIENE
Giorno 03 §3.5 · Giorno 04 §9.2, §10.3, §11.3, §13.2, §13.8, §13.9

DOVE SI USA NEGLI ESERCIZI
10.2, casa_10.2

ESEMPIO OUTPUT
[OK] candidato di 34 anni, sede REMOTO
[ERRORE] età: 'trenta' non è un numero. Scrivete gli anni in cifre
[ERRORE] età: 15 fuori intervallo. Ammessi da 18 a 67
[ERRORE] età: campo vuoto. Scrivete gli anni in cifre
[ERRORE] sede: 'MILANO' non prevista. Scegliete fra SALERNO, NAPOLI, REMOTO
"""

# ==========================================================================
# LO SCHEMA — lo stampo da copiare. Non si esegue: è commentato.
# ==========================================================================
# MINIMO = 18                                          # <-- adattare
# MASSIMO = 67                                         # <-- adattare
# AMMESSI = ["SALERNO", "NAPOLI", "REMOTO"]            # <-- adattare
#
#
# def motivo_rifiuto(testo_numero, testo_scelta):
#     """Restituisce "" se i dati vanno bene, altrimenti il motivo del rifiuto."""
#     numero = testo_numero.strip()
#     scelta = testo_scelta.strip().upper()
#     errore = ""
#     if not numero:                                   # 1. presenza
#         errore = "campo vuoto"                       # <-- adattare i messaggi
#     elif not numero.isdecimal():                     # 2. forma
#         errore = f"'{numero}' non è un numero"
#     elif not MINIMO <= int(numero) <= MASSIMO:       # 3. intervallo
#         errore = f"{numero} fuori intervallo {MINIMO}-{MASSIMO}"
#     elif scelta not in AMMESSI:                      # 4. valori ammessi
#         errore = f"'{scelta}' non ammesso"
#     return errore


# ==========================================================================
# IN AZIONE — lo schema su un caso del corso. Si esegue.
# ==========================================================================
ETA_MINIMA = 18
ETA_MASSIMA = 67
SEDI_AMMESSE = ["SALERNO", "NAPOLI", "REMOTO"]
PROVE = [("34", " remoto "), ("trenta", "Napoli"), ("15", "Salerno"),
         ("", "Napoli"), ("29", "Milano")]

for testo_eta, testo_sede in PROVE:
    eta = testo_eta.strip()
    sede = testo_sede.strip().upper()
    errore = ""
    if not eta:
        errore = "età: campo vuoto. Scrivete gli anni in cifre"
    elif not eta.isdecimal():
        errore = f"età: '{eta}' non è un numero. Scrivete gli anni in cifre"
    # TRABOCCHETTO: l'intervallo va verificato dopo la forma. Messo prima,
    #   int("trenta") fermerebbe tutto con ValueError: invalid literal for int()
    #   with base 10: 'trenta'. Il controllo 2 e' la precondizione del 3.
    elif not ETA_MINIMA <= int(eta) <= ETA_MASSIMA:
        errore = (f"età: {eta} fuori intervallo. "
                  f"Ammessi da {ETA_MINIMA} a {ETA_MASSIMA}")
    elif sede not in SEDI_AMMESSE:
        errore = (f"sede: '{sede}' non prevista. "
                  f"Scegliete fra {', '.join(SEDI_AMMESSE)}")
    # Punto di uscita unico: la variabile errore decide fra rifiuto e
    # accettazione, e il ramo di successo esiste una volta sola.
    if errore:
        print(f"[ERRORE] {errore}")
    else:
        print(f"[OK] candidato di {eta} anni, sede {sede}")
