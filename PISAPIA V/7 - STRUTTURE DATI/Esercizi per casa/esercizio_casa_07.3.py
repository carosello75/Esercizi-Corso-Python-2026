"""
ESERCIZIO PER CASA 07.3 — Istogramma delle categorie   ⭐⭐⭐ (impegnativo)

CASO D'USO REALE
Il Poliambulatorio Aurora smista i ticket in cinque categorie, sempre le
stesse: PRENOTAZIONE, REFERTO, PAGAMENTO, RECLAMO, ALTRO. Ogni sera
l'addetto scrive su un foglio quanti ne sono arrivati per tipo, e il
foglio finisce in un cassetto. La direzione vuole invece un grafico: non
serve un programma di grafica, basta una barra di cancelletti larga
quanto il conteggio. Ventiquattro ticket di ieri, cinque categorie, un
dizionario.

ARGOMENTI TEORICI: Cap. 12 — Contare le occorrenze con un dizionario ·
Cap. 8 — Ordinare per costruire una classifica

ISTRUZIONI
1) Mettete le ventiquattro categorie dei ticket in una lista di stringhe,
   nell'ordine in cui sono arrivati.
2) Scrivete conta(categorie) che restituisce il dizionario dei conteggi
   con il pattern conteggi[c] = conteggi.get(c, 0) + 1.
3) Scrivete riga_istogramma(categoria, conteggio, totale) che restituisce
   la riga completa: nome, puntini di riempimento fino a
   LARGHEZZA_ETICHETTA, conteggio, quota percentuale e barra di "#".
4) Stampate l'istogramma NELL'ORDINE IN CUI SONO COMPARSI, cioè
   semplicemente scorrendo il dizionario con .items().
5) Stampate le categorie IN ORDINE ALFABETICO su una riga sola, unite con
   ", ", usando sorted() sulle chiavi.
6) Stampate la classifica DALLA PIÙ FREQUENTE ALLA MENO FREQUENTE,
   costruendo una lista di tuple (conteggio, categoria), ordinandola e
   rovesciandola.
7) Chiudete con categoria più frequente, categoria meno frequente,
   numero di categorie diverse e due righe di lettura.

DATI DI PARTENZA (copiateli così come sono)
     TICKET = [
         "PRENOTAZIONE", "REFERTO", "PRENOTAZIONE", "PAGAMENTO", "ALTRO",
         "PRENOTAZIONE", "RECLAMO", "REFERTO", "PRENOTAZIONE", "PAGAMENTO",
         "REFERTO", "PRENOTAZIONE", "ALTRO", "PRENOTAZIONE", "PAGAMENTO",
         "REFERTO", "RECLAMO", "PRENOTAZIONE", "REFERTO", "PAGAMENTO",
         "PRENOTAZIONE", "ALTRO", "REFERTO", "PRENOTAZIONE",
     ]
     LARGHEZZA = 60
     LARGHEZZA_ETICHETTA = 16
     LARGHEZZA_ETICHETTA_FINALE = 26

SUGGERIMENTI
- Tre modi diversi di guardare lo stesso dizionario: ordine di
  inserimento, ordine alfabetico, ordine di frequenza. Non sono un
  esercizio di stile: sono tre domande diverse e in tre riunioni diverse
  ve le chiederanno tutte e tre.
- La barra è "#" * conteggio. Con conteggi grandi si divide: qui i numeri
  sono piccoli e la barra si legge già così.
- Per la categoria meno frequente non serve un secondo giro: è l'ultima
  della classifica, cioè l'elemento in posizione -1.
- Le quote si stampano con :.1% e vanno allineate a destra su cinque
  caratteri, perché " 8.3%" è più corto di "37.5%".

SE HAI FINITO PRIMA (opzionale)
- Aggiungete un controllo sulle categorie previste: costruite la lista
  CATEGORIE_PREVISTE con le cinque ammesse e segnalate con [!] una
  categoria comparsa nei ticket che non è nell'elenco. Poi provate a
  scrivere "URGENZA" in un ticket e verificate che il programma lo dica.
- Aggiungete la quota cumulata: scorrendo la classifica, stampate accanto
  a ogni categoria la somma delle quote fino a lì. Alla terza riga
  scoprirete che tre categorie su cinque fanno quasi l'ottanta per cento.

ESEMPIO OUTPUT
============================================================
POLIAMBULATORIO AURORA - Ticket per categoria
============================================================
Ticket esaminati: 24
------------------------------------------------------------
NELL'ORDINE IN CUI SONO COMPARSI
PRENOTAZIONE ...  9  37.5%  #########
REFERTO ........  6  25.0%  ######
PAGAMENTO ......  4  16.7%  ####
ALTRO ..........  3  12.5%  ###
RECLAMO ........  2   8.3%  ##
------------------------------------------------------------
IN ORDINE ALFABETICO
ALTRO, PAGAMENTO, PRENOTAZIONE, RECLAMO, REFERTO
------------------------------------------------------------
DALLA PIÙ FREQUENTE ALLA MENO FREQUENTE
 1. PRENOTAZIONE    9
 2. REFERTO         6
 3. PAGAMENTO       4
 4. ALTRO           3
 5. RECLAMO         2
------------------------------------------------------------
Categoria più frequente .. PRENOTAZIONE
Categoria meno frequente . RECLAMO
Categorie diverse ........ 5
------------------------------------------------------------
Nove ticket su ventiquattro sono prenotazioni. Se domani si
mette una persona in più al telefono, adesso si sa dove.
============================================================
"""

# Scrivi il tuo codice qui
