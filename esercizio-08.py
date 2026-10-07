# ==========================================================
# ESERCIZIO 8 - FUNZIONI + STRUTTURE DATI: ROUTER DI RICHIESTE
# ==========================================================

"""
COSA DEVE FARE L'ESERCIZIO

Realizzare un piccolo sistema che riceva diverse richieste
degli ospiti e le assegni automaticamente al reparto corretto.

Le categorie disponibili sono:

- Reception;
- Housekeeping;
- Ristorante;
- SPA;
- Altro.

Il programma deve:

1. creare una funzione classifica_richiesta() che analizzi
   il testo e restituisca il reparto corretto;

2. creare una funzione crea_ticket() che generi un dizionario
   contenente:
   - id;
   - testo della richiesta;
   - reparto;
   - stato;

3. elaborare una lista di richieste;

4. salvare tutti i ticket in una lista di dizionari;

5. stampare tutti i ticket creati;

6. contare e stampare quanti ticket sono stati assegnati
   a ciascun reparto.

Utilizzare:
- funzioni;
- if;
- return;
- liste;
- dizionari;
- ciclo for;
- enumerate();
- append().
"""


# ==========================================================
# SVOLGIMENTO
# ==========================================================

def classifica_richiesta(testo):

    testo = testo.lower()

    if (
        "check-in" in testo
        or "checkin" in testo
        or "prenotazione" in testo
        or "camera" in testo
    ):
        return "Reception"

    if (
        "asciugamani" in testo
        or "cuscini" in testo
        or "pulizia" in testo
    ):
        return "Housekeeping"

    if (
        "cena" in testo
        or "ristorante" in testo
        or "colazione" in testo
    ):
        return "Ristorante"

    if (
        "spa" in testo
        or "massaggio" in testo
        or "piscina" in testo
    ):
        return "SPA"

    return "Altro"


def crea_ticket(numero, testo):

    reparto = classifica_richiesta(testo)

    ticket = {
        "id": numero,
        "testo": testo,
        "reparto": reparto,
        "stato": "Aperto"
    }

    return ticket


richieste = [
    "Vorrei due cuscini aggiuntivi",
    "A che ora posso fare il check-in?",
    "Vorrei prenotare un massaggio",
    "Posso cenare alle 21?",
    "Avete biciclette?"
]

tickets = []


# Ogni richiesta viene trasformata in un ticket
# e aggiunta alla lista dei ticket.
for numero, richiesta in enumerate(richieste, start=1):

    ticket = crea_ticket(numero, richiesta)
    tickets.append(ticket)


print("\n--- TICKET CREATI ---")

for ticket in tickets:

    print(
        f"#{ticket['id']} | "
        f"{ticket['reparto']} | "
        f"{ticket['stato']} | "
        f"{ticket['testo']}"
    )


print("\n--- CONTEGGIO PER REPARTO ---")

conteggi = {}

for ticket in tickets:

    reparto = ticket["reparto"]

    # Se il reparto non è ancora presente nel dizionario,
    # inizializziamo il suo contatore a zero.
    if reparto not in conteggi:
        conteggi[reparto] = 0

    conteggi[reparto] += 1


for reparto, numero in conteggi.items():
    print(f"{reparto} -> {numero}")