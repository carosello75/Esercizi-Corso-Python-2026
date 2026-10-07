"""
ESERCIZIO PER CASA 07.1 — La rubrica   ⭐⭐ (media)

CASO D'USO REALE
Alla segreteria del Poliambulatorio Aurora i numeri dei pazienti stanno su
un quaderno ad anelli, in ordine di quando sono stati scritti. Cercarne uno
vuol dire sfogliare. Voi fate la versione elettronica minima: si digita un
nome, il programma risponde con il numero, e se il nome non c'è lo chiede
e lo salva. Si va avanti finché non si scrive FINE. È il primo programma
del corso che si ricorda qualcosa che gli avete detto voi mentre girava —
almeno finché non lo chiudete: il rimedio arriverà quando impareremo a
scrivere i dati su un file.

ARGOMENTI TEORICI: Cap. 10 — Il dizionario · Cap. 11 — .get() con valore
predefinito e aggiunta di una chiave (più il ciclo con sentinella del
Giorno 05)

ISTRUZIONI
1) Partite dal dizionario rubrica con i tre contatti già presenti.
2) Stampate quanti contatti ci sono e le istruzioni d'uso.
3) Ciclo con sentinella: chiedete un nome con
   input("Nome (o FINE): ") e ripulitelo con .strip(). Se il testo, messo
   in maiuscolo, è uguale a SENTINELLA, uscite dal ciclo con break.
4) Normalizzate il nome con .title(): così "rossi anna", "ROSSI ANNA" e
   "Rossi Anna" diventano la stessa chiave. Senza questo passo la rubrica
   si riempie di doppioni e nessuno capisce perché.
5) Cercate il nome con .get(nome, NON_TROVATO). Se il risultato è diverso
   da NON_TROVATO, stampate la riga [OK] con i puntini di riempimento.
   Altrimenti stampate la riga [--], chiedete il numero e salvatelo nel
   dizionario, poi stampate la conferma.
6) Tenete tre contatori: ricerche fatte, trovati subito, aggiunti oggi.
7) Alla fine stampate la rubrica completa, i tre contatori e la nota
   sull'ordine dei contatti.

DATI DI PARTENZA (copiateli così come sono)
     RUBRICA_INIZIALE = {
         "Rossi Anna": "089 111222",
         "Bianchi Marco": "089 333444",
         "Verdi Luca": "089 555666",
     }
     SENTINELLA = "FINE"
     NON_TROVATO = ""
     LARGHEZZA = 60
     LARGHEZZA_ETICHETTA = 20

SUGGERIMENTI
- Scrivete una funzione riga_contatto(nome, numero) che restituisce la
  riga con i puntini: puntini = "." * (LARGHEZZA_ETICHETTA - len(nome) - 1).
  La userete tre volte e vi risparmia di contare gli spazi a mano.
- Il confronto con la sentinella si fa su .strip().upper(), altrimenti
  "fine " con lo spazio non ferma il ciclo e voi restate lì.
- .title() su "de luca mario" dà "De Luca Mario": non è perfetto per tutti
  i cognomi italiani, e va bene lo stesso per oggi. Sapere che una
  normalizzazione è imperfetta è meglio che non normalizzare.
- Per aggiungere un contatto si assegna: rubrica[nome] = numero. Se il
  nome c'era già lo sovrascrivete, ma qui non può succedere, perché in
  quel ramo ci arrivate solo quando non c'era.

SE HAI FINITO PRIMA (opzionale)
- Aggiungete il comando ELENCO: se l'utente scrive ELENCO invece di un
  nome, il programma stampa tutta la rubrica e riparte con la domanda,
  senza contarlo come ricerca. Serve un continue.
- Aggiungete la cancellazione: se l'utente scrive un nome preceduto da un
  meno ("-Verdi Luca"), togliete il contatto dalla rubrica. Attenzione a
  cosa succede se il nome non c'era.

ESEMPIO OUTPUT
============================================================
POLIAMBULATORIO AURORA - Rubrica dei contatti
============================================================
Rubrica di partenza: 3 contatti.
Scrivete un nome per cercarlo, oppure FINE per chiudere.

Nome (o FINE): Rossi Anna
[OK] Rossi Anna ......... 089 111222

Nome (o FINE): neri sara
[--] Neri Sara non è in rubrica.
Numero da salvare: 089 777888
[OK] Neri Sara: contatto salvato.

Nome (o FINE): rossi anna
[OK] Rossi Anna ......... 089 111222

Nome (o FINE): fine

------------------------------------------------------------
RUBRICA FINALE (4 contatti)
Rossi Anna ......... 089 111222
Bianchi Marco ...... 089 333444
Verdi Luca ......... 089 555666
Neri Sara .......... 089 777888
------------------------------------------------------------
Ricerche fatte ..... 3
Trovati subito ..... 2
Aggiunti oggi ...... 1
------------------------------------------------------------
I contatti escono nell'ordine in cui sono entrati in rubrica.
Neri Sara è l'ultima perché è stata aggiunta oggi, non perché
il suo cognome venga dopo: un dizionario non ordina niente.
============================================================
"""

# Scrivi il tuo codice qui
