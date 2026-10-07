"""
P14 — Il menu a scelta: while True, una funzione per voce, break sull'uscita

Catalogo dei pattern, Giorno 10 — capitolo 6, Ripetere
Teoria: TEORIA_GIORNO_10.md §6.2

IN SINTESI
Tiene aperto un programma interattivo che esegue la funzione associata alla
voce scelta e torna al menu fino alla voce d'uscita.

DESCRIZIONE
Il file definisce il dizionario MENU, che associa codici e voci, e tre
funzioni senza argomenti, una per voce, che stampano la risposta come
effetto collaterale. La funzione sportello() riceve le scelte simulate e, in
un for che fa le veci del while True, stampa l'eco e smista ogni stringa con
una catena if/elif: le voci chiamano la loro funzione, 0 stampa la chiusura
ed esce con break, ogni altro valore finisce nell'else come scelta non
valida. Il programma stampa il menu scorrendo MENU.items() e chiama
sportello() con quattro scelte.

LO SCHEMA
Lo schema sta qui sotto, subito dopo questa docstring, come blocco
commentato: è uno stampo, non un programma, e non ha output. Si copia nel
proprio script, si tolgono i commenti (Ctrl+/ in PyCharm, Cmd+/ su Mac) e si
cambiano solo le righe marcate # <-- adattare.

IN AZIONE
Il codice eseguibile di questo file è l'In azione: lanciatelo, e l'output
deve essere quello di ESEMPIO OUTPUT in fondo a questa docstring.

VARIANTI
- La voce d'uscita che salva la situazione in un JSON prima di chiudere
  (P30).

- Le voci che chiedono un dato usano chiedi_intero() di P9: il menu delega.

ERRORI TIPICI
- Il confronto con 1 intero invece di "1" (nel codice qui sotto): la voce
  non scatta mai, senza errori. input() restituisce sempre una stringa.

- La logica delle voci dentro il ciclo: il while diventa di ottanta righe e
  nessuna voce si prova da sola (Giorno 06 §2.3).

DA DOVE VIENE
Giorno 04 §5.1 · Giorno 05 §8.4, §10.1 · Giorno 06 §1.3, §2.3 · Giorno 09
§8.7

DOVE SI USA NEGLI ESERCIZI
10.7, 10.12

ESEMPIO OUTPUT
1) Certificato di residenza
2) Stato di una pratica
3) Orari dello sportello
0) Esci
Scelta (1-3, 0 per uscire): 1
   Certificato di residenza: pronto in giornata.
Scelta (1-3, 0 per uscire): 3
   Sportello aperto la mattina, dalle 8.30 alle 12.30.
Scelta (1-3, 0 per uscire): 9
   [!] Scelta non valida: 9
Scelta (1-3, 0 per uscire): 0
   Sportello chiuso.
"""

# ==========================================================================
# LO SCHEMA — lo stampo da copiare. Non si esegue: è commentato.
# ==========================================================================
# def voce_uno():                                      # <-- adattare: una per voce
#     """Il lavoro della voce 1 sta qui, non dentro il ciclo."""
#     print("Voce uno eseguita.")
#
#
# def main():
#     while True:
#         print("1) Prima voce   0) Esci")             # <-- adattare
#         scelta = input("Scelta: ").strip()
#         if scelta == "1":
#             voce_uno()
#         elif scelta == "0":
#             print("Arrivederci.")
#             break
#         else:
#             print(f"[!] Scelta non valida: {scelta}")


# ==========================================================================
# IN AZIONE — lo schema su un caso del corso. Si esegue.
# ==========================================================================
MENU = {"1": "Certificato di residenza", "2": "Stato di una pratica",
        "3": "Orari dello sportello", "0": "Esci"}


def voce_certificato():
    """Voce 1: il lavoro sta in una funzione, non dentro il ciclo."""
    print("   Certificato di residenza: pronto in giornata.")


def voce_pratica():
    """Voce 2: lo stato di una pratica."""
    print("   Pratica in lavorazione.")


def voce_orari():
    """Voce 3: gli orari dello sportello."""
    print("   Sportello aperto la mattina, dalle 8.30 alle 12.30.")


def sportello(risposte):
    """Il menu: ogni scelta chiama la sua funzione, 0 chiude."""
    # Con le risposte simulate, il for sulla lista sostituisce while True:
    # l'uscita resta affidata al break sulla voce 0, come alla tastiera.
    for scelta in risposte:
        print(f"Scelta (1-3, 0 per uscire): {scelta}")
        # TRABOCCHETTO: il confronto e' con la stringa "1". Con 1 intero
        #   l'uguaglianza fra str e int e' sempre falsa: nessuna voce scatta mai,
        #   e ogni scelta finisce in "non valida".
        if scelta == "1":
            voce_certificato()
        elif scelta == "2":
            voce_pratica()
        elif scelta == "3":
            voce_orari()
        elif scelta == "0":
            print("   Sportello chiuso.")
            break
        else:
            print(f"   [!] Scelta non valida: {scelta}")


# Le righe del menu sono generate dal dizionario MENU: per stamparne una
# in piu' basta una coppia, il ramo elif va aggiunto a parte.
for codice, voce in MENU.items():
    print(f"{codice}) {voce}")
sportello(["1", "3", "9", "0"])
