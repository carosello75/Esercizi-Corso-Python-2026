# ==========================================================
# ESERCIZIO 2 - IF / ELIF / ELSE: CLASSIFICATORE DI PROMPT
# ==========================================================

"""
COSA DEVE FARE L'ESERCIZIO

Realizzare un semplice classificatore di prompt.

L'utente deve inserire una richiesta e il programma deve
analizzare il testo e assegnarlo a una delle seguenti categorie:

- "Prenotazione"
  se contiene parole come:
  prenota, camera, disponibilità

- "Ristorante"
  se contiene parole come:
  ristorante, cena, colazione

- "SPA"
  se contiene parole come:
  spa, massaggio, piscina

- "Informazioni"
  se contiene parole come:
  orario, parcheggio, wifi

- "Altro"
  se non viene individuata nessuna delle parole precedenti.

Utilizzare:
- if / elif / else;
- operatori booleani;
- operatore in;
- stringhe;
- lower().
"""


# ==========================================================
# SVOLGIMENTO
# ==========================================================

richiesta = input(
    "Inserisci la richiesta dell'ospite: "
).strip()

# Convertiamo tutto in minuscolo per rendere il confronto
# indipendente da come l'utente ha scritto maiuscole e minuscole.
testo = richiesta.lower()


# Controlliamo in ordine le diverse categorie.
# Appena una condizione risulta vera, Python assegna
# la categoria e non valuta gli elif successivi.

if (
    "prenota" in testo
    or "camera" in testo
    or "disponibilità" in testo
    or "disponibilita" in testo
):
    categoria = "Prenotazione"

elif (
    "ristorante" in testo
    or "cena" in testo
    or "colazione" in testo
):
    categoria = "Ristorante"

elif (
    "spa" in testo
    or "massaggio" in testo
    or "piscina" in testo
):
    categoria = "SPA"

elif (
    "orario" in testo
    or "parcheggio" in testo
    or "wifi" in testo
):
    categoria = "Informazioni"

else:
    categoria = "Altro"


print(f"\nCategoria individuata: {categoria}")