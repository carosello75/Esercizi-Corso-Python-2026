# ==========================================================
# ESERCIZIO 7 - LISTE, DIZIONARI E TUPLE: KNOWLEDGE BASE
# ==========================================================

"""
COSA DEVE FARE L'ESERCIZIO

Realizzare una piccola knowledge base contenente
le informazioni di un hotel.

Utilizzare:

- una tupla per memorizzare gli orari della SPA;
- una lista per memorizzare i servizi;
- un dizionario per raccogliere le informazioni dell'hotel.

Il programma deve:

1. stampare tutti i servizi disponibili;
2. stampare l'orario di apertura e chiusura della SPA;
3. cercare una determinata informazione nel dizionario;
4. aggiungere un nuovo servizio;
5. modificare un'informazione esistente;
6. stampare la knowledge base aggiornata.

Utilizzare:
- liste;
- tuple;
- dizionari;
- ciclo for;
- operatore in;
- append().
"""


# ==========================================================
# SVOLGIMENTO
# ==========================================================

orari_spa = (
    "09:00",
    "20:00"
)

servizi = [
    "Wi-Fi",
    "SPA",
    "Ristorante",
    "Transfer"
]

hotel = {
    "nome": "Hotel Aurora",
    "citta": "Napoli",
    "stelle": 4,
    "checkin": "14:00",
    "checkout": "11:00",
    "servizi": servizi,
    "orari_spa": orari_spa
}


print("\n--- SERVIZI ---")

for servizio in hotel["servizi"]:
    print("-", servizio)


print("\n--- ORARI SPA ---")

print(f"Apertura: {hotel['orari_spa'][0]}")
print(f"Chiusura: {hotel['orari_spa'][1]}")


print("\n--- RICERCA INFORMAZIONE ---")

chiave = "checkin"

# L'operatore "in" verifica se la chiave
# è presente nel dizionario.
if chiave in hotel:
    print(f"{chiave}: {hotel[chiave]}")
else:
    print("Informazione non presente.")


# append() aggiunge un nuovo elemento alla lista.
hotel["servizi"].append("Parcheggio")

# Assegnando un nuovo valore a una chiave esistente
# modifichiamo l'informazione nel dizionario.
hotel["checkout"] = "10:30"


print("\n--- KNOWLEDGE BASE AGGIORNATA ---")

print(hotel)