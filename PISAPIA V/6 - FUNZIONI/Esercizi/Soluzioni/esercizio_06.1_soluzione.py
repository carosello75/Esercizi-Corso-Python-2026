"""
SOLUZIONE — Esercizio 06.1: Le prime funzioni

Il problema: stampare tre preventivi identici nella forma e diversi nei dati,
senza ricopiare sei righe per ogni cliente e senza che l'aliquota IVA compaia
in più di un punto del file.

La strategia: tre funzioni, tre mestieri, e nessuno dei tre invade il
mestiere degli altri.

    saluta_cliente(nome)              stampa  ->  non restituisce niente
    calcola_iva(imponibile)           calcola ->  non stampa niente
    stampa_preventivo(nome, imp.)     compone ->  chiama le altre due

La distinzione fra le prime due è quella del capitolo 5, ed è quella su cui
si inciampa per tutta la giornata: una funzione che STAMPA vi fa vedere il
risultato, una funzione che RESTITUISCE ve lo mette in mano. Solo il secondo
si può sommare, confrontare, passare a qualcun altro.

La terza è la novità rispetto alla prima versione di questo esercizio, ed è
il motivo per cui main() si è accorciato: le sei righe del blocco preventivo
esistono una volta sola, e i clienti diventano una riga per uno. È la stessa
mossa che in 06.4 si fa su un programma intero (cap. 14), qui in piccolo.

Il controllo da fare quando avete finito: main() contiene un calcolo, un
importo o un'etichetta formattata? Se sì, il lavoro non è finito.

Concetti di teoria: cap. 3 (def, due punti, indentazione), cap. 4 (parametri
e argomenti), cap. 5 (return), cap. 6 (la funzione senza return e None),
cap. 7 (composizione), cap. 12 (verbo più oggetto), cap. 13 (docstring).
"""

# --- Costanti -----------------------------------------------------------
# L'aliquota compare in un punto solo di tutto il file. Il giorno che il
# legislatore la cambia si tocca questa riga e basta: il calcolo la legge
# dentro calcola_iva, l'etichetta la rilegge dentro stampa_preventivo, e
# nessuna delle due ha il numero 22 scritto a mano.
ALIQUOTA_IVA = 0.22

# Larghezza delle righe di separazione, comune agli esercizi della giornata.
LARGHEZZA = 60

# Gli imponibili delle tre richieste del mattino. Sono dati, non risultati:
# stanno in costanti perché main() deve poterli passare senza che nel corpo
# del programma compaia un numero senza nome.
IMPONIBILE_FERRI = 150.00
IMPONIBILE_CONTI = 250.00
IMPONIBILE_SETTE = 80.00


def saluta_cliente(nome):
    """Stampa la riga di saluto del preventivo. Non restituisce niente."""
    # Una riga sola nel corpo, e non c'è nessun return: questa funzione
    # lavora sullo standard output e al chiamante non consegna niente.
    # Chiamarla dentro una somma darebbe TypeError, perché il valore che
    # torna indietro è None (cap. 6.1).
    #
    # TRABOCCHETTO: sostituire print con return "spegne" la funzione senza
    #   rompere niente. Il programma gira, non dà nessun errore, e le tre
    #   righe "Buongiorno ..." spariscono dall'output: la stringa viene
    #   costruita, restituita a stampa_preventivo, e lì nessuno la prende.
    #   È il caso peggiore, perché il sintomo è un'assenza.
    print(f"Buongiorno {nome}, ecco il preventivo che ha chiesto.")


def calcola_iva(imponibile):
    """Restituisce l'IVA dovuta su un imponibile, senza stamparla."""
    # Nessuna print qui dentro, ed è voluto: chi calcola non decide come si
    # mostra il risultato. Questa funzione non sa se il numero finirà su uno
    # schermo, in una somma o in un file, e proprio per questo si riusa.
    #
    # TRABOCCHETTO: aggiungere una print "per vedere se funziona" e poi
    #   dimenticarla. La funzione continua a restituire il valore giusto, ma
    #   stampa una riga in più per ogni chiamata: con tre clienti, tre righe
    #   fantasma in mezzo ai preventivi. Per vedere se funziona si stampa
    #   dal chiamante, non da dentro (cap. 5.1).
    return imponibile * ALIQUOTA_IVA


def stampa_preventivo(nome, imponibile):
    """Stampa saluto, imponibile, IVA, totale e riga di chiusura."""
    # 1. Il saluto. Questa riga è una CHIAMATA: le parentesi ci sono e
    #    l'argomento è dentro.
    #
    # TRABOCCHETTO: scrivere saluta_cliente(nome) senza le parentesi, cioè
    #   la sola riga "saluta_cliente". Non è un errore per Python: è
    #   un'espressione che vale la funzione stessa, viene valutata e
    #   buttata via. Nessun messaggio, nessun saluto, e il preventivo
    #   comincia direttamente dall'imponibile (cap. 15, errore E5).
    saluta_cliente(nome)

    # 2. Il calcolo. Il valore restituito va SALVATO, altrimenti il
    #    risultato torna indietro e nessuno lo prende.
    #
    # TRABOCCHETTO: scrivere calcola_iva(imponibile) da sola, senza
    #   "iva =" davanti. L'IVA viene calcolata davvero, e poi buttata via.
    #   L'errore non esce su questa riga ma tre righe più sotto, quando il
    #   nome iva viene usato per la prima volta:
    #   NameError: name 'iva' is not defined
    #   Il nome non è mai assegnato in questo corpo, quindi Python lo cerca
    #   fuori dalla funzione e non lo trova. Se invece l'assegnazione c'è ma
    #   arriva DOPO l'uso, il messaggio cambia e diventa UnboundLocalError:
    #   sono due guasti diversi, e il messaggio vi dice quale dei due è.
    iva = calcola_iva(imponibile)

    # 3. Il totale si compone qui, dove i due pezzi sono già numeri.
    #
    # TRABOCCHETTO: imponibile + calcola_iva, senza parentesi e senza
    #   argomento. Qui l'errore arriva subito ed è esplicito:
    #   TypeError: unsupported operand type(s) for +: 'float' and 'function'
    #   "float and function" è la spia: state sommando un numero e una
    #   funzione, non un numero e il suo risultato. Le parentesi sono
    #   l'operatore che trasforma la seconda cosa nella prima.
    totale = imponibile + iva

    # 4. La presentazione. I puntini sono scritti a mano per tenere gli
    #    importi in colonna; :.2f fissa i due decimali, perché 17.6 su un
    #    preventivo si scrive 17.60.
    #
    # TRABOCCHETTO: scrivere "IVA 22%" a mano nell'etichetta. Il programma
    #   stampa la cosa giusta oggi e mente domani: portate ALIQUOTA_IVA a
    #   0.10 e il primo preventivo uscirà "IVA 22% .......... 15.00 euro",
    #   con l'etichetta che dice 22 e il numero accanto che vale il 10 per
    #   cento di 150. Lo specificatore
    #   :.0% moltiplica per cento, arrotonda a zero decimali e aggiunge il
    #   segno: 0.22 diventa la scritta 22%.
    print(f"Imponibile ....... {imponibile:.2f} euro")
    print(f"IVA {ALIQUOTA_IVA:.0%} .......... {iva:.2f} euro")
    print(f"Totale ........... {totale:.2f} euro")

    # 5. La riga di separazione chiude il blocco e sta qui dentro, non in
    #    main(): fa parte di "un preventivo stampato", e chi aggiunge un
    #    cliente non deve ricordarsi di scriverla.
    print("-" * LARGHEZZA)


def main():
    """Stampa i tre preventivi del mattino, uno per chiamata."""
    # TRABOCCHETTO: l'ordine in cui le tre funzioni sono scritte sopra NON
    #   conta, e conviene saperlo perché si sente dire il contrario. In un
    #   file fatto così, Python legge tutte le definizioni prima che
    #   qualcuno chiami main(), e a quel punto i tre nomi esistono già. Il
    #   NameError del capitolo 3.4 scatta solo se la chiamata è a colonna 0
    #   e sta SOPRA il def: qui l'unica chiamata a colonna 0 è l'ultima riga
    #   del file, e più in basso di così non si può andare.
    print("=" * LARGHEZZA)
    print("LOGISUD TRASPORTI - Preventivi del mattino")
    print("=" * LARGHEZZA)

    # Tre clienti, tre righe. Il blocco da sei righe che le stampa esiste
    # una volta sola: è questo il guadagno, e si misura provando ad
    # aggiungere un quarto cliente.
    stampa_preventivo("Marta Ferri", IMPONIBILE_FERRI)
    stampa_preventivo("Studio Legale Conti", IMPONIBILE_CONTI)
    stampa_preventivo("Panificio Sette", IMPONIBILE_SETTE)

    print("Tre preventivi, e il blocco che li stampa è scritto una volta sola.")
    print("=" * LARGHEZZA)


# Il programma parte solo se il file viene eseguito direttamente: è la
# formula fissa di ogni soluzione del corso.
if __name__ == "__main__":
    main()
