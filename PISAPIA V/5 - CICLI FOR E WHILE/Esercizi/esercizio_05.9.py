"""
ESERCIZIO 05.9 — Il controllo dei codici di tracciamento   ⭐⭐ (media)

CASO D'USO REALE
Al bancone di LogiSud l'operatore batte i codici dei colli che il magazziniere
gli legge, finché il bancale non è vuoto. Un codice battuto male manda il collo
nel magazzino sbagliato: va scartato subito, dicendo perché.

ARGOMENTI TEORICI: Cap. 5 — `for` su una stringa · Cap. 6 — Contatore e
accumulatore · Cap. 9 — La sentinella · Cap. 11 — `for` o `while`

ISTRUZIONI
Leggete codici finché l'operatore non scrive fine, in qualunque forma la scriva.
Per ogni codice stampate subito il verdetto: accettato, oppure scartato con il
primo motivo che lo rende sbagliato. In fondo il riepilogo della giornata, che
non deve fermarsi nemmeno se non è stato battuto nessun codice. Nel programma
servono tutti e due i cicli: decidete voi dove va ciascuno, e perché.

DATI DI PARTENZA (copiateli così come sono)
     PREFISSO = "LS"
     CIFRE_SERIALE = 5
Un codice buono è PREFISSO, poi le cifre del seriale, poi una cifra di
controllo: l'ultima cifra della somma delle cifre del seriale.
     LS123455   ->   1+2+3+4+5 = 15, l'ultima cifra è 5: accettato
Maiuscole e minuscole non contano. I motivi di scarto, in quest'ordine:
lunghezza, prefisso, caratteri che non sono cifre, cifra di controllo.

SUGGERIMENTI
- Per ognuno dei due cicli chiedetevi: «so quante volte, prima di partire?»
  (Cap. 11.1).
- Provate un codice con una lettera in mezzo, e anche fine come primo dato.

SE HAI FINITO PRIMA (opzionale)
- Portate il seriale a sei cifre cambiando una costante sola.
- Fate stampare, per ogni codice scartato, il codice che sarebbe stato giusto.

ESEMPIO OUTPUT
============================================================
LOGISUD - Controllo dei codici di tracciamento
============================================================
Formato: LS + 5 cifre + 1 di controllo.

Codice collo (o 'fine'): LS123455
  [OK] LS123455 accettato
Codice collo (o 'fine'): ls900016
  [ERRORE] LS900016: cifra di controllo errata (attesa 0, letta 6)
Codice collo (o 'fine'): LS12345
  [ERRORE] LS12345: servono 8 caratteri, ne ha 7
Codice collo (o 'fine'): XY123455
  [ERRORE] XY123455: deve iniziare con LS
Codice collo (o 'fine'): LS12A455
  [ERRORE] LS12A455: dopo LS servono solo cifre
Codice collo (o 'fine'): LS400004
  [OK] LS400004 accettato
Codice collo (o 'fine'): fine

------------------------------------------------------------
Codici esaminati ...... 6
Accettati ............. 2
Scartati .............. 4
Quota accettati ....... 33.3%
============================================================
"""

# Scrivi il tuo codice qui
