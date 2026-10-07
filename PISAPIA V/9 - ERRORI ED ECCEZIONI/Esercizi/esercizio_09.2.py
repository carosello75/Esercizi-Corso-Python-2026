"""
ESERCIZIO 09.2 — La media del turno, anche a turno vuoto   ⭐ (facile)

CASO D'USO REALE
Il Poliambulatorio Aurora raccoglie il gradimento dei pazienti (0-100) in
un file per turno. Il turno di notte non genera file mentre eventuali file 
vuoti creano problemi al calcolo della media.

ARGOMENTI TEORICI: Cap. 4.4 — Il file che non c'è, catturato; Cap. 6.3 —
ZeroDivisionError; Cap. 8.4 — La media: if contro except

ISTRUZIONI
Entrano tre file della cartella dati, nell'ordine dei DATI DI PARTENZA:
un punteggio intero per riga. Il terzo manca di proposito.

Produce una tabella con una riga per file: quanti punteggi letti, l'esito
calcolato in due modi — una volta prevenendo con if, una volta
gestendo con try — e se i due esiti coincidono. Sotto, il riepilogo nel
formato dell'ESEMPIO OUTPUT.

Vincoli:
- le due strade sono due funzioni distinte, che ricevono il percorso e
  restituiscono l'esito; la stampa sta altrove;
- la strada con if non contiene try, la strada con try non contiene if
  sul file assente né sul turno vuoto;
- i tre esiti possibili sono sempre le stesse tre scritte, in costante;
- i file si trovano con Path(__file__).resolve().parent.parent / "dati";
  nessun percorso completo compare nell'output;

DATI DI PARTENZA (copiateli così come sono)
     FILE_TURNI = ("punteggi_turno.txt", "punteggi_vuoto.txt",
                   "punteggi_notte.txt")
     ESITO_ASSENTE = "file assente"
     ESITO_VUOTO = "nessun dato"
     LARGHEZZA = 70

SE HAI FINITO PRIMA (opzionale)
- Aggiungete un quarto file con una riga "novanta" in mezzo: quale delle
  due strade si ferma? Fate in modo che nessuna delle due si fermi.
- Stampate anche il punteggio minimo e il massimo del turno, con la
  stessa doppia strada per il turno vuoto: max() su una lista vuota
  solleva anche lui un'eccezione, ma non la stessa.

ESEMPIO OUTPUT
======================================================================
POLIAMBULATORIO AURORA - Media del gradimento per turno
======================================================================
FILE                  LETTI  CON IF          CON TRY         UGUALI
punteggi_turno.txt        8  media 74.50     media 74.50     sì
punteggi_vuoto.txt        0  nessun dato     nessun dato     sì
punteggi_notte.txt        -  file assente    file assente    sì
----------------------------------------------------------------------
Le due strade concordano su 3 file su 3.
File letti ........... 2 su 3
Punteggi letti ....... 8
----------------------------------------------------------------------

======================================================================
"""

# Scrivi il tuo codice qui
