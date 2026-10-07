"""
SOLUZIONE — Esercizio 07.1: Il catalogo

IL PROBLEMA
Tenere un elenco di prodotti che si possa stampare numerato, allungare,
accorciare, interrogare e riordinare, senza che una modifica distrugga i
dati di partenza.

LA STRATEGIA
Una lista sola, modificata in sequenza dai quattro metodi della giornata,
e quattro funzioni di servizio.
- stampa_catalogo() viene chiamata tre volte su liste diverse: è la prova
  che una funzione con parametri serve a questo, non a fare scena.
- posizione_in_catalogo() risponde a "dov'è questo prodotto?" con un
  numero umano, contato da 1, perché è quello che dirà a voce l'addetto
  al magazzino. Dentro, il controllo con `in` viene prima di .index(): è
  l'ordine che evita l'unico errore possibile in questo esercizio.
- catalogo_ordinato() mostra la differenza fra chiedere una lista nuova e
  riordinare quella che si ha in mano. È la differenza fra cercare un
  prodotto a occhio e riordinare gli scaffali del magazzino.
- conta_nomi_lunghi() è il pattern del contatore: si azzera fuori dal
  ciclo, si incrementa dentro, si restituisce alla fine.

LIMITI NOTI DI QUESTA SOLUZIONE
- I prodotti sono scritti dentro il file, quindi ogni modifica al listino
  è una modifica al codice. Quando i dati arriveranno da un file, il
  programma resterà questo e cambierà solo la riga che riempie la lista.
- Il conteggio dei nomi lunghi conta i caratteri, spazi compresi, e non
  ha nessuna idea di che cosa sia una parola.
- posizione_in_catalogo() trova la PRIMA occorrenza. Se lo stesso
  prodotto fosse a catalogo due volte, la seconda sarebbe invisibile.

Concetti di teoria: cap. 3 (la lista), cap. 4 (modificare), cap. 6
(scorrere con enumerate), cap. 8 (sort contro sorted).
"""

PRODOTTI_INIZIALI = [
    "Cuffie Bluetooth",
    "Tastiera meccanica",
    "Mouse verticale",
    "Monitor 27 pollici",
    "Webcam HD",
    "Hub USB-C",
]
PRODOTTO_NUOVO = "Lampada da scrivania"
PRODOTTO_IN_TESTA = "Supporto monitor"
PRODOTTO_FUORI_LISTINO = "Webcam HD"
PRODOTTO_DA_CERCARE = "Mouse verticale"
LUNGHEZZA_NOME_LUNGO = 15
LARGHEZZA = 60
LARGHEZZA_ETICHETTA = 23


def stampa_catalogo(titolo, prodotti):
    """Stampa il titolo con il numero di prodotti e l'elenco numerato."""
    print(f"{titolo} ({len(prodotti)} prodotti)")
    # enumerate(prodotti, 1) fa partire il contatore da 1: l'alternativa
    # e' scrivere posizione + 1 dentro la f-string, e prima o poi ci si
    # dimentica il + 1 in uno dei punti in cui serve.
    # La funzione non sa da dove arriva la lista, e non le interessa: per
    # questo puo' stampare il catalogo vero, la sua copia ordinata e
    # qualunque altro elenco di stringhe senza che si tocchi una riga.
    for posizione, nome in enumerate(prodotti, 1):
        print(f"  {posizione}. {nome}")


def posizione_in_catalogo(prodotti, nome):
    """Posizione umana (da 1) del prodotto, oppure 0 se non c'è."""
    # TRABOCCHETTO: .index() su un nome che non c'e' ferma il programma con
    #   ValueError: list.index(x): x not in list. Per questo il controllo con
    #   `in` viene PRIMA, sempre: `in` non fallisce mai, .index() si'.
    # TRABOCCHETTO: 0 come ripiego funziona perche' nessuna posizione umana
    #   vale 0. Se al suo posto si restituisse -1, chi chiama potrebbe
    #   usarlo come indice senza accorgersene e leggerebbe l'ULTIMO
    #   prodotto: una risposta sbagliata invece di un errore, che e' il
    #   caso peggiore dei due.
    if nome in prodotti:
        return prodotti.index(nome) + 1
    return 0


def catalogo_ordinato(prodotti):
    """Copia ordinata in alfabetico: l'originale non viene toccato."""
    # TRABOCCHETTO: qui sorted(prodotti) e prodotti.sort() sembrano la
    #   stessa cosa e non lo sono. .sort() riordina IL catalogo, quindi
    #   "Supporto monitor" non sarebbe piu' il primo e la riga di controllo
    #   in main() stamperebbe "Cuffie Bluetooth": nessun errore, e gli
    #   scaffali del magazzino riordinati per sbaglio. E la variante
    #   `return prodotti.sort()` e' peggio ancora: .sort() non restituisce
    #   la lista, quindi chi chiama si ritrova un None in mano e il guaio
    #   esplode altrove, dentro stampa_catalogo(), su len(None).
    return sorted(prodotti)


def conta_nomi_lunghi(prodotti, soglia):
    """Stampa i nomi più lunghi della soglia e ne restituisce il numero."""
    # Il contatore si azzera QUI, fuori dal ciclo. Se si azzerasse dentro,
    # tornerebbe a zero a ogni giro e la funzione restituirebbe 0 oppure 1,
    # mentre le righe stampate sopra resterebbero quattro: il conto finale
    # smentirebbe l'elenco appena stampato, che e' il modo piu' rapido di
    # perdere la fiducia di chi legge il report.
    quanti = 0
    for nome in prodotti:
        # TRABOCCHETTO: "piu' lungo di quindici" e' > soglia, non >= soglia.
        #   "Mouse verticale" e' lungo esattamente 15 caratteri: con >= il
        #   conteggio passa da 4 a 5 e nessuno dei due numeri da' errore.
        #   Le soglie si sbagliano sempre sul caso che ci sta esatto sopra,
        #   ed e' sempre quello che nessuno prova.
        if len(nome) > soglia:
            print(f"  {nome:<20} {len(nome)} caratteri")
            quanti += 1
    return quanti


def riga_ricerca(nome, esito):
    """Compone una riga 'nome ..... esito' con i puntini di riempimento."""
    # I puntini si calcolano, non si scrivono a mano: cosi' la colonna
    # resta allineata anche se domani un prodotto cambia nome. Il - 1
    # tiene conto dello spazio che la f-string mette fra nome e puntini.
    puntini = "." * (LARGHEZZA_ETICHETTA - len(nome) - 1)
    return f"{nome} {puntini} {esito}"


def main():
    """Costruisce il catalogo NovaStore, lo modifica e lo interroga."""
    # La lista di lavoro parte da una COPIA fatta con lo slicing completo.
    # TRABOCCHETTO: senza [:], catalogo e PRODOTTI_INIZIALI sarebbero due
    #   etichette sullo stesso barattolo. Nessun errore, e il danno si
    #   vede solo alla fine: la costante che doveva restare la fotografia
    #   del listino di apertura si ritroverebbe "Supporto monitor" al primo
    #   posto e "Webcam HD" sparita, cioe' tutte le modifiche di oggi.
    catalogo = PRODOTTI_INIZIALI[:]

    print("=" * LARGHEZZA)
    print("NOVASTORE - Catalogo prodotti")
    print("=" * LARGHEZZA)
    stampa_catalogo("CATALOGO INIZIALE", catalogo)
    print("-" * LARGHEZZA)

    # Indice 0 il primo, indice -1 l'ultimo. L'indice negativo evita di
    # scrivere catalogo[len(catalogo) - 1], che e' giusto ma illeggibile,
    # e soprattutto evita catalogo[len(catalogo)], che e' l'errore vicino:
    # sei elementi hanno indici da 0 a 5, e l'indice 6 non esiste.
    print(f"Primo del catalogo .... {catalogo[0]}")
    print(f"Ultimo del catalogo ... {catalogo[-1]}")
    print(f"Prodotti in elenco .... {len(catalogo)}")
    print("-" * LARGHEZZA)

    print("MODIFICHE DI OGGI")
    # TRABOCCHETTO: .append() modifica la lista e restituisce None, quindi
    #   `catalogo = catalogo.append(...)` manda via la lista e lascia un
    #   None al suo posto. L'errore non si vede su questa riga e nemmeno
    #   sulla riga di log, che il catalogo non lo tocca: si vede alla
    #   prima riga che ci rimette le mani, cioe' l'insert qui sotto, con
    #   AttributeError: 'NoneType' object has no attribute 'insert'.
    #   Chi modifica non si assegna, ed e' la regola del capitolo 4.
    catalogo.append(PRODOTTO_NUOVO)
    print(f"[OK] append   -> {PRODOTTO_NUOVO} va in fondo")

    # insert(0, ...) infila in testa e fa scalare tutti gli altri di un
    # posto: la lista si allunga di uno. L'altra scrittura che viene in
    # mente, catalogo[0] = PRODOTTO_IN_TESTA, rimpiazza il primo prodotto
    # e la lista resta lunga uguale: "Cuffie Bluetooth" sparirebbe.
    catalogo.insert(0, PRODOTTO_IN_TESTA)
    print(f"[OK] insert   -> {PRODOTTO_IN_TESTA} va al primo posto")

    # .remove() lavora per VALORE e toglie soltanto la PRIMA occorrenza.
    # Se "Webcam HD" fosse a catalogo due volte, dopo questa riga ce ne
    # sarebbe ancora una e il conteggio direbbe 7 invece di 6, senza
    # nessun errore. Per togliere una POSIZIONE c'e' .pop(indice).
    catalogo.remove(PRODOTTO_FUORI_LISTINO)
    print(f"[OK] remove   -> {PRODOTTO_FUORI_LISTINO} esce dal listino")

    # TRABOCCHETTO: .pop() toglie l'ultimo E lo restituisce. Chi scrive
    #   catalogo.pop() senza salvare il risultato ha fatto la cosa giusta a
    #   meta': l'elemento e' sparito e non si puo' piu' nominare, quindi la
    #   riga di log qui sotto andrebbe scritta a mano e resterebbe ferma a
    #   un nome scritto a dito mentre il catalogo cambia.
    tolto = catalogo.pop()
    print(f"[OK] pop      -> tolto l'ultimo: {tolto}")
    print("-" * LARGHEZZA)

    stampa_catalogo("CATALOGO AGGIORNATO", catalogo)
    print("-" * LARGHEZZA)

    print("RICERCHE")
    # Il risultato si legge PRIMA di usarlo: 0 vuol dire "non trovato", e
    # solo nell'altro ramo il numero e' una posizione vera da stampare.
    # E' lo stesso schema che si ritrovera' con .get() sui dizionari.
    posizione = posizione_in_catalogo(catalogo, PRODOTTO_DA_CERCARE)
    if posizione == 0:
        print(riga_ricerca(PRODOTTO_DA_CERCARE, "non in catalogo"))
    else:
        print(riga_ricerca(PRODOTTO_DA_CERCARE,
                           f"in catalogo, posizione {posizione}"))

    # Seconda chiamata sulla stessa funzione, con il prodotto appena tolto
    # dal listino: e' il caso che porta al ramo del ripiego. Una funzione
    # si prova sempre su tutti e due i rami, non solo su quello buono.
    posizione = posizione_in_catalogo(catalogo, PRODOTTO_FUORI_LISTINO)
    if posizione == 0:
        print(riga_ricerca(PRODOTTO_FUORI_LISTINO, "non in catalogo"))
    else:
        print(riga_ricerca(PRODOTTO_FUORI_LISTINO,
                           f"in catalogo, posizione {posizione}"))
    print("-" * LARGHEZZA)

    # catalogo_ordinato() restituisce una lista NUOVA, e il catalogo vero
    # resta nell'ordine del magazzino, dove "Supporto monitor" sta per
    # primo perche' e' il primo scaffale che si incontra entrando.
    # L'ordine alfabetico serve a cercare a occhio, non a lavorare: sono
    # due ordini diversi per due usi diversi, e servono tutti e due.
    ordinato = catalogo_ordinato(catalogo)
    stampa_catalogo("CATALOGO IN ORDINE ALFABETICO", ordinato)
    # La prova che l'originale non e' stato toccato si fa guardando il suo
    # primo elemento: se qui comparisse "Cuffie Bluetooth", vorrebbe dire
    # che da qualche parte e' stato chiamato .sort() al posto di sorted().
    print("L'originale non è cambiato: al primo posto c'è ancora "
          f"{catalogo[0]}")
    print("-" * LARGHEZZA)

    print(f"NOMI PIÙ LUNGHI DI {LUNGHEZZA_NOME_LUNGO} CARATTERI")
    # Il numero delle righe stampate dalla funzione e il numero che la
    # funzione restituisce devono coincidere: sono la stessa informazione
    # detta due volte, una in elenco e una in sintesi. Quando su un report
    # i due numeri non coincidono, e' quasi sempre il contatore azzerato
    # nel posto sbagliato.
    lunghi = conta_nomi_lunghi(catalogo, LUNGHEZZA_NOME_LUNGO)
    print(riga_ricerca("Nomi lunghi", f"{lunghi} su {len(catalogo)}"))
    print("=" * LARGHEZZA)


if __name__ == "__main__":
    main()
