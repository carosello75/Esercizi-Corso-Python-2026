"""
ESERCIZIO 05.4 — Chiedi finché non è giusto   ⭐⭐ (media)

CASO D'USO REALE
Allo sportello unico del Comune di Villanova l'operatore digita il CAP che il
cittadino gli detta, e ogni CAP sbagliato fa tornare indietro la pratica.
Serve un controllo che non accetti il dato finché non è giusto.

ARGOMENTI TEORICI: Cap. 13 — Chiedere finché il dato non è buono (il ciclo
di validazione, i messaggi specifici, il tetto ai tentativi)

ISTRUZIONI
Un CAP valido ha LUNGHEZZA_CAP cifre e inizia con PREFISSO_PROVINCIA. Il
programma lo chiede al massimo MAX_TENTATIVI volte e a ogni rifiuto dice la
causa, controllando nell'ordine: lunghezza, sole cifre, prefisso. Finiti i
tentativi, al posto della pratica rinvia allo sportello di assistenza:
    [!] Troppi tentativi: sportello 2.

DATI DI PARTENZA (copiateli così come sono)
     LARGHEZZA = 60
     LUNGHEZZA_CAP = 5
     PREFISSO_PROVINCIA = "84"
     MAX_TENTATIVI = 3
     SPORTELLO_ASSISTENZA = 2

SUGGERIMENTI
- La condizione del ciclo descrive quando si RESTA dentro, non quando si
  esce (Cap. 7.3).
- Dopo il ciclo dovete sapere perché ne siete usciti: dato buono o tentativi
  finiti. Il ciclo da solo non ve lo dice (Cap. 6.6).

SE HAI FINITO PRIMA (opzionale)
- Validate anche il numero di pratica, un intero fra 1 e 9999.
- Contate i tentativi sbagliati per ciascuna delle tre cause e stampateli.

ESEMPIO OUTPUT
============================================================
COMUNE DI VILLANOVA - Sportello unico: verifica del CAP
============================================================
Il CAP ha 5 cifre e inizia per 84.
Hai 3 tentativi.

CAP (tentativo 1 di 3): 8409
  [ERRORE] servono 5 cifre, tu ne hai 4
CAP (tentativo 2 di 3): 84o91
  [ERRORE] solo cifre: niente lettere, spazi o trattini
CAP (tentativo 3 di 3): 84091
  [OK] CAP accettato al tentativo 3.

------------------------------------------------------------
CAP registrato ........ 84091
Tentativi usati ....... 3
------------------------------------------------------------
Pratica avviata. Ritira il numero e attendi la chiamata.
============================================================
"""

# Scrivi il tuo codice qui
