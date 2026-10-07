"""
SOLUZIONE — Esercizio 05.1: Promemoria e conto alla rovescia

Il problema: da un solo numero, gli appuntamenti della giornata, ricavare
tre elenchi che ne dipendono tutti — promemoria, cartello della sala
d'attesa, chiamate al microfono.

La strategia: tre cicli `for` su `range()`, uno per ciascuna delle tre
forme viste al capitolo 3.
    range(1, quanti + 1)                    avanti, da 1 a quanti compreso
    range(quanti, 0, -1)                    indietro, da quanti a 1
    range(PASSO_CHIAMATA, quanti + 1, ...)  a salti: 2, 4, 6...

Perché `for` e non `while`: il numero di giri è noto PRIMA che il ciclo
parta, perché l'operatore lo ha appena digitato. Quando si sa quante volte,
`for` parte, avanza e si ferma da solo. Un `while` farebbe lo stesso con
tre righe di contabilità in più — inizializzare, condizionare, aggiornare —
e ognuna delle tre si può sbagliare (Cap. 11).

Che cosa sopravvive ai cicli: soltanto `quanti`, creata prima e mai più
modificata. Le variabili dei cicli (`numero`, `rimasti`) servono dentro il
giro; dopo non si leggono più, e il totale finale si stampa da `quanti`.

I bordi, cioè che cosa succede con i numeri piccoli:
    quanti = 1   un promemoria, "Manca 1 paziente", nessuna chiamata al
                 microfono: range(2, 2, 2) è vuoto, ed è giusto così.
    quanti = 0   i tre cicli fanno zero giri, senza nessun errore: restano
                 le intestazioni, "[OK] Sala d'attesa vuota" e il totale 0.
    negativo     come zero, perché un range con gli estremi "al contrario"
                 è vuoto. Nessuno lo impedisce: validare è l'esercizio 05.4.

Concetti di teoria: Cap. 3 (le tre forme di range), Cap. 4 (la variabile
del ciclo e il suo nome), e l'if del Giorno 04 messo dentro un ciclo.
"""

# --- Costanti -----------------------------------------------------------
# Larghezza delle righe di "=" che incorniciano l'output. 60 è la misura
# comune agli esercizi della giornata, così le schermate si confrontano a
# colpo d'occhio. Cambiarla qui allarga le tre cornici insieme.
LARGHEZZA = 60

# Ogni quanti numeri si fa una chiamata al microfono. La regola della
# segreteria è "uno sì e uno no", cioè 2. Finisce come terzo argomento di
# range(), il passo: con 3 si chiamerebbe un paziente ogni tre, senza
# toccare una sola riga del ciclo.
PASSO_CHIAMATA = 2


def main():
    """Stampa promemoria, conto alla rovescia e chiamate al microfono."""
    # 1. Intestazione. "=" * LARGHEZZA è la ripetizione di stringhe: una
    #    str per un int dà una str lunga 60. Ripete, ma non è un ciclo: lo
    #    fa l'operatore * in un colpo solo, e non c'è niente da contare.
    print("=" * LARGHEZZA)
    print("POLIAMBULATORIO AURORA - Promemoria della giornata")
    print("=" * LARGHEZZA)

    # 2. Lettura e conversione, in una riga che si legge dall'interno:
    #      input(...)   ->  "4 "  (str)  come l'ha digitato l'operatore
    #      .strip()     ->  "4"   (str)  senza spazi ai bordi
    #      int(...)     ->   4    (int)  il numero che range() accetta
    #    È l'unico dato del programma: tutti e tre i cicli dipendono da lui.
    #
    # TRABOCCHETTO: qui si converte senza controllare. Se l'operatore scrive
    #   "quattro" il programma si ferma subito con
    #   ValueError: invalid literal for int() with base 10: 'quattro'.
    #   Oggi va bene così: il ciclo che richiede il dato finché non è buono
    #   è l'esercizio 05.4, e la gestione professionale degli errori
    #   (try/except) non è materia di queste giornate.
    #
    # TRABOCCHETTO: senza int(), quanti resta la stringa "4" e la riga
    #   non protesta. Protesta il primo range(), perché quanti + 1 prova a
    #   sommare una str e un int:
    #   TypeError: can only concatenate str (not "int") to str.
    #   Il messaggio indica la riga del ciclo, ma l'errore sta qui.
    quanti = int(input("Quanti appuntamenti ci sono oggi? ").strip())

    # 3. Primo ciclo: i promemoria, numerati da 1.
    #    Che cosa ripete: una riga di stampa per appuntamento.
    #    Quando si ferma: dopo il valore quanti, perché range(1, quanti + 1)
    #    produce 1, 2, ..., quanti e poi si esaurisce.
    #    Che cosa aggiorna: solo numero, che range() cambia da sé a ogni
    #    giro. Nessuna variabile del programma viene modificata.
    print()
    print("PROMEMORIA DA STAMPARE")
    # TRABOCCHETTO: range(1, quanti) si ferma a quanti - 1. L'estremo
    #   destro è ESCLUSO, quindi per arrivare a quanti compreso serve il
    #   + 1. Sintomo: l'ultima riga è "Promemoria 3 di 4", nessun errore,
    #   e l'ultimo paziente resta senza foglietto. È l'off-by-one (Cap.
    #   14.4), l'errore che oggi mezza aula farà almeno una volta.
    for numero in range(1, quanti + 1):
        # numero è int, quanti è int: l'f-string li trasforma in testo al
        # momento della stampa, senza bisogno di str().
        print(f"  Promemoria {numero} di {quanti}")

    # 4. Secondo ciclo: il cartello della sala d'attesa, all'indietro.
    #    Che cosa ripete: una riga per ogni paziente ancora da ricevere.
    #    Quando si ferma: il passo -1 fa scendere, e lo zero è l'estremo
    #    escluso, quindi l'ultimo valore prodotto è 1. Esattamente dove il
    #    cartello deve arrivare.
    #    Che cosa aggiorna: solo rimasti, gestita da range().
    print()
    print("CONTO ALLA ROVESCIA DELLA SALA D'ATTESA")
    # TRABOCCHETTO: il passo negativo non si può omettere. range(quanti, 0)
    #   ha il passo di default +1, e salire da 4 fino a 0 è impossibile:
    #   zero giri. Sintomo: sotto l'intestazione compare soltanto
    #   "[OK] Sala d'attesa vuota". E con range(quanti, 1, -1), all'opposto,
    #   sparisce la riga "Manca 1 paziente".
    for rimasti in range(quanti, 0, -1):
        # Dentro un ciclo si può mettere tutto quello che si sa già: qui
        # un if del Giorno 04. Il singolare è un caso a parte perché
        # "Mancano 1 pazienti" non è italiano, e il ciclo da solo non lo sa.
        if rimasti == 1:
            print("  Manca 1 paziente")
        else:
            print(f"  Mancano {rimasti} pazienti")
    # TRABOCCHETTO: la riga qui sotto sta FUORI dal ciclo, e lo dice solo
    #   il rientro: stessa colonna del for, non del corpo. Rientrata di
    #   quattro spazi in più, entra nel ciclo e viene eseguita a ogni giro.
    #   Sintomo: "[OK] Sala d'attesa vuota" stampato quattro volte, una
    #   dopo ogni riga del cartello, mentre in sala c'è ancora gente.
    print("  [OK] Sala d'attesa vuota")

    # 5. Terzo ciclo: le chiamate al microfono, una sì e una no.
    #    Che cosa ripete: una chiamata per ogni numero pari.
    #    Quando si ferma: all'ultimo multiplo del passo che non supera
    #    quanti. Si parte dal passo e si sale di passo: 2, 4, 6...
    #    Con quanti dispari, l'ultimo paziente non viene chiamato al
    #    microfono: è il comportamento voluto, non una perdita.
    print()
    print("CHIAMATE AL MICROFONO (uno sì e uno no)")
    # TRABOCCHETTO: il punto di partenza decide quali numeri escono.
    #   Con range(0, quanti + 1, PASSO_CHIAMATA) la prima riga è
    #   "Numero 0", un paziente che non esiste; con range(1, ...) escono
    #   i dispari. E senza il + 1 finale, con 4 appuntamenti la chiamata
    #   "Numero 4" sparisce, per la stessa ragione del primo ciclo.
    for numero in range(PASSO_CHIAMATA, quanti + 1, PASSO_CHIAMATA):
        print(f"  Numero {numero}")

    # 6. Chiusura. Il totale è quanti: ogni appuntamento ha avuto il suo
    #    promemoria, quindi non c'è niente da contare.
    #
    # TRABOCCHETTO: stampare qui numero invece di quanti. La variabile del
    #   ciclo sopravvive al ciclo e conserva l'ultimo valore (Cap. 4.1):
    #   qui è l'ultimo numero pari. Con 4 appuntamenti coincide per caso;
    #   con 5 il programma dice "Promemoria stampati: 4". E con 0 nessun
    #   ciclo ha mai assegnato numero: il programma si ferma con
    #   UnboundLocalError, la forma che il NameError del Cap. 4.2 prende
    #   dentro una funzione come main().
    print()
    print(f"Promemoria stampati: {quanti}")
    print("=" * LARGHEZZA)


# Il programma parte solo se il file viene eseguito direttamente, non se
# qualcuno lo importa: è la formula fissa di ogni soluzione del corso.
if __name__ == "__main__":
    main()


# =======================================================================
# SE HAI FINITO PRIMA — le due voci opzionali della traccia
# =======================================================================
# Non sono eseguite da main(), apposta: il programma qui sopra produce
# esattamente l'ESEMPIO OUTPUT della traccia, ed è quello che il collaudo
# confronta riga per riga. Qui sotto c'è come si fanno. Per provarle,
# copiate le righe al punto indicato e togliete il "# " iniziale.
#
# -----------------------------------------------------------------------
# 1. Gli orari: uno ogni mezz'ora dalle 9, ricavando ore e minuti
# -----------------------------------------------------------------------
# L'orario non si legge da nessuna parte: si ricava dal numero del
# promemoria. L'appuntamento n comincia (n - 1) mezz'ore dopo le 9, e quei
# minuti si spezzano in ore e minuti con la divisione intera // e il resto
# % del Giorno 02. È lo stesso conto che fa chi guarda un orologio.
#
# Tre costanti nuove, in cima al file insieme alle altre:
#
#     ORA_INIZIO = 9               # il primo appuntamento, in ore
#     DURATA_APPUNTAMENTO = 30     # minuti: ogni quanto se ne apre uno
#     MINUTI_IN_UN_ORA = 60        # la definizione di ora, non un 60 nudo
#
# Nel primo ciclo, al posto della riga di stampa del promemoria:
#
#     minuti_dall_inizio = (numero - 1) * DURATA_APPUNTAMENTO
#     ora = ORA_INIZIO + minuti_dall_inizio // MINUTI_IN_UN_ORA
#     minuti = minuti_dall_inizio % MINUTI_IN_UN_ORA
#     print(f"  Promemoria {numero} di {quanti} - ore {ora}:{minuti:0>2}")
#
# Passo per passo, con 4 appuntamenti: numero vale 1, 2, 3, 4; i minuti
# dall'inizio 0, 30, 60, 90 (int); 90 // 60 = 1 ora intera e 90 % 60 = 30
# minuti che avanzano, quindi 9 + 1 = 10 e 30.
#
# {minuti:0>2} è larghezza 2, allineata a destra, con lo ZERO come
# carattere di riempimento: 0 -> "00", 30 -> "30". È il meccanismo di
# {' SCONTRINO ':=^50} del Giorno 03, §9.7.
#
# Che cosa stampa, con 4:
#     Promemoria 1 di 4 - ore 9:00
#     Promemoria 2 di 4 - ore 9:30
#     Promemoria 3 di 4 - ore 10:00
#     Promemoria 4 di 4 - ore 10:30
#
# TRABOCCHETTO: senza il - 1 il primo appuntamento parte alle 9:30 e
#   tutti gli altri mezz'ora dopo il dovuto. Nessun errore: quattro
#   pazienti che arrivano all'ora sbagliata. È l'off-by-one del + 1 di
#   range(), dall'altra parte.
# TRABOCCHETTO: / al posto di // trasforma l'ora in un float, 9 + 90 / 60
#   = 10.5, e il promemoria dice "ore 10.5:30". / divide sempre con la
#   virgola; // tiene la parte intera, che è proprio "quante ore intere".
# TRABOCCHETTO: {minuti} senza :0>2 fa uscire "ore 9:0". Il numero è
#   giusto, è la scrittura che non lo è.
#
# -----------------------------------------------------------------------
# 2. Contare le chiamate al microfono invece di calcolarle
# -----------------------------------------------------------------------
# Il numero delle chiamate si potrebbe ottenere con una formula, quanti //
# PASSO_CHIAMATA; ma la formula è vera solo finché il ciclo parte da
# PASSO_CHIAMATA e sale di PASSO_CHIAMATA. Un contatore conta i giri che il
# ciclo ha fatto DAVVERO, qualunque forma abbia: se la segreteria cambia
# regola, il ciclo cambia e il conto resta giusto senza pensarci.
#
# Prima del terzo ciclo, un contatore a zero (int):
#
#     chiamate = 0
#
# Dentro il terzo ciclo, allo stesso rientro della stampa del numero:
#
#     chiamate += 1
#
# In fondo, sotto il totale dei promemoria:
#
#     print(f"Chiamate al microfono: {chiamate}")
#
# Che cosa stampa, con 4:  "Chiamate al microfono: 2".
#
# TRABOCCHETTO: chiamate = 0 scritto DENTRO il ciclo lo azzera a ogni giro,
#   subito prima di incrementarlo. Sintomo: "Chiamate al microfono: 1"
#   qualunque sia il numero di appuntamenti. E con 0 appuntamenti il ciclo
#   non entra mai, il nome non riceve mai un valore, e il programma si
#   ferma sulla stampa finale con
#   UnboundLocalError: cannot access local variable 'chiamate'...
#   È il NameError del Cap. 4.2 visto da dentro una funzione.
# TRABOCCHETTO: chiamate += 1 tolto di quattro spazi esce dal ciclo e
#   viene eseguito una volta sola, dopo. Sintomo: i numeri chiamati sono
#   tutti al loro posto sopra, e il totale dice comunque 1.
