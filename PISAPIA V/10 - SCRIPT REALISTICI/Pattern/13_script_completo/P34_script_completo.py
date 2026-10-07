"""
P34 — Carica, valida, elabora, riporta: lo scheletro che tiene insieme il
    catalogo

Catalogo dei pattern, Giorno 10 — capitolo 13, Lo script completo
Teoria: TEORIA_GIORNO_10.md §13.1

IN SINTESI
Monta i pattern del catalogo in uno script a quattro fasi, carica, valida,
elabora e riporta, separando una parte generale riusabile da una parte
specifica del caso.

DESCRIZIONE
Il file separa una parte generale, carica_righe(), conta_per_chiave(),
somma_per_chiave() e stampa_righe(), da una parte specifica con le costanti,
i percorsi costruiti da Path(__file__), prepara_file_di_prova(), che scrive
resi.txt, il validatore valida_reso() e componi_report(), che restituisce le
righe del report sui motivi dichiarati in MOTIVI. main() crea output/resi,
carica le righe numerate, le smista fra resi e scarti stampando ogni scarto,
raccoglie motivi e coppie e individua il reso più alto; poi stampa il
report, lo scrive in report_resi.txt, scrive scarti_resi.txt con
intestazione, entrambi in "w", elenca i file scritti e chiude con un assert:
8 = 6 + 2.

LO SCHEMA
Due zone separate dal commento a riquadro delle soluzioni; le quattro fasi
nel main(), che fa il regista (Giorno 06 §1.3).

Lo schema sta qui sotto, subito dopo questa docstring, come blocco
commentato: è uno stampo, non un programma, e non ha output. Si copia nel
proprio script, si tolgono i commenti (Ctrl+/ in PyCharm, Cmd+/ su Mac) e si
cambiano solo le righe marcate # <-- adattare.

IN AZIONE
Il codice eseguibile di questo file è l'In azione: lanciatelo, e l'output
deve essere quello di ESEMPIO OUTPUT in fondo a questa docstring.

ERRORI TIPICI
- Logica del caso dentro una funzione generale → funziona qui, sbaglia in
  silenzio dove la ricopiate (il TRABOCCHETTO).

- piu_alto = resi[0] su un file senza resi buoni → IndexError: list index
  out of range. Se il caso lo prevede, prima if resi:.

DA DOVE VIENE
Giorno 03 §12.1 · Giorno 06 §1.3 · Giorno 08 §14.1, §14.2 · Giorno 09 §16.1,
§16.2

DOVE SI USA NEGLI ESERCIZI
10.11, 10.12

ERRORI TIPICI DELLA GIORNATA COLLEGATI (teoria, capitolo 14)
- E1 — Lo schema copiato senza toccare le righe # <-- adattare: il report di
  un altro caso

ESEMPIO OUTPUT
[!] riga 6: importo non numerico: 'dodici'
[!] riga 8: motivo sconosciuto: SCONTENTO
RESI PER MOTIVO
DIFETTOSO       2    268.90   69.5%
RIPENSAMENTO    2     81.00   20.9%
ERRATO          2     36.90    9.5%
Totale          6    386.80
Reso più alto: NS-R03 (DIFETTOSO) 219.00
File scritto: report_resi.txt (6 righe)
File scritto: scarti_resi.txt (3 righe)
[OK] righe utili 8 = resi 6 + scarti 2
"""

# ==========================================================================
# LO SCHEMA — lo stampo da copiare. Non si esegue: è commentato.
# ==========================================================================
# # ===== PARTE GENERALE: si riusa cosi' com'e' =====
# # Funzioni dei pattern con firme invariate e nessun riferimento al caso:
# # si copiano identiche. carica_righe (P26), conta_per_chiave (P17),
# # somma_per_chiave (P18), stampa_righe (P28).
#
# # ===== PARTE SPECIFICA: si cambia per un altro caso =====
# CATEGORIE = ["PRIMA", "SECONDA"]  # <-- adattare: costanti, validatore, report
#
#
# def main():
#     # 1. CARICA: dal file alle righe numerate (P25, P26).
#     # 2. VALIDA: ogni riga fra i buoni o fra gli scarti (P20, P24, P32).
#     # 3. ELABORA: contare, sommare, massimo, classifica (P15-P18, P22).
#     # 4. RIPORTA: report a video e su file, scarti, invariante (P28, P29).
#     assert len(righe) == len(buoni) + len(scarti), "righe perse nel conto"


# ==========================================================================
# IN AZIONE — lo schema su un caso del corso. Si esegue.
# ==========================================================================
from pathlib import Path

# ===== PARTE GENERALE: si riusa cosi' com'e' =====


def carica_righe(percorso):
    """P26. [(numero_riga, campi), ...] delle righe utili del file."""
    righe = []
    with open(percorso, encoding="utf-8") as f:
        for numero, riga in enumerate(f, 1):
            riga = riga.rstrip("\n")
            if riga.strip() == "" or riga.startswith("#"):
                continue
            campi = []
            for campo in riga.split(SEPARATORE):
                campi.append(campo.strip())
            righe.append((numero, campi))
    return righe


def conta_per_chiave(chiavi):
    """P17. Dizionario chiave -> quante volte compare."""
    conteggi = {}
    for chiave in chiavi:
        conteggi[chiave] = conteggi.get(chiave, 0) + 1
    return conteggi


def somma_per_chiave(coppie):
    """P18. Dizionario chiave -> somma, da coppie (chiave, importo)."""
    somme = {}
    for chiave, importo in coppie:
        somme[chiave] = somme.get(chiave, 0) + importo
    return somme


def stampa_righe(righe, file=None):
    """P28. Le righe a video, o sul file aperto che riceve."""
    for riga in righe:
        print(riga, file=file)


# ===== PARTE SPECIFICA: si cambia per un altro caso =====

SEPARATORE = ";"
CAMPI_ATTESI = 3
MOTIVI = ["DIFETTOSO", "RIPENSAMENTO", "ERRATO"]
IMPORTO_MASSIMO = 1000.00
CARTELLA = Path(__file__).resolve().parent
PERCORSO_RESI = CARTELLA / "resi.txt"
OUTPUT = CARTELLA / "output" / "resi"


def prepara_file_di_prova():
    """Crea il file di partenza: nel programma vero lo manda il negozio."""
    PERCORSO_RESI.write_text(
        "# resi del mese, negozio centro\n"
        "NS-R01;DIFETTOSO;49.90\n"
        "NS-R02;ripensamento;19.50\n"
        "NS-R03;DIFETTOSO;219.00\n"
        "NS-R04;ERRATO;9.90\n"
        "NS-R05;RIPENSAMENTO;dodici\n"
        "NS-R06;ERRATO;27.00\n"
        "NS-R07;SCONTENTO;15.00\n"
        "NS-R08;RIPENSAMENTO;61.50\n",
        encoding="utf-8",
    )


def valida_reso(campi):
    """P24. ((codice, motivo, importo), "") oppure (None, motivo dello scarto)."""
    if len(campi) != CAMPI_ATTESI:
        return None, f"servono {CAMPI_ATTESI} campi, ne ha {len(campi)}"
    codice, motivo, importo_testo = campi
    motivo = motivo.upper()
    if motivo not in MOTIVI:
        return None, f"motivo sconosciuto: {motivo}"
    try:
        importo = float(importo_testo)
    except ValueError:
        return None, f"importo non numerico: '{importo_testo}'"
    if not 0 < importo <= IMPORTO_MASSIMO:
        return None, f"importo fuori intervallo: {importo}"
    return (codice, motivo, importo), ""


def componi_report(conteggi, somme, piu_alto):
    """P28 con P2 e P3. Le righe del report: non stampa, non scrive."""
    totale = sum(somme.values())
    righe = ["RESI PER MOTIVO"]
    # Iterazione sui motivi dichiarati, non sulle chiavi trovate: un motivo
    # senza resi compare comunque, con 0 fornito da get(motivo, 0).
    for motivo in MOTIVI:
        importo = somme.get(motivo, 0)
        quota = importo / totale
        righe.append(f"{motivo:<14}{conteggi.get(motivo, 0):>3}"
                     f"{importo:>10.2f}{quota:>8.1%}")
    righe.append(f"{'Totale':<14}{sum(conteggi.values()):>3}{totale:>10.2f}")
    codice, motivo, importo = piu_alto
    righe.append(f"Reso più alto: {codice} ({motivo}) {importo:.2f}")
    return righe


def main():
    prepara_file_di_prova()
    OUTPUT.mkdir(parents=True, exist_ok=True)
    # 1. CARICA
    righe = carica_righe(PERCORSO_RESI)
    # 2. VALIDA: partizione delle righe in resi e scarti (P20, P24); ogni
    #    scarto conserva numero di riga, motivo e contenuto originale.
    resi = []
    scarti = []
    for numero, campi in righe:
        reso, motivo_scarto = valida_reso(campi)
        if motivo_scarto:
            print(f"[!] riga {numero}: {motivo_scarto}")
            scarti.append(f"{numero};{motivo_scarto};{SEPARATORE.join(campi)}")
        else:
            resi.append(reso)
    # 3. ELABORA: un solo passaggio sui resi prepara le chiavi (P17) e le
    #    coppie (P18) e aggiorna il massimo corrente (P16).
    motivi = []
    coppie = []
    piu_alto = resi[0]
    for reso in resi:
        motivi.append(reso[1])
        coppie.append((reso[1], reso[2]))
        if reso[2] > piu_alto[2]:
            piu_alto = reso
    conteggi = conta_per_chiave(motivi)
    somme = somma_per_chiave(coppie)
    # 4. RIPORTA: una sola lista di righe verso due destinazioni (P28),
    #    poi il file degli scarti con la sua intestazione.
    report = componi_report(conteggi, somme, piu_alto)
    stampa_righe(report)
    with open(OUTPUT / "report_resi.txt", "w", encoding="utf-8") as f:
        stampa_righe(report, file=f)
    with open(OUTPUT / "scarti_resi.txt", "w", encoding="utf-8") as f:
        print("riga;motivo;contenuto", file=f)
        stampa_righe(scarti, file=f)
    for percorso in sorted(OUTPUT.glob("*.txt")):
        quante = len(percorso.read_text(encoding="utf-8").splitlines())
        print(f"File scritto: {percorso.name} ({quante} righe)")
    assert len(righe) == len(resi) + len(scarti), "righe perse nel conto"
    print(f"[OK] righe utili {len(righe)} = resi {len(resi)} + scarti {len(scarti)}")


if __name__ == "__main__":
    main()

# TRABOCCHETTO: se carica_righe() facesse anche .upper() sul secondo campo,
#   qui funzionerebbe lo stesso. Ricopiata nell'anagrafe di Villanova,
#   scriverebbe "DE LUCA" dove il file dice "De Luca", e nessuno l'avrebbe
#   chiesto: la logica del caso NON entra nella parte generale.
