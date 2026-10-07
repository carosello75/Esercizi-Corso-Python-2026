"""
SOLUZIONE — Esercizio 03.4: Preventivo spedizione in una riga

Tre dati digitati e due meccanismi diversi per smontarli.

Le prime due righe si aprono con .split() e un unpacking: uno a tre
variabili per la spedizione, uno a due per il listino. È lo stesso
meccanismo applicato a due formati, ed è il motivo per cui l'esercizio
ne chiede due.

Il codice di spedizione invece non ha separatori: i pezzi stanno sempre
nelle stesse posizioni, quindi si aprono con lo slicing del Giorno 02.
Sono due strumenti per due formati, e sceglierli è metà dell'esercizio:
dove c'è un separatore si taglia, dove ci sono posizioni fisse si conta.

La pulizia va fatta DOPO lo split, pezzo per pezzo: .split() taglia e
basta, gli spazi attorno ai pezzi restano dentro i pezzi.

Il programma assume che la prima riga contenga esattamente due punti e
virgola e la seconda esattamente uno. Con un separatore in meno o in più
salta l'unpacking, ed è un comportamento voluto: il messaggio di errore
di quel caso è materiale dell'esercizio 03.7.

Il programma è diviso in quattro fasi dichiarate — lettura, pulizia,
calcolo, presentazione — e nessuna torna indietro: dopo la pulizia
nessun dato grezzo viene più letto, dopo il calcolo nessun numero viene
più toccato. È la forma che regge quando il preventivo cresce.
"""

# --- Listino e formato del documento ---------------------------------
DIRITTI_FISSI = 4.50
ALIQUOTA_IVA = 0.22
RIGA_DOPPIA = "=" * 50
RIGA_SINGOLA = "-" * 50
VETTORE = "LOGISUD TRASPORTI - PREVENTIVO DI SPEDIZIONE"

# --- Posizioni dentro il codice LS-2026-MI-0042 ----------------------
# Contate una volta sola e messe qui: se il formato del codice cambia,
# si cambia in un punto solo invece che dentro le f-string.
ANNO_DA = 3
ANNO_A = 7
PROVINCIA_DA = 8
PROVINCIA_A = 10


def main():
    """Calcola il preventivo di una spedizione da tre dati digitati."""

    # ---------------------------------------------------------------- #
    # FASE 1 — LETTURA. Qui si raccoglie soltanto: nessuna pulizia,     #
    # nessun calcolo. Tutto ciò che arriva è di tipo str.               #
    # ---------------------------------------------------------------- #
    riga_spedizione = input("Spedizione (zona;peso;urgenza): ")
    riga_listino = input("Listino (tariffa_kg;maggiorazione_%): ")
    codice_grezzo = input("Codice spedizione: ")

    # ---------------------------------------------------------------- #
    # FASE 2 — PULIZIA. Da qui in poi i dati grezzi non si usano più.   #
    # ---------------------------------------------------------------- #

    # TRABOCCHETTO 1: i nomi a sinistra dell'uguale devono essere
    # esattamente quanti i pezzi prodotti da .split(). Tre qui, due
    # sotto. Sbagliare il conteggio non produce un dato strano: produce
    # un ValueError e il programma finisce lì.
    zona_grezza, peso_grezzo, urgenza_grezza = riga_spedizione.split(";")
    tariffa_grezza, maggiorazione_grezza = riga_listino.split(";")

    # TRABOCCHETTO 2: la pulizia viene dopo lo split, mai prima. Uno
    # .strip() sulla riga intera toglierebbe solo gli spazi ai due
    # estremi, e quelli attorno al peso ("sud; 12,5 ;URGENTE")
    # resterebbero al loro posto facendo saltare float().
    zona = zona_grezza.strip().upper()
    urgenza = urgenza_grezza.strip().lower()
    peso_kg = float(peso_grezzo.strip().replace(",", "."))
    tariffa_kg = float(tariffa_grezza.strip().replace(",", "."))

    maggiorazione_pulita = maggiorazione_grezza.strip().replace(",", ".")
    maggiorazione_percentuale = float(maggiorazione_pulita)

    # TRABOCCHETTO 3: il codice si normalizza PRIMA di tagliarlo. Se
    # arriva con uno spazio davanti, ogni posizione slitta di uno e
    # l'anno diventa "026-". Lo slicing non protesta: restituisce il
    # pezzo sbagliato, e l'errore si vede solo a documento stampato.
    codice = codice_grezzo.strip().upper()

    # Due strumenti per due formati: sopra il separatore, qui le
    # posizioni. Lo slicing prende da ANNO_DA incluso ad ANNO_A escluso,
    # quindi 3 e 7 danno i quattro caratteri di indice 3, 4, 5 e 6.
    anno = codice[ANNO_DA:ANNO_A]
    provincia = codice[PROVINCIA_DA:PROVINCIA_A]

    # ---------------------------------------------------------------- #
    # FASE 3 — CALCOLO. Solo numeri: nessuna stampa, nessuna lettura.   #
    # ---------------------------------------------------------------- #
    trasporto = peso_kg * tariffa_kg
    imponibile_base = DIRITTI_FISSI + trasporto
    maggiorazione = imponibile_base * maggiorazione_percentuale / 100
    imponibile = imponibile_base + maggiorazione
    iva = imponibile * ALIQUOTA_IVA
    totale = imponibile + iva

    # TRABOCCHETTO 4: l'etichetta dell'IVA nasce dalla costante, non è
    # scritta a mano. Il giorno che l'aliquota passa al 10% cambia una
    # riga sola e l'etichetta la segue da sé.
    etichetta_iva = f"IVA {ALIQUOTA_IVA:.0%}:"

    # ---------------------------------------------------------------- #
    # FASE 4 — PRESENTAZIONE. Qui nessun valore cambia più: le          #
    # f-string producono testo e lasciano i numeri come stanno.         #
    # ---------------------------------------------------------------- #
    print()
    print(RIGA_DOPPIA)
    print(VETTORE)
    print(RIGA_DOPPIA)
    print(f"{'Zona:':<24}{zona:>10}")
    print(f"{'Peso in kg:':<24}{peso_kg:>10.2f}")
    print(f"{'Urgenza:':<24}{urgenza:>10}")
    print(f"{'Anno di riferimento:':<24}{anno:>10}")
    print(f"{'Provincia di partenza:':<24}{provincia:>10}")
    print(f"{'Tariffa al kg:':<24}{tariffa_kg:>10.2f}")
    print(f"{'Maggiorazione:':<24}{maggiorazione_percentuale:>9.0f}%")
    print(RIGA_SINGOLA)
    print(f"{'Diritti fissi:':<24}{DIRITTI_FISSI:>10.2f}")
    print(f"{'Trasporto:':<24}{trasporto:>10.2f}")
    print(f"{'Imponibile base:':<24}{imponibile_base:>10.2f}")
    print(f"{'Maggiorazione urgenza:':<24}{maggiorazione:>10.2f}")
    print(f"{'Imponibile:':<24}{imponibile:>10.2f}")
    print(f"{etichetta_iva:<24}{iva:>10.2f}")
    print(RIGA_SINGOLA)
    print(f"{'TOTALE PREVENTIVO:':<24}{totale:>10.2f}")
    print(RIGA_DOPPIA)
    print("Importi in euro. Preventivo valido 15 giorni.")


if __name__ == "__main__":
    main()
