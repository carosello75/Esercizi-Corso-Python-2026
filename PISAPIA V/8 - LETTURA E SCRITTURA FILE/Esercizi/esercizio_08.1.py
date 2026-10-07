"""
ESERCIZIO 08.1 — Il registro dello sportello   ⭐ (facile)

CASO D'USO REALE
Lo sportello unico del Comune di Villanova segna gli accessi su un quaderno,
e a fine mese nessuno riesce più a contarli. Da oggi il programma li scrive
su un file, e li rilegge dal disco per contarli.

ARGOMENTI TEORICI: Cap. 3 — with open() e le modalità · Cap. 4 — Leggere
un file · Cap. 6 — Scrivere un file

ISTRUZIONI
Ingresso: la lista ACCESSI qui sotto, sei coppie (cognome, servizio).
Uscita:
- il file registro_accessi.txt nella cartella giorno_08/output, una riga
  per accesso nella forma cognome;servizio. Il file si riscrive da capo a
  ogni esecuzione: lanciato due volte, deve contenere sei righe, non dodici;
- a video, quante righe e quanti caratteri avete scritto;
- la rilettura DAL FILE, non dalla lista: una riga numerata per accesso,
  il numero di righe rilette e i caratteri riletti, con un verdetto [OK]
  se coincidono con quelli scritti e [!] se non coincidono;
- il numero di accessi per servizio e il servizio più richiesto, calcolati
  sulle righe rilette.
Vincoli: il percorso della cartella si costruisce con pathlib a partire
dalla posizione dello script, Path(__file__).resolve().parent.parent,
e la cartella output va creata se non c'è. A video si stampa solo il nome
del file, mai il percorso intero.

DATI DI PARTENZA (copiateli così come sono)
     ACCESSI = [
         ("Esposito", "ANAGRAFE"),
         ("Russo", "TRIBUTI"),
         ("Greco", "ANAGRAFE"),
         ("Romano", "SERVIZI SOCIALI"),
         ("Colombo", "TRIBUTI"),
         ("Ricci", "ANAGRAFE"),
     ]
     NOME_FILE = "registro_accessi.txt"
     LARGHEZZA = 60

SUGGERIMENTI
- write() non va a capo da sola, e restituisce un numero che vi serve
  (Cap. 6.1).
- Una riga letta con for porta con sé il suo a capo: decidete voi quando
  toglierlo e quando contarlo (Cap. 4.3 e 5.1).
- Il conta-occorrenze è quello del Giorno 07, Cap. 12.

SE HAI FINITO PRIMA (opzionale)
- Scrivete in testa al file una riga di commento che comincia con # e
  fate in modo che la rilettura la salti senza contarla fra gli accessi.
- Provate a scrivere le righe con print(..., file=f) invece di write():
  che cosa succede al conteggio dei caratteri scritti, e perché?

ESEMPIO OUTPUT
============================================================
COMUNE DI VILLANOVA - Registro degli accessi allo sportello
============================================================
[OK] Scritto registro_accessi.txt: 6 righe, 101 caratteri
------------------------------------------------------------
RILETTURA DAL DISCO
  N.  COGNOME       SERVIZIO
   1  Esposito      ANAGRAFE
   2  Russo         TRIBUTI
   3  Greco         ANAGRAFE
   4  Romano        SERVIZI SOCIALI
   5  Colombo       TRIBUTI
   6  Ricci         ANAGRAFE
Righe rilette ............ 6
Caratteri riletti ........ 101
[OK] Il file contiene esattamente quello che è stato scritto.
------------------------------------------------------------
ACCESSI PER SERVIZIO
  ANAGRAFE .............. 3
  TRIBUTI ............... 2
  SERVIZI SOCIALI ....... 1
Servizio più richiesto ... ANAGRAFE (3 accessi)
============================================================
"""

# Scrivi il tuo codice qui
