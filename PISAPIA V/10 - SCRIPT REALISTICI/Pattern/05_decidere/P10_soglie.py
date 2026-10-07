"""
P10 — La decisione a soglie: la tabella delle soglie come lista di tuple

Catalogo dei pattern, Giorno 10 — capitolo 5, Decidere
Teoria: TEORIA_GIORNO_10.md §5.1

IN SINTESI
Assegna un valore numerico alla prima fascia che lo contiene, con le soglie
tenute come dati in una lista di tuple invece che come rami di codice.

DESCRIZIONE
Il file definisce le quote della mensa come lista di tuple (limite, quota)
in SOGLIE_ISEE e la funzione fascia(), che scorre le coppie con un for e
restituisce la quota del primo limite per cui vale valore <= limite, oppure
QUOTA_OLTRE se nessun limite basta. Un ciclo applica la funzione ai cinque
ISEE di bordo di BORDI e stampa la quota di ciascuno, incolonnata; un assert
fissa il risultato atteso per 8000 euro. In coda la stessa funzione riceve
una tabella in disordine e assegna 45.00 a un ISEE di 7999, senza sollevare
eccezioni.

LO SCHEMA
Lo schema sta qui sotto, subito dopo questa docstring, come blocco
commentato: è uno stampo, non un programma, e non ha output. Si copia nel
proprio script, si tolgono i commenti (Ctrl+/ in PyCharm, Cmd+/ su Mac) e si
cambiano solo le righe marcate # <-- adattare.

IN AZIONE
Il codice eseguibile di questo file è l'In azione: lanciatelo, e l'output
deve essere quello di ESEMPIO OUTPUT in fondo a questa docstring.

VARIANTI
- La catena di elif del Giorno 04 §6.5, equivalente riga per riga. Con due o
  tre soglie fisse si legge meglio, e va benissimo così:

    # La stessa decisione come catena di elif: una soglia, un ramo.
    if isee <= FASCIA_ISEE_1:
        quota = QUOTA_FASCIA_1
    elif isee <= FASCIA_ISEE_2:
        quota = QUOTA_FASCIA_2
    elif isee <= FASCIA_ISEE_3:
        quota = QUOTA_FASCIA_3
    else:
        quota = QUOTA_FASCIA_4

- La lista conviene quando le soglie sono tante, cambiano, o arrivano da un
  file (P27): una fascia in più è una coppia in più, non un ramo.

- Etichette al posto degli importi: [(50, "BASE"), (120, "MEDIA")], "ALTA".

ERRORI TIPICI
- Le soglie non ordinate (nel codice qui sotto): la prima si prende tutto.

- < al posto di <=: 8.000 esatti finiscono in seconda fascia, 30.00 invece
  di 15.00, senza errori. Il bordo si chiede all'ufficio prima (Giorno 04
  §6.3).

DA DOVE VIENE
Giorno 04 §5.1, §6.1, §6.2, §6.3, §6.5 · Giorno 06 §6.4 · Giorno 07 §14.1 ·
Giorno 09 §14.3

DOVE SI USA NEGLI ESERCIZI
10.1, 10.8, casa_10.3

ERRORI TIPICI DELLA GIORNATA COLLEGATI (teoria, capitolo 14)
- E3 — La soglia con >= al posto di >: i casi sul bordo cambiano fascia in
  silenzio

ESEMPIO OUTPUT
ISEE   7999  quota mensile  15.00
ISEE   8000  quota mensile  15.00
ISEE   8001  quota mensile  30.00
ISEE  28000  quota mensile  45.00
ISEE  28001  quota mensile  60.00
Soglie in disordine, ISEE 7999: quota 45.00
"""

# ==========================================================================
# LO SCHEMA — lo stampo da copiare. Non si esegue: è commentato.
# ==========================================================================
# SOGLIE = [(8000, "fascia 1"), (16000, "fascia 2")]   # <-- adattare: crescenti
# OLTRE = "fascia 3"                                   # <-- adattare
#
#
# def fascia(valore, soglie, oltre):
#     """Restituisce l'esito della prima fascia con valore <= limite, o oltre."""
#     # Precondizione: coppie (limite, esito) in ordine crescente di limite.
#     # L'esito e' deciso dal PRIMO limite che soddisfa valore <= limite.
#     for limite, esito in soglie:
#         if valore <= limite:
#             return esito
#     return oltre


# ==========================================================================
# IN AZIONE — lo schema su un caso del corso. Si esegue.
# ==========================================================================
SOGLIE_ISEE = [(8000, 15.00), (16000, 30.00), (28000, 45.00)]
QUOTA_OLTRE = 60.00
BORDI = [7999, 8000, 8001, 28000, 28001]


def fascia(valore, soglie, oltre):
    """Restituisce l'esito della prima fascia con valore <= limite, o oltre."""
    for limite, esito in soglie:
        # <= e non <: la regola dice "fino a 8.000", il limite e' incluso.
        if valore <= limite:
            return esito
    return oltre


# 1. Test sui valori di bordo: limite - 1, limite, limite + 1. Solo li'
#    un operatore sbagliato (< al posto di <=) cambia l'esito.
for isee in BORDI:
    quota = fascia(isee, SOGLIE_ISEE, QUOTA_OLTRE)
    print(f"ISEE {isee:>6}  quota mensile {quota:>6.2f}")
# 2. assert come test di regressione sul bordo (Giorno 09 §14.3): con <
#    al posto di <= il programma si ferma con AssertionError.
assert fascia(8000, SOGLIE_ISEE, QUOTA_OLTRE) == 15.00, "bordo 8000 sbagliato"
# TRABOCCHETTO: le soglie in disordine. La prima coppia e' (28000, 45.00), e
#   7999 <= 28000 e' vero: la prima soglia si prende tutto, senza errori.
DISORDINATE = [(28000, 45.00), (8000, 15.00), (16000, 30.00)]
sbagliata = fascia(7999, DISORDINATE, QUOTA_OLTRE)
print(f"Soglie in disordine, ISEE 7999: quota {sbagliata:.2f}")
