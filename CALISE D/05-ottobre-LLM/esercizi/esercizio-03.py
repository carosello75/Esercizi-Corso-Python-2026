# ==========================================================
# ESERCIZIO 3 - CONDIZIONI MULTIPLE: VALUTATORE DI PROMPT
# ==========================================================

"""
COSA DEVE FARE L'ESERCIZIO

Realizzare un programma che valuti la qualità di un prompt
prima di inviarlo a un LLM.

L'utente deve:

- scrivere un prompt;
- indicare se contiene un obiettivo chiaro;
- indicare se contiene un contesto;
- indicare se specifica il formato dell'output.

Il programma deve assegnare:

+1 punto se il prompt contiene almeno 30 caratteri
+1 punto se contiene un obiettivo chiaro
+1 punto se contiene un contesto
+1 punto se specifica il formato dell'output

In base al punteggio ottenuto deve classificare il prompt come:

0-1 punti -> Debole
2 punti   -> Sufficiente
3 punti   -> Buono
4 punti   -> Ottimo

Utilizzare:
- variabili booleane;
- if / elif / else;
- condizioni multiple;
- len();
- contatori.
"""


# ==========================================================
# SVOLGIMENTO
# ==========================================================

prompt = input("Scrivi un prompt: ").strip()

# Il risultato dell'operatore "in" è un booleano:
# True se la risposta è presente nell'insieme, False altrimenti.
obiettivo = input(
    "Il prompt contiene un obiettivo chiaro? (sì/no): "
).strip().lower() in {"si", "sì", "s"}

contesto = input(
    "Contiene contesto? (sì/no): "
).strip().lower() in {"si", "sì", "s"}

formato = input(
    "Specifica il formato dell'output? (sì/no): "
).strip().lower() in {"si", "sì", "s"}


# Il punteggio parte da zero e viene incrementato
# ogni volta che una condizione viene soddisfatta.
punteggio = 0

if len(prompt) >= 30:
    punteggio += 1

if obiettivo:
    punteggio += 1

if contesto:
    punteggio += 1

if formato:
    punteggio += 1


# Trasformiamo il punteggio numerico
# in una valutazione comprensibile.
if punteggio <= 1:
    livello = "Debole"

elif punteggio == 2:
    livello = "Sufficiente"

elif punteggio == 3:
    livello = "Buono"

else:
    livello = "Ottimo"


print("\n--- RISULTATO ---")

print(f"Prompt: {prompt}")
print(f"Lunghezza: {len(prompt)} caratteri")
print(f"Punteggio: {punteggio} / 4")
print(f"Livello: {livello}")