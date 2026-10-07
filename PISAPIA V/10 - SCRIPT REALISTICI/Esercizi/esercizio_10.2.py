"""
ESERCIZIO 10.2 — Il rimborso chilometrico   ⭐ (facile)

PATTERN USATI: P1, P2, P4, P5, P7, P12

CASO D'USO REALE
In TalentHub Giulia inserisce a mano le trasferte dei consulenti, e ogni
mese qualche richiesta torna indietro: km scritti con la virgola, veicoli
inventati, cifre impossibili. Il modulo deve rifiutarle subito, e dire
perché.

ISTRUZIONI
Ingresso da tastiera, in quest'ordine: nome e cognome del consulente,
veicolo, chilometri percorsi.

Uscita:
- se i tre dati sono buoni, la scheda di rimborso (consulente, veicolo,
  km, tariffa, rimborso) con il rimborso anche nella forma da scrivere sul
  modulo cartaceo, cioè con la virgola;
- altrimenti TUTTI gli errori trovati, non solo il primo, e la richiesta
  non registrata. Ogni errore dice il campo, che cosa non va e che cosa
  scrivere al suo posto.

Vincoli:
- il nome si accetta comunque scritto ("sara NERI"), ma servono almeno
  due parole; il veicolo si accetta in maiuscolo o minuscolo;
- i km si accettano con il punto o con la virgola decimale e devono stare
  fra KM_MINIMI e KM_MASSIMI, estremi compresi;
- la tariffa si cerca nel dizionario, senza una catena di if/elif; un
  veicolo che non c'è è un errore, non un crash;
- il rimborso è arrotondato al centesimo; nessun traceback, mai.

DATI DI PARTENZA (copiateli così come sono)
     TARIFFE_KM = {"AUTO": 0.42, "MOTO": 0.21, "FURGONE": 0.55}
     KM_MINIMI = 1
     KM_MASSIMI = 1500
     LARGHEZZA = 60

SE HAI FINITO PRIMA (opzionale)
- Aggiungete il pedaggio autostradale, facoltativo: si digita 0 se non
  c'è, con la virgola se c'è, e si somma al rimborso.
- Tetto mensile: se il rimborso supera 300 euro la scheda esce comunque,
  ma con un [!] che chiede la firma del responsabile.

PER RIUSARLO
Il dizionario delle tariffe e i due limiti stanno in cima: con
{"PRANZO": 8.00, "CENA": 12.00} e un tetto di pasti al mese lo stesso
modulo diventa il rimborso pasti, con le ore al posto dei km gli
straordinari.

ESEMPIO OUTPUT — richiesta accettata
============================================================
TALENTHUB - Rimborso chilometrico
============================================================
Nome e cognome del consulente: sara NERI
Veicolo (AUTO, MOTO, FURGONE): auto
Chilometri percorsi (da 1 a 1500): 128,5
------------------------------------------------------------
SCHEDA DI RIMBORSO
Consulente ............ Sara Neri
Veicolo ............... AUTO
Chilometri ............ 128.5
Tariffa al km ......... 0.42
Rimborso .............. 53.97
Sul modulo cartaceo ... 53,97 euro
------------------------------------------------------------
[OK] Richiesta registrata.
============================================================

ESEMPIO OUTPUT — km fuori intervallo
============================================================
TALENTHUB - Rimborso chilometrico
============================================================
Nome e cognome del consulente: Luca Fabbri
Veicolo (AUTO, MOTO, FURGONE): Furgone
Chilometri percorsi (da 1 a 1500): 1600
------------------------------------------------------------
[ERRORE] Chilometri: 1600 è fuori dall'intervallo ammesso (da 1 a 1500).
         Per un viaggio più lungo compilate una richiesta per tratta.
------------------------------------------------------------
[!] Richiesta NON registrata: 1 dato da correggere.
============================================================

ESEMPIO OUTPUT — tre errori insieme
============================================================
TALENTHUB - Rimborso chilometrico
============================================================
Nome e cognome del consulente: marco
Veicolo (AUTO, MOTO, FURGONE): bici
Chilometri percorsi (da 1 a 1500): trenta
------------------------------------------------------------
[ERRORE] Consulente: 'marco' è una parola sola.
         Scrivete nome e cognome.
[ERRORE] Veicolo: 'BICI' non ha una tariffa.
         Scrivete uno di questi: AUTO, MOTO, FURGONE.
[ERRORE] Chilometri: 'trenta' non è un numero.
         Scrivetelo in cifre, per esempio 128,5.
------------------------------------------------------------
[!] Richiesta NON registrata: 3 dati da correggere.
============================================================
"""

# Scrivi il tuo codice qui
