"""
ESERCIZIO PER CASA 10.2 — Il questionario di gradimento   ⭐⭐⭐ (impegnativo)

PATTERN USATI: P6, P7, P15, P17, P18, P22, P26

CASO D'USO REALE
Il Poliambulatorio Aurora raccoglie un voto da 1 a 5 e un commento dopo
ogni visita. La direzione vuole sapere quale ambulatorio convince, quale
no, e che cosa scrivono i pazienti scontenti.

ISTRUZIONI
Entra il file questionario_gradimento.txt, una risposta per riga nel
formato ambulatorio;voto;commento.

Esce, nel formato dell'ESEMPIO OUTPUT:
- le righe scartate con numero di riga e motivo (voto non numerico, voto
  fuori scala), e i conteggi;
- per ambulatorio: risposte, media dei voti, soddisfatti (voto 4 o 5) su
  risposte e in percentuale; una riga TUTTI con gli stessi numeri globali;
- la classifica degli ambulatori per media;
- la distribuzione dei voti da 1 a 5, tutti e cinque anche se a zero, con
  una barra proporzionale;
- la quota globale di insoddisfatti (voto 1 o 2) e il saldo di gradimento,
  cioè la percentuale di soddisfatti meno quella di insoddisfatti;
- le tre parole più frequenti nei commenti con voto 1 o 2: parole di
  almeno quattro lettere, senza distinzione fra maiuscole e minuscole,
  virgole tolte.

Vincoli
- A parità di conteggio o di media, l'ordine è quello che dà una
  classifica a coppie (valore, nome) ordinata al contrario: il nome che
  viene dopo nell'alfabeto esce prima. È voluto, e un commento nella
  soluzione lo deve spiegare.
- Nessuna divisione per zero, nemmeno se un ambulatorio non avesse
  risposte valide.

DATI DI PARTENZA
     La cartella dati sta due livelli sopra il vostro file:
     Path(__file__).resolve().parent.parent / "dati"
     AMBULATORI = ["CARDIOLOGIA", "DERMATOLOGIA", "ORTOPEDIA"]
     VOTO_MINIMO = 1    VOTO_MASSIMO = 5
     SODDISFATTO_DA = 4    INSODDISFATTO_FINO_A = 2
     LETTERE_MINIME = 4    LARGHEZZA = 60    LARGHEZZA_BARRA = 40

SUGGERIMENTI
- L'ordine dei quattro controlli su un voto non è indifferente: uno dei
  due ordini possibili ferma il programma alla riga 9 (Cap. 4.1).
- Contare le parole è contare categorie che non conoscete in anticipo
  (Cap. 7.3); la classifica si fa sulle coppie, non sul dizionario
  (Cap. 8.4).
- Per le medie per ambulatorio servono due grandezze per chiave nello
  stesso giro (Cap. 7.4).

SE HAI FINITO PRIMA (opzionale)
- Aggiungete una lista di parole da ignorare (per esempio "nessuno",
  "sono") e controllate come cambia la classifica.
- Fate la stessa analisi delle parole sui commenti con voto 4 o 5: che
  cosa apprezzano i pazienti contenti?

PER RIUSARLO
Cambiate la scala dei voti e le due soglie di soddisfatto e insoddisfatto:
lo stesso programma legge il gradimento di un corso di formazione o di uno
sportello comunale.

ESEMPIO OUTPUT
============================================================
POLIAMBULATORIO AURORA - Questionario di gradimento
============================================================
File letto: questionario_gradimento.txt
[!] riga  6  voto fuori scala 1-5: 6
[!] riga  9  voto non numerico: 'ottimo'
Righe lette ............... 12
Risposte valide ........... 10
Righe scartate ............ 2
------------------------------------------------------------
AMBULATORIO     RISPOSTE   MEDIA     SODDISFATTI
CARDIOLOGIA            3    4.00     2/3   66.7%
DERMATOLOGIA           3    4.67     3/3  100.0%
ORTOPEDIA              4    2.00     0/4    0.0%
------------------------------------------------------------
TUTTI                 10    3.40    5/10   50.0%
------------------------------------------------------------
CLASSIFICA PER MEDIA
1. DERMATOLOGIA    4.67
2. CARDIOLOGIA     4.00
3. ORTOPEDIA       2.00
------------------------------------------------------------
DISTRIBUZIONE DEI VOTI
voto 1    1 ####
voto 2    2 ########
voto 3    2 ########
voto 4    2 ########
voto 5    3 ############
------------------------------------------------------------
Soddisfatti ............... 5 (50.0%)
Insoddisfatti ............. 3 (30.0%)
Saldo di gradimento ....... +20.0 punti
------------------------------------------------------------
PAROLE NEI COMMENTI NEGATIVI (3 commenti)
1. attesa          3
2. poca            2
3. lunga           2
============================================================
"""

# Scrivi il tuo codice qui
