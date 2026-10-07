"""
SOLUZIONE — Esercizio 06.2: Lo sconto con il valore di default

Il problema: un listino in cui quasi tutti gli articoli prendono lo stesso
sconto, alcuni ne prendono uno diverso, uno non ne prende affatto, e su uno
si aggiunge un buono in euro. Chi scrive il listino deve poter tacere sul
caso normale e parlare solo quando si discosta.

La strategia: una sola funzione di calcolo con due parametri facoltativi.

    applica_sconto(prezzo, percentuale=..., buono=...)
        prezzo        obbligatorio   non esiste un prezzo "normale"
        percentuale   facoltativo    quasi sempre è quella di direzione
        buono         facoltativo    quasi sempre non c'è, e vale 0.0

La regola per decidere che cosa mettere a default è nel capitolo 8.3, e non
è "quello che capita più spesso" ma "quello che, se chi chiama tace, è la
scelta che avrebbe fatto comunque". Un prezzo non ce l'ha, uno sconto sì.

Le cinque chiamate sono scritte apposta in cinque forme diverse, e sono la
parte da leggere per ultima, riga per riga: sono il capitolo 9 in pratica.

Due parametri facoltativi al posto di uno è anche la dimostrazione del
perché servono. Il buono fedeltà è stato aggiunto alla funzione DOPO che le
altre quattro chiamate erano già scritte, e quelle quattro non sono state
toccate: continuano a funzionare come prima perché il nuovo parametro ha un
valore di partenza. Un parametro nuovo senza default le avrebbe rotte tutte
e quattro nello stesso istante.

Il limite di questa soluzione, dichiarato perché si vede: la funzione
restituisce il prezzo scontato e non dice quale sconto ha applicato, quindi
la colonna "Sconto%" va ristampata da fuori con lo stesso valore passato
dentro. La via d'uscita è il capitolo 10, restituire due valori insieme.

Concetti di teoria: cap. 5 (return), cap. 8 (valori di default, ordine dei
parametri, il default che nasconde un errore), cap. 9 (argomenti nominati),
cap. 12 (nomi che si spiegano da soli), cap. 13 (docstring che dichiara i
limiti).
"""

# --- Costanti -----------------------------------------------------------
# Lo sconto deciso dalla direzione. Sta in una costante perché finisce in
# due posti: nella riga del def come valore di partenza del parametro, e
# nella riga del listino delle Cuffie, che deve dire lo stesso numero.
PERCENTUALE_PREDEFINITA = 10

# Il buono fedeltà, in euro e non in percentuale: si toglie dopo lo sconto,
# a saldo già fatto.
BUONO_FEDELTA = 5.00

# Larghezza del listino: 22 + 8 + 8 + 10 sono esattamente 48, ed è il
# motivo per cui le righe di separazione combaciano con la tabella.
LARGHEZZA = 48

PREZZO_CUFFIE = 49.90
PREZZO_TASTIERA = 89.00
PREZZO_MONITOR = 219.00
PREZZO_HUB = 27.00
PREZZO_WEBCAM = 59.90

# Gli sconti diversi da quello standard. Le Cuffie non compaiono qui: il
# loro sconto è il default, e l'assenza di una costante SCONTO_CUFFIE è
# essa stessa un'informazione.
SCONTO_TASTIERA = 25
SCONTO_MONITOR = 50
SCONTO_HUB = 0
SCONTO_WEBCAM = 20


def applica_sconto(prezzo, percentuale=PERCENTUALE_PREDEFINITA, buono=0.0):
    """Restituisce il prezzo scontato; con sconti alti può andare sotto zero."""
    # 1. Lo sconto percentuale si calcola sul prezzo pieno.
    #
    # TRABOCCHETTO: l'uguale nella riga del def non è un'assegnazione che
    #   viene eseguita a ogni chiamata. È la dichiarazione di un valore di
    #   partenza, valutata una volta sola quando Python legge il def
    #   (cap. 8.5). Da quel momento PERCENTUALE_PREDEFINITA è congelato
    #   dentro la firma: cambiarlo più sotto nel programma non cambierebbe
    #   il comportamento della funzione.
    sconto = prezzo * percentuale / 100

    # 2. Il buono si toglie DOPO la percentuale, ed è l'ordine che la
    #    direzione ha deciso. Sembra un dettaglio e vale un euro tondo.
    #
    # TRABOCCHETTO: togliere prima il buono e poi la percentuale. Nessun
    #   errore, nessun avviso, un risultato diverso: la Webcam da 59.90
    #   diventerebbe 43.92 invece di 42.92, perché lo sconto del 20% si
    #   applicherebbe a 54.90 invece che a 59.90. Uno sconto sopra uno
    #   sconto non si somma: dipende dall'ordine.
    #
    # 3. La funzione non controlla che il risultato resti positivo: con
    #    percentuale=100 e un buono restituisce un numero negativo, e il
    #    listino stampa un prezzo sotto zero. Non è una svista, è una
    #    scelta dichiarata nella docstring (cap. 13.4): un limite scritto è
    #    un limite noto, un limite taciuto è una sorpresa.
    return prezzo - sconto - buono


def stampa_riga(nome, prezzo_pieno, percentuale, prezzo_scontato):
    """Stampa una riga del listino incolonnata. Non restituisce niente."""
    # Le larghezze stanno qui dentro: sono impaginazione, non regole
    # commerciali. Il nome a sinistra su 22, gli importi a destra con due
    # decimali, la percentuale a destra come intero.
    #
    # TRABOCCHETTO: dimenticare la larghezza e scrivere {percentuale} e
    #   basta. Il numero esce attaccato a quello prima e la riga delle
    #   Cuffie diventa "Cuffie Bluetooth         49.9010     44.91": senza
    #   la larghezza non c'è nessuna colonna, c'è solo testo messo di
    #   seguito. L'intestazione invece resta incolonnata, perché lì la
    #   larghezza l'avete scritta, e le due righe non combaciano più.
    print(f"{nome:<22}{prezzo_pieno:>8.2f}{percentuale:>8}{prezzo_scontato:>10.2f}")


def main():
    """Stampa il listino di fine stagione con cinque forme di chiamata."""
    print("=" * LARGHEZZA)
    print("NOVASTORE - Listino di fine stagione")
    print("=" * LARGHEZZA)
    print(f"{'Articolo':<22}{'Pieno':>8}{'Sconto%':>8}{'Da pagare':>10}")
    print("-" * LARGHEZZA)

    # Forma 1: un argomento solo. Gli altri due parametri non sono spariti
    # e non sono "vuoti": valgono il loro default, cioè 10 e 0.0. Chi legge
    # questa riga capisce "sconto standard" senza aprire la funzione.
    scontato_cuffie = applica_sconto(PREZZO_CUFFIE)

    # Forma 2: due argomenti posizionali. L'unica cosa che lega un valore
    # alla sua casella è la posizione, e la posizione la decide la riga del
    # def, non l'ordine in cui vengono in mente.
    #
    # TRABOCCHETTO: applica_sconto(SCONTO_TASTIERA, PREZZO_TASTIERA), cioè
    #   gli stessi due valori scambiati. Nessun errore: sono entrambi
    #   numeri e il conto si può fare. Calcola 25 meno l'89% di 25 e
    #   restituisce 2.75, che il listino stampa come prezzo da pagare di
    #   una tastiera meccanica. Il programma gira, il listino è sbagliato,
    #   e se ne accorge un cliente. È il motivo per cui esistono gli
    #   argomenti nominati (cap. 9.2).
    scontato_tastiera = applica_sconto(PREZZO_TASTIERA, SCONTO_TASTIERA)

    # Forma 3: il prezzo resta posizionale, la percentuale prende il nome.
    # È la forma mista del capitolo 9.3, ed è quella che si usa di più:
    # posizionale quello che è ovvio, nominato quello che è una scelta.
    scontato_monitor = applica_sconto(PREZZO_MONITOR, percentuale=SCONTO_MONITOR)

    # Forma 4: tutti e due nominati, e scritti in ordine invertito rispetto
    # alla definizione. Con i nomi l'ordine non conta più.
    #
    # TRABOCCHETTO: lo sconto zero va passato per forza. "Zero" e "non
    #   passare niente" sembrano la stessa cosa e sono l'opposto: senza
    #   quell'argomento entrerebbe in vigore il default del 10% e l'Hub
    #   USB-C finirebbe a 24.30 invece che a 27.00, in saldo senza che
    #   nessuno l'abbia deciso. È il caso del capitolo 8.4: un default
    #   comodo che copre un dato mancante.
    scontato_hub = applica_sconto(percentuale=SCONTO_HUB, prezzo=PREZZO_HUB)

    # Forma 5: due posizionali più il terzo parametro nominato. Il nome qui
    # non serve a Python — buono è il terzo e sarebbe arrivato lo stesso —
    # serve a chi legge: senza, la riga finirebbe con "20, 5.00" e nessuno
    # saprebbe che cos'è quel 5.
    #
    # TRABOCCHETTO: nominare un argomento e poi rimetterne uno posizionale
    #   dopo, per esempio applica_sconto(percentuale=20, PREZZO_WEBCAM).
    #   Python non arriva nemmeno a eseguire il file:
    #   SyntaxError: positional argument follows keyword argument
    #   Il motivo è meccanico: dopo un nome, la posizione non è più
    #   contabile, e Python non saprebbe in quale casella mettere il valore
    #   rimasto senza nome.
    scontato_webcam = applica_sconto(PREZZO_WEBCAM, SCONTO_WEBCAM,
                                     buono=BUONO_FEDELTA)

    # Le cinque righe del listino. La percentuale va ristampata da fuori,
    # perché la funzione restituisce solo il prezzo: è il limite dichiarato
    # in cima al file.
    #
    # TRABOCCHETTO: scrivere 10 a mano in questa prima riga invece di
    #   PERCENTUALE_PREDEFINITA. Il listino oggi è giusto e domani mente:
    #   portate la costante a 15 e la colonna Sconto% continuerà a dire 10
    #   accanto a un prezzo che è stato scontato del 15. Il numero applicato
    #   e il numero stampato devono venire dalla stessa fonte.
    stampa_riga("Cuffie Bluetooth", PREZZO_CUFFIE,
                PERCENTUALE_PREDEFINITA, scontato_cuffie)
    stampa_riga("Tastiera meccanica", PREZZO_TASTIERA,
                SCONTO_TASTIERA, scontato_tastiera)
    stampa_riga("Monitor 27 pollici", PREZZO_MONITOR,
                SCONTO_MONITOR, scontato_monitor)
    stampa_riga("Hub USB-C", PREZZO_HUB, SCONTO_HUB, scontato_hub)
    stampa_riga("Webcam HD", PREZZO_WEBCAM, SCONTO_WEBCAM, scontato_webcam)

    # I due totali. Le parentesi tonde tengono insieme l'espressione su due
    # righe senza bisogno di altro: dentro una parentesi aperta Python non
    # considera finita l'istruzione.
    totale_pieno = (PREZZO_CUFFIE + PREZZO_TASTIERA + PREZZO_MONITOR
                    + PREZZO_HUB + PREZZO_WEBCAM)
    totale_scontato = (scontato_cuffie + scontato_tastiera + scontato_monitor
                       + scontato_hub + scontato_webcam)

    print("-" * LARGHEZZA)
    # Il buono compare in una riga sua: nella colonna "Da pagare" della
    # Webcam è già stato tolto, ma la colonna "Sconto%" dice 20 e i conti a
    # occhio non tornerebbero. Una riga di scontrino che non si spiega da
    # sola è una telefonata all'assistenza.
    print(f"Buono fedeltà applicato .... {BUONO_FEDELTA:>6.2f}")
    print(f"Totale a prezzo pieno ...... {totale_pieno:.2f}")
    print(f"Totale da pagare ........... {totale_scontato:.2f}")
    print(f"Risparmio del cliente ...... {totale_pieno - totale_scontato:.2f}")
    print("=" * LARGHEZZA)


# Il programma parte solo se il file viene eseguito direttamente: è la
# formula fissa di ogni soluzione del corso.
if __name__ == "__main__":
    main()
