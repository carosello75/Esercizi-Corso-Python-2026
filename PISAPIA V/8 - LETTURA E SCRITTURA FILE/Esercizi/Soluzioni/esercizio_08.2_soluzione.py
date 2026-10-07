"""
SOLUZIONE — Esercizio 08.2: La lettera che supera il limite

IL PROBLEMA
Il portale di TalentHub rifiuta le lettere oltre 120 parole o 800 caratteri,
e il modulo web taglia le righe più lunghe di 74 caratteri. Chi se ne accorge
dopo aver premuto Invia riscrive tutto. Giulia vuole la risposta prima, e la
vuole dal file che ha già scritto, non da un testo incollato a mano.

È la stessa domanda di casa_05.2 (Conta le parole), con una differenza sola:
lì il testo arrivava da input() su una riga, qui arriva dal disco, su più
righe, con le righe vuote fra i paragrafi e gli spazi in coda che nessuno vede.

LA STRATEGIA
Un solo giro sul file con for riga in f (Cap. 4.3), e dentro il giro tutti
gli accumulatori del Giorno 05 insieme:
    righe_totali     contatore, +1 a ogni riga
    righe_non_vuote  contatore, +1 solo se la riga pulita non è ""
    caratteri        accumulatore, + len(riga) PRIMA della pulizia
    parole           accumulatore, + quante parole ha la riga
    riga più lunga   il massimo tenuto da parte, con il suo numero
    parola più lunga il massimo tenuto da parte, sulla parola ripulita
    frasi            contatore, +1 per ogni parola che finisce con il punto
    righe_lunghe     una lista di tuple (numero, lunghezza, testo)
Il file si legge UNA volta sola: un secondo giro sullo stesso file aperto fa
zero giri senza nessun errore (Cap. 4.5), e riaprirlo per ogni misura sarebbe
fare sei volte la stessa fatica.

DUE LUNGHEZZE DIVERSE, E TUTTE E DUE GIUSTE
    caratteri del file   len(riga) così come arriva: a capo e spazi in coda
                         compresi. È quello che il portale riceve.
    lunghezza di riga    len(riga.rstrip()): quello che si VEDE. È quello che
                         il modulo web taglia.
La riga 6 del file è costruita per distinguerle: 74 caratteri visibili, più
uno spazio in coda, più l'a capo.

LA FUNZIONE CHE RESTITUISCE
misura_lettera() non stampa niente: restituisce un dizionario con le misure,
e main() decide che cosa farne (Giorno 06, Cap. 5: return contro print).
Domani le stesse misure possono finire in un file di report senza toccare
una riga della funzione.

Concetti di teoria: Cap. 4.3 (for riga in f), Cap. 4.5 (il file si legge una
volta), Cap. 5.1-5.2 (l'a capo e la pulizia), Cap. 7.4 (il percorso dallo
script). Dal Giorno 02 split() e strip() con argomento, dal Giorno 05 i
contatori e il massimo tenuto da parte, dal Giorno 06 la funzione che
restituisce, dal Giorno 07 la lista di tuple e il dizionario.
"""

from pathlib import Path

# --- Costanti -----------------------------------------------------------
NOME_FILE = "lettera_candidatura.txt"
MASSIMO_PAROLE = 120
MASSIMO_CARATTERI = 800
MASSIMO_CARATTERI_RIGA = 74
LARGHEZZA_ANTEPRIMA = 40
LARGHEZZA = 60

# I dati si cercano partendo dallo script, non dalla directory di lavoro
# (Cap. 7.4): soluzioni -> giorno_08 -> dati.
CARTELLA_DATI = Path(__file__).resolve().parent.parent / "dati"

# I segni di punteggiatura che possono restare attaccati a una parola.
# L'apostrofo NON c'è: in "all'amministrazione" fa parte della parola, e
# toglierlo dai bordi non lo toccherebbe comunque, perché sta in mezzo.
PUNTEGGIATURA = ".,;:!?"


def misura_lettera(percorso):
    """Legge la lettera una volta e restituisce un dizionario di misure."""
    righe_totali = 0
    righe_non_vuote = 0
    caratteri = 0
    parole = 0
    riga_piu_lunga = 0
    lunghezza_riga_max = 0
    parola_piu_lunga = ""
    frasi = 0
    righe_lunghe = []

    # TRABOCCHETTO: aprire senza encoding="utf-8". Su macOS e Linux non
    #   cambia niente, perché lì il default è già UTF-8. Su un Windows
    #   italiano il default è cp1252, e le tre lettere accentate della
    #   lettera (contabilità, perché, più) vengono lette come due caratteri
    #   ciascuna: "Caratteri, a capo compresi 563" invece di 560, nessun
    #   errore. Lo stesso programma dà due numeri su due macchine (Cap. 2.3).
    with open(percorso, "r", encoding="utf-8") as f:
        for riga in f:
            # Il numero di riga cresce a OGNI riga, vuote comprese: è il
            # numero che Giulia vede nell'editor, e deve coincidere.
            #
            # TRABOCCHETTO: contare solo le righe non vuote e usare quel
            #   contatore come numero di riga. Nessun errore: esce "riga 7,
            #   78 caratteri", e Giulia va a correggere la riga sbagliata,
            #   perché la riga vuota fra i paragrafi non è stata contata.
            righe_totali += 1

            # I caratteri del file si sommano sulla riga GREZZA: a capo e
            # spazi in coda li riceve anche il portale.
            caratteri += len(riga)

            # rstrip() senza argomenti toglie in coda TUTTO ciò che non si
            # vede: l'a capo e gli spazi. Qui è la scelta giusta perché si
            # misura quello che il lettore vede, non si separano campi.
            #
            # TRABOCCHETTO: rstrip("\n") da solo, la pulizia minima di Cap.
            #   5.2. Toglie l'a capo ma lascia lo spazio in coda alla riga 6,
            #   che misura 75 invece di 74. Sintomo: "[!] Righe oltre 74
            #   caratteri: 2", con la riga 6 accusata per uno spazio che a
            #   schermo non esiste. Senza nessuna pulizia è peggio: +1 a ogni
            #   riga, e la riga più lunga diventa di 79.
            pulita = riga.rstrip()
            lunghezza = len(pulita)

            # Una riga vuota letta dal file è "\n", non "": il confronto si
            # fa sulla riga pulita.
            #
            # TRABOCCHETTO: if riga != "" sulla riga grezza. Le due righe
            #   vuote fra i paragrafi contengono l'a capo, quindi sono diverse
            #   da "": "Righe non vuote ... 12", lo stesso numero delle righe
            #   totali, e nessun errore a segnalarlo (Cap. 5.1).
            if pulita != "":
                righe_non_vuote += 1

            # split() senza argomenti: spezza su qualunque sequenza di spazi
            # e ignora quelli ai bordi. Su una riga vuota restituisce [], e
            # il for qui sotto fa zero giri: nessun caso speciale da gestire.
            for parola in pulita.split():
                parole += 1

                # Una frase finisce dove una parola finisce con il punto. Il
                # controllo si fa sulla parola GREZZA, prima di togliere la
                # punteggiatura: il punto è proprio l'informazione che serve.
                #
                # TRABOCCHETTO: spostare questo if sotto la riga di strip() e
                #   controllare nuda.endswith("."). La punteggiatura è già
                #   stata tolta, nessuna parola finisce più con il punto e le
                #   frasi restano 0. Se in main() manca il controllo sullo
                #   zero, la media si ferma con ZeroDivisionError: division
                #   by zero; se c'è, esce "Frasi ... 0" su una lettera che di
                #   frasi ne ha cinque.
                if parola.endswith("."):
                    frasi += 1

                # La punteggiatura attaccata si toglie dai bordi, non da
                # dentro: strip() con argomento (Giorno 02).
                #
                # TRABOCCHETTO: confrontare la parola grezza. Vince lo stesso
                #   "all'amministrazione", ma con il punto finale: "(20
                #   caratteri)". Il numero è sbagliato di uno e sembra giusto.
                nuda = parola.strip(PUNTEGGIATURA)
                # Maggiore stretto: a parità vince la prima incontrata, come
                # in casa_05.2.
                if len(nuda) > len(parola_piu_lunga):
                    parola_piu_lunga = nuda

            if lunghezza > lunghezza_riga_max:
                lunghezza_riga_max = lunghezza
                riga_piu_lunga = righe_totali

            # Le righe oltre il limite si mettono da parte, una tupla per
            # riga (Giorno 07, Cap. 14): si stampano dopo, quando il file è
            # già chiuso.
            if lunghezza > MASSIMO_CARATTERI_RIGA:
                righe_lunghe.append((righe_totali, lunghezza, pulita))

    # TRABOCCHETTO: chiamare f.read() qui, dopo il for, per avere il totale
    #   dei caratteri con len(). Il for ha già portato il file fino in fondo:
    #   read() restituisce "" e il totale vale 0, senza errori (Cap. 4.5).
    #   Fuori dal with, poi, il file è chiuso e read() si ferma con
    #   ValueError: I/O operation on closed file.

    # Un dizionario come valore di ritorno: le misure hanno un nome, e main()
    # le legge per nome invece di ricordarsi l'ordine di nove valori.
    return {
        "righe_totali": righe_totali,
        "righe_non_vuote": righe_non_vuote,
        "caratteri": caratteri,
        "parole": parole,
        "riga_piu_lunga": riga_piu_lunga,
        "lunghezza_riga_max": lunghezza_riga_max,
        "parola_piu_lunga": parola_piu_lunga,
        "frasi": frasi,
        "righe_lunghe": righe_lunghe,
    }


def verdetto(etichetta, valore, massimo):
    """Stampa [OK] o [!] per un limite e restituisce True se è rispettato."""
    # <= perché il limite è compreso: 120 parole su 120 si possono caricare.
    if valore <= massimo:
        print(f"[OK] {etichetta}: {valore} su {massimo}.")
        return True
    print(f"[!] {etichetta}: {valore} su {massimo}, oltre il limite.")
    return False


def main():
    """Misura la lettera e stampa i verdetti sui tre limiti."""
    print("=" * LARGHEZZA)
    print("TALENTHUB - Controllo della lettera prima del caricamento")
    print("=" * LARGHEZZA)

    percorso = CARTELLA_DATI / NOME_FILE
    # Solo il nome: il percorso intero cambia da macchina a macchina.
    print(f"File letto: {percorso.name}")
    print("-" * LARGHEZZA)

    misure = misura_lettera(percorso)
    print(f"Righe totali ............. {misure['righe_totali']}")
    print(f"Righe non vuote .......... {misure['righe_non_vuote']}")
    print(f"Caratteri, a capo compresi {misure['caratteri']}")
    print(f"Parole ................... {misure['parole']}")
    print(f"Riga più lunga ........... riga {misure['riga_piu_lunga']}, "
          f"{misure['lunghezza_riga_max']} caratteri")
    parola = misure["parola_piu_lunga"]
    print(f"Parola più lunga ......... {parola} ({len(parola)} caratteri)")

    # La media di parole per frase. Il conteggio delle parole comprende
    # anche l'intestazione e la firma, che non finiscono con il punto: è una
    # misura grezza, e va letta come tale.
    #
    # TRABOCCHETTO: dividere senza guardare se le frasi sono zero. Una
    #   lettera senza nessun punto (un elenco, una bozza) ferma il programma
    #   con ZeroDivisionError: division by zero proprio sull'ultima misura,
    #   dopo che tutte le altre sono già state stampate.
    frasi = misure["frasi"]
    print(f"Frasi .................... {frasi}")
    if frasi > 0:
        media = misure["parole"] / frasi
        print(f"Parole per frase, in media {media:.1f}")
    else:
        print("Parole per frase, in media n.d. (nessun punto nel testo)")
    print("-" * LARGHEZZA)

    # I tre limiti. I primi due con la stessa funzione; il terzo ha un
    # dettaglio in più da stampare e si scrive a parte.
    parole_ok = verdetto("Parole", misure["parole"], MASSIMO_PAROLE)
    caratteri_ok = verdetto("Caratteri", misure["caratteri"], MASSIMO_CARATTERI)

    righe_lunghe = misure["righe_lunghe"]
    if len(righe_lunghe) == 0:
        print(f"[OK] Nessuna riga oltre {MASSIMO_CARATTERI_RIGA} caratteri.")
    else:
        print(f"[!] Righe oltre {MASSIMO_CARATTERI_RIGA} caratteri: "
              f"{len(righe_lunghe)}")
        for numero, lunghezza, testo in righe_lunghe:
            # L'anteprima con lo slicing del Giorno 02: i primi 40 caratteri
            # bastano a riconoscere la riga, e la stampa resta dentro la
            # cornice.
            anteprima = testo[:LARGHEZZA_ANTEPRIMA]
            print(f"    riga {numero} ({lunghezza}): {anteprima}...")
    print("-" * LARGHEZZA)

    # La frase finale mette insieme i tre verdetti con and (Giorno 04).
    if parole_ok and caratteri_ok and len(righe_lunghe) == 0:
        print("La lettera rispetta i limiti: si può caricare.")
    else:
        print("La lettera va sistemata prima del caricamento.")
    print("=" * LARGHEZZA)


if __name__ == "__main__":
    main()
