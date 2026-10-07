"""
ESERCIZIO 01.2 — Etichetta di scaffale   ⭐ (base)

CASO D'USO REALE
Nel magazzino di NovaStore ogni ripiano ha un cartellino con il nome del
prodotto, il codice interno, il prezzo e la posizione. I cartellini si
scrivono a mano da anni, e il magazziniere ha smesso di rifarli quando un
prezzo cambia. Il vostro compito è stampare l'etichetta di un articolo
sempre con lo stesso schema, in modo che ristamparla costi dieci secondi.

ISTRUZIONI
1) Partite dalla struttura standard: docstring, costanti, main().
2) Il codice interno di NovaStore è fatto di quattro pezzi separati da un
   trattino: sigla dell'azienda, anno, sigla della categoria, progressivo.
   Stampatelo con UN SOLO print, usando sep="-".
3) L'intestazione è composta da due pezzi separati da " - ": anche qui un
   solo print con sep.
4) La riga del prezzo deve risultare "Prezzo: 49.9 euro" senza spazi in
   più: usate un print con sep="".
5) La riga della posizione deve risultare su una riga sola ma essere
   prodotta da DUE print: il primo finisce con end=" | ".
6) Chiudete con una riga di trattini.

DATI DI PARTENZA
     SIGLA_AZIENDA = "NS"      ANNO = 2026
     categoria = "CUF"         progressivo = "0007"
     nome_prodotto = "Cuffie Bluetooth"
     prezzo = 49.90
     scaffale = "A3"           ripiano = 2

SUGGERIMENTI
- sep dice cosa mettere FRA gli argomenti, end cosa mettere DOPO l'ultimo.
- "Codice:" e il codice vero sono due print diversi: al primo mettete
  end=" " così la riga non si chiude.
- Il progressivo "0007" è scritto fra virgolette apposta: come numero
  perderebbe gli zeri davanti.
- Il prezzo lo stampa Python come 49.9, non 49.90. È corretto, non
  correggetelo: domani impareremo a dargli la forma da cartellino.

SE HAI FINITO PRIMA (opzionale)
- Stampate una seconda etichetta per il Mouse verticale (34.50, categoria
  "MOU", progressivo "0021", scaffale "B1", ripiano 4) senza duplicare le
  costanti: cambiano solo le variabili dentro main().
- Aggiungete una riga "Prezzo al pubblico IVA inclusa" calcolando il
  prezzo per 1.22 e stampandolo: guardate quante cifre escono.

ESEMPIO OUTPUT
NOVASTORE - REPARTO INFORMATICA
Cuffie Bluetooth
Codice: NS-2026-CUF-0007
Prezzo: 49.9 euro
Scaffale: A3 | Ripiano: 2
------------------------------
"""

# Scrivi il tuo codice qui
