"""
ESERCIZIO PER CASA 10.3 — Le ore dei consulenti   ⭐⭐⭐ (impegnativo)

PATTERN USATI: P3, P5, P10, P18, P24, P26, P30, P32

CASO D'USO REALE
TalentHub fattura ai clienti le ore dei suoi consulenti, che le segnano a
mano giornata per giornata. A fine settimana servono le ore per persona e
per progetto, e un riepilogo che l'amministrazione possa ricaricare.

ISTRUZIONI
Entra il file ore_consulenti.txt, una giornata per riga nel formato
consulente;progetto;ore, con la virgola decimale.

Esce, nel formato dell'ESEMPIO OUTPUT:
- le righe scartate con numero di riga e motivo (ore non numeriche, ore
  fuori intervallo), e i conteggi;
- la tabella per consulente: ore, giornate segnate, media ore per
  giornata, fascia di carico, e [!] per chi supera le ore settimanali;
- la tabella per progetto: ore, quota sul totale, barra;
- output/ore_consulenti.json con ore per consulente, ore per progetto,
  totale e l'elenco degli scarti (riga e motivo);
- il JSON riletto: da quello si stampano i conteggi di controllo;
- la verifica finale: righe lette = buone + scartate, e il totale riletto
  dal JSON uguale a quello calcolato.

Vincoli
- Una giornata vale se le ore sono più di zero e al massimo dodici.
- La fascia di carico si decide con una tabella di soglie, non con una
  catena di if scritta a mano.
- Una riga sbagliata non ferma il programma, un difetto del programma sì.

DATI DI PARTENZA
     La cartella dati sta due livelli sopra il vostro file:
     Path(__file__).resolve().parent.parent / "dati"
     I file prodotti vanno nella cartella output, accanto a dati.
     ORE_MINIME_ESCLUSE = 0    ORE_MASSIME_GIORNO = 12
     ORE_SETTIMANALI = 40
     SOGLIE_CARICO = [(30, "LEGGERO"), (40, "PIENO")]    CARICO_OLTRE = "OLTRE"
     LARGHEZZA = 60    LARGHEZZA_BARRA = 40

SUGGERIMENTI
- Le ore arrivano come "6,5": la conversione è già nel catalogo, e quando
  fallisce solleva. Chi la chiama decide se è uno scarto (Cap. 3.2, 12.1).
- La fascia si trova scorrendo le soglie e fermandosi alla prima che il
  valore non supera (Cap. 5.1). L'ordine delle soglie non è indifferente.
- Il JSON non ricorda le tuple: scegliete per gli scarti una forma che
  torni uguale da com'è partita (Cap. 11.3).

SE HAI FINITO PRIMA (opzionale)
- Le ore oltre le 40 sono straordinari, pagati il 25% in più: calcolate
  per ogni consulente le ore normali, le straordinarie e l'importo con una
  tariffa oraria in costante.
- Stampate la tabella incrociata consulente per progetto, con le ore di
  ognuno su ogni progetto e zero dove non ha lavorato.

PER RIUSARLO
Cambiate le soglie di carico e il nome dei due campi: lo stesso programma
conta gli straordinari del personale di Villanova o le ore dei tecnici di
LogiSud per cliente.

ESEMPIO OUTPUT
============================================================
TALENTHUB - Ore dei consulenti
============================================================
File letto: ore_consulenti.txt
[!] riga  8  ore non numeriche: 'otto'
[!] riga 13  ore fuori intervallo (oltre 0, al massimo 12): -2.0
[!] riga 15  ore fuori intervallo (oltre 0, al massimo 12): 14.0
Righe lette ............... 16
Giornate valide ........... 13
Righe scartate ............ 3
------------------------------------------------------------
CONSULENTE           ORE  GIORNATE  MEDIA/G  CARICO
Amato Chiara        43.0         6      7.2  OLTRE [!]
Bruno Dario         34.5         4      8.6  PIENO
Caruso Elisa        23.0         3      7.7  LEGGERO
------------------------------------------------------------
PROGETTO             ORE   QUOTA
ERP-VILLANOVA       45.5   45.3% ##################
APP-AURORA          40.0   39.8% ################
PORTALE-LOGISUD     15.0   14.9% ######
------------------------------------------------------------
TOTALE             100.5
------------------------------------------------------------
File scritto: ore_consulenti.json
Riletto: 3 consulenti, 3 progetti, 100.5 ore, 3 scarti
[OK] 16 righe = 13 buone + 3 scartate
[OK] totale riletto 100.5 = totale calcolato 100.5
============================================================
"""

# Scrivi il tuo codice qui
