"""
P20 — Filtrare e partizionare: i buoni in una lista, gli scarti con il
    motivo in un'altra

Catalogo dei pattern, Giorno 10 — capitolo 8, Cercare, filtrare, ordinare
Teoria: TEORIA_GIORNO_10.md §8.2

IN SINTESI
Divide un insieme di elementi in due liste disgiunte, i buoni e gli scarti
con il loro motivo, e verifica con un assert che nessuno vada perso.

DESCRIZIONE
Il file definisce le zone ammesse in ZONE, le richieste testuali zona;peso
in RICHIESTE e le due liste vuote buone e scarti. Per ogni richiesta,
split(";") separa i campi, motivo riparte dalla stringa vuota e una catena
if/elif lo valorizza se la zona non è in ZONE o se il peso, tolto un punto,
non supera isdecimal(). La richiesta va negli scarti con la sua causa,
oppure fra le buone come tupla (zona, float(peso_testo)). Il programma
stampa le buone, gli scarti incolonnati e, dopo un assert sulla somma delle
lunghezze, il conteggio 4 = 2 + 2.

LO SCHEMA
Lo schema sta qui sotto, subito dopo questa docstring, come blocco
commentato: è uno stampo, non un programma, e non ha output. Si copia nel
proprio script, si tolgono i commenti (Ctrl+/ in PyCharm, Cmd+/ su Mac) e si
cambiano solo le righe marcate # <-- adattare.

IN AZIONE
Il codice eseguibile di questo file è l'In azione: lanciatelo, e l'output
deve essere quello di ESEMPIO OUTPUT in fondo a questa docstring.

VARIANTI
Filtro senza scarti (if prezzo > SOGLIA: e basta), o continue quando lo
scarto va solo contato (Giorno 05 §10.2); i controlli spostati in un
validatore che restituisce il motivo, P24, e il ciclo si riduce a tre righe.

ERRORI TIPICI
- .remove() sulla lista che si sta scorrendo (Giorno 07 E6) → SUD;venti
  viene saltata e resta fra le buone senza essere mai stata controllata.

- Due if separati al posto di if/elif → il secondo controllo gira anche
  sulla riga già scartata e ne sovrascrive il motivo.

DA DOVE VIENE
Giorno 04 §5.2, §13.5 · Giorno 05 §10.2 · Giorno 07 §6.2, E6 · Giorno 08
§9.3, §9.4, §11.4

DOVE SI USA NEGLI ESERCIZI
10.3, 10.5, 10.6

ESEMPIO OUTPUT
Buone: [('NORD', 12.5), ('CENTRO', 7.2)]
[!] ESTERO;3    zona sconosciuta: ESTERO
[!] SUD;venti   peso non numerico: 'venti'
Richieste 4 = buone 2 + scartate 2
"""

# ==========================================================================
# LO SCHEMA — lo stampo da copiare. Non si esegue: è commentato.
# ==========================================================================
# buoni = []
# scarti = []
# for elemento in elementi:  # <-- adattare
#     # motivo reinizializzato a ogni iterazione: e' stato del singolo
#     # elemento. La catena if/elif registra solo il primo controllo fallito.
#     motivo = ""
#     if not controllo_1(elemento):  # <-- adattare: i controlli del caso
#         motivo = "primo motivo"
#     elif not controllo_2(elemento):  # <-- adattare
#         motivo = "secondo motivo"
#     if motivo:
#         scarti.append((elemento, motivo))
#     else:
#         buoni.append(elemento)
# assert len(buoni) + len(scarti) == len(elementi), "elementi persi nel conto"


# ==========================================================================
# IN AZIONE — lo schema su un caso del corso. Si esegue.
# ==========================================================================
ZONE = ["NORD", "CENTRO", "SUD", "ISOLE"]
RICHIESTE = ["NORD;12.5", "ESTERO;3", "SUD;venti", "CENTRO;7.2"]

buone = []
scarti = []
for richiesta in RICHIESTE:
    zona, peso_testo = richiesta.split(";")
    # 1. Reinizializzazione per iterazione: senza, il motivo del giro
    #    precedente sopravvive e classifica la riga successiva.
    motivo = ""
    if zona not in ZONE:
        motivo = f"zona sconosciuta: {zona}"
    # 2. Controllo di forma senza try: tolto al piu' un punto decimale,
    #    isdecimal() accetta solo cifre, e rifiuta segno e stringa vuota.
    elif not peso_testo.replace(".", "", 1).isdecimal():
        motivo = f"peso non numerico: '{peso_testo}'"
    # 3. Unico punto di smistamento: ogni elemento entra in una sola lista,
    #    condizione che rende verificabile l'assert finale.
    if motivo:
        scarti.append((richiesta, motivo))
    else:
        buone.append((zona, float(peso_testo)))

print("Buone:", buone)
for richiesta, motivo in scarti:
    print(f"[!] {richiesta:<12}{motivo}")
assert len(buone) + len(scarti) == len(RICHIESTE), "richieste perse"
print(f"Richieste {len(RICHIESTE)} = buone {len(buone)} + scartate {len(scarti)}")

# TRABOCCHETTO: con motivo = "" scritto una volta sola, prima del for, il
#   motivo di "SUD;venti" resta attaccato al giro dopo: CENTRO;7.2 finisce
#   fra gli scarti con il peso di un'altra riga. Buone 1, scarti 3.
