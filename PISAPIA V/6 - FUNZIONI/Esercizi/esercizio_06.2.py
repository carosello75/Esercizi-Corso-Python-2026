"""
ESERCIZIO 06.2 — Lo sconto con il valore di default   ⭐ (facile)

CASO D'USO REALE
NovaStore manda in saldo mezzo catalogo. Lo sconto standard deciso dalla
direzione è il 10%, ma su alcuni articoli il responsabile ne vuole uno
diverso e su uno vuole zero. Chi compila il listino non deve ricordarsi
il 10% a ogni riga, e non deve poterlo sbagliare.

ARGOMENTI TEORICI: Cap. 5 — return; Cap. 8 — Valori di default; Cap. 9 —
Argomenti nominati

ISTRUZIONI
Due funzioni e un main() che stampa il listino.

  - una riceve il prezzo e restituisce il prezzo scontato. La percentuale
    è facoltativa: chi non la indica prende quella standard. È facoltativo
    anche un buono fedeltà in euro, tolto dopo la percentuale, che se non
    viene indicato non toglie niente
  - una stampa una riga di listino incolonnata e non restituisce niente

La funzione di calcolo va chiamata cinque volte, una per articolo, e ogni
chiamata deve avere una forma diversa dalle altre:

  - Cuffie Bluetooth: solo il prezzo, lasciando lavorare il default
  - Tastiera meccanica: prezzo e percentuale, in ordine e senza nomi
  - Monitor 27 pollici: la percentuale passata come argomento nominato
  - Hub USB-C: tutti e due gli argomenti nominati, e in ordine invertito
  - Webcam HD: prezzo e percentuale, più il buono fedeltà con il suo nome

In coda al listino vanno il buono applicato, il totale a prezzo pieno, il
totale da pagare e il risparmio. Le colonne sono quelle dell'esempio: il
nome a sinistra, i numeri a destra, e le larghezze si contano da lì.

DATI DI PARTENZA (copiateli così come sono)
     PERCENTUALE_PREDEFINITA = 10
     BUONO_FEDELTA = 5.00
     LARGHEZZA = 48
     Cuffie Bluetooth      49.90   sconto standard
     Tastiera meccanica    89.00   sconto 25
     Monitor 27 pollici   219.00   sconto 50
     Hub USB-C             27.00   sconto 0
     Webcam HD             59.90   sconto 20, più il buono fedeltà

SUGGERIMENTI
- Un parametro diventa facoltativo per come è scritta la riga del def, non
  per come viene chiamata la funzione: Cap. 8.1. E i facoltativi vanno in
  fondo, Cap. 8.2.
- Sconto zero e sconto non indicato non sono la stessa cosa: uno è una
  decisione, l'altro è un'assenza. Cap. 8.4 dice che cosa nasconde un
  default comodo.
- Con i nomi l'ordine non conta più, ma i posizionali devono restare
  davanti: Cap. 9.3. La regola ha un motivo meccanico, e il messaggio
  d'errore lo dice.

SE HAI FINITO PRIMA (opzionale)
- Scrivete una chiamata con la percentuale nominata PRIMA del prezzo
  posizionale, leggete il messaggio d'errore e spiegate in un commento
  perché Python non può accettare quella forma.
- Il listino dice la percentuale ma non quanti euro si risparmiano su ogni
  articolo. Aggiungete la colonna del risparmio senza toccare la funzione
  che calcola lo sconto.

ESEMPIO OUTPUT
================================================
NOVASTORE - Listino di fine stagione
================================================
Articolo                 Pieno Sconto% Da pagare
------------------------------------------------
Cuffie Bluetooth         49.90      10     44.91
Tastiera meccanica       89.00      25     66.75
Monitor 27 pollici      219.00      50    109.50
Hub USB-C                27.00       0     27.00
Webcam HD                59.90      20     42.92
------------------------------------------------
Buono fedeltà applicato ....   5.00
Totale a prezzo pieno ...... 444.80
Totale da pagare ........... 291.08
Risparmio del cliente ...... 153.72
================================================
"""

# Scrivi il tuo codice qui
