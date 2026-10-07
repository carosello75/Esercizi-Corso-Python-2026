"""
ESERCIZIO PER CASA 07.2 — Sotto scorta   ⭐⭐⭐ (impegnativo)

CASO D'USO REALE
Il magazzino LogiSud si accorge di essere sotto scorta quando arriva
l'ordine e la merce non c'è. Il controllo si fa a occhio, il venerdì, se
c'è tempo. Voi scrivete il programma che lo fa in un secondo: per ogni
articolo confronta la giacenza con la scorta minima, dice quanti pezzi
mancano e quanto costa rimetterli a posto. Il numero finale — il costo del
riordino — è quello che serve a chi deve firmare.

ARGOMENTI TEORICI: Cap. 6 — Scorrere una lista · Cap. 9 — Conti su una
lista · Cap. 14 — Una tabella in Python: lista di tuple

ISTRUZIONI
1) Costruite la lista magazzino con sei tuple da quattro campi:
   (articolo, giacenza, scorta_minima, prezzo_unitario).
2) Scrivete stampa_magazzino(righe) che stampa l'intestazione e, per ogni
   articolo, giacenza, scorta minima, prezzo e valore a magazzino
   (giacenza per prezzo).
3) Scrivete valore_magazzino(righe) che restituisce la somma dei valori, e
   pezzi_a_magazzino(righe) che restituisce la somma delle giacenze.
4) Scrivete da_riordinare(righe) che restituisce una lista di tuple
   (articolo, mancanti, costo) per i soli articoli con giacenza sotto la
   scorta minima. I pezzi mancanti sono scorta_minima meno giacenza.
5) Stampate la sezione DA RIORDINARE con una riga [!] per articolo.
6) Stampate il blocco finale: quanti articoli vanno riordinati su quanti,
   quanti pezzi in tutto, il costo totale del riordino, l'articolo il cui
   riordino costa di più e l'elenco degli articoli esauriti (giacenza
   zero).
7) Per l'articolo con il riordino più costoso e per gli esauriti scrivete
   due funzioni separate: non infilate tutto dentro main().

DATI DI PARTENZA (copiateli così come sono)
     MAGAZZINO = [
         ("Cuffie Bluetooth", 12, 20, 49.90),
         ("Tastiera meccanica", 25, 15, 89.00),
         ("Mouse verticale", 4, 10, 34.50),
         ("Monitor 27 pollici", 8, 5, 219.00),
         ("Webcam HD", 0, 12, 59.90),
         ("Hub USB-C", 30, 10, 27.00),
     ]
     LARGHEZZA = 60
     LARGHEZZA_ETICHETTA = 24

SUGGERIMENTI
- L'unpacking a quattro nomi dentro il for rende leggibile tutto il
  resto. Con righe[0], righe[1] funziona, e fra un mese non si capisce.
- "sotto scorta" vuol dire giacenza < scorta_minima, con il minore
  stretto: chi ha esattamente la scorta minima non va riordinato. È una
  decisione, non un dettaglio, e va scritta in un commento.
- La funzione da_riordinare restituisce una LISTA DI TUPLE nuova, non
  stampa niente. Chi la chiama decide cosa farne: è la regola di ieri.
- Per l'elenco degli esauriti costruite una lista di nomi e unitela con
  ", ".join(). Se la lista è vuota, join dà una stringa vuota: prevedete
  un testo di ripiego, per esempio "nessuno".
- I valori in euro si stampano sempre con il formato :.2f. Senza, uno di
  questi conti vi esce con una coda di decimali che spaventa.

SE HAI FINITO PRIMA (opzionale)
- Aggiungete una colonna "copertura", cioè giacenza diviso scorta minima,
  stampata in percentuale con :.0%. Attenzione alla scorta minima uguale
  a zero: non c'è in questi dati, ma il controllo si scrive lo stesso.
- Ordinate la sezione DA RIORDINARE dal costo più alto al più basso,
  costruendo una lista di tuple (costo, articolo, mancanti).

ESEMPIO OUTPUT
============================================================
LOGISUD TRASPORTI - Controllo delle scorte
============================================================
ARTICOLO             GIAC  MIN   PREZZO   VALORE
------------------------------------------------------------
Cuffie Bluetooth       12   20    49.90   598.80
Tastiera meccanica     25   15    89.00  2225.00
Mouse verticale         4   10    34.50   138.00
Monitor 27 pollici      8    5   219.00  1752.00
Webcam HD               0   12    59.90     0.00
Hub USB-C              30   10    27.00   810.00
------------------------------------------------------------
Articoli a magazzino ... 6
Pezzi a magazzino ...... 79
Valore del magazzino ... 5523.80 euro
------------------------------------------------------------
DA RIORDINARE
[!] Cuffie Bluetooth     mancano  8 pezzi ->   399.20 euro
[!] Mouse verticale      mancano  6 pezzi ->   207.00 euro
[!] Webcam HD            mancano 12 pezzi ->   718.80 euro
------------------------------------------------------------
Articoli da riordinare . 3 su 6
Pezzi da ordinare ...... 26
Costo del riordino ..... 1325.00 euro
Riordino più costoso ... Webcam HD
Articoli esauriti ...... Webcam HD
============================================================
"""

# Scrivi il tuo codice qui
