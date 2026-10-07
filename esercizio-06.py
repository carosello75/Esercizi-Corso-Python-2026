# ==========================================================
# ESERCIZIO 6 - FUNZIONI: PROMPT BUILDER
# ==========================================================

"""
COSA DEVE FARE L'ESERCIZIO

Realizzare una funzione che costruisca automaticamente
un prompt strutturato.

La funzione deve ricevere quattro parametri:

- ruolo;
- compito;
- contesto;
- formato dell'output.

Utilizzando questi dati deve costruire e restituire
una stringa contenente il prompt completo.

Successivamente utilizzare la stessa funzione per creare
almeno 3 prompt differenti e stamparli a video.

Utilizzare:
- def;
- parametri;
- return;
- f-string;
- ciclo for;
- enumerate().
"""


# ==========================================================
# SVOLGIMENTO
# ==========================================================

def crea_prompt(ruolo, compito, contesto, formato):

    prompt = f"""
RUOLO
{ruolo}

COMPITO
{compito}

CONTESTO
{contesto}

FORMATO OUTPUT
{formato}
""".strip()

    # return restituisce il prompt costruito al punto
    # del programma in cui la funzione è stata chiamata.
    return prompt


prompt_1 = crea_prompt(
    ruolo="Copywriter hospitality",
    compito="Scrivi una descrizione camera",
    contesto="Camera deluxe vista mare con balcone",
    formato="Massimo 120 parole"
)

prompt_2 = crea_prompt(
    ruolo="Assistente reception",
    compito="Scrivi una email pre-arrival",
    contesto="Ospite in arrivo domani alle 18:00",
    formato="Email con oggetto e corpo"
)

prompt_3 = crea_prompt(
    ruolo="Analista recensioni",
    compito="Riassumi i punti critici",
    contesto="Recensioni degli ultimi 30 giorni",
    formato="3 bullet point"
)


# Inseriamo i prompt in una lista per poterli
# elaborare tutti con lo stesso ciclo.
prompts = [
    prompt_1,
    prompt_2,
    prompt_3
]

for numero, prompt in enumerate(prompts, start=1):

    print(f"\n--- PROMPT {numero} ---")
    print(prompt)