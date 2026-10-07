"""
SOLUZIONE — Esercizio 05.2: Il totale della spesa

Il problema: battere NUMERO_ARTICOLI prezzi uno alla volta, mostrare il
totale che cresce a ogni battuta e, alla fine, quattro numeri di riepilogo.

La strategia: un ciclo `for` su `range()` che a ogni giro legge un prezzo,
lo converte, lo usa e lo dimentica. Nessun prezzo viene conservato: ogni
giro lascia la sua traccia soltanto in quattro variabili di lavoro,
create PRIMA del ciclo, che sono i pattern del capitolo 6.
    totale         accumulatore  (float)  la somma dei prezzi visti
    articoli_cari  contatore     (int)    quanti hanno superato la soglia
    piu_caro       massimo       (float)  il prezzo più alto visto finora
    piu_economico  minimo        (float)  il prezzo più basso visto finora

Massimo e minimo sembrano simmetrici e non lo sono: il massimo può partire
da 0.0, il minimo no. È il punto più istruttivo dell'esercizio (Cap. 6.5).

L'aliquota IVA si chiede una volta sola, PRIMA del ciclo: vale per tutta la
cassa. Dopo il ciclo il totale lordo viene scorporato in imponibile e
imposta.

Perché `for` e non `while`: il numero di giri è fissato prima di partire,
ed è addirittura una costante. Quando si sa quante volte, `for` con
`range()` è la forma che non si può sbagliare nel conteggio (Cap. 11).

Che cosa sopravvive al ciclo: le quattro variabili di lavoro, che sono la
ragione per cui esistono fuori. Le variabili del giro — numero, testo,
prezzo — vengono riscritte a ogni battuta; dopo il ciclo nessuno le legge.

I bordi:
    un solo articolo     media, totale e più caro coincidono con il suo
                         prezzo: il programma non ha bisogno di casi a parte.
    nessuno sopra soglia il contatore resta 0, ed è quello che si stampa.
    NUMERO_ARTICOLI = 0  zero giri, e la media fa ZeroDivisionError. Qui
                         non succede perché la costante vale 5; in 05.3,
                         dove i giri dipendono dall'utente, servirà un if.

Concetti di teoria: Cap. 6 (contare, accumulare, tenere il massimo, e dove
si inizializza ciascuno) e Cap. 3 (`for` con `range` quando si sa quante
volte).
"""

# --- Costanti -----------------------------------------------------------
# Larghezza delle righe di separazione, comune agli esercizi della
# giornata.
LARGHEZZA = 60

# Quanti articoli batte la cassa di prova. Decide il numero di giri del
# ciclo, compare nell'intestazione e fa da divisore nella media: tre usi,
# un valore solo. Con 8 cambia tutto il programma da questa riga.
NUMERO_ARTICOLI = 5

# La soglia oltre la quale un articolo conta come "caro" nel report di fine
# turno. È un float perché si confronta con prezzi float, e perché la riga
# del riepilogo la stampa con due decimali: "Articoli sopra 50.00".
SOGLIA_ARTICOLO_CARO = 50.00


def main():
    """Batte cinque prezzi: totale, media, estremi, conteggio e IVA."""
    # 1. Intestazione. NUMERO_ARTICOLI compare due volte nel testo e non è
    #    mai scritto a mano: se la costante cambia, le frasi la seguono.
    print("=" * LARGHEZZA)
    print(f"NOVASTORE - Cassa: totale di {NUMERO_ARTICOLI} articoli")
    print("=" * LARGHEZZA)
    print(f"Batti il prezzo di {NUMERO_ARTICOLI} articoli, uno alla volta.")
    print()

    # 1b. L'aliquota IVA, chiesta UNA volta sola e prima del ciclo: vale per
    #     tutta la cassa, non per il singolo articolo. input() dà una str,
    #     "22"; int() la porta al numero 22, che serve al calcolo in fondo.
    #
    # TRABOCCHETTO: scrivere questa domanda DENTRO il ciclo. Il programma la
    #   ripete a ogni articolo: con cinque articoli, cinque volte
    #   "Aliquota IVA (%): ". Nessun errore, solo un cassiere esasperato.
    #   Una cosa che vale per tutti i giri si chiede prima del primo giro.
    # TRABOCCHETTO: dimenticare int(). aliquota resta la stringa "22", e
    #   l'errore non esce qui ma sulla riga dell'imponibile, molto più giù:
    #   TypeError: unsupported operand type(s) for /: 'str' and 'int'.
    #   Il messaggio indica il calcolo, ma lo sbaglio sta in questa lettura.
    aliquota = int(input("Aliquota IVA (%): ").strip())
    print()

    # 2. Le variabili di lavoro, create PRIMA del ciclo.
    #    Ognuna parte dal valore "neutro" per il suo compito: la somma di
    #    niente è 0.0, il conteggio di niente è 0.
    #
    # TRABOCCHETTO: queste righe stanno FUORI dal ciclo. Spostate dentro,
    #   vengono rieseguite a ogni giro e azzerano tutto quello che il giro
    #   precedente aveva accumulato. Sintomo: "Totale ... 59.90 EUR", cioè
    #   l'ultimo prezzo battuto, e "Articoli sopra 50.00 .. 1" al massimo.
    #   Nessun messaggio d'errore: solo numeri sbagliati, ed è per questo
    #   che è l'errore numero uno della giornata (Cap. 6.3).
    totale = 0.0
    articoli_cari = 0
    # Il massimo parte dal minimo possibile per un prezzo, cioè zero: così
    # il primo prezzo battuto lo supera di sicuro e diventa il primo "più
    # caro visto finora".
    #
    # TRABOCCHETTO: inizializzare il massimo a un numero alto, "per stare
    #   larghi". Con piu_caro = 999.0 nessun prezzo lo supera mai, l'if più
    #   sotto non scatta, e il riepilogo stampa
    #   "Articolo più caro ..... 999.00 EUR", un articolo che non esiste
    #   (Cap. 6.5). Per il minimo vale il ragionamento rovesciato.
    piu_caro = 0.0

    # Il minimo, e qui il valore di partenza è il punto di tutto. Per il
    # massimo 0.0 funziona perché ogni prezzo vero è più alto di zero e lo
    # sostituisce al primo giro. Per il minimo lo stesso trucco si rompe:
    # nessun prezzo è più BASSO di zero. Questo 0.0 quindi non viene MAI
    # usato come confronto: serve solo perché il nome esista prima del
    # ciclo, e al primo giro viene sostituito comunque (vedi 3e bis).
    piu_economico = 0.0

    # 3. Il ciclo.
    #    Che cosa ripete: leggi un prezzo, convertilo, aggiorna le tre
    #    variabili di lavoro, mostra il totale progressivo.
    #    Quando si ferma: dopo NUMERO_ARTICOLI giri. range(1, N + 1) conta
    #    da 1 a N compreso, perché il numero finisce nel prompt e alla
    #    cassa si comincia da "articolo 1", non da "articolo 0".
    #    Che cosa aggiorna: totale sempre, articoli_cari e piu_caro solo
    #    quando la loro condizione è vera.
    for numero in range(1, NUMERO_ARTICOLI + 1):
        # 3a. Lettura: input() restituisce SEMPRE una str, anche se chi
        #     batte digita soltanto cifre.
        testo = input(f"Prezzo articolo {numero} (EUR): ").strip()
        # 3b. Normalizzazione e conversione, in una riga:
        #       testo                    ->  "49,90"  (str)
        #       testo.replace(",", ".")  ->  "49.90"  (str)
        #       float(...)               ->   49.9    (float)
        #
        # TRABOCCHETTO: alla cassa si scrive "49,90", all'italiana. Senza
        #   il replace, float() si ferma con
        #   ValueError: could not convert string to float: '49,90'
        #   e il programma perde anche i prezzi già battuti. Il controllo
        #   completo del dato si costruisce in 05.4 e in 05.8; la gestione
        #   professionale degli errori non è materia di queste giornate.
        prezzo = float(testo.replace(",", "."))

        # 3c. L'accumulatore: il nuovo totale è il vecchio più il prezzo.
        #     La forma lunga e la forma += (Cap. 6.2) sono equivalenti;
        #     qui la lunga, perché dice ad alta voce che cosa succede.
        totale = totale + prezzo
        # 3d. Il contatore: aumenta di uno solo se il prezzo è caro.
        #
        # TRABOCCHETTO: >= e non >. Un articolo da 50.00 esatti, con >, non
        #   verrebbe contato: sintomo, il riepilogo dice un articolo in meno
        #   e nessuno se ne accorge finché non capita il prezzo tondo. La
        #   regola del report è "dalla soglia in su", e la condizione deve
        #   dire la stessa cosa, anche se l'etichetta dice "sopra".
        if prezzo >= SOGLIA_ARTICOLO_CARO:
            articoli_cari += 1
        # 3e. Il massimo: se questo prezzo batte il record, diventa il
        #     record. Qui > basta: a parità, il record non cambia valore.
        if prezzo > piu_caro:
            piu_caro = prezzo

        # 3e bis. Il minimo. Al primo giro numero == 1 è vero, e il minimo
        #     prende il primo prezzo VERO, qualunque sia; dal secondo giro in
        #     poi lo scalzano solo i prezzi più bassi. È la risposta alla
        #     domanda della traccia, «da quale valore si parte?»: dal primo
        #     dato, perché è l'unico valore sicuramente possibile. or è
        #     pigro (Giorno 04, Cap. 9): se numero == 1 è vero, il confronto
        #     con 0.0 non viene nemmeno valutato.
        #
        # TRABOCCHETTO: copiare il massimo e girare solo il verso, cioè
        #   if prezzo < piu_economico partendo da 0.0. Nessun prezzo è
        #   minore di zero, la condizione non è mai vera, e il riepilogo
        #   dice "Prezzo più basso ...... 0.00 EUR": un articolo gratis che
        #   nessuno ha battuto. Nessun errore, solo un numero falso.
        # TRABOCCHETTO: partire da un numero «impossibile», come 999999.0.
        #   Funziona finché qualcuno non batte un articolo che costa di più,
        #   ed è un numero magico che non dice che cosa significa.
        if numero == 1 or prezzo < piu_economico:
            piu_economico = prezzo

        # 3f. Il totale progressivo sta DENTRO il ciclo, allo stesso rientro
        #     delle righe sopra: esce una volta per articolo, come il display
        #     del supermercato. Tolto di un rientro, uscirebbe una volta sola,
        #     dopo l'ultimo prezzo. {totale:.2f} fissa due decimali: senza,
        #     un float può mostrare una coda di cifre che su uno scontrino
        #     non si stampa.
        print(f"  [OK] totale progressivo: {totale:.2f} EUR")

    # 4. Dopo il ciclo. La media si calcola qui, una volta sola, perché
    #    serve il totale completo: calcolata dentro il ciclo sarebbe la
    #    media parziale di ogni giro, rifatta cinque volte per niente.
    #    Il divisore è sicuramente diverso da zero perché è la costante 5.
    #
    # TRABOCCHETTO: dividere per numero, la variabile del ciclo, invece che
    #   per NUMERO_ARTICOLI. Qui funziona per caso, perché all'ultimo giro
    #   numero vale 5. Basta riscrivere il ciclo come range(NUMERO_ARTICOLI),
    #   che conta da 0 a 4, e numero finisce a 4: la media esce più alta di
    #   un quarto, senza nessun errore a schermo (Cap. 4.1).
    media = totale / NUMERO_ARTICOLI

    # 4 bis. Lo scorporo dell'IVA. I prezzi del cartellino sono GIÀ
    #     comprensivi di imposta: il totale va scorporato, non maggiorato.
    #     L'IVA si calcola sull'imponibile, quindi lordo = imponibile x 1.22
    #     e, al contrario, imponibile = lordo / 1.22. aliquota / 100 porta
    #     22 a 0.22. L'imposta è quello che avanza: lordo meno imponibile.
    #     Con i dati dell'esempio: 452.30 / 1.22 = 370.74 e 452.30 - 370.74
    #     = 81.56. La somma dei due torna al totale, ed è il controllo da
    #     fare a occhio ogni volta.
    #
    # TRABOCCHETTO: scorporare come uno sconto, totale * (1 - aliquota /
    #   100). Sembra la stessa cosa e toglie il 22% del LORDO, non l'IVA che
    #   c'è dentro. Sintomo: imponibile 352.79 e imposta 99.51, entrambi
    #   sbagliati di quasi 18 euro, e nessuno se ne accorge fino alla
    #   dichiarazione. Il 22% va tolto dall'imponibile, che è più piccolo
    #   del lordo: per tornarci si divide per 1.22, non si toglie il 22%.
    imponibile = totale / (1 + aliquota / 100)
    imposta = totale - imponibile

    # 5. Il riepilogo. I puntini sono scritti a mano per allineare i valori
    #    in colonna. Le variabili di lavoro vengono lette qui per la
    #    prima e unica volta fuori dal ciclo: è per questo che esistevano.
    print()
    print("-" * LARGHEZZA)
    print(f"Articoli battuti ...... {NUMERO_ARTICOLI}")
    print(f"Totale ................ {totale:.2f} EUR")
    print(f"Prezzo medio .......... {media:.2f} EUR")
    print(f"Articolo più caro ..... {piu_caro:.2f} EUR")
    print(f"Prezzo più basso ...... {piu_economico:.2f} EUR")
    # articoli_cari è un int: niente :.2f, perché tre articoli non sono
    # 3.00 articoli. La soglia invece è un importo, e i decimali li vuole.
    print(f"Articoli sopra {SOGLIA_ARTICOLO_CARO:.2f} .. {articoli_cari}")
    print(f"Imponibile ............ {imponibile:.2f} EUR")
    print(f"Imposta ............... {imposta:.2f} EUR")
    print("-" * LARGHEZZA)


# Il programma parte solo se il file viene eseguito direttamente: è la
# formula fissa di ogni soluzione del corso.
if __name__ == "__main__":
    main()
