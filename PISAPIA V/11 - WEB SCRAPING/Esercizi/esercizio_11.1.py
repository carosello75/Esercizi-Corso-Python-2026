"""
ESERCIZIO 11.1 — Il primo sguardo al catalogo   ⭐ (facile)

CASO D'USO REALE
Giulia ricopia a mano i prodotti del catalogo NovaStore. Prima di
automatizzare vuole sapere che cosa c'è nella prima pagina, e perché i
prezzi che vede sono uno di più dei prodotti.

ARGOMENTI TEORICI: Cap. 3-5 (HTML, albero, find/find_all), Cap. 7.4
(class è una lista)

PRIMA DI COMINCIARE
La libreria si installa una volta sola, dal terminale di PyCharm:
    python -m pip install beautifulsoup4
e si verifica con
    python -c "import bs4; print(bs4.__version__)"
Si lavora sulla pagina SALVATA su disco, non sul sito: niente rete.

ISTRUZIONI
Ingresso: giorno_11/dati/novastore/catalogo/pagina_1.html. Cartella dei
dati: Path(__file__).resolve().parent.parent / "dati". Parser
"html.parser".

Uscita: il formato dell'ESEMPIO OUTPUT. Titolo e intestazione della
pagina; una riga per scheda prodotto (codice, nome, categoria, stato); i
conteggi per categoria con una barra di "#"; i prezzi contati nella pagina
e dentro le schede; per il prezzo che sta fuori dalle schede, il percorso
nell'albero dal tag main fino a lui, il prodotto in offerta e la scheda a
cui corrisponde; lo stesso percorso per il prezzo della prima scheda.

Vincoli:
- ogni campo si cerca dentro la sua scheda, non nella pagina;
- codice e categoria vengono dagli attributi data-*, lo stato dalla
  classe "esaurito";
- i prezzi NON si stampano: la conversione è materia del 11.2;
- se il file non c'è, un messaggio [ERRORE] con il solo nome del file.

SE HAI FINITO PRIMA (opzionale)
- Confrontate, scheda per scheda, la disponibilità scritta nel testo con
  la classe "esaurito", e segnalate le schede in cui non concordano.
- Contate i tag <a> della pagina e quanti stanno dentro le schede: la
  differenza è la navigazione del sito (Cap. 5.2 e 5.4).

ESEMPIO OUTPUT
======================================================================
NOVASTORE - Primo sguardo al catalogo
======================================================================
Pagina ............... pagina_1.html
Titolo ............... NovaStore - Catalogo, pagina 1 di 3
Intestazione ......... Catalogo prodotti
----------------------------------------------------------------------
 N  CODICE    NOME                     CATEGORIA     STATO
 1  NS-2001   Cuffie wireless          AUDIO         disponibile
 2  NS-2002   Tastiera meccanica       INFORMATICA   disponibile
 3  NS-2003   Monitor 4K 32 pollici    VIDEO         disponibile
 4  NS-2004   Cavo USB-C 2 m           ACCESSORI     disponibile
 5  NS-2005   Casse bluetooth          AUDIO         ESAURITO
 6  NS-2006   Mouse wireless           INFORMATICA   disponibile
----------------------------------------------------------------------
Schede prodotto ...... 6
Esauriti ............. 1 (NS-2005)
PER CATEGORIA
AUDIO           2  ##
INFORMATICA     2  ##
VIDEO           1  #
ACCESSORI       1  #
----------------------------------------------------------------------
I PREZZI
Prezzi nella pagina .. 7
Prezzi nelle schede .. 6
Fuori dalle schede ... 1
  percorso: main > aside.offerta-giorno > p > span.prezzo
  in offerta: Mouse wireless, cioè la scheda NS-2006
Prezzo della scheda 1:
  percorso: main > ul.catalogo > li.prodotto > span.prezzo
======================================================================
"""

# Scrivi il tuo codice qui
