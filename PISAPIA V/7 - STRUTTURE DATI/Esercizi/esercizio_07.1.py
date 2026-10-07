"""
ESERCIZIO 07.1 — Il catalogo   ⭐ (facile)

CASO D'USO REALE
Il catalogo di NovaStore sta in un foglio di calcolo che tre persone
modificano a turno, e ogni tanto qualcuno cancella una riga per sbaglio.
Giulia deve preparare la versione "di prova" in Python: un elenco di
prodotti che si possa stampare numerato e gestire (aggiungere, rimuovere, cercare). 

ARGOMENTI TEORICI: Cap. 3 — La lista · Cap. 4 — Modificare una lista ·
Cap. 6 — Scorrere una lista con enumerate()

ISTRUZIONI
1) Mettete i sei prodotti in una lista chiamata catalogo. Sono quelli del
   listino NovaStore che usiamo dal Giorno 01.
2) Scrivete una funzione stampa_catalogo(titolo, prodotti) che stampa il
   titolo con il numero di prodotti fra parentesi e poi l'elenco numerato
   da 1. Usate enumerate() per avere posizione e nome insieme.
3) Stampate il primo prodotto con l'indice 0 e l'ultimo con l'indice -1.
   Non contate a mano quanti sono: l'indice negativo esiste per questo.
4) Applicate, in quest'ordine, le quattro modifiche di oggi:
   - append   -> "Lampada da scrivania" in fondo
   - insert   -> "Supporto monitor" al primo posto (posizione 0)
   - remove   -> togliete "Webcam HD", che esce di listino
   - pop      -> togliete l'ultimo, e stampate il nome di quello tolto
   Dopo ognuna stampate una riga [OK] come nell'esempio.
5) Ristampate il catalogo aggiornato con la stessa funzione del punto 2.
6) Scrivete una funzione posizione_in_catalogo(prodotti, nome) che
   restituisce la posizione UMANA (da 1) se il prodotto c'è, e 0 se non
   c'è. Dentro usate `in` prima di usare .index().
7) Provatela su "Mouse verticale" e su "Webcam HD" e stampate le due
   righe finali come nell'esempio.
8) Scrivete una funzione catalogo_ordinato(prodotti) che restituisce una
   copia ordinata alfabeticamente con sorted(), senza toccare
   l'originale. Stampate la copia con la stessa funzione del punto 2, sotto
   il titolo "CATALOGO IN ORDINE ALFABETICO", e poi una riga che dimostra
   che il catalogo vero non è cambiato, nominando il suo primo prodotto.
9) Scrivete una funzione conta_nomi_lunghi(prodotti, soglia) che stampa i
   prodotti con il nome più lungo della soglia — nome e numero di
   caratteri — e restituisce quanti sono. Chiamatela con
   LUNGHEZZA_NOME_LUNGO e chiudete con la riga di riepilogo che dice
   quanti sono su quanti.

DATI DI PARTENZA (copiateli così come sono)
     PRODOTTI_INIZIALI = [
         "Cuffie Bluetooth",
         "Tastiera meccanica",
         "Mouse verticale",
         "Monitor 27 pollici",
         "Webcam HD",
         "Hub USB-C",
     ]
     PRODOTTO_NUOVO = "Lampada da scrivania"
     PRODOTTO_IN_TESTA = "Supporto monitor"
     PRODOTTO_FUORI_LISTINO = "Webcam HD"
     LUNGHEZZA_NOME_LUNGO = 15
     LARGHEZZA = 60

SUGGERIMENTI
- enumerate(prodotti, 1) fa partire il conteggio da 1 invece che da 0:
  vi risparmia il "+1" sparso in giro.
- .index(nome) si arrabbia se il nome non c'è. Per questo al punto 6 il
  controllo con `in` viene PRIMA, sempre.
- .pop() senza argomenti toglie l'ultimo E ve lo restituisce. Salvatelo in
  una variabile: se non lo fate, l'avete buttato via.
- La funzione del punto 2 riceve la lista come parametro e non stampa
  niente che non le sia stato passato. È la regola di ieri.

SE HAI FINITO PRIMA (opzionale)
- Stampate il catalogo in ordine alfabetico INVERSO, sempre senza toccare
  l'originale: sorted() ha un argomento che lo fa, e non serve riordinare
  due volte.
- Trovate il prodotto con il nome più lungo di tutti, tenendo da parte il
  migliore incontrato finora mentre scorrete la lista. Chiedetevi cosa
  dovrebbe rispondere il programma se due nomi fossero lunghi uguali.

ESEMPIO OUTPUT
============================================================
NOVASTORE - Catalogo prodotti
============================================================
CATALOGO INIZIALE (6 prodotti)
  1. Cuffie Bluetooth
  2. Tastiera meccanica
  3. Mouse verticale
  4. Monitor 27 pollici
  5. Webcam HD
  6. Hub USB-C
------------------------------------------------------------
Primo del catalogo .... Cuffie Bluetooth
Ultimo del catalogo ... Hub USB-C
Prodotti in elenco .... 6
------------------------------------------------------------
MODIFICHE DI OGGI
[OK] append   -> Lampada da scrivania va in fondo
[OK] insert   -> Supporto monitor va al primo posto
[OK] remove   -> Webcam HD esce dal listino
[OK] pop      -> tolto l'ultimo: Lampada da scrivania
------------------------------------------------------------
CATALOGO AGGIORNATO (6 prodotti)
  1. Supporto monitor
  2. Cuffie Bluetooth
  3. Tastiera meccanica
  4. Mouse verticale
  5. Monitor 27 pollici
  6. Hub USB-C
------------------------------------------------------------
RICERCHE
Mouse verticale ....... in catalogo, posizione 4
Webcam HD ............. non in catalogo
------------------------------------------------------------
CATALOGO IN ORDINE ALFABETICO (6 prodotti)
  1. Cuffie Bluetooth
  2. Hub USB-C
  3. Monitor 27 pollici
  4. Mouse verticale
  5. Supporto monitor
  6. Tastiera meccanica
L'originale non è cambiato: al primo posto c'è ancora Supporto monitor
------------------------------------------------------------
NOMI PIÙ LUNGHI DI 15 CARATTERI
  Supporto monitor     16 caratteri
  Cuffie Bluetooth     16 caratteri
  Tastiera meccanica   18 caratteri
  Monitor 27 pollici   18 caratteri
Nomi lunghi ........... 4 su 6
============================================================
"""

# Scrivi il tuo codice qui
