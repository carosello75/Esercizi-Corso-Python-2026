"""
ESERCIZIO 01.8 — Mini-progetto: Apertura conto   ⭐⭐⭐⭐ (progetto)

CASO D'USO REALE
In filiale, alla Banca Meridiana, l'apertura di un conto corrente finisce
con un foglio che il cliente porta a casa: chi è l'intestatario, quale
conto ha aperto, quanto costa in un anno, quanto ha versato e quanto ha
sul conto adesso. Oggi quel foglio lo compila l'operatore copiando da tre
schermate diverse, e i costi del primo anno li scrive a memoria. Voi
scrivete il programma che lo stampa sempre uguale, con i conti fatti.


ISTRUZIONI
1) Il file deve avere la struttura completa: docstring di modulo che
   spiega a cosa serve, costanti in maiuscolo, def main() con la sua
   docstring di una riga.
2) In costante vanno i valori del listino, uguali per tutti i clienti:
   canone mensile (3.50), mesi in un anno (12), imposta di bollo annua
   (34.20), costo della carta di debito (12.00), più le due righe di
   separazione.
3) In variabili, dentro main(), i dati di questa apertura: intestatario,
   filiale, IBAN, nome del prodotto, versamento iniziale.
4) Calcolate: il canone annuo, il totale dei costi del primo anno, e il
   saldo disponibile dopo l'addebito del primo canone mensile.
5) Stampate il documento in tre sezioni separate da righe: anagrafica,
   costi del primo anno, movimenti di apertura. I valori vanno
   incolonnati tutti alla stessa colonna.
6) Chiudete con una riga vuota e una nota che contenga la parola
   "provvisorio" fra virgolette doppie visibili nell'output.

DATI DI PARTENZA
     intestatario = "Elena Marino"
     filiale = "Battipaglia - Agenzia 2"
     iban = "IT60X0542811101000000123456"
     prodotto = "Conto Base"
     versamento_iniziale = 1500.00

SUGGERIMENTI
- Partite dall'ossatura vuota: docstring, costanti, def main().
  Poi riempite. Chi comincia dai print si perde.
- Le righe con un valore di testo si costruiscono con il +, quelle con
  un numero con la virgola: sono due incolonnamenti diversi e vanno
  contati separatamente. Nell'etichetta di una riga con la virgola gli
  spazi sono uno in meno.
- Il canone annuo non si scrive: si calcola moltiplicando il canone
  mensile per i mesi.
- Il saldo disponibile è il versamento meno il primo canone mensile.
- Se una colonna vi esce storta di un carattere, contate gli spazi:
  quasi sempre è lo spazio automatico della virgola.

SE HAI FINITO PRIMA (opzionale)
- Aggiungete una quarta sezione con il costo mensile medio del conto nel
  primo anno, cioè il totale dei costi diviso i mesi. Guardate quante
  cifre decimali escono e provate a spiegare a un collega perché.
- Rifate il documento cambiando SOLO le costanti, come se la banca
  avesse aggiornato il listino: canone 4.00, carta 15.00. Il programma
  non va toccato in nessun altro punto.

ESEMPIO OUTPUT
==================================================
BANCA MERIDIANA - APERTURA CONTO CORRENTE
==================================================
Intestatario:            Elena Marino
Filiale:                 Battipaglia - Agenzia 2
IBAN:                    IT60X0542811101000000123456
Prodotto:                Conto Base
--------------------------------------------------
COSTI DEL PRIMO ANNO
Canone mensile:          3.5
Canone annuo:            42.0
Imposta di bollo:        34.2
Carta di debito:         12.0
Totale primo anno:       88.2
--------------------------------------------------
MOVIMENTI DI APERTURA
Versamento iniziale:     1500.0
Addebito primo canone:   3.5
Saldo disponibile:       1496.5
==================================================

Documento "provvisorio": fa fede la contabile dello sportello.
"""

# Scrivi il tuo codice qui
