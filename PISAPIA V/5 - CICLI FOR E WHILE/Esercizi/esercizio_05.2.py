"""
ESERCIZIO 05.2 — Il totale della spesa   ⭐ (base)

CASO D'USO REALE
La cassa di prova di NovaStore batte cinque articoli; per il report di fine
turno servono totale, media, il più caro e quanti superano la soglia.

ARGOMENTI TEORICI: Cap. 6 — Contare e accumulare (accumulatore, contatore,
massimo, e dove si inizializzano)

ISTRUZIONI
Battete NUMERO_ARTICOLI prezzi (anche con la virgola) e mostrate il totale
progressivo. Conservarli tutti si impara quando arriveranno le strutture dati.

DATI DI PARTENZA (copiateli così come sono)
     LARGHEZZA = 60
     NUMERO_ARTICOLI = 5
     SOGLIA_ARTICOLO_CARO = 50.00

SUGGERIMENTI
- Il totale finale coincide con l'ultimo prezzo battuto? Cap. 6.3.
- Il più caro parte da un valore che il primo prezzo batte sempre: Cap. 6.5.

SE HAI FINITO PRIMA (opzionale)
- Aggiungete il prezzo più basso, facendo attenzione al valore di partenza.
- Chiedete l'aliquota IVA una volta sola e stampate imponibile e imposta.

ESEMPIO OUTPUT
============================================================
NOVASTORE - Cassa: totale di 5 articoli
============================================================
Batti il prezzo di 5 articoli, uno alla volta.

Prezzo articolo 1 (EUR): 49.90
  [OK] totale progressivo: 49.90 EUR
Prezzo articolo 2 (EUR): 89.00
  [OK] totale progressivo: 138.90 EUR
Prezzo articolo 3 (EUR): 34.50
  [OK] totale progressivo: 173.40 EUR
Prezzo articolo 4 (EUR): 219.00
  [OK] totale progressivo: 392.40 EUR
Prezzo articolo 5 (EUR): 59.90
  [OK] totale progressivo: 452.30 EUR

------------------------------------------------------------
Articoli battuti ...... 5
Totale ................ 452.30 EUR
Prezzo medio .......... 90.46 EUR
Articolo più caro ..... 219.00 EUR
Articoli sopra 50.00 .. 3
------------------------------------------------------------
"""

# Scrivi il tuo codice qui
