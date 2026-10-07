"""
P24 — Il validatore di record: return record, "" oppure return None, motivo

Catalogo dei pattern, Giorno 10 — capitolo 9, Funzioni che si riusano
Teoria: TEORIA_GIORNO_10.md §9.2

IN SINTESI
Valida i campi di un record e restituisce sempre due valori: il record
pulito e una stringa vuota, oppure None e il motivo dello scarto.

DESCRIZIONE
Il file definisce ZONE, CAMPI_ATTESI e PESO_MASSIMO, e la funzione
valida_spedizione(), che riceve una lista di campi e restituisce sempre una
coppia: (None, motivo) al primo controllo fallito, nell'ordine numero di
campi, zona normalizzata con strip().upper(), conversione float() in un try,
intervallo 0 < peso <= PESO_MASSIMO; altrimenti il record pulito e la
stringa vuota. Un ciclo con enumerate(RIGHE, 1) la applica alle righe già
spezzate, spacchetta record, motivo e stampa, dopo il numero di riga, [OK]
con il record oppure [!] con il motivo.

LO SCHEMA
Lo schema sta qui sotto, subito dopo questa docstring, come blocco
commentato: è uno stampo, non un programma, e non ha output. Si copia nel
proprio script, si tolgono i commenti (Ctrl+/ in PyCharm, Cmd+/ su Mac) e si
cambiano solo le righe marcate # <-- adattare.

IN AZIONE
Il codice eseguibile di questo file è l'In azione: lanciatelo, e l'output
deve essere quello di ESEMPIO OUTPUT in fondo a questa docstring.

VARIANTI
Il validatore che solleva invece di restituire il motivo, P8, quando chi
chiama è uno sportello che deve richiedere il dato; una lista di motivi al
posto della stringa, quando all'utente di un modulo conviene saperli tutti
in una volta.

ERRORI TIPICI
- L'unpacking prima del conteggio dei campi → ValueError: not enough values
  to unpack (expected 3, got 2) sulla riga corta.

- Un print dentro il validatore → il messaggio esce anche quando il
  chiamante voleva solo contare gli scarti.

DA DOVE VIENE
Giorno 04 §11.2, §13.9 · Giorno 06 §6.4, §10.1, §10.2 · Giorno 08 §9.2, §9.4
· Giorno 09 §4.5

DOVE SI USA NEGLI ESERCIZI
10.3, 10.5, 10.12, casa_10.3

ESEMPIO OUTPUT
riga 1: [OK] ('LS-0601', 'NORD', 12.5)
riga 2: [!] servono 3 campi, ne ha 2
riga 3: [!] peso fuori intervallo: -4.0
riga 4: [OK] ('LS-0604', 'CENTRO', 7.2)
"""

# ==========================================================================
# LO SCHEMA — lo stampo da copiare. Non si esegue: è commentato.
# ==========================================================================
# def valida_record(campi):  # <-- adattare: valida_<cosa>
#     """Restituisce (record, "") se la riga regge, (None, motivo) se no."""
#     # 1. Numero dei campi verificato prima di qualunque indice o
#     #    spacchettamento: su una riga corta solleverebbero un'eccezione.
#     if len(campi) != CAMPI_ATTESI:
#         return None, f"servono {CAMPI_ATTESI} campi, ne ha {len(campi)}"
#     codice, valore_testo = campi  # <-- adattare: i nomi dei campi
#     # 2. Poi forma e intervallo (P7). Il try racchiude la sola conversione:
#     #    un'eccezione altrove non va scambiata per un dato non numerico.
#     try:
#         valore = float(valore_testo)  # <-- adattare: la conversione
#     except ValueError:
#         return None, f"valore non numerico: '{valore_testo}'"
#     if not MINIMO <= valore <= MASSIMO:  # <-- adattare
#         return None, f"valore fuori intervallo: {valore}"
#     return (codice.strip(), valore), ""


# ==========================================================================
# IN AZIONE — lo schema su un caso del corso. Si esegue.
# ==========================================================================
ZONE = ["NORD", "CENTRO", "SUD", "ISOLE"]
CAMPI_ATTESI = 3
PESO_MASSIMO = 30.0


def valida_spedizione(campi):
    if len(campi) != CAMPI_ATTESI:
        return None, f"servono {CAMPI_ATTESI} campi, ne ha {len(campi)}"
    codice, zona, peso_testo = campi
    zona = zona.strip().upper()
    if zona not in ZONE:
        return None, f"zona sconosciuta: {zona}"
    # float("-4") riesce: la conversione verifica la forma, non il dominio.
    # Il valore negativo lo esclude il controllo d'intervallo successivo.
    try:
        peso = float(peso_testo)
    except ValueError:
        return None, f"peso non numerico: '{peso_testo}'"
    if not 0 < peso <= PESO_MASSIMO:
        return None, f"peso fuori intervallo: {peso}"
    # Il record restituito e' gia' normalizzato: la pulizia avviene in un
    # solo punto e il codice a valle non la ripete.
    return (codice.strip(), zona, peso), ""


RIGHE = [["LS-0601", "nord", "12.5"], ["LS-0602", "SUD"],
         ["LS-0603", "ISOLE", "-4"], ["LS-0604", " centro ", "7.2"]]
for numero, campi in enumerate(RIGHE, 1):
    # 1. Spacchettamento del return multiplo: l'ordine dei nomi deve
    #    ricalcare quello della tupla restituita, (record, motivo).
    record, motivo = valida_spedizione(campi)
    # 2. Valore di verita' della stringa (Giorno 04 §11.2): vuota e' falsa,
    #    quindi un motivo presente seleziona il ramo dello scarto.
    if motivo:
        print(f"riga {numero}: [!] {motivo}")
    else:
        print(f"riga {numero}: [OK] {record}")

# TRABOCCHETTO: scritto motivo, record = valida_spedizione(campi), nessun
#   errore e tutto al contrario: "riga 1: [!] ('LS-0601', 'NORD', 12.5)" e
#   "riga 2: [OK] servono 3 campi, ne ha 2" (Giorno 06 §10.2).
