"""
ESERCIZIO 02.4 — Ripulitura anagrafiche   ⭐⭐ (media)

CASO D'USO REALE
Il Comune di Villanova sta spegnendo un gestionale del 2004. I dati
escono come li hanno digitati vent'anni di operatori diversi: nomi tutti
minuscoli, cognomi con due spazi in mezzo, email urlate in maiuscolo,
numeri di telefono con la barra e gli spazi. Il sistema nuovo li rifiuta
tutti. Nessuno ha intenzione di correggere ottomila schede a mano, e
comunque a mano si sbaglia. Voi scrivete la ripulitura di una scheda: il
giorno in cui sapremo ripetere la stessa cosa su ottomila, il lavoro sarà
già fatto.

ISTRUZIONI
1) Struttura standard: docstring, costanti, main().
2) Dentro main() mettete i sei campi grezzi, copiati IDENTICI da qui
   sotto, spazi compresi. Gli spazi fanno parte dell'esercizio.
3) Per ogni campo create la versione normalizzata:
   - nome: senza spazi ai bordi, iniziale maiuscola
   - cognome: senza spazi ai bordi, senza il doppio spazio interno,
     iniziali maiuscole
   - email: senza spazi ai bordi, tutta minuscola
   - telefono: solo cifre (via gli spazi interni e la barra)
   - indirizzo: senza il doppio spazio, iniziali maiuscole
   - comune: senza spazi ai bordi, tutto maiuscolo
4) Estraete il prefisso telefonico come i primi tre caratteri del
   telefono ripulito.
5) Stampate per ogni campo il valore importato e quello normalizzato,
   fra parentesi quadre e con la lunghezza in caratteri.
6) Stampate la scheda finale pronta per il caricamento.
7) Chiudete con cinque controlli stampati come True o False.

DATI DI PARTENZA (copiateli con gli spazi esatti)
     nome_grezzo = "   mario   "
     cognome_grezzo = "de  luca "
     email_grezza = "  MARIO.DELUCA@Comune.Villanova.IT "
     telefono_grezzo = " 089 / 12 34 56 "
     indirizzo_grezzo = "via  roma, 12"
     comune_grezzo = " villanova "

SUGGERIMENTI
- I metodi si concatenano e si leggono da sinistra a destra:
  cognome_grezzo.strip().replace("  ", " ").title()
- L'ordine conta: se date .title() prima di togliere il doppio spazio,
  il doppio spazio resta.
- .replace(" ", "") toglie TUTTI gli spazi, anche quelli in mezzo.
- Le parentesi quadre nell'output servono a far vedere gli spazi
  invisibili: scrivetele voi dentro la f-string, [{nome_grezzo}].
- len() conta i caratteri, spazi compresi.
- .isdecimal() e .isalpha() rispondono True o False.

SE HAI FINITO PRIMA (opzionale)
- Aggiungete un campo CAP grezzo (" 84091 ") e verificate che dopo la
  pulizia sia fatto di sole cifre e lungo esattamente cinque caratteri.
- Costruite l'iniziale puntata dell'intestatario (M.D.) prendendo il
  primo carattere del nome e del cognome normalizzati.

ESEMPIO OUTPUT
============================================================
COMUNE DI VILLANOVA - BONIFICA ANAGRAFICHE
Importazione dal vecchio gestionale - pratica 2026/00418
============================================================
NOME
  importato:    [   mario   ] - 11 caratteri
  normalizzato: [Mario] - 5 caratteri
COGNOME
  importato:    [de  luca ] - 9 caratteri
  normalizzato: [De Luca] - 7 caratteri
EMAIL
  importato:    [  MARIO.DELUCA@Comune.Villanova.IT ] - 35 caratteri
  normalizzato: [mario.deluca@comune.villanova.it] - 32 caratteri
TELEFONO
  importato:    [ 089 / 12 34 56 ] - 16 caratteri
  normalizzato: [089123456] - 9 caratteri
INDIRIZZO
  importato:    [via  roma, 12] - 13 caratteri
  normalizzato: [Via Roma, 12] - 12 caratteri
COMUNE
  importato:    [ villanova ] - 11 caratteri
  normalizzato: [VILLANOVA] - 9 caratteri
------------------------------------------------------------
SCHEDA PRONTA PER IL CARICAMENTO
Intestatario:  De Luca Mario
Residenza:     Via Roma, 12 - VILLANOVA
Email:         mario.deluca@comune.villanova.it
Telefono:      089123456 (prefisso 089)
------------------------------------------------------------
CONTROLLI AUTOMATICI
Una sola chiocciola nell'email: True
Email che finisce con .it:      True
Telefono di sole cifre:         True
Nome di sole lettere:           True
Comune uguale al maiuscolo:     True
============================================================
"""

# Scrivi il tuo codice qui
