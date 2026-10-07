"""
ESERCIZIO 04.4 — Riparare la cassa   ⭐⭐ (media)

CASO D'USO REALE
Avete già scritto la cassa di NovaStore (esercizio 03.2). Funziona
benissimo, a una condizione: che chi la usa digiti esattamente quello
che vi aspettate. Il giorno dopo la cassiera ha scritto "tre" nella
quantità e il programma si è chiuso con sei righe rosse davanti a un
cliente in fila. Oggi non riscrivete la cassa: le insegnate a dire di
no.

Nel frattempo è arrivata anche la tessera fedeltà, che vale il 5% di
sconto. Alla cassa si chiede a voce, si registra con un si o con un no,
e non c'è terza risposta: anche quella va controllata, perché una "s"
digitata di fretta non è un si.

Questo è l'esercizio che chiude il cerchio aperto l'ultima volta, ed è quello
da fare anche se oggi salterete tutto il resto.

ISTRUZIONI
Entrano quattro dati digitati alla cassa: prezzo unitario, quantità,
tessera fedeltà (si/no), contanti ricevuti.

Esce una delle due cose, nel formato dell'ESEMPIO OUTPUT: lo scontrino
completo, oppure un solo messaggio d'errore seguito dalla riga
"Nessuno scontrino emesso. Ripetere l'operazione.". Intestazione e riga
di chiusura escono in tutti e due i casi.

Requisiti:
- struttura standard: docstring, costanti, main(), guard;
- in costante: aliquota IVA (0.22), sconto tessera (0.05), quantità
  massima per scontrino (100), risposte ammesse e righe di
  separazione;
- nessun dato viene convertito prima di essere stato controllato: il
  programma non deve potersi fermare da solo, qualunque cosa venga
  digitata;
- i controlli, in quest'ordine di precedenza: prezzo numerico,
  quantità numerica, risposta sulla tessera ammessa, contanti
  numerici, prezzo maggiore di zero, quantità almeno 1, quantità entro
  il massimo, contanti sufficienti a coprire il totale;
- l'errore si stampa una volta sola, da un punto solo del programma,
  qualunque sia il controllo fallito, e dice che cosa non va e che
  cosa fare, in italiano e senza nominare Python (capitolo 13.8);
- lo sconto della tessera abbassa l'imponibile, quindi si applica
  prima dell'IVA; sullo scontrino compare la percentuale davvero
  applicata, che senza tessera è zero.

SUGGERIMENTI
- Il totale serve per controllare i contanti, e si può calcolare solo
  dopo che i testi sono stati riconosciuti come numeri: mai prima.
- "si oppure no" è un controllo sui valori ammessi, non sulla forma del
  dato: il capitolo 13.7 lo tratta a parte dagli altri tre, e c'è un
  motivo. Attenzione a come si nega una condizione fatta di OPPURE, che
  è il trabocchetto del capitolo 8.5.
- Il campo lasciato in bianco e il numero scritto col segno meno sono
  già rifiutati dai controlli di forma del capitolo 13.4: provateli per
  crederci, e non aggiungete controlli che non servono.

SE HAI FINITO PRIMA (opzionale)
- Fate in modo che il messaggio d'errore ripeta anche quello che era
  stato digitato, così chi sta alla cassa vede l'errore senza dover
  rileggere il campo.
- Aggiungete il controllo che il resto non sia assurdo: se i contanti
  superano il totale di più di 500 euro, segnalatelo come possibile
  errore di battitura senza bloccare lo scontrino.

ESEMPIO OUTPUT — dati validi
Prezzo unitario in euro: 12,90
Quantità: 4
Tessera fedeltà? (si/no): si
Contanti ricevuti in euro: 70
==================================================
NOVASTORE - CASSA
==================================================
Prezzo unitario:    12.90 euro
Quantità:               4
Imponibile:         51.60 euro
Sconto tessera 5%:   2.58 euro
Imponibile netto:   49.02 euro
IVA 22%:            10.78 euro
--------------------------------------------------
Totale:             59.80 euro
Contanti:           70.00 euro
Resto:              10.20 euro
Scontrino emesso. Grazie e arrivederci.
==================================================

ESEMPIO OUTPUT — quantità non valida
Prezzo unitario in euro: 12,90
Quantità: tre
Tessera fedeltà? (si/no): si
Contanti ricevuti in euro: 70
==================================================
NOVASTORE - CASSA
==================================================
[ERRORE] La quantità deve essere un numero intero, senza decimali.
Nessuno scontrino emesso. Ripetere l'operazione.
==================================================

"""

# Scrivi il tuo codice qui
