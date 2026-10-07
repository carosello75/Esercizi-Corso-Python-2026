"""
ESERCIZIO 01.3 — Conto della spesa senza formattazione   ⭐⭐ (media)

CASO D'USO REALE
Un cliente aziendale di NovaStore ordina quattro articoli per l'ufficio.
La cassa deve produrre il riepilogo: somma degli articoli, IVA al 22% e
totale da pagare. Oggi lo fanno con la calcolatrice del telefono e ogni
tanto l'IVA la calcolano sul totale sbagliato. Voi scrivete il conto una
volta sola, e da quel momento non sbaglia più.

ISTRUZIONI
1) Struttura standard: docstring, costanti, main().
2) Mettete l'aliquota IVA in una costante ALIQUOTA_IVA = 0.22. Una
   percentuale, nei calcoli, si scrive come numero con la virgola: il
   22% è 0.22.
3) Create una variabile per il prezzo di ciascuno dei quattro articoli.
4) Calcolate in tre variabili distinte: il subtotale (somma dei quattro
   prezzi), l'IVA (subtotale per l'aliquota) e il totale.
5) Calcolate anche la quota a testa, dividendo il totale per il numero
   di colleghi che si dividono la spesa (4). Il numero di colleghi va in
   una variabile: nel conto non ci vanno numeri scritti a mano.
6) Stampate il riepilogo: una riga per articolo, poi subtotale, IVA,
   totale e quota a testa.

DATI DI PARTENZA
     Tastiera meccanica     89.00
     Mouse verticale        34.50
     Hub USB-C              27.00
     Monitor 27 pollici    219.00
     ALIQUOTA_IVA = 0.22
     colleghi = 4

SUGGERIMENTI
- A destra dell'uguale può esserci un calcolo, non solo un valore:
  subtotale = prezzo_uno + prezzo_due + ...
- Per l'IVA moltiplicate il subtotale per l'aliquota. Mettete le
  parentesi anche quando non servono: si legge meglio.
- Per stampare testo e numeri insieme usate la virgola dentro print.
- Non spaventatevi dell'output: Python scrive 369.5 e non 369,50 euro,
  e la quota a testa esce con quattro cifre dopo la virgola. È corretto
  così: la forma da scontrino è la giornata di domani.

SE HAI FINITO PRIMA (opzionale)
- Aggiungete uno sconto fisso di 20.00 euro applicato al subtotale PRIMA
  dell'IVA, e verificate che il totale cambi di più di venti euro.
  Sapete spiegare perché?
- Stampate anche il totale IVA esclusa e quello IVA inclusa affiancati
  sulla stessa riga, usando end.

ESEMPIO OUTPUT
NovaStore - Riepilogo ordine
------------------------------
Tastiera meccanica 89.0
Mouse verticale 34.5
Hub USB-C 27.0
Monitor 27 pollici 219.0
------------------------------
Subtotale: 369.5
IVA 22%: 81.29
Totale: 450.79
Quota a testa: 112.6975
"""

# Scrivi il tuo codice qui
