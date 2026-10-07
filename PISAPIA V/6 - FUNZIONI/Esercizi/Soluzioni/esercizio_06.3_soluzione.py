"""
SOLUZIONE — Esercizio 06.3: Chiedere un numero, sul serio

Il problema: tre numeri da chiedere allo sportello, e nessuno dei tre può
essere sbagliato. Il ciclo di validazione del Giorno 05 funziona, ma è
dodici righe: ricopiato tre volte diventa trentasei righe che bisogna
ricordarsi di correggere tutte insieme.

La strategia: il ciclo entra dentro una funzione con tre parametri — la
domanda da fare e i due estremi ammessi — e da quel momento chiedere un
numero valido costa una riga. I messaggi d'errore esistono in un punto solo
del programma.

    chiedi_intero(messaggio, minimo, massimo)   -> int, sempre valido
    chiedi_si_o_no(messaggio)                   -> True oppure False
    anni_compiuti(nascita, riferimento)         -> int

Nessuna delle tre stampa il riepilogo: restituiscono e basta. È la
separazione fra "calcolare" e "mostrare" del capitolo 5, ed è quello che
rende chiedi_intero riusabile in qualunque altro programma senza portarsi
dietro l'impaginazione di questo.

Il contatore dei tentativi sbagliati è la parte che mostra l'ambito locale
al lavoro (cap. 11.1): nasce dentro la funzione, vive quanto la chiamata e
sparisce. Tre chiamate, tre contatori indipendenti, e la prima domanda non
può "avvelenare" la terza.

I bordi:
    risposta vuota        .isdecimal() su "" restituisce False: finisce nel
                          primo messaggio d'errore, che è la cosa giusta.
    numero negativo       .isdecimal() dice di no al segno meno, quindi -3
                          non arriva mai al controllo sull'intervallo.
    minimo uguale a       il ciclo accetta solo quel valore. Non è un caso
    massimo               da trattare a parte: funziona già.

Concetti di teoria: cap. 4 (parametri), cap. 5 (return dopo il ciclo),
cap. 7 (funzione chiamata dentro un'altra), cap. 11 (ambito locale),
cap. 12 (il prefisso chiedi_ dichiara che la funzione parla con l'utente),
cap. 13 (docstring).
"""

# --- Costanti -----------------------------------------------------------
ANNO_CORRENTE = 2026

# Gli estremi delle tre domande. Sono costanti perché ognuno compare DUE
# volte: nel testo della domanda e come argomento della funzione. Due usi
# dello stesso numero sono due occasioni di scriverne uno diverso.
MIN_COMPONENTI = 1
MAX_COMPONENTI = 12
ANNO_MINIMO = 1900
SPORTELLO_MINIMO = 1
SPORTELLO_MASSIMO = 6

# Dopo quanti errori di fila lo sportello smette di ripetere lo stesso
# messaggio e dice la cosa in modo più esplicito.
TENTATIVI_PRIMA_DELL_AIUTO = 3

LARGHEZZA = 60


def chiedi_intero(messaggio, minimo, massimo):
    """Chiede un intero finché non ne arriva uno valido nell'intervallo."""
    # 1. Variabili di lavoro locali, create PRIMA del ciclo: il valore
    #    raccolto, la bandiera che dice se siamo a posto, il contatore
    #    degli errori. Nascono a ogni chiamata e muoiono con lei.
    #
    #    valore parte da minimo e non da zero, e non è una scelta di
    #    comodo: se il return finisse per errore dentro il ciclo, un valore
    #    di partenza fuori intervallo uscirebbe dalla funzione come se
    #    fosse un dato buono. Partendo da minimo, il dato sbagliato è
    #    almeno un dato ammissibile.
    valore = minimo
    valido = False
    sbagliati = 0

    # 2. Il ciclo. Si ferma quando valido diventa True, e diventa True in
    #    un punto solo di tutta la funzione: il ramo else.
    while not valido:
        # Il dato letto è SEMPRE testo, anche quando sono tutte cifre.
        # .strip() toglie gli spazi ai bordi, che allo sportello arrivano
        # sempre: " 4 " senza strip non è fatto solo di cifre.
        testo = input(messaggio).strip()

        # 3. Prima la forma, poi il merito, e in quest'ordine: int(testo)
        #    nei due rami successivi è sicuro solo perché il primo ramo ha
        #    già escluso tutto ciò che non è una sequenza di cifre.
        #
        # TRABOCCHETTO: invertire i rami e scrivere int(testo) < minimo per
        #   primo. Su "tre" la conversione non si può fare e il programma
        #   si ferma con
        #   ValueError: invalid literal for int() with base 10: 'tre'
        #   Il ciclo di validazione esiste proprio per evitare questo, e
        #   messo nell'ordine sbagliato lo provoca lui stesso.
        if not testo.isdecimal():
            print("[ERRORE] Servono solo cifre: niente lettere, niente spazi.")
            sbagliati += 1
        elif int(testo) < minimo:
            # Due messaggi diversi per due guasti diversi. "Fuori
            # intervallo" non dice da che parte si è usciti, e chi sta allo
            # sportello ha bisogno di saperlo per correggersi.
            print(f"[ERRORE] Il valore minimo ammesso è {minimo}.")
            sbagliati += 1
        elif int(testo) > massimo:
            print(f"[ERRORE] Il valore massimo ammesso è {massimo}.")
            sbagliati += 1
        else:
            # 4. Solo qui il dato è buono: da str a int, e si alza la
            #    bandiera. La conversione avviene una volta sola, sul dato
            #    già controllato.
            valore = int(testo)
            valido = True

        # 5. L'aiuto dopo tre errori di fila. Due condizioni, e servono
        #    tutte e due.
        #
        # TRABOCCHETTO: due modi di rovinare questa riga, nessuno dei due
        #   dà errore. Scrivendo >= al posto di ==, il suggerimento
        #   ricompare a ogni errore successivo al terzo, quarto, quinto, e
        #   lo sportello diventa una macchina che urla. Togliendo
        #   "not valido", chi sbaglia tre volte e poi risponde bene si vede
        #   stampare il suggerimento DOPO la risposta giusta, perché il
        #   contatore vale ancora tre anche nel giro che chiude il ciclo.
        if not valido and sbagliati == TENTATIVI_PRIMA_DELL_AIUTO:
            print(f"[!] Serve un numero intero fra {minimo} e {massimo}, "
                  f"cifre e nient'altro.")

    # 6. Il return è a quattro spazi, allineato con il while: è FUORI dal
    #    ciclo, e ci si arriva solo quando valido è diventato True.
    #
    # TRABOCCHETTO: spostare questo return dentro il while, a otto spazi.
    #   Non dà nessun errore e distrugge la funzione: esce al primo giro
    #   qualunque cosa sia stato digitato. Digitando "tre" lo sportello
    #   stampa il messaggio d'errore e poi, nel riepilogo,
    #   "Componenti del nucleo ..... 1", cioè il valore di partenza,
    #   accettato come se il cittadino l'avesse dichiarato.
    return valore


def chiedi_si_o_no(messaggio):
    """Chiede una domanda da sì o no e restituisce True oppure False."""
    risposta = False
    valido = False

    while not valido:
        # .lower() normalizza le maiuscole, .strip() gli spazi. Le stringhe
        # sono immutabili: i due metodi non modificano il testo digitato,
        # ne restituiscono una copia lavorata, e qui la copia è l'unica
        # cosa che ci interessa.
        #
        # TRABOCCHETTO: dimenticare .lower(). Chi risponde "S" maiuscola
        #   non corrisponde a nessuno dei cinque casi, finisce nell'else e
        #   si vede ripetere la domanda all'infinito: dal suo punto di
        #   vista ha risposto correttamente e il programma non lo ascolta.
        #   Il ciclo non è infinito per un difetto del while, ma perché la
        #   condizione di uscita non può diventare vera.
        testo = input(messaggio).strip().lower()

        # Le tre forme del sì e le due del no, scritte per esteso con or.
        # Elencare i casi ammessi in una struttura dati sarà molto più
        # comodo, e sarà possibile quando avremo le strutture dati.
        if testo == "s" or testo == "si" or testo == "sì":
            risposta = True
            valido = True
        elif testo == "n" or testo == "no":
            risposta = False
            valido = True
        else:
            print("[ERRORE] Rispondete s oppure n.")

    return risposta


def anni_compiuti(anno_nascita, anno_riferimento):
    """Restituisce gli anni compiuti nell'anno di riferimento indicato."""
    # TRABOCCHETTO: i due parametri sono entrambi interi a quattro cifre e
    #   Python non ha modo di accorgersi di uno scambio. Chiamandola come
    #   anni_compiuti(ANNO_CORRENTE, anno) il riepilogo stampa
    #   "Anni compiuti nel 2026 .... -41": nessun errore, un'età negativa,
    #   e il segno meno è l'unico indizio. È il capitolo 15, errore E6.
    return anno_riferimento - anno_nascita


def main():
    """Raccoglie i dati della pratica e ne stampa il riepilogo."""
    print("=" * LARGHEZZA)
    print("COMUNE DI VILLANOVA - Sportello anagrafe")
    print("=" * LARGHEZZA)

    # Le domande si costruiscono con le stesse costanti che la funzione
    # userà per controllare.
    #
    # TRABOCCHETTO: scrivere "(1-12)" a mano dentro il testo e poi passare
    #   MAX_COMPONENTI = 10 alla funzione. Il programma è coerente con se
    #   stesso e mente al cittadino: legge che può arrivare a dodici, prova
    #   con undici e si sente dire che il massimo è dieci. I due numeri
    #   devono venire dalla stessa fonte, e qui la fonte è una costante.
    componenti = chiedi_intero(
        f"Componenti del nucleo ({MIN_COMPONENTI}-{MAX_COMPONENTI}): ",
        MIN_COMPONENTI,
        MAX_COMPONENTI,
    )
    anno = chiedi_intero(
        f"Anno di nascita ({ANNO_MINIMO}-{ANNO_CORRENTE}): ",
        ANNO_MINIMO,
        ANNO_CORRENTE,
    )
    sportello = chiedi_intero(
        f"Sportello di destinazione ({SPORTELLO_MINIMO}-{SPORTELLO_MASSIMO}): ",
        SPORTELLO_MINIMO,
        SPORTELLO_MASSIMO,
    )

    # La quarta domanda non è un numero, ma il meccanismo è identico: la
    # funzione non restituisce finché la risposta non è utilizzabile.
    urgente = chiedi_si_o_no("Pratica urgente? (s/n): ")

    eta = anni_compiuti(anno, ANNO_CORRENTE)

    # urgente è un bool, e nel riepilogo serve una parola italiana.
    # Questo if non è un controllo di validità — quelli stanno tutti dentro
    # le funzioni, come chiede la traccia — è una scelta di presentazione:
    # decide come si scrive un dato già valido.
    #
    # TRABOCCHETTO: stampare urgente così com'è. La riga esce
    #   "Urgente ................... True", con la maiuscola e in inglese,
    #   perché è il modo in cui Python scrive un booleano. Nessun errore, e
    #   una ricevuta comunale che parla una lingua che non è la sua.
    if urgente:
        etichetta_urgenza = "sì"
    else:
        etichetta_urgenza = "no"

    print("-" * LARGHEZZA)
    print("RIEPILOGO DELLA RICHIESTA")
    print(f"Componenti del nucleo ..... {componenti}")
    print(f"Anno di nascita ........... {anno}")
    print(f"Anni compiuti nel {ANNO_CORRENTE} .... {eta}")
    print(f"Sportello ................. {sportello}")
    print(f"Urgente ................... {etichetta_urgenza}")
    print("-" * LARGHEZZA)
    print("La funzione chiedi_intero è stata scritta una volta e")
    print("chiamata tre volte. Senza di lei gli stessi tre controlli")
    print("sarebbero ricopiati in tre punti diversi, e il giorno che")
    print("cambia il messaggio d'errore bisogna ricordarsi di tutti.")
    print("=" * LARGHEZZA)


# Il programma parte solo se il file viene eseguito direttamente: è la
# formula fissa di ogni soluzione del corso.
if __name__ == "__main__":
    main()
