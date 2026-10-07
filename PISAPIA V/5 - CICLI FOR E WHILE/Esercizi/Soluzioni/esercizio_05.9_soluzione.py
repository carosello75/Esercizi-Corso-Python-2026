"""
SOLUZIONE — Esercizio 05.9: Il controllo dei codici di tracciamento

Il problema: il magazziniere di LogiSud legge a voce alta i codici dei colli
e l'operatore li batte uno alla volta, finché i colli non finiscono. Ogni
codice va accettato o scartato subito, con il motivo; alla fine servono i
conti della giornata.

La strategia sta tutta in una domanda, fatta due volte: «so quante volte?»

    Quanti codici arriveranno?     Nessuno lo sa: dipende dai colli sul
                                   bancale. Il numero di giri NON è noto
                                   prima di partire  ->  while, con la
                                   sentinella "fine".
    Quante cifre sommare?          Sempre cinque: il formato del codice
                                   lo fissa. Il numero di giri È noto
                                   prima di partire  ->  for.

Stessa giornata, stesso programma, due risposte diverse alla stessa domanda:
è il punto dell'esercizio. Il for sta DENTRO il while, perché a ogni codice
buono si rifà il conto delle sue cifre: due livelli di ciclo, il massimo
consentito (Cap. 12).

Il while segue la forma base della sentinella (Cap. 9.2): una lettura PRIMA
del ciclo, una IN CODA al corpo. È la forma in cui i tre obblighi del while
si vedono uno per riga:
    inizializzare   la prima lettura, prima del while
    condizionare    codice != SENTINELLA
    aggiornare      la seconda lettura, ultima riga del corpo
Niente `continue` nel corpo: con la lettura in coda, un continue la
salterebbe e il ciclo non finirebbe più (vedi il trabocchetto relativo).

La cifra di controllo: le cinque cifre del seriale si sommano, e l'ultima
cifra del codice deve essere l'ultima cifra di quella somma, cioè la somma
modulo 10. È un controllo che esiste davvero sui codici a barre: se
l'operatore sbaglia a battere UNA cifra, la somma cambia e il codice viene
scartato invece di finire nel magazzino sbagliato.

    LS123455   seriale 12345   1+2+3+4+5 = 15   15 % 10 = 5   ultima 5  OK
    LS900016   seriale 90001   9+0+0+0+1 = 10   10 % 10 = 0   ultima 6  NO

Che cosa sopravvive al ciclo: i due contatori `esaminati` e `accettati`,
creati prima del while e aggiornati dentro. Gli scartati NON si contano: si
ricavano per differenza, e qui è corretto farlo (vedi la chiusura).

I bordi:
    "fine" come primo dato   il while fa zero giri; i contatori restano a
                             0 e la quota non si calcola, perché
                             dividerebbe per zero.
    un codice solo           un giro, e la quota è 0.0% o 100.0%.
    "Fine", " FINE "         si ferma lo stesso: si normalizza prima di
                             confrontare.

Concetti di teoria: Cap. 5 (for su una stringa), Cap. 6 (contatore e
accumulatore), Cap. 7 (while), Cap. 9 (la sentinella), Cap. 11 (for o
while), Cap. 12 (due cicli annidati). Dal Giorno 02 lo slicing e il resto
%, dal Giorno 04 la catena di elif e .isdecimal().
"""

# --- Costanti -----------------------------------------------------------
# Larghezza delle cornici, la stessa di tutti gli esercizi della giornata.
LARGHEZZA = 60

# Il formato del codice, un pezzo per costante. Da queste tre righe si
# ricavano tutte le posizioni usate più sotto: se LogiSud passasse a sei
# cifre di seriale, si cambia CIFRE_SERIALE e il resto segue da solo.
PREFISSO = "LS"
CIFRE_SERIALE = 5
CIFRE_CONTROLLO = 1

# Posizioni ricavate, non scritte a mano. INIZIO_SERIALE è dove finisce il
# prefisso (2); POSIZIONE_CONTROLLO è l'indice dell'ultimo carattere (7);
# LUNGHEZZA_CODICE è quanti caratteri deve avere un codice buono (8).
# Scrivere 2, 7 e 8 nel codice funzionerebbe oggi e mentirebbe domani.
INIZIO_SERIALE = len(PREFISSO)
POSIZIONE_CONTROLLO = INIZIO_SERIALE + CIFRE_SERIALE
LUNGHEZZA_CODICE = POSIZIONE_CONTROLLO + CIFRE_CONTROLLO

# La cifra di controllo è l'ultima cifra della somma: la somma modulo 10.
# 10 perché una cifra va da 0 a 9, e il resto della divisione per 10 è
# esattamente l'ultima cifra di un numero.
BASE_CONTROLLO = 10

# La parola che chiude la giornata. Scritta in MAIUSCOLO perché si confronta
# con il dato già normalizzato: "fine", "Fine" e "FINE" diventano tutti
# "FINE" prima del confronto.
SENTINELLA = "FINE"

# Il prompt compare due volte (prima del ciclo e in coda al corpo): in
# costante, perché le due letture devono chiedere esattamente la stessa
# cosa, e due copie scritte a mano prima o poi smettono di coincidere.
PROMPT = "Codice collo (o 'fine'): "


def main():
    """Controlla i codici dei colli finché l'operatore non scrive fine."""
    # 1. Intestazione e istruzioni per l'operatore.
    print("=" * LARGHEZZA)
    print("LOGISUD - Controllo dei codici di tracciamento")
    print("=" * LARGHEZZA)
    print(f"Formato: {PREFISSO} + {CIFRE_SERIALE} cifre + 1 di controllo.")
    print()

    # 2. I due contatori, creati PRIMA del ciclo e a zero: dopo il while
    #    varranno quanti codici sono passati e quanti sono stati accettati.
    #    Sono int, e restano int per tutto il programma.
    #
    # TRABOCCHETTO: creati DENTRO il while si azzerano a ogni codice.
    #   Sintomo: a fine giornata "Codici esaminati ...... 1" e al massimo
    #   un accettato, qualunque cosa sia stata battuta. E con "fine" come
    #   primo dato il ciclo non entra mai, i nomi non vengono mai
    #   assegnati e il programma si ferma sul riepilogo con
    #   UnboundLocalError (Cap. 6.3).
    esaminati = 0
    accettati = 0

    # 3. Prima lettura, PRIMA del ciclo: è l'«inizializzare» del while.
    #    input() restituisce una str; .strip() toglie gli spazi ai bordi,
    #    .upper() porta tutto in maiuscolo. codice resta una str per tutto
    #    il programma: un codice di tracciamento non è un numero, anche se
    #    è fatto quasi solo di cifre, e non si converte mai per intero.
    #
    # TRABOCCHETTO: confrontare con la sentinella SENZA normalizzare.
    #   L'operatore scrive "Fine" con la maiuscola: il confronto con
    #   "FINE" è falso, e "Fine" viene trattato come un codice.
    #   Sintomo: "[ERRORE] Fine: servono 8 caratteri, ne ha 4", e il
    #   programma chiede un altro codice invece di chiudere (Cap. 9.4).
    codice = input(PROMPT).strip().upper()

    # 4. Il ciclo esterno: un giro per codice.
    #    Che cosa ripete: esamina un codice, stampa il verdetto, ne legge
    #    un altro.
    #    Quando si ferma: quando l'ultimo codice letto è la sentinella. Il
    #    controllo avviene PRIMA di ogni giro, quindi la sentinella stessa
    #    non viene mai esaminata né contata.
    #    Che cosa aggiorna: esaminati sempre, accettati solo sui codici
    #    buoni, e codice con la lettura in coda al corpo.
    while codice != SENTINELLA:
        esaminati += 1

        # 5. I controlli, in un ordine che non è indifferente: dal più
        #    grossolano al più fine, e ognuno protegge quelli dopo.
        #      lunghezza  ->  solo così le posizioni 2..7 esistono davvero
        #      prefisso   ->  solo così ha senso parlare di "seriale"
        #      cifre      ->  solo così int() sulle cifre non si ferma
        #      controllo  ->  l'unico che fa un conto, e va fatto per ultimo
        #    È una catena di elif: al primo controllo che fallisce si esce
        #    con il suo messaggio, e i successivi non vengono nemmeno letti.
        if len(codice) != LUNGHEZZA_CODICE:
            print(f"  [ERRORE] {codice}: servono {LUNGHEZZA_CODICE} caratteri,"
                  f" ne ha {len(codice)}")
        # codice[:INIZIO_SERIALE] sono i primi due caratteri: lo slicing del
        # Giorno 02, con l'estremo sinistro omesso che vuol dire "dall'inizio".
        elif codice[:INIZIO_SERIALE] != PREFISSO:
            print(f"  [ERRORE] {codice}: deve iniziare con {PREFISSO}")
        # .isdecimal() restituisce True solo se TUTTI i caratteri sono cifre.
        # Qui si controlla tutto quello che segue il prefisso, cifra di
        # controllo compresa: anche quella passerà per int().
        #
        # TRABOCCHETTO: saltare questo controllo, o metterlo dopo il for.
        #   Su "LS12A455" il for arriva alla "A" e int("A") ferma tutto il
        #   programma con
        #   ValueError: invalid literal for int() with base 10: 'A'.
        #   Non si perde un codice: si perde la giornata, perché il
        #   magazziniere deve ricominciare da capo (Giorno 04, Cap. 13).
        elif not codice[INIZIO_SERIALE:].isdecimal():
            print(f"  [ERRORE] {codice}: dopo {PREFISSO} servono solo cifre")
        else:
            # 6. Il ciclo interno: la somma delle cifre del seriale.
            #    Perché for e non while: le cifre sono CIFRE_SERIALE, cioè
            #    cinque, e lo si sa prima di cominciare. Un for su una
            #    stringa (Cap. 5) prende un carattere per giro e si ferma
            #    da solo in fondo, senza indici da far avanzare a mano.
            #    Che cosa ripete: somma una cifra.
            #    Quando si ferma: finiti i caratteri della fetta.
            #    Che cosa aggiorna: somma, l'accumulatore.
            #
            # TRABOCCHETTO: somma = 0 va QUI, dentro l'else, cioè una volta
            #   per codice. Messa prima del while, la somma di un codice si
            #   porta dietro quelle dei codici precedenti. Sintomo: il primo
            #   codice buono passa, poi LS900016 dice "attesa 5, letta 6"
            #   invece di "attesa 0", e LS400004, che è giusto, viene
            #   scartato con "attesa 9, letta 4".
            somma = 0
            # La fetta va da INIZIO_SERIALE compreso a POSIZIONE_CONTROLLO
            # escluso: posizioni 2, 3, 4, 5, 6, cioè le cinque cifre del
            # seriale e NON la cifra di controllo.
            #
            # TRABOCCHETTO: scorrere codice[INIZIO_SERIALE:], fino alla
            #   fine. Sembra la stessa cosa e include anche l'ultima cifra,
            #   che è proprio quella da verificare: la si somma a sé stessa.
            #   Il controllo diventa (somma + c) % 10 == c, cioè vero solo
            #   quando il seriale somma a un multiplo di 10, qualunque sia
            #   la cifra finale. Sintomo, ed è il peggiore possibile: un
            #   codice giusto viene scartato (LS123455, "attesa 0, letta 5")
            #   e uno SBAGLIATO viene accettato (LS900016, seriale 9+0+0+0+1
            #   = 10). Il riepilogo dice ancora "Accettati ...... 1" e sembra
            #   tutto a posto: è il collo sbagliato a partire.
            for cifra in codice[INIZIO_SERIALE:POSIZIONE_CONTROLLO]:
                # cifra è una str di un carattere, "1": int() la trasforma
                # nel numero 1. Senza int(), somma += "1" proverebbe a
                # sommare un int e una str: TypeError.
                somma += int(cifra)

            # 7. Il verdetto. attesa è l'ultima cifra della somma, letta è
            #    l'ultima cifra del codice: due int da confrontare.
            #    codice[POSIZIONE_CONTROLLO] è un carattere, "5"; int() lo
            #    porta a 5. Confrontare "5" con 5 darebbe sempre False,
            #    senza nessun errore (Giorno 04, Cap. 7.3).
            attesa = somma % BASE_CONTROLLO
            letta = int(codice[POSIZIONE_CONTROLLO])
            if letta == attesa:
                accettati += 1
                print(f"  [OK] {codice} accettato")
            else:
                print(f"  [ERRORE] {codice}: cifra di controllo errata"
                      f" (attesa {attesa}, letta {letta})")

        # 8. Lettura in coda al corpo: è l'«aggiornare» del while, e sta
        #    FUORI dalla catena di if, allo stesso rientro di esaminati += 1.
        #    Così viene eseguita a ogni giro, qualunque verdetto sia uscito.
        #
        # TRABOCCHETTO: dimenticarla, o rientrarla dentro l'else. Senza
        #   questa riga codice non cambia mai, la condizione resta vera per
        #   sempre, e il programma ristampa lo stesso verdetto all'infinito:
        #   si ferma solo con Ctrl+C (Cap. 8). Rientrata dentro l'else,
        #   succede lo stesso al primo codice sbagliato, perché i rami di
        #   errore non leggono più niente. E per la stessa ragione qui non
        #   c'è nessun continue: in un ramo di errore salterebbe proprio
        #   questa riga, e il codice sbagliato verrebbe riesaminato per
        #   sempre. Con la lettura in coda, i rami si chiudono da soli.
        codice = input(PROMPT).strip().upper()

    # 9. Il riepilogo, dopo il ciclo. Gli scartati si ricavano per
    #    differenza, ed è corretto: ogni codice esaminato finisce in uno e
    #    uno solo dei due mucchi, accettati o scartati, quindi i due numeri
    #    sommano per costruzione a esaminati. È diverso dalle chiamate al
    #    microfono di 05.1, dove la formula dipendeva dalla forma del ciclo:
    #    qui dipende solo da una regola che il programma garantisce.
    scartati = esaminati - accettati
    print()
    print("-" * LARGHEZZA)
    print(f"Codici esaminati ...... {esaminati}")
    print(f"Accettati ............. {accettati}")
    print(f"Scartati .............. {scartati}")
    # La quota è una divisione, e con "fine" come primo dato esaminati vale
    # 0. L'if la protegge. :.1% moltiplica già per cento e aggiunge il
    # simbolo: 2 / 6 = 0.333... diventa "33.3%".
    #
    # TRABOCCHETTO: senza questo if, chi apre il programma e scrive subito
    #   "fine" lo vede fermarsi con ZeroDivisionError: division by zero,
    #   dopo aver stampato tre righe di zeri. Il caso sembra assurdo e
    #   capita il primo giorno, quando qualcuno prova se il programma parte.
    if esaminati > 0:
        print(f"Quota accettati ....... {accettati / esaminati:.1%}")
    else:
        print("Quota accettati ....... nessun codice esaminato")
    print("=" * LARGHEZZA)


# Il programma parte solo se il file viene eseguito direttamente, non se
# qualcuno lo importa: è la formula fissa di ogni soluzione del corso.
if __name__ == "__main__":
    main()
