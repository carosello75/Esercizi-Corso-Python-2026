"""
SOLUZIONE — Esercizio 07.4: Il listino

IL PROBLEMA
Il prezzo di una zona è una coppia nome-valore. Finora lo si cercava in
una catena di if lunga venti righe, e ogni volta che cambiava una tariffa
bisognava rileggerla tutta per capire dove mettere le mani. Qui non serve
un elenco ordinato, serve una rubrica: il listino diventa un dizionario e
aggiungere l'ESTERO costa una riga.

LA STRATEGIA
Un dizionario zona -> prezzo, e due modi diversi di leggerlo, scelti
apposta e non per gusto.
- L'accesso diretto listino["SUD"] si usa quando la chiave DEVE esserci:
  se non c'è, il programma si ferma, ed è giusto così, perché significa
  che i dati sono rotti e continuare vorrebbe dire stampare un preventivo
  sbagliato.
- Il .get() si usa quando la chiave può mancare per motivi legittimi:
  l'ESTERO non è a listino e non è un errore, è una zona da preventivare
  a mano. Sapere quale dei due usare è tutto il capitolo 11.
Il secondo dizionario, i pesi massimi, serve a mostrare la cosa che con
due liste parallele non si può fare: due rubriche sulle stesse chiavi si
interrogano insieme senza doverle tenere allineate a mano, e a una delle
due può legittimamente mancare una voce. Il terzo, i giorni di consegna,
serve a mostrare che le rubriche restano indipendenti fra loro: i buchi
dell'una non sono quelli dell'altra, e la riga si compone lo stesso
perché a decidere che cosa scrivere è .get(), una rubrica per volta.

Le due funzioni gemelle, zona_piu_cara() e zona_meno_cara(), sono il
punto in cui si paga la fretta: fra l'una e l'altra cambiano insieme il
verso del confronto E il valore da cui il confronto parte. Chi ne cambia
uno solo ottiene una risposta sbagliata senza nessun errore.

LIMITI NOTI DI QUESTA SOLUZIONE
- Le chiavi sono scritte a mano in maiuscolo. Un dato che arrivasse da
  fuori andrebbe normalizzato con .strip() e .upper() PRIMA di cercarlo,
  o "sud " e "SUD" sarebbero due zone diverse.
- zona_piu_cara() parte da zero come massimo: funziona perché i prezzi
  sono tutti positivi. Su un listino di sconti, con valori negativi,
  restituirebbe il ripiego invece della zona meno negativa.
- zona_meno_cara() parte da una soglia più alta di qualunque tariffa, ed
  è una scommessa sul fatto che nessun prezzo la superi: su un listino
  di trasporti eccezionali andrebbe rialzata. La strada che non
  scommette è far partire il confronto dal primo prezzo incontrato, al
  costo di un indicatore in più da gestire dentro il ciclo.
- La riga a tre colonne fa crescere la firma della funzione di un
  parametro per ogni rubrica aggiunta. Alla quarta informazione per zona
  la strada giusta non è più questa, ma tenere insieme i dati della
  stessa zona invece di sparpagliarli su rubriche parallele.
- Se due zone avessero lo stesso prezzo massimo, verrebbe nominata la
  prima incontrata, cioè la prima inserita.
- Il peso massimo dell'ESTERO non esiste e viene stampato come testo: la
  colonna dei pesi contiene numeri e una scritta, quindi non ci si
  possono fare conti sopra.

Concetti di teoria: cap. 10 (il dizionario), cap. 11 (.get(), nuove
chiavi, in, .items()).
"""

LISTINO_INIZIALE = {
    "NORD": 8.50,
    "CENTRO": 7.00,
    "SUD": 9.50,
    "ISOLE": 14.00,
}
PESI_MASSIMI = {
    "NORD": 30,
    "CENTRO": 30,
    "SUD": 25,
    "ISOLE": 20,
}
GIORNI_CONSEGNA = {
    "NORD": 2,
    "CENTRO": 2,
    "SUD": 3,
    "ISOLE": 5,
    "ESTERO": 8,
}
ZONA_NOTA = "SUD"
ZONA_IGNOTA = "ESTERO"
ZONA_NUOVA = "ESTERO"
PREZZO_ZONA_NUOVA = 22.00
ZONA_DA_AUMENTARE = "ISOLE"
AUMENTO = 1.10
TESTO_RIPIEGO = "non a listino, prezzo da concordare"
PESO_NON_DICHIARATO = "n.d."
# Stesso testo del ripiego dei pesi, ma costante diversa apposta: il
# ripiego di una colonna e' una decisione di quella colonna, e quando i
# giorni mancanti andranno scritti "su richiesta" si cambia questa riga
# sola, senza toccare la colonna dei pesi. Due costanti con lo stesso
# valore non sono una duplicazione se rispondono a due domande diverse.
GIORNI_NON_DICHIARATI = "n.d."
ZONA_NON_TROVATA = "nessuna"
PREZZO_PIU_BASSO_POSSIBILE = 0.0
# La partenza del confronto per il MINIMO, ed e' l'opposto della riga
# qui sopra: una soglia piu' alta di qualunque tariffa a listino, che la
# prima zona incontrata abbassa subito. Il perche' non possa essere zero
# sta dentro zona_meno_cara().
PREZZO_PIU_ALTO_POSSIBILE = 999999.99
ZONA_DA_TOGLIERE = "NORD"
LARGHEZZA = 60
LARGHEZZA_ETICHETTA = 22


def stampa_listino(titolo, prezzi):
    """Stampa il titolo con il numero di zone e una riga per ogni coppia."""
    print(f"{titolo} ({len(prezzi)} zone)")
    # .items() restituisce le coppie, e l'unpacking le divide in due nomi.
    # Senza .items() il for darebbe solo le chiavi e servirebbe un secondo
    # accesso al dizionario per ogni giro: funziona, ma e' lavoro doppio.
    # Il nome dei due contenitori qui e' zona e prezzo, non chiave e
    # valore: il codice si legge meglio quando i nomi dicono il mestiere.
    for zona, prezzo in prezzi.items():
        print(f"  {zona:<7} .... {prezzo:>5.2f} euro")


def stampa_prezzi_pesi_e_giorni(prezzi, pesi, giorni):
    """Stampa prezzo, peso massimo e giorni di consegna di ogni zona."""
    # DECISIONE: questa funzione stampava due rubriche ed e' stata estesa
    # alla terza, invece di scriverne accanto una seconda quasi identica.
    # Due funzioni gemelle vanno corrette due volte e una delle due la si
    # dimentica: e' il difetto che l'esercizio 07.8 fa toccare con mano.
    # Il prezzo da pagare e' la firma, che cresce di un parametro per
    # ogni rubrica: la scelta regge a tre, a cinque non reggerebbe piu'.
    # L'intestazione usa gli stessi formati delle righe qui sotto, con un
    # testo al posto del numero: e' cosi' che le colonne restano sotto il
    # loro titolo senza contare gli spazi a mano.
    print(f"  {'ZONA':<7} {'PREZZO':>11}   {'KG MAX':>7}   {'GIORNI':>6}")
    for zona, prezzo in prezzi.items():
        # Il ciclo scorre il LISTINO: e' lui a decidere quali righe
        # esistono. Le altre due rubriche vengono interrogate per chiave,
        # e ognuna ha i buchi suoi: l'ESTERO un peso massimo non ce l'ha,
        # i giorni di consegna si'. .get() con ripiego e' esattamente il
        # caso per cui esiste: la riga si stampa lo stesso e dichiara
        # quale dato manca, invece di far sparire l'intera zona.
        peso = pesi.get(zona, PESO_NON_DICHIARATO)
        giorni_zona = giorni.get(zona, GIORNI_NON_DICHIARATI)
        # TRABOCCHETTO: la colonna dei pesi contiene numeri interi e, per
        #   una zona, un testo. Il formato :>7 funziona su tutti e due
        #   perche' non dice di che tipo sia il dato. Scrivendo :>7.0f,
        #   che e' quello che viene in mente per incolonnare numeri, la
        #   riga dell'ESTERO si fermerebbe con
        #   ValueError: Unknown format code 'f' for object of type 'str'.
        #   Una colonna mista numeri-e-testo si stampa, ma non si somma.
        # TRABOCCHETTO: con l'accesso diretto pesi[zona] al posto di
        #   .get() questa riga si fermerebbe due volte per due motivi
        #   diversi. Alla prima chiamata su KeyError: 'ESTERO', per una
        #   zona che un peso non l'ha mai avuto; e se anche l'ESTERO
        #   avesse il suo, alla seconda chiamata su KeyError: 'NORD',
        #   per un peso che c'era e non c'e' piu'. La stessa riga passa e
        #   poi esplode: .get() e' l'unica forma che regge tutti e due i
        #   casi senza sapere in anticipo quale dei due si presentera'.
        print(f"  {zona:<7} {prezzo:>6.2f} euro   {peso:>7}   {giorni_zona:>6}")


def riga_etichetta(testo, valore):
    """Compone 'testo ..... valore' con i puntini di riempimento."""
    # La lunghezza dei puntini si calcola dall'etichetta, cosi' la colonna
    # dei valori resta allineata anche quando si aggiunge una voce con un
    # nome piu' lungo. Il - 1 tiene conto dello spazio che la f-string
    # qui sotto mette fra il testo e i puntini.
    puntini = "." * (LARGHEZZA_ETICHETTA - len(testo) - 1)
    return f"{testo} {puntini} {valore}"


def zona_piu_cara(prezzi):
    """Nome della zona col prezzo più alto, scorrendo le coppie del listino."""
    # E' il pattern dell'accumulatore visto sui cicli: si tiene da parte il
    # migliore trovato finora e lo si sostituisce solo quando ne arriva uno
    # migliore. Serve perche' max(prezzi.values()) da' il PREZZO e non la
    # ZONA: lo stesso problema del mese peggiore nell'esercizio 07.3.
    # TRABOCCHETTO: queste due righe stanno fuori dal ciclo. Spostandole
    #   dentro, il massimo si azzererebbe a ogni giro e la funzione
    #   restituirebbe sempre l'ULTIMA zona del dizionario. Su questi dati
    #   l'ultima zona e' ESTERO, che e' anche la risposta giusta: il
    #   difetto darebbe il risultato corretto e resterebbe li' finche' non
    #   arriva un listino in cui l'ultima zona non e' la piu' cara.
    zona_cara = ZONA_NON_TROVATA
    prezzo_massimo = PREZZO_PIU_BASSO_POSSIBILE
    for zona, prezzo in prezzi.items():
        if prezzo > prezzo_massimo:
            prezzo_massimo = prezzo
            zona_cara = zona
    return zona_cara


def zona_meno_cara(prezzi):
    """Nome della zona col prezzo più basso: la gemella di zona_piu_cara."""
    # La gemella non si ottiene girando il segno del confronto e basta.
    # Le righe da cambiare sono DUE, e la seconda e' quella che nessuno
    # guarda: il valore da cui il confronto parte. Lo zero e' una
    # partenza sicura per il massimo, perche' un prezzo negativo non
    # esiste e quindi la prima zona lo supera di certo; per il minimo e'
    # la partenza peggiore possibile, perche' nessun prezzo riesce a
    # scendere sotto zero e il confronto non scatta mai. Qui si parte
    # dall'alto, da una soglia che la prima zona abbassa subito.
    # TRABOCCHETTO: lasciando PREZZO_PIU_BASSO_POSSIBILE come partenza,
    #   il ciclo gira su tutte le zone senza entrare mai nell'if e la
    #   funzione restituisce il ripiego: la riga dei conti stampa
    #   Zona meno cara ....... nessuna
    #   e il programma arriva in fondo senza un errore. Il ripiego esce
    #   come se fosse una risposta, ed e' il difetto che in ufficio
    #   sopravvive piu' a lungo, perche' non fa rumore.
    zona_economica = ZONA_NON_TROVATA
    prezzo_minimo = PREZZO_PIU_ALTO_POSSIBILE
    for zona, prezzo in prezzi.items():
        # TRABOCCHETTO: la copia incompleta piu' insidiosa e' quella che
        #   cambia i nomi e lascia tutto il resto, cioe' lo zero di
        #   partenza E il > di zona_piu_cara(). Non esce nessun errore e
        #   non esce nemmeno il ripiego: esce ESTERO, esattamente la
        #   stessa zona che la riga della zona piu' cara stampa poco
        #   sopra. Due etichette opposte con la stessa risposta: si vede
        #   solo leggendo le due righe una accanto all'altra, ed e' il
        #   motivo per cui vengono stampate vicine.
        if prezzo < prezzo_minimo:
            prezzo_minimo = prezzo
            zona_economica = zona
    return zona_economica


def pesi_senza(pesi, zona_esclusa):
    """Copia dei pesi priva di una zona, ricostruita coppia per coppia."""
    # Per togliere una chiave da un dizionario esiste un'istruzione
    # apposita, che pero' non e' materia di questa giornata: qui si parte
    # da un dizionario vuoto e ci si copiano dentro tutte le coppie
    # tranne una. Il risultato e' lo stesso a un dettaglio decisivo:
    # l'originale non viene toccato, e infatti il programma alla fine
    # ristampa quante zone hanno ancora un peso nella costante.
    rimasti = {}
    for zona, peso in pesi.items():
        # Il filtro e' tutto qui: la coppia entra nel dizionario nuovo
        # solo se la chiave non e' quella da escludere. Assegnare a una
        # chiave che non c'e' la crea, e nessuna riga in piu' serve.
        if zona != zona_esclusa:
            rimasti[zona] = peso
    # TRABOCCHETTO: questa funzione restituisce un dizionario NUOVO, non
    #   modifica quello ricevuto. Chi la chiama e poi ristampa passando
    #   ancora PESI_MASSIMI vede la seconda tabella identica alla prima,
    #   con il NORD che dichiara ancora 30, e nessun errore: sembra che
    #   la funzione non abbia funzionato, mentre e' la chiamata che butta
    #   via il risultato. Il segnale che lo smaschera e' due righe sotto:
    #   la tabella mostra cinque zone col peso, e "Pesi dopo il taglio"
    #   continua a dire 3, perche' quel numero viene dal dizionario nuovo
    #   che nessuno ha stampato. Due numeri che si contraddicono nella
    #   stessa schermata. E' lo stesso inganno di sorted() contro sort()
    #   del capitolo 8, con i dizionari al posto delle liste.
    return rimasti


def aumenta(prezzi, zona, moltiplicatore):
    """Aumenta il prezzo di una zona e restituisce vecchio e nuovo prezzo."""
    # Il vecchio prezzo si legge PRIMA di sovrascriverlo: dopo la riga di
    # assegnazione non esiste piu' da nessuna parte, e la riga di log che
    # dice "da 14.00 a 15.40" non si potrebbe piu' scrivere.
    vecchio = prezzi[zona]
    # TRABOCCHETTO: 14.00 * 1.10 in Python fa 15.400000000000002, non
    #   15.40. E' il righello con le tacche del Giorno 02. Il round a due
    #   decimali qui non e' cosmetica: senza, il valore SALVATO nel listino
    #   sarebbe quello lungo, la ristampa con :>5.2f lo nasconderebbe, e la
    #   coda di decimali salterebbe fuori nella somma finale.
    nuovo = round(vecchio * moltiplicatore, 2)
    prezzi[zona] = nuovo
    # Due valori restituiti insieme, che chi chiama divide in due nomi:
    # sono il prima e il dopo della stessa modifica, e separarli in due
    # funzioni vorrebbe dire leggere il listino due volte.
    return vecchio, nuovo


def main():
    """Costruisce il listino LogiSud, lo interroga e lo aggiorna."""
    # dict(...) fa una copia del dizionario di partenza, come [:] per le
    # liste: la costante resta il listino di inizio giornata. La stessa
    # copia la fa LISTINO_INIZIALE.copy(), che e' la forma che si incontra
    # piu' spesso: due strade per lo stesso risultato, e ne basta una.
    # TRABOCCHETTO: senza dict(...) i due nomi indicherebbero lo stesso
    #   dizionario e l'aumento dell'ISOLE finirebbe dentro
    #   LISTINO_INIZIALE. Nessun errore, e la tariffa di partenza, 14.00,
    #   resterebbe scritta soltanto nella riga di log gia' stampata: da
    #   nessuna parte nel programma si potrebbe piu' recuperare.
    listino = dict(LISTINO_INIZIALE)
    print("=" * LARGHEZZA)
    print("LOGISUD TRASPORTI - Listino per zona")
    print("=" * LARGHEZZA)
    stampa_listino("LISTINO DI PARTENZA", listino)
    print("-" * LARGHEZZA)

    print("RICERCHE NEL LISTINO")
    # Accesso diretto: la zona SUD deve esserci. Se un giorno sparisse, il
    # KeyError e' l'informazione che vogliamo, non un fastidio.
    prezzo_noto = listino[ZONA_NOTA]
    print(riga_etichetta(f"Zona {ZONA_NOTA}", f"{prezzo_noto:.2f} euro"))

    # TRABOCCHETTO: qui l'accesso diretto listino["ESTERO"] fermerebbe il
    #   programma con KeyError: 'ESTERO', e il preventivo non uscirebbe.
    #   Ma il ripiego va SCRITTO: .get(ZONA_IGNOTA) senza secondo
    #   argomento restituisce None senza fermarsi, e questa riga
    #   stamperebbe la parola None al posto del prezzo: un preventivo
    #   consegnabile e sbagliato. Peggio ancora se il None finisse in un
    #   formato numerico come quello della riga qui sopra: li' si
    #   fermerebbe con
    #   TypeError: unsupported format string passed to NoneType.__format__.
    prezzo_ignoto = listino.get(ZONA_IGNOTA, TESTO_RIPIEGO)
    print(riga_etichetta(f"Zona {ZONA_IGNOTA}", prezzo_ignoto))

    print(f"'CENTRO' è una chiave? {'CENTRO' in listino}")
    # TRABOCCHETTO: le chiavi distinguono maiuscole e minuscole. "estero" e
    #   "ESTERO" sono due chiavi diverse come due nomi diversi in rubrica,
    #   e questa riga stampa False anche dopo che l'ESTERO e' stato
    #   aggiunto. E' la causa numero uno dei "ma io ce l'avevo messo" in
    #   aula: la cura e' normalizzare la chiave quando ENTRA.
    print(f"'estero' è una chiave? {'estero' in listino}")
    print("-" * LARGHEZZA)

    print("AGGIORNAMENTI")
    # Per aggiungere una chiave si assegna e basta: non esiste un metodo
    # .aggiungi(). Se la chiave c'era gia', il valore viene sovrascritto
    # senza avvisare, ed e' la stessa identica riga: inserire e
    # sovrascrivere si scrivono uguale, e solo chi scrive sa quale delle
    # due cose sta facendo.
    listino[ZONA_NUOVA] = PREZZO_ZONA_NUOVA
    print(f"[OK] Nuova zona {ZONA_NUOVA} a {PREZZO_ZONA_NUOVA:.2f} euro")

    vecchio, nuovo = aumenta(listino, ZONA_DA_AUMENTARE, AUMENTO)
    print(f"[!] {ZONA_DA_AUMENTARE} aumenta del 10%: da {vecchio:.2f} a "
          f"{nuovo:.2f} euro")
    print("-" * LARGHEZZA)

    stampa_listino("LISTINO AGGIORNATO", listino)
    print("-" * LARGHEZZA)
    print("Le zone escono nell'ordine in cui sono state inserite, non in")
    print("ordine alfabetico. In ordine alfabetico sarebbero:")
    # sorted() sulle chiavi restituisce una LISTA nuova: il dizionario non
    # viene riordinato, e infatti la stampa qui sopra resta in ordine di
    # inserimento. Il join incolla gli elementi con la virgola e lo spazio.
    print(f"  {', '.join(sorted(listino.keys()))}")
    print("-" * LARGHEZZA)

    print("PREZZO, PESO MASSIMO (kg) E GIORNI DI CONSEGNA")
    # Tre dizionari sulle stesse chiavi, interrogati insieme. Con tre
    # liste parallele questo pezzo funzionerebbe solo finche' nessuno
    # inserisce una zona in una sola delle tre: qui invece ogni rubrica
    # ha i buchi suoi e nessuno di quei buchi rompe la riga, perche' e'
    # .get() a decidere che cosa scrivere quando il dato non c'e'.
    stampa_prezzi_pesi_e_giorni(listino, PESI_MASSIMI, GIORNI_CONSEGNA)
    print("-" * LARGHEZZA)

    print(f"LA STESSA TABELLA SENZA IL PESO DEL {ZONA_DA_TOGLIERE}")
    # Il caso della zona che un peso non l'ha mai avuto lo ha gia'
    # mostrato l'ESTERO. Questo e' il caso opposto, e in ufficio e' il
    # piu' frequente: il dato c'era, qualcuno lo toglie, e il preventivo
    # deve continuare a uscire. Cambia il dizionario, non la funzione che
    # lo legge: la tabella qui sotto e' stampata dalla stessa riga di
    # codice di quella qui sopra, con un argomento diverso.
    pesi_ridotti = pesi_senza(PESI_MASSIMI, ZONA_DA_TOGLIERE)
    stampa_prezzi_pesi_e_giorni(listino, pesi_ridotti, GIORNI_CONSEGNA)
    # Le due lunghezze sono la prova che pesi_senza() ha costruito un
    # dizionario nuovo invece di intervenire su quello ricevuto: la
    # costante ha ancora tutte e quattro le sue zone, e un secondo
    # preventivo che partisse da li' ripartirebbe dai dati interi.
    print(riga_etichetta("Pesi dopo il taglio", len(pesi_ridotti)))
    print(riga_etichetta("Pesi nella costante", len(PESI_MASSIMI)))
    print("-" * LARGHEZZA)

    print("CONTI SUL LISTINO")
    # .values() non e' una lista: e' una vista sui valori, sempre
    # aggiornata. Qui va benissimo perche' serve solo per sum, max e min,
    # ma prezzi[0] si fermerebbe con
    # TypeError: 'dict_values' object is not subscriptable: un dizionario
    # non ha posizioni, ha chiavi.
    prezzi = listino.values()
    somma = sum(prezzi)
    # TRABOCCHETTO: len(listino) e sum(listino.values()) rispondono a due
    #   domande diverse e danno 5 e 62.40. Chiamare "totale" il primo dei
    #   due e' l'errore che manda in riunione il numero sbagliato, e non e'
    #   un errore di Python: il nome della variabile deve dire QUALE delle
    #   due domande e' stata fatta.
    print(riga_etichetta("Zone a listino", len(listino)))
    print(riga_etichetta("Somma dei prezzi", f"{somma:>5.2f} euro"))
    print(riga_etichetta("Prezzo medio", f"{somma / len(listino):>5.2f} euro"))
    print(riga_etichetta("Prezzo più alto", f"{max(prezzi):>5.2f} euro"))
    # Il prezzo piu' alto e la zona piu' cara sono due risposte diverse
    # alla stessa curiosita', e servono tutte e due: il numero per il
    # conto, il nome per la telefonata al commerciale.
    print(riga_etichetta("Zona più cara", zona_piu_cara(listino)))
    print(riga_etichetta("Prezzo più basso", f"{min(prezzi):>5.2f} euro"))
    # Stessa coppia numero-nome della zona piu' cara, e le due righe
    # stanno vicine apposta: e' leggendole insieme che si vede subito se
    # la gemella e' stata scritta o soltanto copiata. Se qui comparisse
    # ESTERO, cioe' la zona piu' cara, il verso del confronto e' rimasto
    # quello di prima.
    print(riga_etichetta("Zona meno cara", zona_meno_cara(listino)))
    print("=" * LARGHEZZA)


if __name__ == "__main__":
    main()
