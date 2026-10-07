"""
ESERCIZIO CASA 03.4 — Diario dei crash   ⭐⭐⭐ (impegnativa)

CASO D'USO REALE
In azienda, quando un programma si rompe, la prima domanda non è "come
lo sistemiamo" ma "cosa stava facendo l'utente". La risposta la dà chi ha
scritto un diario dei guasti: input digitato, messaggio esatto, riga in
cui è saltato. È un lavoro noioso, si fa una volta e si consulta per
anni. Stasera lo fate sui vostri tre script di oggi.

Questo esercizio non si può fare senza eseguire davvero i programmi. Il
messaggio va copiato dal vostro terminale, non ricostruito a memoria e
non copiato da qui: la versione di Python che avete voi potrebbe scrivere
qualche freccia in più o in meno, e va bene così.

ARGOMENTI TEORICI: Cap. 14 — Quello che oggi non sappiamo ancora fare

ISTRUZIONI
1) Struttura standard: docstring, costanti, main(), guard. Righe di
   separazione da 70 caratteri.
2) Aprite i vostri script 03.2 (cassa), 03.4 (preventivo) e 03.6
   (bonifico) e lanciateli con questi sei input, uno per volta:

       03.2   Prezzo unitario     quaranta
       03.2   Quantita            2 pezzi
       03.4   Riga spedizione     SUD;12.5
       03.4   Riga spedizione     SUD,12.5,urgente
       03.6   Importo             1.250,00
       03.6   IBAN                IT60X05428

3) Per ognuno annotate su un foglio: che errore è, cosa dice l'ultima
   riga del traceback, e se il programma si è fermato oppure no.
4) Scrivete un programma che chiede due dati (nome di chi compila e
   data) e poi stampa il diario:
   - una testata con etichette larghe 15 caratteri;
   - una tabella con colonne N. (4), SCRIPT (10), CAMPO (18),
     DIGITATO (22) e ESITO (senza larghezza, è l'ultima);
   - sotto la tabella, i sei messaggi esatti numerati;
   - in fondo, una sezione "LEZIONE DEL GIORNO" di quattro righe.
5) Nella lezione del giorno spiegate due cose:
   - perché il caso numero 5 è particolare (guardate bene il valore fra
     apici nel messaggio: coincide con quello che avete digitato?);
   - perché il caso numero 6 è il peggiore di tutti e sei.

SUGGERIMENTI
- Il caso 5: nel vostro 03.6 c'è .replace(",", "."). Applicatela a mano
  su 1.250,00 e guardate cosa esce prima che float() la rifiuti.
- Il caso 6: l'IBAN è troppo corto. Lo slicing su una stringa più corta
  del previsto non dà errore, restituisce meno caratteri o nessuno.
  Guardate la maschera che esce e contate gli asterischi.
- La tabella non ha bisogno di calcoli: i sei casi sono testi fissi
  scritti dentro le f-string.
- Se una riga di codice supera gli 88 caratteri, mettete il testo
  ripetuto in una costante.

SE HAI FINITO PRIMA (opzionale)
- Aggiungete un settimo caso trovato da voi, su uno degli esercizi
  d'aula che qui non compaiono.
- Per ciascuno dei sei casi, scrivete in una riga di commento quale
  difesa preventiva lo avrebbe evitato e quale invece no.

ESEMPIO OUTPUT
Nome di chi compila: laura greco
Data (gg/mm/aaaa): 18/09/2026

======================================================================
DIARIO DEI CRASH - GIORNO 03
======================================================================
Compilato da:  Laura Greco
Data:          18/09/2026
======================================================================
N.  SCRIPT    CAMPO             DIGITATO              ESITO
----------------------------------------------------------------------
1   03.2      Prezzo unitario   quaranta              ValueError
2   03.2      Quantita          2 pezzi               ValueError
3   03.4      Riga spedizione   SUD;12.5              ValueError
4   03.4      Riga spedizione   SUD,12.5,urgente      ValueError
5   03.6      Importo           1.250,00              ValueError
6   03.6      IBAN              IT60X05428            nessun errore
----------------------------------------------------------------------
MESSAGGI ESATTI
1) ValueError: could not convert string to float: 'quaranta'
2) ValueError: invalid literal for int() with base 10: '2 pezzi'
3) ValueError: not enough values to unpack (expected 3, got 2)
4) ValueError: not enough values to unpack (expected 3, got 1)
5) ValueError: could not convert string to float: '1.250.00'
6) Nessun errore: la maschera esce IT60*******************
----------------------------------------------------------------------
LEZIONE DEL GIORNO
La riga 5 mostra una difesa che peggiora le cose: .replace(",", ".")
su 1.250,00 produce 1.250.00, che resta impossibile da convertire.
La riga 6 non si rompe affatto: produce un IBAN mascherato sbagliato
in silenzio, ed è il caso peggiore perché nessuno se ne accorge.
======================================================================
"""

# Scrivi il tuo codice qui
