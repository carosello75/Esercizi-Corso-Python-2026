"""
ESERCIZIO 03.4 — Preventivo spedizione in una riga  

CASO D'USO REALE
Al bancone della filiale LogiSud passano ottanta colli al giorno.
L'addetto vi ha detto una cosa ragionevole: "se devo premere invio tre
volte per ogni collo, sono duecentoquaranta invii, e io faccio prima a
scrivere a mano". Vuole digitare tutto su una riga sola, come fa già sul
vecchio terminale: zona, peso e urgenza separati da punto e virgola. La
tariffa la legge dal listino cartaceo e la digita su una seconda riga.

Il programma assume che la prima riga contenga esattamente due punti e
virgola e la seconda esattamente uno. Con un separatore in più o in meno
il programma si ferma: è previsto, e quel messaggio d'errore vi servirà
nell'esercizio 03.7.

ISTRUZIONI
Struttura standard: docstring, costanti, main(), guard.
In ingresso due sole righe digitate, non cinque: al primo invio la
spedizione (zona, peso, urgenza), al secondo il listino letto dal
cartaceo (tariffa al kg, maggiorazione in percentuale). Dentro ogni riga
i campi sono separati dal punto e virgola, e il formato va scritto nel
prompt, separatore compreso. In uscita il preventivo voce per voce:
l'ESEMPIO OUTPUT qui sotto è la specifica del formato e insieme il
vostro collaudo, perché con quei due input devono uscire quei numeri.

Come si costruisce il prezzo
- Il trasporto dipende dal peso e dalla tariffa al chilo.
- I diritti fissi (4.50) si sommano al trasporto: è l'imponibile base.
- La maggiorazione d'urgenza è una percentuale dell'imponibile base,
  diritti compresi.
- L'IVA (22%) qui si aggiunge all'imponibile: non si scorpora come alla
  cassa dell'esercizio 03.2.

Vincoli
- Diritti fissi e aliquota in costante, e l'etichetta dell'IVA deve
  riportare l'aliquota senza che nessuno la riscriva a mano.
- Ogni pezzo delle due righe finisce in una variabile con un nome suo:
  tre nomi per la prima riga, due per la seconda (Cap. 7.3).
- I pezzi vanno resi utilizzabili prima di essere usati: al bancone si
  digita con gli spazi intorno ai separatori e la virgola nei decimali.

SUGGERIMENTI
- .split() taglia e basta, non pulisce niente. Il pezzo centrale di
  "sud; 12,5 ;URGENTE" è " 12,5 ", spazi compresi (Cap. 7.5).
- 30 vuol dire trenta su cento. Se il preventivo vi esce di qualche
  centinaio di euro, avete applicato il numero e non la percentuale.
- Il simbolo % occupa una colonna anche lui: la maggiorazione è l'unica
  riga in cui il numero non arriva fino al margine destro. Contate,
  invece di aggiungere uno spazio a occhio (Cap. 9.4).

SE HAI FINITO PRIMA (opzionale)
- Aggiungete il codice della spedizione nel formato LS-2026-MI-0042 e
  ricavatene anno e sigla provincia con lo slicing.
- Digitate la prima riga con le virgole al posto dei punti e virgola.
  Leggete il messaggio d'errore e annotatelo: vi servirà.

ESEMPIO OUTPUT
Spedizione (zona;peso;urgenza): sud; 12,5 ;URGENTE
Listino (tariffa_kg;maggiorazione_%): 1,20;30

==================================================
LOGISUD TRASPORTI - PREVENTIVO DI SPEDIZIONE
==================================================
Zona:                          SUD
Peso in kg:                  12.50
Urgenza:                   urgente
Tariffa al kg:                1.20
Maggiorazione:                 30%
--------------------------------------------------
Diritti fissi:                4.50
Trasporto:                   15.00
Imponibile base:             19.50
Maggiorazione urgenza:        5.85
Imponibile:                  25.35
IVA 22%:                      5.58
--------------------------------------------------
TOTALE PREVENTIVO:           30.93
==================================================
Importi in euro. Preventivo valido 15 giorni.
"""

# Scrivi il tuo codice qui
