"""
ESERCIZIO CASA 03.1 — Convertitore di temperatura   ⭐ (facile)

CASO D'USO REALE
Il Poliambulatorio Aurora ha comprato tre sonde di seconda mano da un
fornitore estero. Funzionano, ma leggono in gradi Fahrenheit, e gli
infermieri fanno la conversione a mente con una formula scritta su un
post-it attaccato al monitor. Vi hanno chiesto un convertitore da tenere
aperto sul computer del reparto: si digita la lettura, esce il valore in
Celsius, in Kelvin e lo scostamento dalla soglia di febbre.

Il programma assume che la lettura sia un numero, scritto con la virgola
o con il punto.

ARGOMENTI TEORICI: Cap. 3–6 — input, prompt, igiene del dato,
conversione

ISTRUZIONI
1) Struttura standard: docstring, costanti, main(), guard.
2) In costante: righe di separazione da 50, intestazione, riferimento
   febbre (37.5), zero Kelvin in Celsius (273.15) e i tre numeri della
   formula Fahrenheit (32, 5, 9). Niente numeri sparsi nel codice.
3) Chiedete codice sonda, reparto e lettura in gradi Fahrenheit.
4) Normalizzate: sonda in maiuscolo, reparto con la maiuscola iniziale,
   lettura con la virgola sostituita dal punto e convertita in float.
5) Calcolate Celsius con la formula (F - 32) * 5 / 9, poi Kelvin
   sommando 273.15, poi lo scostamento rispetto al riferimento febbre.
6) Stampate la scheda: etichette larghe 22 caratteri, valori numerici
   allineati a destra su 10 con due decimali.
7) Lo scostamento va mostrato con il segno, anche quando è positivo:
   la specifica di formato è :>+10.2f.
8) Chiudete con una riga che ricorda il valore di riferimento, costruita
   dalla costante e non scritta a mano.

SUGGERIMENTI
- Le parentesi nella formula non sono facoltative: (F - 32) prima di
  tutto. Senza, il risultato è plausibile e sbagliato, e non ve lo dice
  nessuno.
- Se la riga del calcolo supera gli 88 caratteri, spezzatela in due
  assegnazioni.
- L'etichetta dello scostamento contiene il valore di riferimento:
  costruitela con una f-string dalla costante.
- Provate con 100,4 e poi con 100.4: deve uscire lo stesso risultato.

SE HAI FINITO PRIMA (opzionale)
- Aggiungete la conversione inversa: chiedete anche una temperatura in
  Celsius e mostratela in Fahrenheit.
- Fate stampare lo scostamento anche come percentuale rispetto al
  riferimento, con la specifica :.1%.

ESEMPIO OUTPUT
Codice sonda: a-12
Reparto: radiologia
Lettura in gradi Fahrenheit: 100,4

==================================================
POLIAMBULATORIO AURORA - LETTURA SONDA
==================================================
Sonda:                A-12
Reparto:              Radiologia
--------------------------------------------------
Lettura (F):              100.40
Celsius (C):               38.00
Kelvin (K):               311.15
Scostamento da 37.5:       +0.50
==================================================
Valore di riferimento: 37.5 gradi Celsius.
"""

# Scrivi il tuo codice qui
