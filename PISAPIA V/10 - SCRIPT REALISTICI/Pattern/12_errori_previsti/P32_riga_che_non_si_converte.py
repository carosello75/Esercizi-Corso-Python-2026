"""
P32 — La riga che non si converte: try dentro il ciclo, scarti per tipo,
    assert che chiude i conti

Catalogo dei pattern, Giorno 10 — capitolo 12, Gli errori previsti
Teoria: TEORIA_GIORNO_10.md §12.1

IN SINTESI
Converte i campi riga per riga dentro un try interno al ciclo, conta gli
scarti per tipo di eccezione e chiude i conti con un assert.

DESCRIZIONE
Il file crea ordini_lotto.txt con righe codice;quantita;prezzo, fra cui una
quantità in lettere e un prezzo vuoto. Il programma lo apre con with open,
scorre enumerate(f, 1) contando le righe lette e spezza ogni riga sul ;;
dentro un try converte la quantità con int() e il prezzo con float(). Su
ValueError incrementa scarti_per_tipo alla chiave type(e).__name__, stampa
il messaggio dell'eccezione con il numero di riga e prosegue con continue;
altrimenti accoda l'importo. Stampa infine lette, buone e scartate, il
totale di 385.40, e verifica con un assert che i conti tornino.

LO SCHEMA
Lo schema sta qui sotto, subito dopo questa docstring, come blocco
commentato: è uno stampo, non un programma, e non ha output. Si copia nel
proprio script, si tolgono i commenti (Ctrl+/ in PyCharm, Cmd+/ su Mac) e si
cambiano solo le righe marcate # <-- adattare.

IN AZIONE
Il codice eseguibile di questo file è l'In azione: lanciatelo, e l'output
deve essere quello di ESEMPIO OUTPUT in fondo a questa docstring.

VARIANTI
else: al posto del continue (Giorno 09 §10.1): il calcolo va nel ramo del
try riuscito, e il try resta stretto. Gli scarti anche su file, con numero
di riga e motivo: P29.

ERRORI TIPICI
- Il try che abbraccia anche il calcolo → un difetto del programma
  registrato come riga scartata: E7.

- Le righe vuote saltate senza contarle → l'assert scatta su un file sano
  (Giorno 09 §14.4).

DA DOVE VIENE
Giorno 05 §10.2 · Giorno 07 §12.2 · Giorno 09 §4.5, §5.4, §9.6, §12.3,
§14.4, §15.4

DOVE SI USA NEGLI ESERCIZI
10.10, 10.11, casa_10.3

ERRORI TIPICI DELLA GIORNATA COLLEGATI (teoria, capitolo 14)
- E7 — Il try troppo largo: un difetto del programma registrato come riga
  scartata

ESEMPIO OUTPUT
[!] riga 2: invalid literal for int() with base 10: 'due'
[!] riga 4: could not convert string to float: ''
Lette 6, buone 4, scartate 2: {'ValueError': 2}
Totale ordini buoni: 385.40
"""

# ==========================================================================
# LO SCHEMA — lo stampo da copiare. Non si esegue: è commentato.
# ==========================================================================
# buoni = []
# scarti_per_tipo = {}
# for campi in righe:  # <-- adattare: le righe gia' spezzate
#     # Blocco try ristretto alle conversioni, le sole istruzioni che il
#     # dato in ingresso puo' far fallire.
#     try:
#         valore = float(campi[1])  # <-- adattare
#     except (ValueError, IndexError) as e:
#         # Nome della classe d'eccezione come chiave di un contatore (P17).
#         tipo = type(e).__name__
#         scarti_per_tipo[tipo] = scarti_per_tipo.get(tipo, 0) + 1
#         continue
#     # Calcolo fuori dal try: un'eccezione qui e' un difetto del programma
#     # e deve interrompere l'esecuzione, non diventare uno scarto.
#     buoni.append((campi[0], valore))  # <-- adattare
# assert len(righe) == len(buoni) + sum(scarti_per_tipo.values()), "righe perse"


# ==========================================================================
# IN AZIONE — lo schema su un caso del corso. Si esegue.
# ==========================================================================
from pathlib import Path

PERCORSO = Path("ordini_lotto.txt")
PERCORSO.write_text(
    "NS-1101;2;49.90\n"
    "NS-1102;due;9.90\n"
    "NS-1103;1;219.00\n"
    "NS-1104;3;\n"
    "NS-1105;1;27.00\n"
    "NS-1106;4;9.90\n",
    encoding="utf-8",
)

lette = 0
importi = []
scarti_per_tipo = {}
with open(PERCORSO, encoding="utf-8") as f:
    for numero, riga in enumerate(f, 1):
        lette += 1
        codice, quantita_testo, prezzo_testo = riga.rstrip("\n").split(";")
        # 1. try ristretto a int() e float(): l'eccezione attesa e' ValueError
        #    su un campo non numerico o vuoto.
        try:
            quantita = int(quantita_testo)
            prezzo = float(prezzo_testo)
        except ValueError as e:
            # 2. type(e).__name__ fornisce il nome della classe come stringa,
            #    usato come chiave del contatore degli scarti.
            tipo = type(e).__name__
            scarti_per_tipo[tipo] = scarti_per_tipo.get(tipo, 0) + 1
            print(f"[!] riga {numero}: {e}")
            continue
        # 3. Calcolo fuori dal try: un suo errore segnalerebbe un difetto del
        #    programma, non un dato sbagliato.
        importi.append(quantita * prezzo)

scartate = sum(scarti_per_tipo.values())
print(f"Lette {lette}, buone {len(importi)}, scartate {scartate}: {scarti_per_tipo}")
print(f"Totale ordini buoni: {sum(importi):.2f}")
# 4. Invariante di conservazione (Giorno 09 §14.4): ogni riga letta e'
#    buona o scartata. Con questi dati l'assert non scatta.
assert lette == len(importi) + scartate, "righe perse nel conto"

# TRABOCCHETTO: spostate il try fuori dal for (e togliete il continue): la
#   riga 2 ferma la lettura, "Lette 2, buone 1, scartate 1", e l'assert NON
#   scatta, perche' i conti delle righe lette tornano. Le quattro mai lette
#   non le conta nessuno.
