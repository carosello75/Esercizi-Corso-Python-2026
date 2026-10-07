# ==========================================================
# ESERCIZIO 4 - CICLO FOR: ANALISI DI PIÙ PROMPT
# ==========================================================

"""
COSA DEVE FARE L'ESERCIZIO

Data una lista di prompt, il programma deve analizzare
ogni elemento della lista.

Per ogni prompt deve:

- stampare il testo;
- calcolare e mostrare la lunghezza;
- verificare se contiene la parola "hotel";
- contare quanti prompt hanno più di 40 caratteri.

Al termine deve mostrare il numero totale dei prompt
con più di 40 caratteri.

Utilizzare:
- liste;
- ciclo for;
- enumerate();
- contatori;
- len();
- operatore in.
"""


# ==========================================================
# SVOLGIMENTO
# ==========================================================

prompts = [
    "Vorrei prenotare una camera doppia",
    "Quali sono gli orari della SPA?",
    "Scrivi una descrizione per il nostro hotel",
    "Dove posso parcheggiare?",
    "Genera una email di benvenuto per gli ospiti dell'hotel",
]

conteggio_lunghi = 0


# enumerate() permette di ottenere contemporaneamente
# il numero progressivo e il valore presente nella lista.
for indice, prompt in enumerate(prompts, start=1):

    print(f"\n--- PROMPT {indice} ---")

    print(prompt)

    lunghezza = len(prompt)

    print(f"Lunghezza: {lunghezza}")

    contiene_hotel = "hotel" in prompt.lower()

    print(f"Contiene 'hotel': {contiene_hotel}")

    if lunghezza > 40:
        conteggio_lunghi += 1


print(
    f"\nPrompt con più di 40 caratteri: {conteggio_lunghi}"
)