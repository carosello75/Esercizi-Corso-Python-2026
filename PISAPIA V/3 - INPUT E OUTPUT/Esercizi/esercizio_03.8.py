"""
ESERCIZIO 03.8 — Mini-progetto: Totem self-service   

CASO D'USO REALE
TalentHub ha messo un totem all'ingresso della sede: chi passa e vuole
candidarsi compila lì, in piedi, in due minuti, e porta in reception un
foglietto con un codice. Fino a ieri il totem era un blocchetto di
moduli cartacei e una biro legata con lo spago. Giulia, che ha finito il
suo tirocinio all'ufficio IT di NovaStore, ha ricevuto il primo incarico
esterno: scrivere il programma che gira sul totem.

Il totem deve fare tre cose. Guidare la compilazione in sezioni, così
chi ha fretta sa quanto manca. Normalizzare tutto, perché al totem si
scrive male. Stampare una scheda che sembri un documento e non uno
scarabocchio, con un codice candidatura da dettare in reception.

Il programma assume che anno di nascita, anni di esperienza,
retribuzione e giorni di preavviso siano numeri scritti correttamente, e
che nome e cognome non siano vuoti.

ISTRUZIONI
Struttura standard: docstring, costanti, main(), guard. Nessun numero e
nessun testo fisso dentro il corpo del programma: tutto in costante.

In ingresso nove campi, raccolti in tre sezioni annunciate a schermo
perché chi compila in piedi sappia quanto manca: anagrafica, contatti,
candidatura; prima delle sezioni, la schermata di apertura del totem. In
uscita la scheda candidatura da portare in reception. L'ESEMPIO OUTPUT
qui sotto è la specifica completa (apertura, sezioni, domande, scheda) e
si riproduce riga per riga.

Tre valori che nessuno digita
- L'età, ricavata dall'anno di nascita e dall'anno corrente (2026).
- La retribuzione mensile: l'azienda paga tredici mensilità.
- Il codice candidatura, costruito da sigla aziendale, anno, iniziali
  del candidato e anno di nascita.

Vincoli
- Al totem si scrive male, in piedi e di fretta: nessuno dei nove campi
  entra nella scheda come è stato digitato.
- I numeri della schermata di apertura e della checklist finale
  (posizioni aperte, campi per sezione) sono costanti, non cifre scritte
  dentro le print(): il giorno che una sezione cresce di un campo, la
  checklist deve seguirla da sola.
- La checklist non verifica niente: oggi i marcatori [OK] sono sempre
  accesi. Diventeranno il frutto di un controllo vero quando impareremo
  a dire di no.

SUGGERIMENTI
- Fatelo in cinque passaggi e provate dopo ognuno: apertura, sezione 1,
  sezioni 2 e 3, calcoli, scheda. Scrivere centoventi righe e poi
  lanciare è il modo più rapido per perdere mezz'ora a cercare dove.
- La riga della tabella retribuzione porta tre colonne e rischia di
  sfondare gli 88 caratteri: qualche pezzo si può preparare a parte e
  montare dopo (Cap. 9.5).
- Se una riga della scheda esce disallineata, contate le larghezze: non
  aggiustate con gli spazi a mano.

SE HAI FINITO PRIMA (opzionale)
- Aggiungete alla tabella la retribuzione giornaliera, calcolata su 260
  giorni lavorativi (valore didattico inventato).
- Mascherate l'email nella scheda mostrando solo il primo carattere e il
  dominio.

ESEMPIO OUTPUT
==================================================
TALENTHUB
TOTEM CANDIDATURE - SEDE DI BATTIPAGLIA
==================================================
Compilare i campi. INVIO dopo ogni risposta.
Posizioni aperte in questo momento: 4
==================================================

--- SEZIONE 1 DI 3: ANAGRAFICA ---
Nome:   marco
Cognome: ROSSI
Anno di nascita (4 cifre): 1994

--- SEZIONE 2 DI 3: CONTATTI ---
Email:   Marco.Rossi@Posta.IT
Telefono: 349 884 1207

--- SEZIONE 3 DI 3: CANDIDATURA ---
Posizione desiderata: sviluppatore junior
Anni di esperienza: 4
Retribuzione annua lorda attesa in euro: 28500,00
Giorni di preavviso: 15

==================================================
SCHEDA CANDIDATURA
==================================================
Codice:           TH-2026-MR-1994
Nome e cognome:   Marco Rossi
Eta:              32 anni
Email:            marco.rossi@posta.it
Telefono:         3498841207
--------------------------------------------------
Posizione:        SVILUPPATORE JUNIOR
Esperienza:       4 anni
Preavviso:        15 giorni
--------------------------------------------------
VOCE                               ANNUO   MENSILE
Retribuzione lorda attesa       28500.00   2192.31
--------------------------------------------------
CONTROLLO CAMPI RACCOLTI
[OK] Anagrafica      3 campi
[OK] Contatti        2 campi
[OK] Candidatura     4 campi
==================================================
Presentare in reception il codice:
TH-2026-MR-1994
==================================================
"""

# Scrivi il tuo codice qui
