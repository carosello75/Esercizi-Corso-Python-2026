# ==========================================================
# ESERCIZIO 10 - PROGETTO FINALE: MINI APP PER LLM SENZA API
# ==========================================================

"""
COSA DEVE FARE L'ESERCIZIO

Realizzare una piccola applicazione da terminale che simuli
la struttura di un'applicazione destinata a utilizzare un LLM.

Non viene ancora utilizzata una vera API.

Il programma deve:

1. contenere la configurazione e la knowledge base di un hotel;
2. salvare e leggere la knowledge base da un file JSON;
3. mostrare un menu interattivo;
4. permettere all'utente di inserire una richiesta;
5. classificare la richiesta nel reparto corretto;
6. costruire un prompt strutturato;
7. generare una risposta simulata;
8. salvare le conversazioni in un file JSON;
9. mostrare l'ultimo prompt costruito;
10. creare un report delle richieste per reparto.

Utilizzare:
- variabili;
- input e output;
- if / elif / else;
- while e for;
- funzioni;
- liste e dizionari;
- JSON;
- lettura e scrittura di file.
"""


# ==========================================================
# IMPORT E FILE
# ==========================================================

from pathlib import Path
import json


OUTPUT_DIR = Path(__file__).resolve().parent / "output_esercizio_10"
OUTPUT_DIR.mkdir(exist_ok=True)

FILE_KB = OUTPUT_DIR / "knowledge_base.json"
FILE_LOG = OUTPUT_DIR / "conversazioni.json"


# ==========================================================
# KNOWLEDGE BASE INIZIALE
# ==========================================================

hotel = {
    "nome": "Hotel Aurora Palace",
    "citta": "Napoli",
    "checkin": "14:00",
    "checkout": "11:00",
    "wifi": True,
    "spa": {
        "apertura": "09:00",
        "chiusura": "20:00"
    },
    "servizi": [
        "Wi-Fi",
        "SPA",
        "Ristorante",
        "Transfer"
    ]
}


# ==========================================================
# FUNZIONI PER LA KNOWLEDGE BASE
# ==========================================================

def salva_knowledge_base(dati):

    FILE_KB.write_text(
        json.dumps(
            dati,
            ensure_ascii=False,
            indent=2
        ),
        encoding="utf-8"
    )


def carica_knowledge_base():

    # Se il file non esiste ancora, viene creato
    # utilizzando i dati iniziali dell'hotel.
    if not FILE_KB.exists():
        salva_knowledge_base(hotel)

    contenuto = FILE_KB.read_text(
        encoding="utf-8"
    )

    return json.loads(contenuto)


# ==========================================================
# CLASSIFICAZIONE DELLA RICHIESTA
# ==========================================================

def classifica_richiesta(testo):

    testo = testo.lower()

    if any(
        parola in testo
        for parola in [
            "prenota",
            "camera",
            "check-in",
            "checkin",
            "check-out",
            "checkout"
        ]
    ):
        return "Reception"

    if any(
        parola in testo
        for parola in [
            "spa",
            "massaggio",
            "piscina"
        ]
    ):
        return "SPA"

    if any(
        parola in testo
        for parola in [
            "cena",
            "ristorante",
            "colazione"
        ]
    ):
        return "Ristorante"

    if any(
        parola in testo
        for parola in [
            "cuscino",
            "asciugamani",
            "pulizia"
        ]
    ):
        return "Housekeeping"

    return "Altro"


# ==========================================================
# COSTRUZIONE DEL PROMPT
# ==========================================================

def costruisci_prompt(richiesta, reparto, kb):

    prompt = f"""
RUOLO
Sei un assistente virtuale per {kb['nome']}.

REPARTO
{reparto}

RICHIESTA UTENTE
{richiesta}

DATI DISPONIBILI
Check-in: {kb['checkin']}
Check-out: {kb['checkout']}
Wi-Fi: {kb['wifi']}
Servizi: {", ".join(kb['servizi'])}


ISTRUZIONI
Rispondi utilizzando soltanto le informazioni disponibili.
Se il dato manca, invita a contattare la reception.
""".strip()

    return prompt


# ==========================================================
# RISPOSTA SIMULATA
# ==========================================================

def risposta_simulata(richiesta, reparto, kb):

    testo = richiesta.lower()

    if "check-in" in testo or "checkin" in testo:
        return f"Il check-in è disponibile dalle {kb['checkin']}."

    if "check-out" in testo or "checkout" in testo:
        return f"Il check-out è previsto entro le {kb['checkout']}."

    if "spa" in testo:
        return (
            f"La SPA è aperta dalle "
            f"{kb['spa']['apertura']} "
            f"alle {kb['spa']['chiusura']}."
        )

    if "wifi" in testo:

        if kb["wifi"]:
            return "Il Wi-Fi è disponibile in struttura."

        return "Il Wi-Fi non risulta disponibile."

    if reparto == "Housekeeping":
        return "La richiesta può essere inoltrata al reparto Housekeeping."

    if reparto == "Ristorante":
        return (
            "Per dettagli e disponibilità del ristorante "
            "contatta la reception."
        )

    return (
        "Non ho informazioni sufficienti. "
        "Contatta la reception."
    )


# ==========================================================
# SALVATAGGIO CONVERSAZIONI
# ==========================================================

def salva_conversazioni(conversazioni):

    FILE_LOG.write_text(
        json.dumps(
            conversazioni,
            ensure_ascii=False,
            indent=2
        ),
        encoding="utf-8"
    )


# ==========================================================
# REPORT
# ==========================================================

def crea_report(conversazioni):

    conteggi = {}

    for conversazione in conversazioni:

        reparto = conversazione["reparto"]

        if reparto not in conteggi:
            conteggi[reparto] = 0

        conteggi[reparto] += 1

    print("\n--- REPORT CONVERSAZIONI ---")

    print(f"Totale richieste: {len(conversazioni)}")

    for reparto, numero in conteggi.items():
        print(f"{reparto}: {numero}")


# ==========================================================
# AVVIO APPLICAZIONE
# ==========================================================

kb = carica_knowledge_base()

conversazioni = []


while True:

    print("""
====================================
MINI APP PER LLM - VERSIONE DIDATTICA
====================================
1) Nuova richiesta
2) Visualizza knowledge base
3) Visualizza report
4) Visualizza ultimo prompt costruito
0) Esci
""")

    scelta = input("Scelta: ").strip()


    # ------------------------------------------------------
    # NUOVA RICHIESTA
    # ------------------------------------------------------

    if scelta == "1":

        richiesta = input("\nOSPITE: ").strip()

        reparto = classifica_richiesta(richiesta)

        prompt = costruisci_prompt(
            richiesta,
            reparto,
            kb
        )

        risposta = risposta_simulata(
            richiesta,
            reparto,
            kb
        )

        conversazione = {
            "richiesta": richiesta,
            "reparto": reparto,
            "prompt": prompt,
            "risposta": risposta
        }

        conversazioni.append(conversazione)

        salva_conversazioni(conversazioni)

        print(f"\nREPARTO: {reparto}")
        print(f"RISPOSTA: {risposta}")


    # ------------------------------------------------------
    # KNOWLEDGE BASE
    # ------------------------------------------------------

    elif scelta == "2":

        print(
            json.dumps(
                kb,
                ensure_ascii=False,
                indent=2
            )
        )


    # ------------------------------------------------------
    # REPORT
    # ------------------------------------------------------

    elif scelta == "3":

        crea_report(conversazioni)


    # ------------------------------------------------------
    # ULTIMO PROMPT
    # ------------------------------------------------------

    elif scelta == "4":

        if conversazioni:
            print("\n--- ULTIMO PROMPT ---")
            print(conversazioni[-1]["prompt"])

        else:
            print("Nessun prompt ancora costruito.")


    # ------------------------------------------------------
    # USCITA
    # ------------------------------------------------------

    elif scelta == "0":

        print("Chiusura applicazione.")
        break


    else:

        print("Scelta non valida.")