"""
SOLUZIONE — Esercizio per casa 10.3: Le ore dei consulenti

IL PROBLEMA
Sedici giornate segnate a mano, tre sbagliate: una in lettere, una
negativa, una da quattordici ore. Servono le ore per persona con il carico
della settimana, le ore per progetto con la quota, e un riepilogo JSON che
l'amministrazione possa ricaricare senza ricontare niente.

LA STRATEGIA: OTTO PATTERN DEL CATALOGO
- P26 il caricatore, P24 il validatore che restituisce (record, "") o
  (None, motivo), con dentro P5 per le ore scritte con la virgola.
- P32 la riga che non si converte: il try sta stretto sulla conversione,
  dentro il giro sulle righe. Una riga sbagliata diventa uno scarto, un
  difetto del programma resta un traceback.
- P18 la somma per chiave, tre volte: ore per consulente, ore per
  progetto, giornate per consulente (contare è sommare degli uno).
- P10 la decisione a soglie: la fascia di carico viene da una tabella di
  soglie scorsa da una funzione, non da una catena di if.
- P3 due tabelle a larghezza fissa.
- P30 il JSON in andata e ritorno, con gli scarti salvati come
  dizionari: il JSON non conosce le tuple.

COME È DIVISO IL FILE
PARTE GENERALE: i pezzi del catalogo, con le firme della teoria. PARTE
SPECIFICA: costanti, validatore, tabelle, main(). Per contare gli
straordinari del personale comunale si riscrive la seconda.

LIMITI NOTI DI QUESTA SOLUZIONE
- Le ore si sommano per riga, senza guardare se lo stesso consulente ha
  segnato due volte lo stesso progetto nello stesso giorno: il file non
  ha la data, quindi il doppione non si può riconoscere.
- Il tetto di 12 ore vale per riga. Due righe da 8 ore dello stesso giorno
  su due progetti diversi passano entrambe: senza data, è quello che si
  può controllare.
- ORE_SETTIMANALI è una costante: un contratto part-time chiederebbe un
  tetto per persona, cioè un dizionario (P12) al posto del numero.
"""

import json
from pathlib import Path

# --- Costanti ------------------------------------------------------------
# Tre .parent: la soluzione sta un livello più in basso della traccia
# (P25, Giorno 08 §7.3).
CARTELLA_GIORNO = Path(__file__).resolve().parent.parent.parent
DATI = CARTELLA_GIORNO / "dati"
OUTPUT = CARTELLA_GIORNO / "output"
FILE_ORE = DATI / "ore_consulenti.txt"
FILE_RIEPILOGO = OUTPUT / "ore_consulenti.json"

SEPARATORE = ";"
COMMENTO = "#"
CAMPI_ATTESI = 3
LARGHEZZA = 60
LARGHEZZA_BARRA = 40
LARGHEZZA_ETICHETTA = 27
SEGNO_BARRA = "#"
DECIMALI_CONFRONTO = 2

ORE_MINIME_ESCLUSE = 0
ORE_MASSIME_GIORNO = 12
ORE_CARICO_LEGGERO = 30
ORE_SETTIMANALI = 40
# La tabella delle soglie del P10: coppie (limite incluso, etichetta), in
# ordine CRESCENTE. Il secondo limite è la costante delle ore settimanali,
# non un 40 riscritto: se il contratto cambia, cambia in un punto solo.
SOGLIE_CARICO = [(ORE_CARICO_LEGGERO, "LEGGERO"), (ORE_SETTIMANALI, "PIENO")]
CARICO_OLTRE = "OLTRE"
SEGNO_OLTRE = " [!]"

TITOLO = "TALENTHUB - Ore dei consulenti"


# =========================================================================
# ===== PARTE GENERALE: si riusa così com'è ===============================
# =========================================================================

# P26 — Il caricatore: righe utili con il numero di riga dell'editor.
def carica_righe(percorso):
    """Restituisce [(numero_riga, campi), ...], senza righe vuote né commenti."""
    righe_utili = []
    with open(percorso, encoding="utf-8") as ingresso:
        for numero, riga in enumerate(ingresso, start=1):
            testo = riga.strip()
            if testo == "" or testo.startswith(COMMENTO):
                continue
            campi = []
            for campo in testo.split(SEPARATORE):
                campi.append(campo.strip())
            righe_utili.append((numero, campi))
    return righe_utili


# P5 — Il numero scritto all'italiana.
def converti_importo(testo):
    """Converte '1.250,00', '12,50' o '12.50' in float, o solleva ValueError."""
    pulito = testo.strip()
    # Solo se c'è la virgola i punti sono separatori delle migliaia.
    if "," in pulito:
        pulito = pulito.replace(".", "").replace(",", ".")
    try:
        return float(pulito)
    except ValueError:
        raise ValueError(f"importo non numerico: '{testo.strip()}'")


# P10 — La decisione a soglie.
def fascia(valore, soglie, oltre):
    """Restituisce l'etichetta della prima soglia che il valore non supera."""
    # TRABOCCHETTO: la lista va in ordine crescente. Scritta al contrario,
    #   [(40, "PIENO"), (30, "LEGGERO")], il primo limite prende tutto ciò
    #   che sta sotto i 40: Caruso Elisa con 23.0 ore esce PIENO, e la
    #   fascia LEGGERO non la vede più nessuno (Giorno 04 §6.1).
    for limite, etichetta in soglie:
        # <= perché il limite è INCLUSO: 40 ore esatte sono ancora un
        # carico pieno, non uno straordinario.
        if valore <= limite:
            return etichetta
    return oltre


# P18 — La somma per chiave, da coppie (chiave, valore).
def somma_per_chiave(coppie):
    """Restituisce un dizionario chiave -> somma dei valori."""
    somme = {}
    for chiave, valore in coppie:
        # TRABOCCHETTO: con somme[chiave] += valore il programma si ferma
        #   alla prima coppia con KeyError: 'Amato Chiara'. Il dizionario
        #   vuoto non ha ancora nessuna chiave a cui aggiungere; .get() con
        #   il ripiego 0 sì (Giorno 07 §12.3).
        somme[chiave] = somme.get(chiave, 0) + valore
    return somme


# P30 — Salvare in JSON, leggibile e con le lettere accentate intatte.
def salva_json(percorso, dati):
    """Scrive i dati in JSON con rientro di 2 spazi, accenti leggibili."""
    with open(percorso, "w", encoding="utf-8") as uscita:
        json.dump(dati, uscita, indent=2, ensure_ascii=False)


def riga_puntini(etichetta, valore):
    """P2 — 'Etichetta ........ valore', con i valori in colonna."""
    return f"{etichetta + ' ':.<{LARGHEZZA_ETICHETTA}} {valore}"


def barra(quota):
    """P18 — Una barra di '#' lunga quota * LARGHEZZA_BARRA."""
    return SEGNO_BARRA * round(quota * LARGHEZZA_BARRA)


# =========================================================================
# ===== PARTE SPECIFICA: si cambia per un altro caso ======================
# =========================================================================

def valida_giornata(campi):
    """Restituisce ((consulente, progetto, ore), '') oppure (None, motivo)."""
    if len(campi) != CAMPI_ATTESI:
        return None, f"servono {CAMPI_ATTESI} campi, ne ha {len(campi)}"
    consulente, progetto, testo_ore = campi
    # " ".join(split()) riduce gli spazi interni a uno, .title() rimette le
    # iniziali: "amato  chiara" e "Amato Chiara" diventano la stessa chiave
    # (P4, Giorno 03 §5.3).
    consulente = " ".join(consulente.split()).title()
    progetto = progetto.upper()

    # P32: il try è stretto sulla SOLA conversione. Quello che sta sotto
    # (il controllo d'intervallo) non può sollevare, e se un giorno lo
    # facesse sarebbe un difetto del programma, da vedere e non da
    # nascondere fra gli scarti (Giorno 09 §4.5).
    # TRABOCCHETTO: con float(testo_ore) al posto di converti_importo(),
    #   "6,5" non si converte e finisce fra gli scarti insieme a "otto".
    #   Il programma non si ferma: scarta sei righe invece di tre, Amato
    #   Chiara scende a 29.0 ore e fascia LEGGERO, il [!] sparisce e il
    #   totale è 77.0. La settimana più carica sembra la più leggera.
    try:
        ore = converti_importo(testo_ore)
    except ValueError:
        return None, f"ore non numeriche: '{testo_ore}'"

    if not ORE_MINIME_ESCLUSE < ore <= ORE_MASSIME_GIORNO:
        return None, (f"ore fuori intervallo (oltre {ORE_MINIME_ESCLUSE}, "
                      f"al massimo {ORE_MASSIME_GIORNO}): {ore:.1f}")
    return (consulente, progetto, ore), ""


def stampa_consulenti(ore_per_consulente, giornate_per_consulente):
    """Stampa la tabella per consulente con giornate, media e carico."""
    print(f"{'CONSULENTE':<18}{'ORE':>6}{'GIORNATE':>10}{'MEDIA/G':>9}  CARICO")
    for consulente in ore_per_consulente:
        ore = ore_per_consulente[consulente]
        giornate = giornate_per_consulente[consulente]
        # Requisito promosso: giornate e media per giornata. Ogni
        # consulente in tabella ha almeno una giornata valida (è lì per
        # quello), quindi qui la divisione per zero non può capitare.
        media_giorno = ore / giornate
        carico = fascia(ore, SOGLIE_CARICO, CARICO_OLTRE)
        segno = SEGNO_OLTRE if carico == CARICO_OLTRE else ""
        print(f"{consulente:<18}{ore:>6.1f}{giornate:>10}{media_giorno:>9.1f}"
              f"  {carico}{segno}")


def stampa_progetti(ore_per_progetto, totale):
    """Stampa la tabella per progetto con quota e barra."""
    print(f"{'PROGETTO':<18}{'ORE':>6}{'QUOTA':>8}")
    for progetto in ore_per_progetto:
        ore = ore_per_progetto[progetto]
        # La quota si calcola DOPO il giro, a totale completo (P18).
        # TRABOCCHETTO: lo specificatore % moltiplica già per 100. Con
        #   quota = ore / totale * 100 la prima riga dice 4527.4% invece
        #   di 45.3%, e la barra diventa lunga 1811 caratteri.
        quota = ore / totale
        print(f"{progetto:<18}{ore:>6.1f}{quota:>8.1%} {barra(quota)}")
    print("-" * LARGHEZZA)
    print(f"{'TOTALE':<18}{totale:>6.1f}")


def main():
    """Somma le ore, stampa le due tabelle, salva e rilegge il JSON."""
    print("=" * LARGHEZZA)
    print(TITOLO)
    print("=" * LARGHEZZA)

    # 1. CARICA.
    if not FILE_ORE.exists():
        print(f"[ERRORE] {FILE_ORE.name} non trovato nella cartella dati.")
        print("=" * LARGHEZZA)
        return
    righe = carica_righe(FILE_ORE)
    print(f"File letto: {FILE_ORE.name}")

    # 2. VALIDA. Gli scarti si tengono come DIZIONARI e non come tuple,
    #    perché finiranno nel JSON (vedi il TRABOCCHETTO al punto 4).
    giornate = []
    scarti = []
    for numero, campi in righe:
        giornata, motivo = valida_giornata(campi)
        if giornata is None:
            print(f"[!] riga {numero:>2}  {motivo}")
            scarti.append({"riga": numero, "motivo": motivo})
            continue
        giornate.append(giornata)
    print(riga_puntini("Righe lette", len(righe)))
    print(riga_puntini("Giornate valide", len(giornate)))
    print(riga_puntini("Righe scartate", len(scarti)))
    print("-" * LARGHEZZA)

    # 3. ELABORA: tre somme per chiave con la stessa funzione. Le giornate
    #    si contano sommando un 1 per riga: contare è un caso particolare
    #    di sommare, e il pattern P18 basta.
    coppie_consulente = []
    coppie_progetto = []
    coppie_giornate = []
    for consulente, progetto, ore in giornate:
        coppie_consulente.append((consulente, ore))
        coppie_progetto.append((progetto, ore))
        coppie_giornate.append((consulente, 1))
    ore_per_consulente = somma_per_chiave(coppie_consulente)
    ore_per_progetto = somma_per_chiave(coppie_progetto)
    giornate_per_consulente = somma_per_chiave(coppie_giornate)
    totale = sum(ore_per_progetto.values())

    stampa_consulenti(ore_per_consulente, giornate_per_consulente)
    print("-" * LARGHEZZA)
    if totale == 0:
        print("[!] Nessuna ora valida: tabella dei progetti non calcolabile.")
    else:
        stampa_progetti(ore_per_progetto, totale)
    print("-" * LARGHEZZA)

    # 4. SALVA e RILEGGI. Il file va in output/, mai sopra i dati di
    #    partenza; "w" dentro salva_json() è la ripartenza pulita.
    # TRABOCCHETTO: salvate gli scarti come tuple (8, "ore non ...") e il
    #   JSON li riscrive come liste [8, "ore non ..."]. Il file si rilegge
    #   senza errori, ma un confronto riletti["scarti"] == scarti dà False,
    #   e un assert costruito su quel confronto si ferma con AssertionError
    #   anche se i dati sono identici (Giorno 08 §12.3).
    OUTPUT.mkdir(parents=True, exist_ok=True)
    riepilogo = {
        "consulenti": ore_per_consulente,
        "progetti": ore_per_progetto,
        "totale_ore": totale,
        "scarti": scarti,
    }
    salva_json(FILE_RIEPILOGO, riepilogo)
    print(f"File scritto: {FILE_RIEPILOGO.name}")

    # Si rilegge il FILE, non il dizionario in memoria: è la prova che
    # l'amministrazione, aprendo quel file, trova gli stessi numeri.
    with open(FILE_RIEPILOGO, encoding="utf-8") as ingresso:
        riletto = json.load(ingresso)
    print(f"Riletto: {len(riletto['consulenti'])} consulenti, "
          f"{len(riletto['progetti'])} progetti, "
          f"{riletto['totale_ore']:.1f} ore, {len(riletto['scarti'])} scarti")

    # 5. I CONTI. Gli assert controllano il programma, non i dati: se
    #    scattano, qualcosa si è perso fra lettura, validazione e scrittura
    #    (Giorno 09 §14.4).
    assert len(righe) == len(giornate) + len(scarti), (
        f"righe {len(righe)}, ma buone + scartate = "
        f"{len(giornate) + len(scarti)}"
    )
    print(f"[OK] {len(righe)} righe = {len(giornate)} buone + "
          f"{len(scarti)} scartate")
    # Il confronto fra float si fa sugli arrotondati: qui le ore sono tutte
    # mezze ore e la somma è esatta, ma la regola vale anche il giorno in
    # cui qualcuno segna 7,3 ore (Giorno 02 §7.4).
    totale_riletto = riletto["totale_ore"]
    assert round(totale_riletto, DECIMALI_CONFRONTO) == round(
        totale, DECIMALI_CONFRONTO
    ), f"totale riletto {totale_riletto}, calcolato {totale}"
    print(f"[OK] totale riletto {totale_riletto:.1f} = "
          f"totale calcolato {totale:.1f}")
    print("=" * LARGHEZZA)


if __name__ == "__main__":
    main()
