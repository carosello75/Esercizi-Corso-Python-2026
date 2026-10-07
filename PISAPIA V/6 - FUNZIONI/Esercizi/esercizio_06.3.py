"""
ESERCIZIO 06.3 — Chiedere un numero, sul serio   ⭐⭐ (media)

CASO D'USO REALE
Allo sportello anagrafe del Comune di Villanova ogni modulo chiede numeri:
componenti del nucleo, anno di nascita, sportello di destinazione. Il ciclo
che richiede il dato finché non è buono sono dodici righe, e per tre numeri
diventano trentasei righe uguali in tre punti diversi.

ARGOMENTI TEORICI: Cap. 4 — Parametri e argomenti; Cap. 5 — return dopo il
ciclo; Cap. 7 — Chiamare una funzione dentro un'altra; Cap. 11 — Ambito
locale. Riprende il ciclo di validazione del Giorno 05 e lo chiude dentro
una funzione riutilizzabile.

ISTRUZIONI
Tre funzioni e un main() che non contiene nessun controllo.

  - una riceve il testo della domanda e i due estremi ammessi, ripete la
    domanda finché non arriva un intero dentro l'intervallo e alla fine lo
    restituisce. Dentro servono tre messaggi d'errore distinti, perché
    "non è un numero", "è troppo basso" e "è troppo alto" dicono tre cose
    diverse. Dopo tre risposte sbagliate di fila aggiunge un suggerimento
    più esplicito, e lo aggiunge una volta sola
  - una fa lo stesso lavoro con una domanda da sì o no: accetta s, si, sì,
    n, no in qualunque combinazione di maiuscole, e restituisce un booleano
  - una riceve due anni e restituisce gli anni compiuti

main() chiama la prima tre volte, con tre domande e tre intervalli diversi,
la seconda una volta per sapere se la pratica è urgente, e stampa il
riepilogo. Nessun controllo di validità deve comparire dentro main(): è il
punto dell'esercizio. I testi delle domande si costruiscono dalle stesse
costanti che le funzioni useranno per controllare, così l'intervallo
scritto e l'intervallo verificato non possono divergere.

DATI DI PARTENZA (copiateli così come sono)
     ANNO_CORRENTE = 2026
     MIN_COMPONENTI = 1
     MAX_COMPONENTI = 12
     ANNO_MINIMO = 1900
     SPORTELLO_MINIMO = 1
     SPORTELLO_MASSIMO = 6
     TENTATIVI_PRIMA_DELL_AIUTO = 3
     LARGHEZZA = 60

SUGGERIMENTI
- Il ciclo è quello del Giorno 05: una bandiera che parte da False e
  diventa True solo quando il dato è buono. Dove va il return rispetto al
  while lo dice Cap. 5.4, e sbagliarlo non produce nessun errore.
- .isdecimal() dice di no al segno meno, alla virgola e alla stringa vuota.
  Qui va bene così, ma sappiate perché: Cap. 15, errore E8.
- Il contatore dei tentativi vive dentro la funzione e riparte da capo a
  ogni chiamata. È l'ambito locale del Cap. 11.1, ed è quello che rende la
  funzione riusabile senza effetti a distanza.

SE HAI FINITO PRIMA (opzionale)
- La funzione non accetta numeri negativi, perché .isdecimal() li rifiuta
  prima ancora di guardare l'intervallo. Fatele accettare un intervallo che
  parte sotto zero, e dite quale controllo avete dovuto aggiungere.
- Il riepilogo è stampato riga per riga da main(). Estraete la funzione che
  stampa una riga etichetta-valore incolonnata e usatela per tutte e cinque
  le righe, senza che main() scriva più nessun puntino.

ESEMPIO OUTPUT
============================================================
COMUNE DI VILLANOVA - Sportello anagrafe
============================================================
Componenti del nucleo (1-12): tre
[ERRORE] Servono solo cifre: niente lettere, niente spazi.
Componenti del nucleo (1-12): 0
[ERRORE] Il valore minimo ammesso è 1.
Componenti del nucleo (1-12): 13
[ERRORE] Il valore massimo ammesso è 12.
[!] Serve un numero intero fra 1 e 12, cifre e nient'altro.
Componenti del nucleo (1-12): 4
Anno di nascita (1900-2026): 1985
Sportello di destinazione (1-6): 9
[ERRORE] Il valore massimo ammesso è 6.
Sportello di destinazione (1-6): 3
Pratica urgente? (s/n): x
[ERRORE] Rispondete s oppure n.
Pratica urgente? (s/n): S
------------------------------------------------------------
RIEPILOGO DELLA RICHIESTA
Componenti del nucleo ..... 4
Anno di nascita ........... 1985
Anni compiuti nel 2026 .... 41
Sportello ................. 3
Urgente ................... sì
------------------------------------------------------------
La funzione chiedi_intero è stata scritta una volta e
chiamata tre volte. Senza di lei gli stessi tre controlli
sarebbero ricopiati in tre punti diversi, e il giorno che
cambia il messaggio d'errore bisogna ricordarsi di tutti.
============================================================
"""

# Scrivi il tuo codice qui
