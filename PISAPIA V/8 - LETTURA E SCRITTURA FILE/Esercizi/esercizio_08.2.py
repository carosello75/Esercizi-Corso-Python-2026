"""
ESERCIZIO 08.2 — La lettera che supera il limite   ⭐ (facile)

CASO D'USO REALE
Il portale di TalentHub accetta lettere fino a 120 parole e 800 caratteri,
e il modulo web taglia le righe più lunghe di 74 caratteri. Giulia vuole
misurare la sua lettera dal file, prima di caricarla.

ARGOMENTI TEORICI: Cap. 4 — Leggere un file · Cap. 5 — Il fine riga e la
pulizia delle righe

ISTRUZIONI
Ingresso: il file lettera_candidatura.txt nella cartella giorno_08/dati,
trovato con Path(__file__).resolve().parent.parent / "dati".
Uscita, a video:
- righe totali e righe non vuote;
- caratteri del file, a capo compresi, e parole;
- la riga più lunga, con il suo numero e la sua lunghezza;
- la parola più lunga, senza la punteggiatura attaccata;
- un verdetto [OK] o [!] per ciascuno dei tre limiti; per le righe troppo
  lunghe, quante sono e, per ognuna, numero, lunghezza e inizio del testo;
- una frase finale: la lettera si può caricare o va sistemata.
Vincoli: il file si legge una volta sola. La lunghezza di una riga è quella
che si VEDE: l'a capo e gli spazi in coda non contano. Nessun conteggio
fatto a mano: i numeri li trova il programma.

DATI DI PARTENZA (copiateli così come sono)
     NOME_FILE = "lettera_candidatura.txt"
     MASSIMO_PAROLE = 120
     MASSIMO_CARATTERI = 800
     MASSIMO_CARATTERI_RIGA = 74
     LARGHEZZA_ANTEPRIMA = 40
     LARGHEZZA = 60

SUGGERIMENTI
- Quale dei quattro modi di leggere vi dà tutto in un giro solo? La
  tabella di Cap. 4.6.
- Una riga vuota letta dal file non è una stringa vuota (Cap. 4.4 e 5.1).
- La riga 6 del file finisce con uno spazio che non si vede: è lì apposta
  (Cap. 5.2).

SE HAI FINITO PRIMA (opzionale)
- Contate le frasi, cioè le parole che finiscono con un punto, e dite
  quante parole ha in media una frase.
- Fate scrivere al programma una copia della lettera in giorno_08/output
  con le righe troppo lunghe spezzate prima del limite, senza tagliare una
  parola a metà.

ESEMPIO OUTPUT
============================================================
TALENTHUB - Controllo della lettera prima del caricamento
============================================================
File letto: lettera_candidatura.txt
------------------------------------------------------------
Righe totali ............. 12
Righe non vuote .......... 10
Caratteri, a capo compresi 560
Parole ................... 85
Riga più lunga ........... riga 8, 78 caratteri
Parola più lunga ......... all'amministrazione (19 caratteri)
------------------------------------------------------------
[OK] Parole: 85 su 120.
[OK] Caratteri: 560 su 800.
[!] Righe oltre 74 caratteri: 1
    riga 8 (78): Sono una persona precisa, puntuale e abi...
------------------------------------------------------------
La lettera va sistemata prima del caricamento.
============================================================
"""

# Scrivi il tuo codice qui
