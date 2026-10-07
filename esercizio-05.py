# ==========================================================
# ESERCIZIO 5 - WHILE: MENU INTERATTIVO DI UN ASSISTENTE
# ==========================================================

"""
COSA DEVE FARE L'ESERCIZIO

Realizzare un semplice menu interattivo per un assistente
di un hotel.

Il programma deve permettere all'utente di scegliere:

1 - visualizzare un messaggio di benvenuto;
2 - visualizzare i servizi disponibili;
3 - visualizzare gli orari;
4 - visualizzare la lingua configurata;
0 - uscire dal programma.

Dopo ogni operazione il menu deve essere mostrato nuovamente.

Il programma deve continuare a funzionare fino a quando
l'utente sceglie l'opzione 0.

Se viene inserita un'opzione non prevista, il programma
deve mostrare un messaggio di errore e tornare al menu.

Utilizzare:
- while;
- input();
- if / elif / else;
- break;
- controllo del flusso.
"""


# ==========================================================
# SVOLGIMENTO
# ==========================================================

lingua = "Italiano"

# while True crea un ciclo che continua indefinitamente.
# Sarà break a interromperlo quando l'utente sceglie di uscire.
while True:

    print("""
==============================
MINI ASSISTENTE HOTEL
==============================
1) Saluto
2) Servizi
3) Orari
4) Lingua
0) Esci
""")

    scelta = input("Scegli: ").strip()

    if scelta == "1":
        print("Benvenuto! Come posso aiutarti?")

    elif scelta == "2":
        print("Servizi: camere, ristorante, SPA, transfer.")

    elif scelta == "3":
        print("Reception: 24h | SPA: 09:00-20:00")

    elif scelta == "4":
        print(f"Lingua configurata: {lingua}")

    elif scelta == "0":
        print("Programma terminato.")

        # break interrompe immediatamente il ciclo while.
        break

    else:
        print("Scelta non valida.")