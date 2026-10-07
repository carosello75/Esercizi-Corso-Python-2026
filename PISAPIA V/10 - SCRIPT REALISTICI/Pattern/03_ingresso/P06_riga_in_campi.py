"""
P6 — La riga in campi: .split(";"), conteggio dei campi, unpacking

Catalogo dei pattern, Giorno 10 — capitolo 3, L'ingresso: dal testo grezzo al dato
Teoria: TEORIA_GIORNO_10.md §3.3

IN SINTESI
Divide una riga delimitata in campi con .split(), ne verifica il numero
prima dell'unpacking e pulisce ogni campo singolarmente.

DESCRIZIONE
Il file definisce SEPARATORE, CAMPI_ATTESI e due righe di spedizione in
RIGHE. Un for divide ogni riga con .split(SEPARATORE) e confronta len(campi)
con il numero atteso: la riga con 2 campi viene segnalata con il conteggio e
saltata con continue. Sulla riga corretta l'unpacking assegna codice, zona e
peso, puliti uno per uno con .strip(), .upper() e float(), e la riga esce
come [OK] con il peso di 7.2 kg. In coda la prova del trabocchetto applica
.strip() alla riga intera e stampa ' SUD ' False.

LO SCHEMA
Lo schema sta qui sotto, subito dopo questa docstring, come blocco
commentato: è uno stampo, non un programma, e non ha output. Si copia nel
proprio script, si tolgono i commenti (Ctrl+/ in PyCharm, Cmd+/ su Mac) e si
cambiano solo le righe marcate # <-- adattare.

IN AZIONE
Il codice eseguibile di questo file è l'In azione: lanciatelo, e l'output
deve essere quello di ESEMPIO OUTPUT in fondo a questa docstring.

VARIANTI
- csv.reader(f, delimiter=";") quando un campo può contenere il separatore
  fra virgolette (Giorno 08 §9.6).

- Un campo che è un elenco: "python, sql".split(","), e .strip() sui pezzi.

ERRORI TIPICI
- Pulire la riga intera e non i campi (nel codice qui sotto): ' SUD ' resta
  sporco.

- L'unpacking prima del controllo: la riga corta ferma tutto con un
  ValueError. Il suo messaggio cambia fra le versioni di Python: nel report
  stampate il conteggio dei campi, come nel codice di questo file.

DA DOVE VIENE
Giorno 02 §10.3 · Giorno 03 §7.2, §7.3, §7.4, §7.5 · Giorno 07 §13.3 ·
Giorno 08 §9.1, §9.2, §9.6 · Giorno 09 §9.7

DOVE SI USA NEGLI ESERCIZI
10.1, 10.3, 10.4, casa_10.1, casa_10.2, casa_10.4

ESEMPIO OUTPUT
[OK] LS-2026-NA-0510 | SUD | 7.2 kg
[!] servono 3 campi, ne ha 2: LS-2026-MI-0042;NORD
' SUD ' False
"""

# ==========================================================================
# LO SCHEMA — lo stampo da copiare. Non si esegue: è commentato.
# ==========================================================================
# SEPARATORE = ";"
# CAMPI_ATTESI = 3                                     # <-- adattare
#
# riga = "valore uno ; valore due ; 3.5"               # <-- adattare
# campi = riga.split(SEPARATORE)
# # 1. Controllo della cardinalita' prima dell'unpacking: con un numero di
# #    campi diverso da CAMPI_ATTESI l'assegnazione solleverebbe ValueError.
# if len(campi) != CAMPI_ATTESI:
#     print(f"[!] servono {CAMPI_ATTESI} campi, ne ha {len(campi)}")
# else:
#     primo, secondo, terzo = campi                    # <-- adattare: i nomi
#     # 2. Pulizia per campo: ogni valore riceve la normalizzazione o la
#     #    conversione adatta al suo tipo.
#     primo = primo.strip()
#     secondo = secondo.strip().upper()
#     terzo = float(terzo)


# ==========================================================================
# IN AZIONE — lo schema su un caso del corso. Si esegue.
# ==========================================================================
SEPARATORE = ";"
CAMPI_ATTESI = 3
RIGHE = ["LS-2026-NA-0510 ; SUD ; 7.2", "LS-2026-MI-0042;NORD"]

for riga in RIGHE:
    campi = riga.split(SEPARATORE)
    # 1. Controllo della cardinalita' prima dell'unpacking: la riga corta
    #    viene rifiutata qui e continue passa alla successiva.
    if len(campi) != CAMPI_ATTESI:
        print(f"[!] servono {CAMPI_ATTESI} campi, ne ha {len(campi)}: {riga}")
        continue
    codice, zona, peso = campi
    # 2. Pulizia per campo: float() ignora gli spazi ai bordi, mentre le
    #    stringhe li conservano e vanno ripulite con .strip().
    codice = codice.strip()
    zona = zona.strip().upper()
    peso = float(peso)
    print(f"[OK] {codice} | {zona} | {peso} kg")

# TRABOCCHETTO: strip() sulla riga intera agisce sui bordi della riga, non
#   su quelli dei campi. Il secondo campo resta ' SUD ', e il confronto con
#   "SUD" fallisce.
zona_sporca = RIGHE[0].strip().split(SEPARATORE)[1]
print(f"'{zona_sporca}'", zona_sporca == "SUD")
