"""
ESERCIZIO PER CASA 10.4 — Dallo schema al caso nuovo: gli interventi di
manutenzione   ⭐⭐⭐⭐ (avanzato)

PATTERN USATI: P6, P12, P15, P16, P18, P22, P23, P26

CASO D'USO REALE
Il Comune di Villanova ha tre squadre di manutenzione e vuole sapere quale
chiude gli interventi entro le ore previste per il quartiere. È la stessa
domanda dei corrieri di LogiSud nell'esercizio 10.4, su dati diversi.

ISTRUZIONI
Si parte dalla soluzione di 10.4, non da un file vuoto. Entra il file
interventi_manutenzione.csv, con intestazione, nel formato
intervento;squadra;quartiere;ore.

Esce, nel formato dell'ESEMPIO OUTPUT, lo stesso report di 10.4 con le
squadre al posto dei corrieri e le ore al posto dei giorni:
- le righe scartate con il numero di riga dell'editor e il motivo;
- per squadra: interventi, ore totali, media, fuori tempo, quota entro i
  tempi; la riga dei totali; la classifica per puntualità; l'intervento
  con lo sforamento più grande;
- lo stesso report per quartiere, ottenuto con le stesse funzioni e senza
  scriverne di nuove;
- gli interventi chiusi esattamente nelle ore previste, che non sono fuori
  tempo ma stanno sul bordo.

Vincoli — questo è l'esercizio
- Le funzioni della parte generale di 10.4 si copiano IDENTICHE: nemmeno
  il nome di un parametro cambia. Si riscrive solo la parte specifica.
- Fuori tempo significa ore MAGGIORI delle previste, come nei corrieri.
- In testa alla soluzione, due commenti: PATTERN SCELTI (quali P e
  perché, in una riga ciascuno) e RIGHE CAMBIATE RISPETTO A 10.4 (che
  cosa è cambiato e che cosa no).

DATI DI PARTENZA
     La cartella dati sta due livelli sopra il vostro file:
     Path(__file__).resolve().parent.parent / "dati"
     ORE_PREVISTE = {"CENTRO": 3, "PERIFERIA": 4, "MARINA": 5}
     LARGHEZZA = 60

SUGGERIMENTI
- Prima di cambiare una riga, segnate in 10.4 quali righe sanno di
  corrieri e quali no: sono le righe marcate come da adattare (Cap. 1.4,
  13.1).
- Il report per quartiere non chiede una funzione nuova: chiede di
  preparare i record in modo che il quartiere stia dove la funzione cerca
  la chiave (Cap. 7.4).
- Nella classifica per quartiere c'è una parità: prima di stupirvi
  dell'ordine, rileggete l'errore E6 (Cap. 14).

SE HAI FINITO PRIMA (opzionale)
- Per ogni squadra, sommate le ore di sforamento (solo gli interventi
  fuori tempo, solo la parte che eccede).
- Leggete ORE_PREVISTE da un file JSON invece che dalla costante, con un
  ripiego se un quartiere manca (Cap. 10.3).

PER RIUSARLO
Questo esercizio È il riuso. Rifatelo una terza volta con un caso
vostro: i tempi di evasione delle pratiche di Villanova per ufficio,
contro i giorni previsti per tipo di pratica.

ESEMPIO OUTPUT
============================================================
COMUNE DI VILLANOVA - Interventi di manutenzione
============================================================
File letto: interventi_manutenzione.csv
[!] riga  8  ore non numeriche: 'due'
[!] riga 13  servono 4 campi, ne ha 3
Righe di dati ............. 12
Interventi validi ......... 10
Righe scartate ............ 2
------------------------------------------------------------
PER SQUADRA
SQUADRA          N.   ORE   MEDIA  FUORI  ENTRO I TEMPI
SQUADRA_A         4    13    3.25      0         100.0%
SQUADRA_B         4    15    3.75      1          75.0%
SQUADRA_C         2    11    5.50      2           0.0%
TOTALE           10    39    3.90      3          70.0%
Classifica per puntualità:
  1. SQUADRA_A      100.0%
  2. SQUADRA_B       75.0%
  3. SQUADRA_C        0.0%
------------------------------------------------------------
PER QUARTIERE
QUARTIERE        N.   ORE   MEDIA  FUORI  ENTRO I TEMPI
CENTRO            4    11    2.75      1          75.0%
PERIFERIA         3    12    4.00      1          66.7%
MARINA            3    16    5.33      1          66.7%
TOTALE           10    39    3.90      3          70.0%
Classifica per puntualità:
  1. CENTRO          75.0%
  2. PERIFERIA       66.7%
  3. MARINA          66.7%
------------------------------------------------------------
Sforamento massimo: +2 ore, MN-09 (SQUADRA_C, MARINA: 7 contro 5)
Sul bordo (ore = previste): MN-05, MN-06, MN-10
============================================================
"""

# Scrivi il tuo codice qui
