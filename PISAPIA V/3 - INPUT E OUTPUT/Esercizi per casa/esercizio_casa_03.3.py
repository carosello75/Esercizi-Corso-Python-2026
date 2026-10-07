"""
ESERCIZIO CASA 03.3 — Ordine da asporto   ⭐⭐⭐ (impegnativa)

CASO D'USO REALE
NovaStore ha aperto un piccolo punto ristoro, NovaStore Food, e prende
gli ordini da asporto al telefono. Chi risponde scrive su un foglietto,
fa i conti a mente e dice il totale al cliente. Poi al ritiro il totale
non coincide quasi mai, perché lo sconto asporto del dieci per cento
qualcuno se lo dimentica e il contributo di confezionamento nessuno lo
somma. Vi hanno chiesto un riepilogo stampato.

Il programma assume tre piatti, sempre tre, ognuno digitato nel formato
nome;quantita;prezzo, e un contante sufficiente a coprire il totale.

ARGOMENTI TEORICI: Cap. 5 — Igiene del dato; Cap. 7 — `.split()`;
Cap. 9 — Tabelle a larghezza fissa

ISTRUZIONI
1) Struttura standard: docstring, costanti, main(), guard.
2) In costante: righe di separazione da 50, nome del locale, sconto
   asporto in percentuale (10), contributo di confezionamento (1.00) e
   riga di chiusura.
3) Chiedete cliente, telefono, orario di ritiro, tre righe piatto nel
   formato nome;quantita;prezzo e il contante.
4) Normalizzate: cliente con .title(), telefono senza spazi né trattini,
   nomi dei piatti solo con .strip().
5) Calcolate il totale di ogni riga, il subtotale, lo sconto asporto, il
   totale (subtotale meno sconto più confezionamento) e il resto.
6) Stampate: testata con etichette larghe 14, tabella dei piatti,
   sezione dei totali, contante e resto.
7) La tabella ha le stesse larghezze dello scontrino di 03.5:
       piatto     22   a sinistra
       quantità    4   a destra
       prezzo     10   a destra, due decimali
       totale     14   a destra, due decimali
   Le righe dei totali usano etichetta 36 e importo 14.

SUGGERIMENTI
- Lo sconto è una percentuale (si divide per cento), il confezionamento
  è un importo fisso (non si divide per niente). Sono due conti diversi
  che finiscono in due righe che si assomigliano: attenzione.
- L'etichetta dello sconto contiene la percentuale: costruitela dalla
  costante con una f-string.
- Lo sconto si mostra con il segno meno davanti al valore.
- I nomi dei piatti non vanno passati a .title(): "Acqua naturale 1L"
  diventerebbe "Acqua Naturale 1L".

SE HAI FINITO PRIMA (opzionale)
- Aggiungete il numero di coperti e un contributo per coperto, e fate
  comparire la voce fra i totali.
- Fate stampare il numero totale di pezzi ordinati (somma delle tre
  quantità) in una riga sotto il subtotale.

ESEMPIO OUTPUT
Cliente: anna esposito
Telefono: 081 55 44 332
Orario di ritiro (hh:mm): 20:30
Piatto 1 (nome;quantita;prezzo): Pizza margherita;2;6.50
Piatto 2 (nome;quantita;prezzo): Parmigiana;1;8.00
Piatto 3 (nome;quantita;prezzo): Acqua naturale 1L;2;1.50
Contante alla consegna in euro: 25

==================================================
NOVASTORE FOOD - ORDINE DA ASPORTO
==================================================
Cliente:      Anna Esposito
Telefono:     0815544332
Ritiro alle:  20:30
--------------------------------------------------
PIATTO                Q.TA    PREZZO        TOTALE
--------------------------------------------------
Pizza margherita         2      6.50         13.00
Parmigiana               1      8.00          8.00
Acqua naturale 1L        2      1.50          3.00
--------------------------------------------------
SUBTOTALE                                    24.00
SCONTO ASPORTO 10%                           -2.40
CONFEZIONAMENTO                               1.00
TOTALE                                       22.60
--------------------------------------------------
CONTANTE                                     25.00
RESTO                                         2.40
==================================================
Ordine registrato. Ritiro al banco, cassa 2.
"""

# Scrivi il tuo codice qui
