"""
P5 — Il numero scritto all'italiana: virgola, conversione, centesimi
    arrotondati

Catalogo dei pattern, Giorno 10 — capitolo 3, L'ingresso: dal testo grezzo al dato
Teoria: TEORIA_GIORNO_10.md §3.2

IN SINTESI
Converte in float un importo scritto all'italiana, togliendo i punti delle
migliaia solo quando il testo contiene la virgola.

DESCRIZIONE
Il file definisce converti_importo(), che riceve una stringa, toglie gli
spazi e, solo se contiene la virgola, rimuove i punti e cambia la virgola in
punto; float() sta in un try che rilancia un ValueError con il testo
originale. Accanto, converti_sbagliato() toglie i punti sempre. Un for
converte tre importi con entrambe e stampa i risultati affiancati: sulla
terza riga 12.50 diventa 1250.00. Il secondo esempio riscrive l'importo come
1250,00 con .replace(), calcola 1250 centesimi con round() e produce
1.250,00 in tre sostituzioni con un carattere d'appoggio.

LO SCHEMA
La regola in una riga: se c'è la virgola, prima via i punti delle migliaia,
poi la virgola diventa punto. Se la virgola non c'è, il testo resta com'è.

Lo schema sta qui sotto, subito dopo questa docstring, come blocco
commentato: è uno stampo, non un programma, e non ha output. Si copia nel
proprio script, si tolgono i commenti (Ctrl+/ in PyCharm, Cmd+/ su Mac) e si
cambiano solo le righe marcate # <-- adattare.

IN AZIONE
Il codice eseguibile di questo file è l'In azione: lanciatelo, e l'output
deve essere quello di ESEMPIO OUTPUT in fondo a questa docstring.

VARIANTI
Il ritorno all'italiana in uscita, e i centesimi interi.

ERRORI TIPICI
- Togliere i punti sempre: "12.50" diventa 1250.0 in silenzio (nel codice
  qui sotto). Rimedio: la condizione if "," in pulito.

- Le due sostituzioni in ordine inverso, prima la virgola e poi i punti: il
  secondo replace() toglie anche il punto decimale appena messo, e
  "1.250,00" diventa 125000.0. Di nuovo nessun errore, cento volte tanto.

DA DOVE VIENE
Giorno 02 §7.3, §7.4, §12.3, §12.4 · Giorno 03 §5.4, §6.4 · Giorno 04 §13.5
· Giorno 09 §6.1, §11.5

DOVE SI USA NEGLI ESERCIZI
10.2, 10.3, casa_10.1, casa_10.3

ESEMPIO OUTPUT
    12,50 ->    12.50   senza la regola:    12.50
 1.250,00 ->  1250.00   senza la regola:  1250.00
    12.50 ->    12.50   senza la regola:  1250.00
1250,00
1250 centesimi
1.250,00
"""

# ==========================================================================
# LO SCHEMA — lo stampo da copiare. Non si esegue: è commentato.
# ==========================================================================
# testo = "1.250,00"                                   # <-- adattare
# pulito = testo.strip()
# if "," in pulito:
#     # Ordine vincolante: prima si rimuovono i separatori delle migliaia, poi
#     # la virgola decimale diventa punto, il formato atteso da float().
#     pulito = pulito.replace(".", "").replace(",", ".")
# importo = float(pulito)


# ==========================================================================
# IN AZIONE — lo schema su un caso del corso. Si esegue.
# ==========================================================================
def converti_importo(testo):
    """Restituisce l'importo come float. Solleva ValueError se non e' un numero."""
    pulito = testo.strip()
    # Il punto e' separatore delle migliaia solo in presenza della virgola:
    # senza virgola il testo e' gia' nel formato di float() e resta intatto.
    if "," in pulito:
        pulito = pulito.replace(".", "").replace(",", ".")
    try:
        return float(pulito)
    except ValueError as e:
        raise ValueError(f"importo non numerico: '{testo}'") from e


def converti_sbagliato(testo):
    """Toglie i punti SEMPRE, anche quando la virgola non c'e'."""
    return float(testo.replace(".", "").replace(",", "."))


# TRABOCCHETTO: "12.50" scritto all'inglese perde il punto decimale e
#   diventa 1250.0, senza alcuna eccezione. La terza riga lo mostra: un
#   valore cento volte tanto.
for testo in ["12,50", "1.250,00", "12.50"]:
    giusto = converti_importo(testo)
    sbagliato = converti_sbagliato(testo)
    print(f"{testo:>9} -> {giusto:>8.2f}   senza la regola: {sbagliato:>8.2f}")


# ==========================================================================
# ANCORA IN AZIONE — l'esempio che la teoria aggiunge alla scheda.
# ==========================================================================
importo = 1250.0
# 1. Conversione inversa: la f-string produce il punto decimale, poi
#    .replace() lo sostituisce con la virgola.
print(f"{importo:.2f}".replace(".", ","))
# 2. Centesimi interi: round() elimina l'errore di rappresentazione
#    binaria dei float, e i conti sugli importi diventano esatti.
centesimi = round(12.5 * 100)
print(centesimi, "centesimi")
# TRABOCCHETTO: con le migliaia, :,.2f produce "1,250.00", e un solo
#   .replace() non puo' scambiare due caratteri fra loro: servono tre
#   passi, con un carattere d'appoggio.
italiano = f"{importo:,.2f}".replace(",", "_").replace(".", ",").replace("_", ".")
print(italiano)
