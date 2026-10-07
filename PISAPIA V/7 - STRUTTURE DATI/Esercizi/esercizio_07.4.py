"""
ESERCIZIO 07.4 — Il listino   ⭐⭐ (media)

CASO D'USO REALE
LogiSud spedisce in quattro zone e ognuna ha un prezzo base al collo.
Finora il prezzo lo si cercava in una catena di if lunga venti righe, e
ogni volta che cambiava una tariffa bisognava rileggerla tutta per capire
dove mettere le mani. Il prezzo di una zona è una coppia nome-valore: qui
non serve un elenco ordinato, serve una rubrica. Oggi il listino diventa
un dizionario, e aggiungere l'ESTERO costerà una riga.

ARGOMENTI TEORICI: Cap. 10 — Il dizionario · Cap. 11 — Lavorare con i
dizionari: .get(), nuove chiavi, in, .items()

ISTRUZIONI
1) Costruite il dizionario listino con le quattro zone e i loro prezzi.
2) Scrivete una funzione stampa_listino(titolo, prezzi) che stampa il
   titolo con il numero di zone fra parentesi e poi una riga per ogni
   coppia, scorrendo con `for zona, prezzo in prezzi.items():`.
3) Stampate il listino di partenza.
4) Sezione RICERCHE, quattro righe:
   - il prezzo di ZONA_NOTA, preso con l'accesso diretto listino[...]
   - il prezzo di ZONA_IGNOTA, preso con .get(...) e un testo di ripiego:
     la zona non c'è, e il programma non deve fermarsi per questo
   - se "CENTRO" è una chiave del listino (con `in`)
   - se "estero" minuscolo è una chiave del listino: la risposta vi dirà
     una cosa importante sulle chiavi
5) Sezione AGGIORNAMENTI, due righe:
   - aggiungete la zona ZONA_NUOVA con il suo prezzo: basta assegnare a
     una chiave che non esiste ancora. Riga [OK].
   - aumentate del 10% il prezzo di ZONA_DA_AUMENTARE, arrotondando a due
     decimali con round(). Riga [!] con prezzo vecchio e prezzo nuovo.
6) Ristampate il listino con la stessa funzione del punto 2, e fate
   notare l'ordine in cui escono le zone. Poi stampate le chiavi in
   ordine alfabetico usando sorted() e ", ".join().
7) Costruite un secondo dizionario PESI_MASSIMI con il peso massimo
   ammesso per ogni zona e stampate, sotto il titolo "PREZZO E PESO
   MASSIMO PER ZONA (kg)", una riga per zona con prezzo e peso
   affiancati. Attenzione: una delle zone a listino nei pesi non c'è. La
   riga si deve stampare lo stesso e dichiarare che il dato manca.
8) Sezione CONTI SUL LISTINO: quante zone, la somma dei prezzi, il prezzo
   medio, il prezzo massimo, la ZONA più cara e il prezzo minimo. Usate
   len, sum, max e min su listino.values(); per il nome della zona più
   cara serve invece una funzione che scorre .items() tenendo da parte il
   massimo trovato finora, perché max() dà il prezzo e non il nome.

DATI DI PARTENZA (copiateli così come sono)
     LISTINO_INIZIALE = {
         "NORD": 8.50,
         "CENTRO": 7.00,
         "SUD": 9.50,
         "ISOLE": 14.00,
     }
     PESI_MASSIMI = {
         "NORD": 30,
         "CENTRO": 30,
         "SUD": 25,
         "ISOLE": 20,
     }
     ZONA_NOTA = "SUD"
     ZONA_IGNOTA = "ESTERO"
     ZONA_NUOVA = "ESTERO"
     PREZZO_ZONA_NUOVA = 22.00
     ZONA_DA_AUMENTARE = "ISOLE"
     AUMENTO = 1.10
     LARGHEZZA = 60

SUGGERIMENTI
- listino["ESTERO"] su una chiave che non esiste ferma il programma con un
  KeyError. listino.get("ESTERO", "non a listino") non si ferma e vi
  restituisce il ripiego. Al punto 4 servono tutti e due i comportamenti,
  ed è il cuore dell'esercizio.
- Le chiavi fanno differenza fra maiuscole e minuscole: "ESTERO" e
  "estero" sono due chiavi diverse, come due nomi diversi in rubrica.
- Per aggiungere una zona non esiste un metodo .aggiungi(): si assegna e
  basta, listino["ESTERO"] = 22.00. Se la chiave c'era, la sovrascrivete.
- round(prezzo * 1.10, 2) evita la coda di decimali che salta fuori
  moltiplicando i float. Il perché è del Giorno 02.
- max(listino.values()) dà il prezzo più alto, non la zona più cara: per
  il nome bisogna scorrere le coppie. È il pattern dell'accumulatore del
  Giorno 05, con il massimo tenuto da parte fuori dal ciclo.

SE HAI FINITO PRIMA (opzionale)
- Scrivete la funzione gemella zona_meno_cara(prezzi) e chiedetevi da
  quale valore deve partire il confronto: zero qui non va bene, e capire
  perché vale più della funzione.
- Aggiungete un terzo dizionario con i giorni di consegna per zona e
  stampate le tre informazioni sulla stessa riga. Poi togliete una zona
  dai pesi e controllate che il programma non si fermi lo stesso.

ESEMPIO OUTPUT
============================================================
LOGISUD TRASPORTI - Listino per zona
============================================================
LISTINO DI PARTENZA (4 zone)
  NORD    ....  8.50 euro
  CENTRO  ....  7.00 euro
  SUD     ....  9.50 euro
  ISOLE   .... 14.00 euro
------------------------------------------------------------
RICERCHE NEL LISTINO
Zona SUD ............. 9.50 euro
Zona ESTERO .......... non a listino, prezzo da concordare
'CENTRO' è una chiave? True
'estero' è una chiave? False
------------------------------------------------------------
AGGIORNAMENTI
[OK] Nuova zona ESTERO a 22.00 euro
[!] ISOLE aumenta del 10%: da 14.00 a 15.40 euro
------------------------------------------------------------
LISTINO AGGIORNATO (5 zone)
  NORD    ....  8.50 euro
  CENTRO  ....  7.00 euro
  SUD     ....  9.50 euro
  ISOLE   .... 15.40 euro
  ESTERO  .... 22.00 euro
------------------------------------------------------------
Le zone escono nell'ordine in cui sono state inserite, non in
ordine alfabetico. In ordine alfabetico sarebbero:
  CENTRO, ESTERO, ISOLE, NORD, SUD
------------------------------------------------------------
PREZZO E PESO MASSIMO PER ZONA (kg)
  NORD      8.50 euro        30
  CENTRO    7.00 euro        30
  SUD       9.50 euro        25
  ISOLE    15.40 euro        20
  ESTERO   22.00 euro      n.d.
------------------------------------------------------------
CONTI SUL LISTINO
Zone a listino ....... 5
Somma dei prezzi ..... 62.40 euro
Prezzo medio ......... 12.48 euro
Prezzo più alto ...... 22.00 euro
Zona più cara ........ ESTERO
Prezzo più basso .....  7.00 euro
============================================================
"""

# Scrivi il tuo codice qui
