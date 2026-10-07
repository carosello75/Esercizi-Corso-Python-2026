"""
ESERCIZIO 10.3 — Le note spese del trimestre   ⭐⭐ (media)

PATTERN USATI: P5, P6, P12, P17, P18, P20, P24, P26

CASO D'USO REALE
Un consulente TalentHub consegna dodici note spese in un file di testo.
L'amministrazione rimborsa ogni nota fino al tetto della sua categoria:
Giulia deve sapere quanto si rimborsa davvero, e quali note tornano
indietro perché scritte male.

ISTRUZIONI
Ingresso: giorno_10/dati/note_spese.txt, una nota per riga
(codice;categoria;importo;descrizione), importi con la virgola, nessuna
intestazione. Cartella dei dati:
Path(__file__).resolve().parent.parent / "dati".

Uscita a schermo, nel formato dell'ESEMPIO OUTPUT:
- ogni riga scartata con il suo numero (quello dell'editor) e il motivo;
- i conteggi: righe del file, righe vuote, note buone, note scartate;
- per categoria: numero di note, importo, quota sul totale e una barra;
- le note sopra il tetto, con il tetto e l'eccedenza;
- totale presentato, eccedenze, rimborsabile, e la verifica finale che
  righe utili = buone + scartate.

Vincoli:
- una riga si scarta se non ha quattro campi, se la categoria non è fra
  quelle dei TETTI o se l'importo non è un numero positivo; una riga
  scartata non ferma il programma;
- "vitto" e "VITTO" sono la stessa categoria;
- il tetto vale per la singola nota ed è incluso: una nota esattamente
  sul tetto si rimborsa per intero;
- le categorie escono nell'ordine dei TETTI; nessun traceback.

DATI DI PARTENZA (copiateli così come sono)
     TETTI = {"VIAGGIO": 200.00, "VITTO": 30.00, "ALLOGGIO": 120.00,
              "MATERIALE": 50.00}
     LARGHEZZA = 60
     LARGHEZZA_BARRA = 40

SE HAI FINITO PRIMA (opzionale)
- Scrivete le note scartate in giorno_10/output/note_da_correggere.txt,
  una per riga con numero e motivo, da rimandare al consulente.
- Il tetto diventa trimestrale per categoria: VITTO non oltre 30 euro a
  nota ma anche non oltre 80 in tutto. Che cosa cambia nel rimborsabile?

PER RIUSARLO
Il dizionario TETTI e il validatore della riga sono le parti del caso: con i
budget per voce di un ufficio al posto dei tetti, lo stesso programma
controlla gli acquisti del Comune di Villanova contro il bilancio.

ESEMPIO OUTPUT
============================================================
TALENTHUB - Note spese del trimestre
============================================================
File letto: note_spese.txt
[!] riga 7 scartata: importo non numerico: 'trenta'
[!] riga 9 scartata: categoria non ammessa: 'REGALI'
[!] riga 10 scartata: servono 4 campi, ne ha 3
------------------------------------------------------------
Righe del file ............. 13
Righe vuote ................ 1
Note buone ................. 9
Note scartate .............. 3
------------------------------------------------------------
CATEGORIA  NOTE    IMPORTO   QUOTA
VIAGGIO       2     147.70   27.0%  ###########
VITTO         3      92.50   16.9%  #######
ALLOGGIO      2     245.00   44.7%  ##################
MATERIALE     2      62.80   11.5%  #####
------------------------------------------------------------
NOTE SOPRA IL TETTO
SP04  VITTO           38.00  tetto   30.00  eccedenza    8.00
SP07  ALLOGGIO       135.00  tetto  120.00  eccedenza   15.00
------------------------------------------------------------
Totale presentato .......... 548.00
Eccedenze .................. 23.00
Rimborsabile ............... 525.00
------------------------------------------------------------
[OK] 12 righe utili = 9 buone + 3 scartate
============================================================
"""

# Scrivi il tuo codice qui
