"""
ESERCIZIO 04.3 — Triage al pronto soccorso   ⭐⭐ (media)

CASO D'USO REALE
Al Poliambulatorio Aurora l'infermiere di accettazione assegna a ogni
paziente un colore, che decide l'ordine di chiamata. Il protocollo
interno è scritto su un foglio plastificato attaccato al muro e si
basa su poche informazioni raccolte in trenta secondi: se il paziente è
cosciente, quanto dolore dichiara da 0 a 10, che temperatura ha, quanti
battiti al minuto ha il polso. Il foglio è chiaro, ma alle tre di
notte, con la sala piena, si sbaglia. Il vostro programma è quel
foglio, scritto in modo che non si stanchi.

ISTRUZIONI
Entrano cinque dati, raccolti al banco dell'accettazione: nome del
paziente, se è cosciente (si/no), dolore dichiarato da 0 a 10,
temperatura in gradi, frequenza cardiaca in battiti al minuto.

Esce la scheda di triage, nel formato dell'ESEMPIO OUTPUT: i dati
raccolti, il codice colore assegnato, l'attesa stimata e la nota per
l'infermiere.

Il protocollo appeso al muro, che si legge dall'alto:
    ROSSO  : paziente non cosciente OPPURE dolore da 8 in su
    GIALLO : dolore da 5 in su OPPURE temperatura da 39.0 in su
             OPPURE frequenza cardiaca sopra i 120 battiti
    VERDE  : dolore da 2 in su OPPURE temperatura da 37.5 in su
    BIANCO : tutti gli altri casi

I testi da usare:
    ROSSO  -> "accesso immediato"  / "[!] Chiamare subito il medico di guardia."
    GIALLO -> "entro 30 minuti"    / "[!] Rivalutare se l'attesa supera i 30 minuti."
    VERDE  -> "entro 2 ore"        / "[--] Far accomodare in sala di attesa."
    BIANCO -> "oltre 2 ore"        / "[--] Valutare l'invio all'ambulatorio."

Requisiti:
- struttura standard: docstring, costanti, main(), guard;
- tutte le soglie in costante, con un nome che dice di quale soglia si
  tratta: nel corpo non compare nessun numero del protocollo;
- le soglie vanno tradotte come le detta il foglio: "da 8 in su" e
  "sopra i 120 battiti" non sono la stessa condizione;
- il dato "è cosciente" arriva come testo, ma al protocollo serve come
  valore di verità, con un nome che si legga come una frase italiana;
- i rami assegnano colore, attesa e nota; la scheda si stampa una
  volta sola alla fine;
- la temperatura può arrivare con la virgola e le risposte testuali
  arrivano come capita: si normalizzano prima di usarle.

SUGGERIMENTI
- Le condizioni del protocollo sono legate da OPPURE, non da E: basta
  un indizio dei due perché il colore scatti. Le tabelle di verità del
  capitolo 8.2 dicono che differenza fa scambiarli.
- Un confronto produce già da solo un valore di verità, senza bisogno
  di un if che lo traduca: il capitolo 2.4 lo mostra su una riga sola.
  È da lì che passa la prima condizione del protocollo.
- L'ordine dei rami è il protocollo stesso. Se mettete il verde prima
  del rosso, un paziente incosciente esce verde e il programma non
  protesta.

SE HAI FINITO PRIMA (opzionale)
- Aggiungete l'attesa già trascorsa: chiedete da quanti minuti il
  paziente è in sala e segnalate quando ha superato il tempo previsto
  per il suo colore.
- Stampate anche gli indizi che hanno determinato il colore, uno per
  riga, con [!] accanto a quelli fuori norma.

ESEMPIO OUTPUT
Nome del paziente: carla ruggiero
È cosciente? (si/no): si
Dolore dichiarato (0-10): 6
Temperatura in gradi: 38,2
Frequenza cardiaca (battiti al minuto): 88
==================================================
POLIAMBULATORIO AURORA - TRIAGE
==================================================
Paziente:      Carla Ruggiero
Cosciente:     si
Dolore:        6 su 10
Temperatura:   38.2 gradi
Frequenza:     88 battiti
--------------------------------------------------
CODICE ASSEGNATO: GIALLO
Attesa stimata:   entro 30 minuti
[!] Rivalutare se l'attesa supera i 30 minuti.
==================================================

"""

# Scrivi il tuo codice qui
