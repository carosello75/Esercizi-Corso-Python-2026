"""
ESERCIZIO 03.2 — Cassa del negozio 

CASO D'USO REALE
La cassa 1 di NovaStore ha un registratore che stampa lo scontrino ma non
dice mai quanto resto dare, e la collega lo calcola a mente mentre c'è la
fila. Due volte a settimana sbaglia di qualche centesimo. Vi hanno chiesto
un programmino di appoggio: si digita articolo, prezzo, quantità e
contante ricevuto, e lui dice totale, IVA scorporata e resto.

Il programma assume che prezzo, quantità e contante siano numeri scritti
correttamente e che il contante basti a coprire il totale. Su un cliente
che scrive "venti" il programma si schianta: è previsto, ed è il tema
dell'esercizio 03.7.


ISTRUZIONI
Struttura standard: docstring, costanti, main(), guard.
In ingresso: articolo, prezzo unitario, quantità, contante ricevuto,
tutti digitati come testo e con i decimali scritti come si scriverebbero
su carta. In uscita lo scontrino di appoggio con totale, imponibile, IVA
e resto, e l'ESEMPIO OUTPUT qui sotto è la specifica del formato.

Vincoli
- Il prezzo del cartellino è GIÀ comprensivo di IVA: lo scontrino deve
  dire quanta imposta c'è dentro quel prezzo, non aggiungerne altra.
- L'aliquota (22%) sta in costante e compare una volta sola in tutto il
  programma: il giorno che passa al 10%, anche l'etichetta "IVA 22%" deve
  cambiare da sola. Nessun 22 scritto a mano, nemmeno dentro un testo.
- Prezzo e contante sono importi, la quantità è un conteggio di pezzi.
- Nei prompt vanno l'unità di misura e il formato atteso (Cap. 4.2).

SUGGERIMENTI
- Lo scorporo si risolve su carta prima di scrivere codice: 81.80
  aumentato del 22% fa 99.80, e il programma parte da 99.80 per tornare
  a 81.80. Chi invece toglie il 22% da 99.80 ottiene 77.84, e sbaglia di
  quasi quattro euro.
- Se un importo esce con quindici decimali (0.20000000000000284) non
  avete sbagliato il conto: è il modo in cui la macchina tiene i numeri
  con la virgola, e si sistema al momento della stampa (Cap. 9.2).
- Collaudo: 49,90 e 49.90 devono dare lo stesso scontrino (Cap. 5.4).

SE HAI FINITO PRIMA (opzionale)
- Aggiungete lo sconto tessera in percentuale e una riga "SCONTO".
- Fate stampare il totale in centesimi come numero intero (il trucco del
  cassiere del Giorno 02): quanti centesimi sono 99,80 euro?

ESEMPIO OUTPUT
Articolo: cuffie bluetooth
Prezzo unitario in euro (es. 49.90): 49,90
Quantita (numero intero): 2
Contante ricevuto in euro: 100

==================================================
NOVASTORE - CASSA 1
==================================================
Articolo:          Cuffie Bluetooth
Prezzo unitario:        49.90 euro
Quantita:                   2
--------------------------------------------------
Totale da pagare:       99.80 euro
Imponibile:             81.80 euro
IVA 22%:                18.00 euro
--------------------------------------------------
Contante:              100.00 euro
Resto:                   0.20 euro
==================================================
"""

# Scrivi il tuo codice qui
