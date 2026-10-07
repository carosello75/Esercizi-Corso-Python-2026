# ==========================================================
# ESERCIZIO 1 - VARIABILI, TIPI DI DATO, INPUT E OUTPUT
# ==========================================================

"""
COSA DEVE FARE L'ESERCIZIO

Realizzare una semplice scheda di configurazione per un assistente AI
di un hotel.

Il programma deve chiedere all'utente:

- nome dell'hotel;
- numero di camere;
- prezzo medio di una camera;
- presenza o meno della SPA;
- lingua principale dell'assistente.

Al termine deve stampare una scheda riepilogativa contenente tutti
i dati inseriti e mostrare il tipo di dato di ogni variabile.

Utilizzare:
- variabili;
- str, int, float e bool;
- input();
- print();
- conversione dei tipi;
- f-string.
"""


# ==========================================================
# SVOLGIMENTO
# ==========================================================

nome_hotel = input("Nome hotel: ")

# input() restituisce sempre una stringa:
# convertiamo quindi il numero di camere in int.
numero_camere = int(input("Numero camere: "))

# Il prezzo può contenere decimali, quindi utilizziamo float.
prezzo_medio = float(input("Prezzo medio camera (€): "))

spa_input = input(
    "La struttura ha una SPA? (sì/no): "
).strip().lower()

# L'espressione restituisce True se la risposta inserita
# è una delle risposte positive previste, altrimenti False.
ha_spa = spa_input in {"si", "sì", "s", "yes", "y"}

lingua = input(
    "Lingua principale dell'assistente: "
).strip()


# ==========================================================
# RIEPILOGO
# ==========================================================

print("\n--- SCHEDA CONFIGURAZIONE ---")

print(f"Hotel: {nome_hotel}")
print(f"Camere: {numero_camere}")
print(f"Prezzo medio: € {prezzo_medio:.2f}")
print(f"SPA presente: {ha_spa}")
print(f"Lingua principale: {lingua}")


# ==========================================================
# TIPI DI DATO
# ==========================================================

print("\n--- TIPI DI DATO ---")

print("nome_hotel    ->", type(nome_hotel))
print("numero_camere ->", type(numero_camere))
print("prezzo_medio  ->", type(prezzo_medio))
print("ha_spa        ->", type(ha_spa))
print("lingua        ->", type(lingua))