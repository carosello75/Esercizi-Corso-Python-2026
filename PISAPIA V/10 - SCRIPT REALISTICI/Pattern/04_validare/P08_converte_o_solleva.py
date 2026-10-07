"""
P8 — La funzione che converte o solleva: raise ValueError con il messaggio
    giusto

Catalogo dei pattern, Giorno 10 — capitolo 4, Validare
Teoria: TEORIA_GIORNO_10.md §4.2

IN SINTESI
Converte un testo nel valore atteso o solleva ValueError con un messaggio
preciso, lasciando al chiamante la scelta della reazione.

DESCRIZIONE
Il file definisce converti_importo(), che riceve una stringa, la normalizza
come in P5 e la converte con float() in un try stretto che rilancia
ValueError con il testo originale; un secondo raise ValueError respinge gli
importi negativi. Restituisce un float senza stampare. Il ciclo sui tre
importi mette nel try la sola chiamata, stampa il messaggio dell'eccezione e
passa oltre con continue; l'accumulo in totale avviene fuori dal blocco
protetto. Escono un [OK], due [ERRORE] e il totale accettato di 12.50.

LO SCHEMA
Lo schema sta qui sotto, subito dopo questa docstring, come blocco
commentato: è uno stampo, non un programma, e non ha output. Si copia nel
proprio script, si tolgono i commenti (Ctrl+/ in PyCharm, Cmd+/ su Mac) e si
cambiano solo le righe marcate # <-- adattare.

IN AZIONE
Il codice eseguibile di questo file è l'In azione: lanciatelo, e l'output
deve essere quello di ESEMPIO OUTPUT in fondo a questa docstring.

VARIANTI
- converti_intero() dello schema: la stessa forma per quantità, colli, anni.

- Due chiamanti: lo sportello la mette in un ciclo di richiesta (P9), il
  caricatore scarta la riga e la conta (P32).

ERRORI TIPICI
- print() al posto di raise: il chiamante non riceve più nessun segnale. Nel
  ramo dell'importo negativo la funzione stampa l'avviso e restituisce
  comunque -3.0, che entra nel totale senza errori (Totale accettato: 9.50);
  nel ramo non numerico prosegue fino al controllo importo < 0 con importo
  mai assegnato, e si ferma con UnboundLocalError.

- raise "messaggio" senza il tipo (nel codice qui sotto): TypeError.

DA DOVE VIENE
Giorno 06 §5.1, §6.2 · Giorno 09 §8.3, §8.8, §11.2, §11.3, §11.5, §11.6

DOVE SI USA NEGLI ESERCIZI
10.7, 10.12

ESEMPIO OUTPUT
[OK] 12.50
[ERRORE] importo non numerico: 'trenta'
[ERRORE] importo negativo: '-3'
Totale accettato: 12.50
"""

# ==========================================================================
# LO SCHEMA — lo stampo da copiare. Non si esegue: è commentato.
# ==========================================================================
# def converti_intero(testo, minimo, massimo):
#     """Restituisce l'intero; solleva ValueError per forma o intervallo."""
#     pulito = testo.strip()
#     if not pulito.isdecimal():
#         raise ValueError(f"'{testo}' non è un numero intero")      # <-- adattare
#     valore = int(pulito)
#     if not minimo <= valore <= massimo:
#         raise ValueError(f"{valore} fuori intervallo: da {minimo} a {massimo}")
#     return valore
#
#
# # Lato chiamante: il try racchiude solo la chiamata che puo' sollevare,
# # cosi' l'except non intercetta errori nati in altre righe.
# try:
#     colli = converti_intero("7", 1, 50)                            # <-- adattare
# except ValueError as e:
#     print(f"[ERRORE] {e}")


# ==========================================================================
# IN AZIONE — lo schema su un caso del corso. Si esegue.
# ==========================================================================
def converti_importo(testo):
    """Restituisce l'importo come float >= 0. Solleva ValueError se non va."""
    pulito = testo.strip()
    if "," in pulito:
        pulito = pulito.replace(".", "").replace(",", ".")
    try:
        importo = float(pulito)
    except ValueError as e:
        raise ValueError(f"importo non numerico: '{testo}'") from e
    # Controllo di dominio aggiunto rispetto a P5: un importo negativo e'
    # un float valido, ma non e' ammesso come rimborso.
    if importo < 0:
        raise ValueError(f"importo negativo: '{testo}'")
    return importo


totale = 0.0
for testo in ["12,50", "trenta", "-3"]:
    # try stretto: protegge la sola chiamata; accumulo e stampa restano fuori,
    # perche' vanno eseguiti solo dopo una conversione riuscita.
    try:
        importo = converti_importo(testo)
    except ValueError as e:
        print(f"[ERRORE] {e}")
        continue
    totale += importo
    print(f"[OK] {importo:.2f}")
print(f"Totale accettato: {totale:.2f}")

# TRABOCCHETTO: raise "importo negativo" (una stringa, senza il tipo) non
#   solleva l'eccezione prevista: si ferma con TypeError: exceptions must
#   derive from BaseException. raise accetta solo istanze di eccezione.
