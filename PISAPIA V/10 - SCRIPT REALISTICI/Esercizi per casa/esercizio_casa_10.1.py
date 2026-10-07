"""
ESERCIZIO PER CASA 10.1 — Il listino aggiornato   ⭐⭐ (media)

PATTERN USATI: P4, P5, P6, P12, P15, P26, P28

CASO D'USO REALE
NovaStore ritocca i prezzi con un aumento diverso per ogni categoria. Il
listino arriva con i prezzi scritti all'italiana, e il nuovo listino deve
uscire nello stesso formato, pronto da ricaricare.

ISTRUZIONI
Entra il file listino_novastore.txt: una riga di commento in testa, poi
una riga per articolo nel formato codice;descrizione;categoria;prezzo, con
la virgola decimale.

Esce, nel formato dell'ESEMPIO OUTPUT:
- per ogni riga che non si può usare, [!] con numero di riga (quello
  dell'editor) e motivo; per ogni categoria senza aumento, [!] e prezzo
  lasciato invariato;
- la tabella codice, descrizione, categoria, prezzo vecchio, prezzo nuovo,
  con la riga dei totali;
- i conteggi (righe lette, aggiornati, invariati, scartati), l'aumento
  complessivo in euro e in percentuale, il prezzo medio vecchio e nuovo;
- l'aumento medio applicato, cioè la media delle percentuali dei soli
  articoli aumentati: non coincide con l'aumento complessivo, e un commento
  nella soluzione deve dire perché;
- output/listino_aggiornato.txt, stesso formato del file di partenza
  (commento in testa, prezzi con la virgola), solo articoli validi;
- la verifica: il file scritto va riletto con lo stesso caricatore e lo
  stesso convertitore, e il suo totale deve coincidere con il totale nuovo.

Vincoli
- Il prezzo nuovo si arrotonda ai centesimi, articolo per articolo.
- Il file prodotto riparte da zero a ogni esecuzione.
- Si stampa solo il nome dei file, mai il percorso intero.

DATI DI PARTENZA
     La cartella dati sta due livelli sopra il vostro file:
     Path(__file__).resolve().parent.parent / "dati"
     I file prodotti vanno nella cartella output, accanto a dati.
     AUMENTI = {"AUDIO": 3, "VIDEO": 5, "ACCESSORI": 10, "INFORMATICA": 2}
     (percentuali)    LARGHEZZA = 60

SUGGERIMENTI
- "49,90" non è un numero per float(): la regola dello schema è nel P5, e
  vale anche all'andata inversa, quando il prezzo torna testo (Cap. 3.2).
- Una categoria che non compare negli aumenti non è un errore di sintassi:
  decidete se volete saperlo o no, e scegliete fra .get() e in (Cap. 5.3).
- Il report e il file si compongono come lista di righe, una volta sola;
  poi la stessa funzione le manda dove serve (Cap. 11.1).

SE HAI FINITO PRIMA (opzionale)
- Leggete gli aumenti da un file aumenti.txt nel formato categoria;percento,
  invece che dalla costante (Cap. 10.3).
- Per ogni categoria, stampate quanti articoli ha e il totale del listino
  nuovo (Cap. 7.4).

PER RIUSARLO
Cambiate il dizionario AUMENTI e l'intestazione del file: lo stesso
programma adegua le tariffe dei servizi comunali di Villanova, o i prezzi
all'ingrosso di un fornitore.

ESEMPIO OUTPUT
============================================================
NOVASTORE - Listino aggiornato
============================================================
File letto: listino_novastore.txt
[!] riga  9  NS-P08: categoria ARCHIVIAZIONE senza aumento, prezzo invariato
[!] riga 11  scartata: importo non numerico: 'trentaquattro'
------------------------------------------------------------
CODICE  DESCRIZIONE         CATEGORIA       VECCHIO    NUOVO
NS-P01  Cuffie Bluetooth    AUDIO             49.90    51.40
NS-P02  Soundbar compatta   AUDIO            129.00   132.87
NS-P03  Monitor 24 pollici  VIDEO            159.00   166.95
NS-P04  Webcam HD           VIDEO             59.00    61.95
NS-P05  Cavo HDMI 2 m       ACCESSORI          9.90    10.89
NS-P06  Tappetino per mouse ACCESSORI          7.50     8.25
NS-P07  Tastiera meccanica  INFORMATICA       89.00    90.78
NS-P08  Chiavetta USB 64 GB ARCHIVIAZIONE     12.90    12.90 [!]
NS-P09  Mouse wireless      INFORMATICA       19.90    20.30
------------------------------------------------------------
TOTALE                                       536.10   556.29
------------------------------------------------------------
Righe lette ............... 10
Articoli aumentati ........ 8
Articoli invariati ........ 1
Righe scartate ............ 1
Aumento complessivo ....... 20.19 euro (3.8%)
Prezzo medio vecchio ...... 59.57
Prezzo medio nuovo ........ 61.81
Aumento medio applicato ... 5.0% (su 8 articoli)
------------------------------------------------------------
File scritto: listino_aggiornato.txt (10 righe)
[OK] totale riletto 556.29 = totale nuovo 556.29
============================================================
"""

# Scrivi il tuo codice qui
