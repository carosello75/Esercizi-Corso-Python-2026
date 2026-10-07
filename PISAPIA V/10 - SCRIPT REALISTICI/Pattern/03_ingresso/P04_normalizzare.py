"""
P4 — Normalizzare un testo: .strip(), maiuscole, spazi e simboli interni

Catalogo dei pattern, Giorno 10 — capitolo 3, L'ingresso: dal testo grezzo al dato
Teoria: TEORIA_GIORNO_10.md §3.1

IN SINTESI
Riduce un testo digitato a una forma canonica, togliendo gli spazi superflui
e uniformando le maiuscole prima di ogni confronto.

DESCRIZIONE
Il file parte da due input simulati, NOME_DIGITATO e IBAN_DIGITATO, e
definisce due funzioni che restituiscono senza stampare: normalizza_codice()
applica .strip().upper(), normalizza_nome() ricompone le parole con "
".join(testo.split()) e applica .title(). Il nome diventa [Rossi Anna];
l'IBAN, normalizzato, perde anche gli spazi interni con .replace(" ", "") e
risulta di 27 caratteri. Un ciclo mostra il limite di .title() su due
cognomi, e l'ultima riga confronta il nome con il testo cercato, prima
grezzo e poi normalizzato: False True.

LO SCHEMA
Lo schema sta qui sotto, subito dopo questa docstring, come blocco
commentato: è uno stampo, non un programma, e non ha output. Si copia nel
proprio script, si tolgono i commenti (Ctrl+/ in PyCharm, Cmd+/ su Mac) e si
cambiano solo le righe marcate # <-- adattare.

IN AZIONE
Il codice eseguibile di questo file è l'In azione: lanciatelo, e l'output
deve essere quello di ESEMPIO OUTPUT in fondo a questa docstring.

VARIANTI
- normalizza_codice() per codici, sigle, categorie; normalizza_nome() per
  nomi e cognomi. Non si scambiano.

- Un telefono come 333-123.45 67: tre .replace() in catena, o un ciclo su
  una lista di simboli in costante.

ERRORI TIPICI
- .title() rende bene D'ANGELO, ma MCDONALD diventa Mcdonald: è un limite,
  si dichiara nella docstring.

- Normalizzare un lato solo del confronto (nel codice qui sotto): la ricerca
  fallisce senza errori. La stessa funzione va su tutti e due i lati.

DA DOVE VIENE
Giorno 02 §10.2, §10.5 · Giorno 03 §5.2, §5.3, §5.5, §7.6, §12.3 · Giorno 04
§7.2 · Giorno 05 §9.4 · Giorno 08 §5.4

DOVE SI USA NEGLI ESERCIZI
10.2, 10.5, 10.6, 10.9, casa_10.1

ESEMPIO OUTPUT
[Rossi Anna]
[IT60X0542811101000000123456] 27 caratteri
D'ANGELO -> D'Angelo
MCDONALD -> Mcdonald
False True
"""

# ==========================================================================
# LO SCHEMA — lo stampo da copiare. Non si esegue: è commentato.
# ==========================================================================
# def normalizza_codice(testo):
#     """Restituisce il codice senza spazi ai bordi, in maiuscolo."""
#     return testo.strip().upper()
#
#
# def normalizza_nome(testo):
#     """Restituisce il nome con un solo spazio fra le parole, iniziali maiuscole."""
#     return " ".join(testo.split()).title()
#
#
# # I separatori interni (spazi, trattini, punti) richiedono un .replace()
# # ciascuno: .strip() agisce solo sui bordi.
# codice = normalizza_codice(testo_digitato).replace(" ", "")   # <-- adattare


# ==========================================================================
# IN AZIONE — lo schema su un caso del corso. Si esegue.
# ==========================================================================
NOME_DIGITATO = "  rOSSI   anna "
IBAN_DIGITATO = "it60 x054 2811 1010 0000 0123 456"


def normalizza_codice(testo):
    """Restituisce il codice senza spazi ai bordi, in maiuscolo."""
    return testo.strip().upper()


def normalizza_nome(testo):
    """Restituisce il nome con un solo spazio fra le parole, iniziali maiuscole."""
    # split() senza argomenti divide su ogni sequenza di spazi e ignora i
    # bordi; join() ricompone con uno spazio singolo (Giorno 03 §7.6).
    return " ".join(testo.split()).title()


nome = normalizza_nome(NOME_DIGITATO)
# Normalizzazione di bordi e maiuscole, poi .replace() rimuove gli spazi
# interni, che .strip() non tocca.
iban = normalizza_codice(IBAN_DIGITATO).replace(" ", "")
print(f"[{nome}]")
print(f"[{iban}] {len(iban)} caratteri")
for cognome in ["D'ANGELO", "MCDONALD"]:
    print(f"{cognome} -> {normalizza_nome(cognome)}")
# TRABOCCHETTO: normalizzare un solo lato del confronto. "rossi anna" scritto
#   da chi cerca non e' "Rossi Anna": == restituisce False e la ricerca
#   fallisce senza eccezioni.
cercato = "rossi anna"
print(nome == cercato, nome == normalizza_nome(cercato))
