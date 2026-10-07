"""
ESERCIZIO 10.1 — Le letture dei contatori   ⭐ (facile)

PATTERN USATI: P1, P2, P3, P6, P10, P15, P16, P25

CASO D'USO REALE
L'acquedotto di Villanova riceve le letture di otto utenze in un file di
testo. Giulia deve dire quanta acqua ha consumato ognuna, in che fascia
cade e quanto paga, senza rifare i conti a mano su un foglio.

Uscita a schermo, nel formato dell'ESEMPIO OUTPUT:
- la tabella delle utenze (consumo, fascia, importo) con la riga di totale;
- consumo medio, consumo massimo e minimo con l'utenza a cui appartengono;
- quante utenze per fascia, con tutte e tre le fasce anche se a zero;
- le utenze che consumano più della media.

Vincoli:
- consumo = lettura attuale - lettura precedente, in metri cubi (mc);
- la fascia si decide con la lista SOGLIE_CONSUMO: ogni limite è incluso
  nella sua fascia ("fino a 50" comprende 50), oltre l'ultimo è ALTA;
- importo = consumo x TARIFFA_M3, due decimali;
- nessun numero scritto dentro le formule: tutto dalle costanti.

DATI DI PARTENZA (copiateli così come sono)
     SOGLIE_CONSUMO = [(50, "BASE"), (120, "MEDIA")]
     FASCIA_OLTRE = "ALTA"
     TARIFFA_M3 = 1.20
     LARGHEZZA = 60

SE HAI FINITO PRIMA (opzionale)
- Una lettura attuale minore della precedente vuol dire contatore
  sostituito: segnalatela con [!] ed escludetela dai conti.
- Tariffa a scaglioni: i primi 50 mc a 1.20, i successivi a 1.60.
  Cambia l'importo di chi è in fascia MEDIA o ALTA, non degli altri.

PER RIUSARLO
Cambiate il nome del file, le soglie e la tariffa: lo stesso programma dà
il consumo di gas delle stesse utenze o i chilometri dei furgoni LogiSud
fra due rilevazioni del contachilometri.

ESEMPIO OUTPUT
============================================================
ACQUEDOTTO DI VILLANOVA - Consumi del periodo
============================================================
File letto: letture_contatori.txt (8 utenze)
------------------------------------------------------------
UTENZA  INTESTATARIO       CONSUMO  FASCIA       IMPORTO
VL-001  Rossi Anna              48  BASE           57.60
VL-002  Bianchi Marco           82  MEDIA          98.40
VL-003  Esposito Carla         131  ALTA          157.20
VL-004  Ferri Luigi             50  BASE           60.00
VL-005  Greco Paola            120  MEDIA         144.00
VL-006  Marino Ugo              21  BASE           25.20
VL-007  Conti Elisa            121  ALTA          145.20
VL-008  Rizzo Dario             69  MEDIA          82.80
------------------------------------------------------------
TOTALE                         642                770.40
------------------------------------------------------------
Consumo medio .............. 80.25 mc
Consumo massimo ............ 131 mc (VL-003 Esposito Carla)
Consumo minimo ............. 21 mc (VL-006 Marino Ugo)
------------------------------------------------------------
UTENZE PER FASCIA
BASE        3  ###
MEDIA       3  ###
ALTA        2  ##
------------------------------------------------------------
Sopra la media: 4 utenze (VL-002, VL-003, VL-005, VL-007)
============================================================
"""

# Scrivi il tuo codice qui
