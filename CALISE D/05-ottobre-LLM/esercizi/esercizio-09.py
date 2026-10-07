# ==========================================================
# ESERCIZIO 9 - LETTURA E SCRITTURA FILE: LOG E KNOWLEDGE BASE
# ==========================================================

"""
COSA DEVE FARE L'ESERCIZIO

Realizzare un programma che salvi e legga dati utilizzando
tre diversi formati di file: TXT, JSON e CSV.

Il programma deve:

1. creare un file TXT contenente alcune FAQ dell'hotel;
2. leggere e stampare il contenuto del file TXT;
3. creare un file JSON contenente una knowledge base;
4. leggere il JSON e recuperare alcune informazioni;
5. creare un file CSV contenente alcune richieste degli ospiti;
6. leggere e stampare tutte le righe del CSV.

Tutti i file devono essere salvati nella cartella "output_esercizio_09".

Utilizzare:
- Path;
- lettura e scrittura di file;
- JSON;
- CSV;
- with;
- ciclo for.
"""


# ==========================================================
# SVOLGIMENTO
# ==========================================================

from pathlib import Path
import json
import csv


OUTPUT_DIR = Path(__file__).resolve().parent / "output_esercizio_09"
OUTPUT_DIR.mkdir(exist_ok=True)


# ==========================================================
# FILE TXT
# ==========================================================

file_txt = OUTPUT_DIR / "faq.txt"

contenuto_faq = """FAQ HOTEL

1. Check-in?
Dalle 14:00.

2. Check-out?
Entro le 11:00.

3. SPA?
Aperta dalle 09:00 alle 20:00.
"""

file_txt.write_text(
    contenuto_faq,
    encoding="utf-8"
)

testo_letto = file_txt.read_text(
    encoding="utf-8"
)

print("\n--- CONTENUTO TXT ---")
print(testo_letto)


# ==========================================================
# FILE JSON
# ==========================================================

knowledge_base = {
    "hotel": "Hotel Aurora",
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
        "Ristorante"
    ]
}

file_json = OUTPUT_DIR / "knowledge_base.json"

# json.dumps() trasforma il dizionario Python
# in una stringa in formato JSON.
file_json.write_text(
    json.dumps(
        knowledge_base,
        ensure_ascii=False,
        indent=2
    ),
    encoding="utf-8"
)

# json.loads() esegue l'operazione inversa:
# dal testo JSON ricostruisce le strutture dati Python.
dati_json = json.loads(
    file_json.read_text(encoding="utf-8")
)

print("\n--- DATI DAL JSON ---")
print(f"Hotel: {dati_json['hotel']}")
print(f"Check-in: {dati_json['checkin']}")
print(f"SPA: {dati_json['spa']['apertura']} - "
      f"{dati_json['spa']['chiusura']}")


# ==========================================================
# FILE CSV
# ==========================================================

richieste = [
    {
        "id": 1,
        "testo": "Vorrei due cuscini",
        "reparto": "Housekeeping"
    },
    {
        "id": 2,
        "testo": "A che ora apre la SPA?",
        "reparto": "SPA"
    },
    {
        "id": 3,
        "testo": "Posso cenare alle 21?",
        "reparto": "Ristorante"
    }
]

file_csv = OUTPUT_DIR / "richieste.csv"

# DictWriter permette di scrivere nel CSV
# una lista di dizionari.
with file_csv.open(
    "w",
    encoding="utf-8-sig",
    newline=""
) as file:

    writer = csv.DictWriter(
        file,
        fieldnames=["id", "testo", "reparto"]
    )

    writer.writeheader()
    writer.writerows(richieste)


# DictReader legge ogni riga del CSV
# restituendola sotto forma di dizionario.
with file_csv.open(
    "r",
    encoding="utf-8-sig",
    newline=""
) as file:

    reader = csv.DictReader(file)

    print("\n--- RICHIESTE DAL CSV ---")

    for row in reader:
        print(
            f"#{row['id']} | "
            f"{row['reparto']} | "
            f"{row['testo']}"
        )