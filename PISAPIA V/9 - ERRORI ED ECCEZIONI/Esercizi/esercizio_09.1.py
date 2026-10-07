"""
ESERCIZIO 09.1 — Lo screening che non si ferma   ⭐ (facile)

CASO D'USO REALE
Il modulo di screening di TalentHub (esercizio 03.7) si bloccava a ogni
dato scritto male e il candidato ricominciava da capo. Il responsabile
adesso chiede che risponda con un messaggio e chiuda in modo pulito.

ARGOMENTI TEORICI: Cap. 3 — Leggere un traceback; Cap. 4 — try/except;
Cap. 5 — Catturare l'eccezione giusta

ISTRUZIONI
Entrano quattro dati: nome e cognome, età, punteggio del test su 100
(con la virgola o con il punto), anni di esperienza.

Esce la scheda del candidato nel formato del primo ESEMPIO OUTPUT. Se un
dato non si può convertire, il programma non fa le domande successive:
stampa una riga [ERRORE] che nomina il campo, dice che cosa serve e
riporta fra apici quello che è stato digitato, poi la riga di
interruzione. Nessun traceback, in nessun caso.

Vincoli:
- struttura standard: docstring, costanti, main(), guard, funzioni proprie;
- ogni conversione ha il suo try, con dentro solo la riga che converte;
- si cattura soltanto il tipo di eccezione che la conversione solleva;
- un campo lasciato vuoto ha una frase sua al posto degli apici vuoti;
- un punteggio che si converte ma sta fuori da 0-100 è rifiutato lo
  stesso: il try controlla la forma, non l'intervallo.

SE HAI FINITO PRIMA (opzionale)
- Invece di interrompere al primo errore, ripetete la domanda sul campo
  sbagliato fino a tre volte, poi interrompete.
- Aggiungete alla riga [ERRORE] il nome del tipo di eccezione, preso
  dall'eccezione stessa e non scritto a mano.

ESEMPIO OUTPUT — dati validi
Nome e cognome: marco rossi
Eta: 29
Punteggio del test (0-100): 72,5
Anni di esperienza: 3

======================================================================
TALENTHUB - SCREENING CANDIDATO
======================================================================
Candidato:       Marco Rossi
Eta:             29
Punteggio:       72.5 su 100 (72.5%)
Esperienza:      3 anni
======================================================================
[OK] Screening registrato.

ESEMPIO OUTPUT — età scritta in lettere
Nome e cognome: marco rossi
Eta: venti

[ERRORE] Eta: serve un numero intero, avete scritto 'venti'
Screening interrotto: nessun dato registrato.

ESEMPIO OUTPUT — punteggio con il simbolo di percentuale
Nome e cognome: marco rossi
Eta: 29
Punteggio del test (0-100): 72%

[ERRORE] Punteggio: serve un numero, anche con la virgola, avete scritto '72%'
Screening interrotto: nessun dato registrato.

ESEMPIO OUTPUT — punteggio fuori scala
Nome e cognome: marco rossi
Eta: 29
Punteggio del test (0-100): 900

[ERRORE] Punteggio: serve un valore fra 0 e 100, avete scritto '900'
Screening interrotto: nessun dato registrato.
"""

# Scrivi il tuo codice qui
