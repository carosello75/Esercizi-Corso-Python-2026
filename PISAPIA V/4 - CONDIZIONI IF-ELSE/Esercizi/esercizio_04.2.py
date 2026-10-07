"""
ESERCIZIO 04.2 — Sconto a soglie   ⭐ (facile)

CASO D'USO REALE
NovaStore ha lanciato la campagna "più spendi, meno paghi". Alla cassa
il commesso deve applicare lo sconto giusto in base al totale della
spesa: quattro fasce, quattro percentuali. Nella prima settimana sono
stati applicati sconti sbagliati per una quarantina di scontrini,
sempre nella stessa direzione: la percentuale più bassa. Il motivo lo
scoprirete scrivendo il programma, ed è lo stesso motivo per cui questo
esercizio esiste.

Il responsabile del punto vendita ha chiesto una cosa in più: che lo
scontrino dica quanto manca al cliente per salire di fascia. È la frase
che fa tornare indietro a prendere l'ultimo articolo, e alla cassa vale
più dello sconto.


ISTRUZIONI
Entra un dato: il totale della spesa in euro, che alla cassa si digita
all'italiana, con la virgola.

Esce lo scontrino della campagna, nel formato dell'ESEMPIO OUTPUT:
spesa, fascia raggiunta, sconto applicato, risparmio, totale da pagare
e — quando sopra c'è ancora una fascia — quanto manca a raggiungerla.

Le fasce della campagna sono il dato di partenza:
    spesa sotto 50.00 euro ............ fascia BASE,    sconto 0%
    da 50.00 a 99.99 euro ............. fascia BRONZO,  sconto 5%
    da 100.00 a 199.99 euro ........... fascia ARGENTO, sconto 10%
    da 200.00 euro in su .............. fascia ORO,     sconto 15%

Requisiti:
- struttura standard: docstring, costanti, main(), guard;
- le tre soglie e le quattro percentuali in costante, scritte come
  frazioni (0.05 per il 5%): nel corpo del programma non compare
  nessun numero della campagna;
- i rami decidono e non stampano: lo scontrino esce da un punto solo,
  e risparmio, totale e mancante li calcola il programma;
- nella fascia più alta la riga del mancante non esce: sopra non c'è
  niente da raggiungere.

SUGGERIMENTI
- L'ordine dei rami non è indifferente. Scriveteli dal più basso al più
  alto, passate 250.00 e guardate quale fascia esce: il capitolo 6.1
  racconta gli stessi quaranta scontrini.
- I bordi delle fasce sono i valori pericolosi. Provate 49.99, 50.00,
  99.99, 100.00, 199.99, 200.00 prima di dire che funziona.
- La fascia più alta è il caso che rompe la simmetria: anche lì i rami
  devono assegnare le stesse variabili degli altri, ma una di quelle
  variabili non ha niente da dire. Il capitolo 11.3 mostra come si
  riconosce un campo rimasto vuoto.

SE HAI FINITO PRIMA (opzionale)
- Aggiungete una quinta fascia PLATINO sopra i 500.00 euro con il 20%
  di sconto, e verificate che vi basti aggiungere un ramo solo, nel
  punto giusto.
- Segnalate le spese sospette: alla cassa di un negozio un totale sopra
  i 5.000 euro è quasi sempre un errore di battitura.

ESEMPIO OUTPUT
Totale della spesa in euro: 137,50
==================================================
NOVASTORE - CASSA
==================================================
Spesa:              137.50 euro
Fascia:            ARGENTO
Sconto applicato:  10%
--------------------------------------------------
Risparmio:           13.75 euro
Totale da pagare:   123.75 euro
--------------------------------------------------
Alla fascia ORO mancano 62.50 euro.
==================================================

"""

# Scrivi il tuo codice qui
