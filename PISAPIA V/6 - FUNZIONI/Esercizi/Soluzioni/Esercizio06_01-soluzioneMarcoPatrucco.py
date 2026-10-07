"""
ESERCIZIO 06.1 — Le prime funzioni   ⭐ (facile)

CASO D'USO REALE
All'ufficio preventivi di LogiSud Trasporti arrivano tre richieste ogni
mattina e la procedura è sempre la stessa: saluto, imponibile, IVA,
totale. La settimana scorsa qualcuno ha cambiato l'aliquota in due punti
su tre, e il terzo preventivo è partito sbagliato.

ARGOMENTI TEORICI: Cap. 3 — Che cos'è una funzione; Cap. 4 — Parametri e
argomenti; Cap. 5 — return; Cap. 6 — La funzione che non restituisce
niente; Cap. 7 — Una funzione che ne chiama un'altra

ISTRUZIONI
Tre funzioni, ciascuna con la sua docstring di una riga, e un main() che
non calcola niente.

  - una riceve il nome del cliente e stampa la riga di saluto: non
    restituisce niente
  - una riceve un imponibile e restituisce l'IVA dovuta: non stampa nulla
  - una riceve nome e imponibile, chiama le altre due e stampa il blocco
    completo del preventivo, riga di separazione compresa

Dentro main() restano l'intestazione, una chiamata per ciascuno dei tre
clienti e la riga di chiusura: nessun calcolo e nessuna formattazione di
importi. L'aliquota compare in un punto solo di tutto il file, e la
percentuale stampata nell'etichetta esce da lì: il numero 22 non va
digitato da nessuna parte. Il formato delle righe è quello dell'esempio
in coda a questa traccia.

DATI DI PARTENZA (copiateli così come sono)
     ALIQUOTA_IVA = 0.22
     LARGHEZZA = 60
     Marta Ferri            150.00
     Studio Legale Conti    250.00
     Panificio Sette         80.00

SUGGERIMENTI
- Stampare e restituire sono due mestieri diversi, e nel corpo si vedono
  da una parola sola: Cap. 5.1 e Cap. 6.1.
- La percentuale nell'etichetta si ricava dall'aliquota con uno
  specificatore di formato, di quelli visti nel Giorno 02. Scriverla a
  mano è il difetto che l'esercizio vuole togliervi.
- Il nome della terza funzione è metà del lavoro: verbo più oggetto, e se
  vi viene un nome con la "e" dentro sono due funzioni. Cap. 12.1 e 12.3.

SE HAI FINITO PRIMA (opzionale)
- Aggiungete un quarto cliente con imponibile 320.00 e contate quante
  righe avete dovuto scrivere.
- Alcuni clienti sono esenti. Fate in modo che si possa chiedere un
  preventivo con un'aliquota diversa senza toccare le tre chiamate già
  scritte: Cap. 8.

ESEMPIO OUTPUT
============================================================
LOGISUD TRASPORTI - Preventivi del mattino
============================================================
Buongiorno Marta Ferri, ecco il preventivo che ha chiesto.
Imponibile ....... 150.00 euro
IVA 22% .......... 33.00 euro
Totale ........... 183.00 euro
------------------------------------------------------------
Buongiorno Studio Legale Conti, ecco il preventivo che ha chiesto.
Imponibile ....... 250.00 euro
IVA 22% .......... 55.00 euro
Totale ........... 305.00 euro
------------------------------------------------------------
Buongiorno Panificio Sette, ecco il preventivo che ha chiesto.
Imponibile ....... 80.00 euro
IVA 22% .......... 17.60 euro
Totale ........... 97.60 euro
------------------------------------------------------------
Tre preventivi, e il blocco che li stampa è scritto una volta sola.
============================================================
"""

# Scrivi il tuo codice qui

#variabili globali che ci servono per il nostro programma
ALIQUOTA_IVA = 0.22
LARGHEZZA = 60

#scriviamo la prima funzione che stampa il saluto al cliente, senza restituire nulla
def saluto_cliente(nome):
    """Stampa il saluto al cliente"""
    print(f"Buongiorno {nome}, ecco il preventivo che ha chiesto.")

#scriviamo la seconda funzione che calcola l'IVA dovuta, senza stampare nulla
def calcola_iva(imponibile, aliquota=ALIQUOTA_IVA):
    """Calcola l'IVA dovuta"""
    return imponibile * aliquota

#scriviamo la terza funzione che stampa il preventivo completo, chiamando le altre due funzioni
def stampa_preventivo(nome, imponibile, aliquota=ALIQUOTA_IVA):
    """Stampa il preventivo completo"""
    saluto_cliente(nome)
    iva = calcola_iva(imponibile)
    totale = imponibile + iva
    print(f"Imponibile ....... {imponibile:.2f} euro")
    print(f"IVA {aliquota*100:.0f}% .......... {iva:.2f} euro")
    print(f"Totale ........... {totale:.2f} euro")
    print("-" * LARGHEZZA)

#scriviamo il main del programma
"""
- Aggiungete un quarto cliente con imponibile 320.00 e contate quante
  righe avete dovuto scrivere.
- Alcuni clienti sono esenti. Fate in modo che si possa chiedere un
  preventivo con un'aliquota diversa senza toccare le tre chiamate già
  scritte: Cap. 8.
"""
def main():
    print("=" * LARGHEZZA)
    print("LOGISUD TRASPORTI - Preventivi del mattino")
    print("=" * LARGHEZZA)
    conta = 0
    while True:
        nome_cliente = input("Inserisci il nome del cliente (o 'fine' per terminare): ")
        if nome_cliente.lower() == 'fine':
            break
        imponibile = float(input(f"Imponibile per {nome_cliente}: ").strip().replace(",", "."))
        aliquota = input(f"Aliquota IVA per {nome_cliente} (premi invio per default 22%): ")
        if aliquota:
            aliquota = float(aliquota) / 100
        else:
            aliquota = ALIQUOTA_IVA
        stampa_preventivo(nome_cliente, imponibile, aliquota)
        conta += 1
    
    print("-" * LARGHEZZA)
    print(f" {conta} preventivi, e il blocco che li stampa è scritto una volta sola.")
    print("=" * LARGHEZZA)
 
if __name__ == "__main__":
    main()
