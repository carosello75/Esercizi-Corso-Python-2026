"""
SOLUZIONE — Esercizio 10.2: Il rimborso chilometrico

IL PROBLEMA
Quattro dati scritti da una persona, e ognuno può essere sbagliato in un
modo suo: il nome in minuscolo (da riparare), il veicolo che non esiste (da
rifiutare), i km e il pedaggio con la virgola (da riparare) o fuori misura
(da rifiutare). La differenza fra riparare e rifiutare è il cuore del modulo:
si ripara ciò che è un'abitudine di chi scrive, si rifiuta ciò che è un
dato impossibile.

LA STRATEGIA: UN CONTROLLO PER CAMPO, GLI ERRORI IN UNA LISTA
Ogni campo ha la sua funzione di controllo, che restituisce SEMPRE due
cose: il valore ripulito e l'errore (una coppia problema/rimedio, oppure
None se il campo va bene). È il pattern P7 con la "variabile errore",
moltiplicato per quattro: main() raccoglie gli errori in una lista e decide
alla fine, così l'utente li vede tutti in una volta sola invece di
scoprirli uno per tentativo.

    normalizza_nome(testo)         P4   "  sara   NERI " -> "Sara Neri"
    normalizza_codice(testo)       P4   " auto " -> "AUTO"
    converti_importo(testo)        P5   "128,5" -> 128.5, oppure ValueError
    formato_italiano(importo)      P5   53.97 -> "53,97"
    stampa_voce(etichetta, valore) P2   "Rimborso ........ 53.97"
    controlla_nome / _veicolo / _km / _pedaggio
                                        specifiche: le regole di QUESTO modulo
    main()                         P1   chiede, raccoglie, decide, stampa

IL PEDAGGIO E IL TETTO MENSILE
Il pedaggio è un quarto campo con lo stesso schema degli altri: presenza,
forma, intervallo. È facoltativo nel senso dell'importo, non della
risposta: chi non l'ha pagato scrive 0, e il campo vuoto resta un errore,
perché un invio distratto e un "non c'era" non si distinguono.
Il tetto mensile è un'altra cosa: non è un errore del dato, è una soglia
di approvazione. Per questo non entra nella lista degli errori e non
blocca la scheda: la scheda esce, con un [!] in più prima dell'esito.

COME SI RIUSA
La PARTE GENERALE non sa che cosa sia un rimborso: normalizza testi,
converte numeri, stampa voci. La PARTE SPECIFICA contiene le regole del
modulo: quali campi, quali limiti, quale dizionario di tariffe, quali
messaggi. Per il rimborso pasti si cambia il dizionario, i limiti e i
testi delle domande; le funzioni generali restano identiche.

LIMITI NOTI
- float() accetta anche "nan" e "inf". "inf" viene respinto dal controllo
  d'intervallo, "nan" no: ogni confronto con nan è falso, quindi nessuno
  dei due limiti scatta e il rimborso esce nan. Chiuderlo richiederebbe
  un controllo in più che nessun consulente ha mai provocato digitando.
- Il nome non si controlla lettera per lettera: "Luca 3" passa.
- Il tetto si confronta con la sola richiesta, non con quanto il
  consulente ha già chiesto nel mese: il modulo non tiene uno storico.

Riprese dai giorni precedenti: normalizzare con .strip(), .split(),
.title() (Giorno 03 §5.2-5.5); il numero all'italiana (Giorno 02 §7.3,
Giorno 03 §5.4); i quattro controlli e l'ordine forma-prima-di-intervallo
(Giorno 04 §13.2, §13.8); il dizionario con .get() al posto degli elif
(Giorno 07 §11.1); la funzione che solleva e il try stretto nel chiamante
(Giorno 09 §8.3, §11.2); i puntini di riempimento (Giorno 03 §9.7).
"""

# ===== PARTE SPECIFICA (1 di 2): le costanti del caso =======================
# Le regole del modulo in un posto solo. Le domande a schermo si costruiscono
# da queste costanti: intervallo scritto e intervallo controllato non
# possono divergere.
TARIFFE_KM = {"AUTO": 0.42, "MOTO": 0.21, "FURGONE": 0.55}
KM_MINIMI = 1
KM_MASSIMI = 1500
# Il pedaggio di una trasferta: 0 se non c'è, oltre i 100 euro è un
# importo impossibile per una tratta singola, quindi un dato da correggere.
PEDAGGIO_MASSIMO = 100.00
# Oltre questa cifra la richiesta passa lo stesso, ma serve una firma.
TETTO_MENSILE = 300.00
PAROLE_MINIME_NOME = 2
TITOLO = "TALENTHUB - Rimborso chilometrico"
UNITA_MONETA = "euro"

# ===== COSTANTI DI IMPAGINAZIONE: generali ==================================
LARGHEZZA = 60
LARGHEZZA_ETICHETTA = 23
# Il rimedio va a capo sotto il testo dell'errore, non sotto la parentesi:
# il rientro è lungo quanto il marcatore "[ERRORE] ", calcolato e non contato.
MARCATORE_ERRORE = "[ERRORE] "
RIENTRO = " " * len(MARCATORE_ERRORE)


# ===== PARTE GENERALE: si riusa così com'è ==================================

def normalizza_nome(testo):
    """P4. Spazi interni ridotti a uno, iniziali maiuscole."""
    # split() senza argomenti spezza su QUALSIASI sequenza di spazi e butta
    # via quelli ai bordi; join rimette uno spazio solo fra le parole.
    # .title() poi mette la maiuscola a ogni parola (Giorno 03 §5.3).
    return " ".join(testo.split()).title()


def normalizza_codice(testo):
    """P4. Toglie gli spazi ai bordi e porta in maiuscolo."""
    return testo.strip().upper()


def converti_importo(testo):
    """P5. Da testo (anche con la virgola) a float; solleva ValueError."""
    pulito = testo.strip()
    # La regola dello schema: SE c'è la virgola, i punti sono separatori
    # delle migliaia e vanno via, poi la virgola diventa punto. Se la
    # virgola non c'è, il punto è già il separatore decimale e si lascia.
    #
    # TRABOCCHETTO: togliere i punti SEMPRE, anche quando la virgola non
    #   c'è. "128,5" funziona lo stesso, ed è per questo che il difetto
    #   sopravvive alle prove. Ma chi digita 128.5 si vede convertire 1285
    #   km: sono dentro l'intervallo, nessun errore, e la scheda esce con
    #   Rimborso .............. 539.70
    #   dieci volte il dovuto (Giorno 02 §7.4).
    if "," in pulito:
        pulito = pulito.replace(".", "").replace(",", ".")
    try:
        return float(pulito)
    except ValueError:
        # Rilanciamo con un messaggio nostro, uguale in tutti gli script
        # della giornata: il chiamante lo può stampare così com'è, oppure
        # usarlo solo come segnale e scrivere il suo (Giorno 09 §11.2).
        raise ValueError(f"importo non numerico: '{testo}'")


def formato_italiano(importo):
    """P5, ritorno. Da float a testo con due decimali e la virgola."""
    # TRABOCCHETTO: chiamare .replace() sul numero, importo.replace(".",
    #   ","). Un float non è una stringa e non ha quel metodo:
    #   AttributeError: 'float' object has no attribute 'replace'
    #   Prima si trasforma in testo con la f-string, POI si sostituisce.
    return f"{importo:.2f}".replace(".", ",")


def stampa_voce(etichetta, valore):
    """P2. Stampa 'Etichetta ........ valore' a larghezza fissa."""
    # Il punto prima di < è il carattere di riempimento (Giorno 03 §9.7).
    print(f"{etichetta + ' ':.<{LARGHEZZA_ETICHETTA}} {valore}")


def stampa_errori(errori):
    """P7, uscita. Stampa ogni errore come problema + rimedio a capo."""
    for problema, rimedio in errori:
        print(f"{MARCATORE_ERRORE}{problema}")
        print(f"{RIENTRO}{rimedio}")


# ===== PARTE SPECIFICA (2 di 2): le regole del modulo e il regista ==========
# Ogni controlla_ restituisce (valore, errore). errore è None se il campo
# va bene, altrimenti la coppia (problema, rimedio). Stessa forma per tutti
# e tre: main() li tratta allo stesso modo senza sapere che cosa controllano.

def controlla_nome(testo):
    """Presenza e numero di parole del nome del consulente."""
    nome = normalizza_nome(testo)
    if nome == "":
        return nome, ("Consulente: campo vuoto.", "Scrivete nome e cognome.")
    # len(nome.split()) conta le parole: dopo la normalizzazione gli spazi
    # sono già uno solo, ma split() senza argomenti non ne avrebbe bisogno.
    if len(nome.split()) < PAROLE_MINIME_NOME:
        # Nel messaggio il testo come l'ha scritto l'utente (ripulito dai
        # bordi): è lui che deve riconoscerlo.
        return nome, (f"Consulente: '{testo.strip()}' è una parola sola.",
                      "Scrivete nome e cognome.")
    return nome, None


def controlla_veicolo(testo, tariffe):
    """Valori ammessi: il veicolo deve avere una tariffa nel dizionario."""
    # TRABOCCHETTO: confrontare il testo così come arriva. "auto" non è
    #   "AUTO", e la richiesta buona viene respinta con
    #   [ERRORE] Veicolo: 'auto' non ha una tariffa.
    #   Si normalizza PRIMA di cercare, sempre dallo stesso lato delle
    #   chiavi del dizionario, che sono in maiuscolo (Giorno 04 §7.2).
    veicolo = normalizza_codice(testo)

    # .get() restituisce None se la chiave non c'è: niente crash, e il None
    # diventa un errore con un messaggio (Giorno 07 §11.1).
    #
    # TRABOCCHETTO: scrivere tariffe[veicolo] "tanto poi controllo". Sul
    #   terzo esempio il programma non arriva al controllo: si ferma con
    #   KeyError: 'BICI'
    #   e con un traceback, davanti a Giulia. Le quadre sono per le chiavi
    #   che SAPETE esserci; per quelle che arrivano da una persona, .get().
    tariffa = tariffe.get(veicolo)
    if tariffa is None:
        # ", ".join() su un dizionario scorre le chiavi: l'elenco degli
        # ammessi si costruisce dai dati, e resta giusto se ne aggiungete.
        ammessi = ", ".join(tariffe)
        return veicolo, (f"Veicolo: '{veicolo}' non ha una tariffa.",
                         f"Scrivete uno di questi: {ammessi}.")
    return veicolo, None


def controlla_km(testo):
    """Presenza, forma e intervallo dei chilometri."""
    scritto = testo.strip()
    # 1. Presenza.
    if scritto == "":
        return 0.0, ("Chilometri: campo vuoto.",
                     "Scrivete i km del percorso, per esempio 128,5.")

    # 2. Forma. Il try abbraccia UNA riga, la conversione (Giorno 09 §4.5).
    #
    # TRABOCCHETTO: controllare l'intervallo PRIMA della forma, cioè
    #   confrontare il testo con KM_MINIMI. Non esce un errore sul dato:
    #   il programma si ferma con
    #   TypeError: '<' not supported between instances of 'str' and 'int'
    #   Un testo e un numero non si confrontano: prima si converte, poi si
    #   misura (Giorno 04 §13.8).
    try:
        km = converti_importo(scritto)
    except ValueError:
        # TRABOCCHETTO: scrivere solo il messaggio, senza return. La
        #   funzione prosegue fino al controllo d'intervallo e su "trenta"
        #   si ferma con
        #   UnboundLocalError: cannot access local variable 'km' where it
        #   is not associated with a value
        #   perché l'assegnazione dentro il try non è mai avvenuta.
        return 0.0, (f"Chilometri: '{scritto}' non è un numero.",
                     "Scrivetelo in cifre, per esempio 128,5.")

    # 3. Intervallo, estremi compresi.
    if km < KM_MINIMI or km > KM_MASSIMI:
        return km, (f"Chilometri: {scritto} è fuori dall'intervallo ammesso "
                    f"(da {KM_MINIMI} a {KM_MASSIMI}).",
                    "Per un viaggio più lungo compilate una richiesta per "
                    "tratta.")
    return km, None


def controlla_pedaggio(testo):
    """Presenza, forma e intervallo del pedaggio autostradale."""
    scritto = testo.strip()
    # 1. Presenza. Facoltativo non vuol dire "si può lasciare vuoto": lo 0
    #    è una risposta, l'invio a vuoto no.
    #
    # TRABOCCHETTO: trattare il vuoto come zero, "tanto non c'era". Il
    #   consulente che preme invio per sbaglio, dopo aver pagato 12,40 di
    #   autostrada, si vede una scheda accettata con
    #   Pedaggio .............. 0.00
    #   e i soldi persi senza un messaggio. Un errore silenzioso a favore
    #   dell'azienda è comunque un errore.
    if scritto == "":
        return 0.0, ("Pedaggio: campo vuoto.",
                     "Scrivete 0 se non avete pagato pedaggi.")

    # 2. Forma: la stessa conversione dei km, quindi anche la virgola.
    try:
        pedaggio = converti_importo(scritto)
    except ValueError:
        return 0.0, (f"Pedaggio: '{scritto}' non è un numero.",
                     "Scrivetelo in cifre, per esempio 12,40, oppure 0.")

    # 3. Intervallo. Lo zero è ammesso, ed è il caso più frequente: per
    #    questo il confronto è < 0 e non <= 0.
    #
    # TRABOCCHETTO: scrivere pedaggio <= 0 "per escludere i negativi".
    #   Esclude anche lo 0, cioè la risposta che la domanda stessa
    #   suggerisce: chi non ha pedaggi riceve
    #   [ERRORE] Pedaggio: 0 è fuori dall'intervallo ammesso (da 0 a 100).
    #   e la contraddizione è scritta nella stessa riga.
    if pedaggio < 0 or pedaggio > PEDAGGIO_MASSIMO:
        return pedaggio, (f"Pedaggio: {scritto} è fuori dall'intervallo "
                          f"ammesso (da 0 a {PEDAGGIO_MASSIMO:.0f}).",
                          "Allegate la ricevuta e scrivete l'importo di "
                          "una tratta.")
    return pedaggio, None


def main():
    """Chiede i quattro dati, li controlla tutti e stampa scheda o errori."""
    print("=" * LARGHEZZA)
    print(TITOLO)
    print("=" * LARGHEZZA)

    # --- 1. Le quattro domande, costruite dalle costanti --------------------
    # Le risposte si leggono TUTTE prima di controllarne una: così gli
    # errori escono insieme, ed è il requisito promosso del modulo.
    testo_nome = input("Nome e cognome del consulente: ")
    elenco_veicoli = ", ".join(TARIFFE_KM)
    testo_veicolo = input(f"Veicolo ({elenco_veicoli}): ")
    testo_km = input(f"Chilometri percorsi (da {KM_MINIMI} a {KM_MASSIMI}): ")
    testo_pedaggio = input("Pedaggio autostradale in euro (0 se non c'è): ")
    print("-" * LARGHEZZA)

    # --- 2. I controlli, gli errori in una lista ---------------------------
    nome, errore_nome = controlla_nome(testo_nome)
    veicolo, errore_veicolo = controlla_veicolo(testo_veicolo, TARIFFE_KM)
    km, errore_km = controlla_km(testo_km)
    pedaggio, errore_pedaggio = controlla_pedaggio(testo_pedaggio)

    errori = []
    for errore in (errore_nome, errore_veicolo, errore_km, errore_pedaggio):
        # is not None e non "if errore:": qui i due modi danno lo stesso
        # risultato, ma is not None dice esattamente che cosa si controlla.
        if errore is not None:
            errori.append(errore)

    # --- 3. Rifiuto: tutti gli errori, poi l'esito -------------------------
    if len(errori) > 0:
        stampa_errori(errori)
        print("-" * LARGHEZZA)
        # Singolare e plurale: "1 dati" si legge male quanto un conto
        # sbagliato (Giorno 04, la condizione su una stampa).
        if len(errori) == 1:
            parola = "dato"
        else:
            parola = "dati"
        print(f"[!] Richiesta NON registrata: {len(errori)} {parola} "
              f"da correggere.")
        print("=" * LARGHEZZA)
        return

    # --- 4. Accettata: la scheda -------------------------------------------
    # Qui la tariffa esiste di sicuro: controlla_veicolo() ha già escluso le
    # chiavi assenti, quindi le quadre sono lecite.
    tariffa = TARIFFE_KM[veicolo]
    rimborso_km = round(km * tariffa, 2)
    # Il pedaggio si somma DOPO aver arrotondato la quota chilometrica: le
    # due voci compaiono separate sulla scheda, e il totale deve essere la
    # somma di quello che si legge sopra, centesimo per centesimo.
    #
    # TRABOCCHETTO: sommare prima e arrotondare una volta sola,
    #   round(km * tariffa + pedaggio, 2). In moto, 54,5 km e 12,40 di
    #   pedaggio: la quota stampata è 11.45 (11.445 arrotondato), ma il
    #   totale esce 23.84 invece di 23.85. La scheda si smentisce da sola,
    #   di un centesimo, e senza nessun errore.
    rimborso = round(rimborso_km + pedaggio, 2)

    print("SCHEDA DI RIMBORSO")
    stampa_voce("Consulente", nome)
    stampa_voce("Veicolo", veicolo)
    stampa_voce("Chilometri", f"{km:.1f}")
    stampa_voce("Tariffa al km", f"{tariffa:.2f}")
    stampa_voce("Quota chilometrica", f"{rimborso_km:.2f}")
    stampa_voce("Pedaggio", f"{pedaggio:.2f}")
    stampa_voce("Rimborso", f"{rimborso:.2f}")
    # Requisito promosso: la cifra da ricopiare sul modulo di carta, che in
    # Italia vuole la virgola. Il calcolo resta sul float; la virgola si
    # mette solo in uscita.
    stampa_voce("Sul modulo cartaceo",
                f"{formato_italiano(rimborso)} {UNITA_MONETA}")
    print("-" * LARGHEZZA)
    # Il tetto è una soglia di approvazione, non un errore del dato: la
    # richiesta si registra comunque, e il [!] arriva PRIMA dell'esito
    # perché chi legge la scheda lo veda prima di archiviarla.
    #
    # TRABOCCHETTO: confrontare rimborso_km con il tetto invece del totale.
    #   La trasferta da 520 km in furgone vale 286.00 di quota chilometrica
    #   più 18.90 di pedaggio: 304.90 euro, oltre il tetto. Confrontando la
    #   sola quota, 286.00 resta sotto i 300 e la firma non viene chiesta.
    if rimborso > TETTO_MENSILE:
        print(f"[!] Oltre il tetto mensile di {TETTO_MENSILE:.2f} "
              f"{UNITA_MONETA}: serve la firma del responsabile.")
    print("[OK] Richiesta registrata.")
    print("=" * LARGHEZZA)


if __name__ == "__main__":
    main()
