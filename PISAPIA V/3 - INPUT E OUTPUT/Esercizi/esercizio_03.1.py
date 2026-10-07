"""
ESERCIZIO 03.1 — Accettazione paziente   

CASO D'USO REALE
Allo sportello del Poliambulatorio Aurora l'addetta all'accettazione
ricopia a mano su un foglietto i dati di chi si presenta, e poi lo
consegna al paziente perché sappia dove aspettare. I fogli tornano
indietro illeggibili: nomi tutti maiuscoli, codici fiscali con gli spazi
davanti perché incollati dal vecchio gestionale. Vi hanno chiesto un
programma che raccolga i cinque dati e stampi il promemoria sempre nella
stessa forma.

Il programma assume che chi digita risponda a tutte e cinque le domande.
Oggi non sappiamo ancora rifiutare una risposta: si raccoglie e basta.

ISTRUZIONI
Struttura standard: docstring, costanti, main(), guard.
In ingresso, digitati allo sportello: nome, cognome, codice fiscale,
cognome del medico, motivo della visita. Arrivano come li scrive chi ha
il paziente davanti o come li incolla dal vecchio gestionale: maiuscole a
caso e spazi dove capita. In uscita, il promemoria da consegnare, e
l'ESEMPIO OUTPUT qui sotto è la specifica del formato.

Vincoli
- Lo stesso paziente digitato in due modi ("mario", "  MARIO  ") deve
  produrre un promemoria identico.
- I cinque campi non sono dello stesso tipo: un nome proprio, un codice e
  una frase libera non si presentano nello stesso modo. Decidete per
  ognuno, e siate pronti a difendere la scelta.
- Testi e misure fissi (righe di separazione, ambulatorio, sportello,
  sala d'attesa) stanno in costante, non dentro le print().

SUGGERIMENTI
- I metodi per uniformare maiuscole e minuscole sono al Cap. 5.3, la
  tabella che dice quale serve a quale campo al Cap. 5.6. Provatene più
  d'uno sul motivo della visita, che è una frase intera: lì si vede.
- Tenete la variabile grezza separata da quella pulita (nome_grezzo e
  nome): oggi non serve, servirà appena i dati andranno controllati.
- Etichette incolonnate a larghezza fissa: Cap. 9.2.

SE HAI FINITO PRIMA (opzionale)
- Aggiungete la tessera sanitaria e mostratene solo le ultime quattro
  cifre, con lo slicing del Giorno 02.
- Digitate il nome tutto maiuscolo e con tre spazi davanti. Se l'output
  non cambia, avete fatto bene il vostro lavoro.

ESEMPIO OUTPUT
Nome del paziente:   mario
Cognome: rossi
Codice fiscale:   rssmra79e15f839k
Medico (solo cognome): bianchi
Motivo della visita: controllo della pressione

==================================================
POLIAMBULATORIO AURORA - ACCETTAZIONE
==================================================
Paziente:        Mario Rossi
Codice fiscale:  RSSMRA79E15F839K
Medico:          Dott. Bianchi
Motivo:          Controllo della pressione
--------------------------------------------------
Presentarsi a:   Sportello 2
Attesa in:       Sala d'attesa piano terra
==================================================
"""

# Scrivi il tuo codice qui
