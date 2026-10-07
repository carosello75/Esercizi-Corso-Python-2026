"""
ESERCIZIO 04.1 — Maggiore età allo sportello   ⭐ (facile)

CASO D'USO REALE
Allo sportello anagrafe del Comune di Villanova arriva ogni giorno
qualcuno che chiede un certificato. Se chi firma la domanda non ha
ancora compiuto diciotto anni, la domanda non è valida: serve la firma
di un genitore. Finora l'operatore lo controllava a mente, guardando la
data di nascita sul documento. Due volte in un mese è finita male, con
la pratica respinta e il cittadino tornato allo sportello per niente.
Oggi il controllo lo fa il programma.


ISTRUZIONI
Entrano tre dati, digitati di fretta mentre il cittadino è al bancone:
nome e cognome del richiedente, età in anni compiuti, documento
esibito.

Esce la scheda dello sportello, nel formato dell'ESEMPIO OUTPUT: i tre
dati raccolti e l'esito della verifica sulla firma; quando la firma non
è ammessa, anche quanti anni mancano per poterla apporre da soli.

Requisiti:
- struttura standard: docstring, costanti, main(), guard;
- maggiore età e righe di separazione in costante: il numero 18 non
  compare nel corpo del programma;
- gli anni mancanti li calcola il programma, non li chiede all'utente;
- i dati escono uniformati, con la spaziatura dell'esempio;
- intestazione e riga di chiusura escono in tutti i casi.

SUGGERIMENTI
- "Diciotto anni compiuti" e "più di diciotto anni" non sono la stessa
  frase e non sono lo stesso confronto. Il capitolo 6.3 mette i due a
  confronto proprio sul valore esatto della soglia.
- Anche il documento va uniformato prima di finire nella scheda, ma non
  tutti i modi di uniformare un testo reggono un apostrofo: provatene
  due e guardate l'esito (Giorno 03, capitolo 5.3).
- Il capitolo 3.5 mostra che cosa cambia fra una riga scritta a colonna
  zero e la stessa riga rientrata di quattro spazi. Sulla riga di
  chiusura la differenza si vede a occhio nudo nell'output.

SE HAI FINITO PRIMA (opzionale)
- Aggiungete un terzo caso: chi ha superato i 65 anni ha diritto alla
  precedenza in fila. Con due soli rami non ci sta: al capitolo 5 c'è
  la forma che serve.
- Segnalate le età implausibili: oltre 120 anni compiuti il dato non si
  registra, si fa riguardare il documento.

ESEMPIO OUTPUT
Nome e cognome: marta esposito
Età (anni compiuti): 17
Documento esibito: carta d'identità
==================================================
COMUNE DI VILLANOVA - SPORTELLO ANAGRAFE
==================================================
Richiedente:      Marta Esposito
Età dichiarata:   17
Documento:        CARTA D'IDENTITÀ
--------------------------------------------------
[!] FIRMA NON AMMESSA
Serve la firma di un genitore o di chi ne fa le veci.
Anni mancanti alla maggiore età: 1
==================================================

"""

# Scrivi il tuo codice qui
