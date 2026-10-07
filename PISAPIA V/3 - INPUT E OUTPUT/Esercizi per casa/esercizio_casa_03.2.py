"""
ESERCIZIO CASA 03.2 — Registro presenze   ⭐⭐ (media)

CASO D'USO REALE
TalentHub organizza sessioni formative per le aziende clienti e ogni
volta stampa a mano il foglio firme: testata con titolo, docente, data e
aula, poi una riga per partecipante con lo spazio per la firma. Il foglio
viene compilato con la biro poco prima dell'inizio, e le colonne
finiscono storte. Vi hanno chiesto di generarlo dal computer.

Il programma assume tre partecipanti, sempre tre, ognuno digitato nel
formato cognome;nome;azienda.

ARGOMENTI TEORICI: Cap. 9 — Tabelle a larghezza fissa;
Cap. 11 — Maschere di inserimento

ISTRUZIONI
1) Struttura standard: docstring, costanti, main(), guard. Le righe di
   separazione oggi sono da 70 caratteri.
2) In costante: intestazione, capienza dell'aula (12), numero di
   iscritti (3), il segno per la firma ("______") e la nota finale.
3) Chiedete i quattro dati di testata: titolo della sessione, docente,
   data, aula. Poi tre righe partecipante nel formato
   cognome;nome;azienda.
4) Normalizzate: cognome e nome con .title(), il docente con .title(),
   la ragione sociale e il titolo della sessione solo con .strip().
   Guardate cosa succede a "Comune di Villanova" se usate .title().
5) Calcolate i posti liberi e l'occupazione dell'aula in percentuale.
6) Stampate: testata con etichette larghe 14, riga singola, numeri della
   capienza, riga singola, tabella dei partecipanti, riga doppia, nota.
7) La tabella ha queste colonne:
       N.         4    a sinistra
       COGNOME   16    a sinistra
       NOME      14    a sinistra
       AZIENDA   24    a sinistra
       FIRMA           nessuna larghezza (è l'ultima colonna)

SUGGERIMENTI
- L'occupazione con la specifica :.1% va passata come frazione:
  iscritti / capienza, non moltiplicata per cento a mano.
- Le tre righe partecipante si spezzano con .split(";") e unpacking a
  tre variabili, come nell'esercizio 03.4.
- La pulizia si fa dopo lo split, pezzo per pezzo.
- La colonna della firma è un trattino basso ripetuto: mettetelo in
  costante, non scrivetelo sei volte nel corpo.

SE HAI FINITO PRIMA (opzionale)
- Aggiungete una colonna con l'iniziale del nome puntata (L.) al posto
  del nome per esteso, e verificate che le larghezze reggano ancora.
- Fate stampare in fondo quante aziende diverse sono rappresentate.
  Attenzione: oggi non abbiamo modo di confrontarle automaticamente, per
  cui il numero lo scrivete voi in una costante. Segnatevi la data in
  cui questa cosa si potrà fare davvero.

ESEMPIO OUTPUT
Titolo della sessione: Introduzione a Python
Docente: a. ferrante
Data (gg/mm/aaaa): 23/09/2026
Aula: Aula 2 - piano primo
Partecipante 1 (cognome;nome;azienda): greco;laura;Comune di Villanova
Partecipante 2 (cognome;nome;azienda): marino;elena;Banca Meridiana
Partecipante 3 (cognome;nome;azienda): rossi;marco;NovaStore

======================================================================
TALENTHUB - REGISTRO PRESENZE
======================================================================
Sessione:     Introduzione a Python
Docente:      A. Ferrante
Data:         23/09/2026
Aula:         Aula 2 - piano primo
----------------------------------------------------------------------
Capienza:     12
Iscritti:     3
Posti liberi: 9
Occupazione:  25.0%
----------------------------------------------------------------------
N.  COGNOME         NOME          AZIENDA                 FIRMA
----------------------------------------------------------------------
1   Greco           Laura         Comune di Villanova     ______
2   Marino          Elena         Banca Meridiana         ______
3   Rossi           Marco         NovaStore               ______
======================================================================
Il registro va firmato all'ingresso e alla fine della sessione.
"""

# Scrivi il tuo codice qui
