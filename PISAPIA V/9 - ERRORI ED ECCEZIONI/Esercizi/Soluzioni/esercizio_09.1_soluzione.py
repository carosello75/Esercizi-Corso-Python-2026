"""
SOLUZIONE — Esercizio 09.1: Lo screening che non si ferma

IL PROBLEMA
Il modulo del 03.7 convertiva i dati con int() e float() senza nessuna
rete: al primo testo non numerico Python sollevava un ValueError, il
programma si fermava con un traceback e il candidato ricominciava da capo.
Il 03.7 si limitava a catalogare quei crash; il Giorno 04 li aveva
prevenuti con .isdecimal(). Oggi lo stesso punto si risolve dall'altra
parte: si lascia che la conversione ci provi, e se fallisce si raccoglie
l'eccezione.

LA STRATEGIA
- Un try per ogni conversione, con dentro UNA riga: quella che converte.
  Così il ramo except sa esattamente quale campo è andato storto, e il
  messaggio può nominarlo (Cap. 4.5, il try stretto).
- Si cattura solo ValueError: è l'unico tipo che int() e float()
  sollevano su un testo sbagliato. Un errore di tipo diverso è un difetto
  del programma, e deve continuare a fermarlo (Cap. 5.1).
- Ogni domanda numerica si ripete fino a TENTATIVI_MASSIMI volte: il try
  sta dentro un ciclo for, come nel ciclo di validazione del Cap. 8.7.
  Chi sbaglia l'età non perde il nome già scritto, e chi sbaglia tre volte
  di fila viene fermato: un ciclo senza tetto terrebbe lo sportello
  bloccato su un candidato che non sa rispondere.
- Le domande stanno in due funzioni, chiedi_intero() e chiedi_punteggio(),
  che restituiscono il valore buono oppure None se i tentativi finiscono.
  main() guarda solo quel risultato: sa che cosa chiedere, non come.
- Il nome del tipo di eccezione arriva dall'eccezione stessa, con
  except ValueError as errore e type(errore).__name__ (Cap. 5.4). Scritto
  a mano sarebbe una seconda copia del tipo, che il giorno in cui cambia
  l'except nessuno si ricorda di aggiornare.
- Il controllo d'intervallo del punteggio resta un if, DOPO il try. Il
  try verifica che il testo sia un numero, non che sia un numero sensato:
  "900" si converte benissimo. Un punteggio fuori scala consuma un
  tentativo come un testo sbagliato.

LIMITI NOTI DI QUESTA SOLUZIONE
- Età ed esperienza non hanno un controllo d'intervallo: un'età di -4
  passa. Il punteggio sì, perché la traccia lo chiede solo per lui.
- Il nome non si ripete mai: è testo, e un testo non può fallire la
  conversione. Un nome lasciato vuoto passa, e la scheda esce con la riga
  del candidato in bianco.
- I tentativi si contano per campo, non per candidato: chi sbaglia due
  volte l'età e due volte il punteggio arriva in fondo con quattro errori.

Concetti di teoria: cap. 3 (leggere il traceback), cap. 4 (try/except,
il try stretto, la variabile dopo l'except), cap. 5 (except ValueError,
except ... as e, type(e).__name__), cap. 6.1 (ValueError di int() e di
float()), cap. 8.7 (il ciclo di validazione con try).
"""

# --- Costanti ---------------------------------------------------------------
LARGHEZZA = 70
RIGA_DOPPIA = "=" * LARGHEZZA
AZIENDA = "TALENTHUB - SCREENING CANDIDATO"

# Estremi della scala del test. Compaiono tre volte: nel prompt, nel
# controllo d'intervallo e nel messaggio d'errore. Tre copie a mano sono
# tre occasioni di scrivere un numero diverso.
PUNTEGGIO_MINIMO = 0
PUNTEGGIO_MASSIMO = 100

# Quante volte si ripete una domanda prima di interrompere lo screening.
# Compare nel ciclo e nel messaggio "Tentativo 1 di 3": una costante sola
# tiene d'accordo le due cose.
TENTATIVI_MASSIMI = 3

# Larghezza della colonna delle etichette nella scheda, come nel 03.7.
LARGHEZZA_ETICHETTA = 17

MESSAGGIO_INTERRUZIONE = "Screening interrotto: nessun dato registrato."
MESSAGGIO_REGISTRATO = "[OK] Screening registrato."
FRASE_CAMPO_VUOTO = "il campo è vuoto"
SERVE_UN_INTERO = "serve un numero intero"
SERVE_UN_NUMERO = "serve un numero, virgola ammessa"


def descrivi_digitato(testo):
    """Frase che riporta all'utente che cosa ha digitato, anche se niente."""
    # Un invio a vuoto produce la stringa "", e fra apici diventerebbe ''.
    # Due apici appiccicati in fondo a un messaggio sembrano un refuso, non
    # un'informazione: meglio dirlo a parole. È lo stesso caso degli apici
    # vuoti in fondo al traceback del 03.7, riga 2 del suo catalogo.
    if testo == "":
        return FRASE_CAMPO_VUOTO
    # TRABOCCHETTO: scrivere f"avete scritto {testo!r}" sembra equivalente,
    #   perché repr() mette gli apici da solo. Lo è finché il testo non
    #   contiene un apostrofo: digitando vent'anni come età, repr() sceglie
    #   le virgolette doppie e la riga esce
    #   [ERRORE] Eta (ValueError): serve un numero intero, avete scritto
    #   "vent'anni"
    #   Nessun errore, solo un messaggio che cambia forma a seconda di quello
    #   che scrive l'utente. Gli apici messi a mano non cambiano mai.
    return f"avete scritto '{testo}'"


def segnala_errore(campo, che_cosa_serve, testo, tipo_errore):
    """Stampa la riga [ERRORE] per un campo, con il tipo d'eccezione se c'è."""
    # Il messaggio ha le tre parti del Cap. 11.2 (e del Giorno 04, 13.8):
    # quale campo, che cosa serviva, che cosa è arrivato. In più, fra
    # parentesi, il tipo di eccezione: all'operatore dello sportello dice
    # poco, a chi mantiene il programma dice subito che cosa è successo.
    #
    # tipo_errore è una stringa vuota quando il dato è stato rifiutato da un
    # if e non da un'eccezione (il punteggio fuori scala): lì non c'è nessun
    # tipo da mostrare, e inventarne uno sarebbe proprio lo "scritto a mano"
    # che la traccia vieta.
    if tipo_errore == "":
        etichetta = campo
    else:
        etichetta = f"{campo} ({tipo_errore})"
    print()
    print(f"[ERRORE] {etichetta}: {che_cosa_serve}, {descrivi_digitato(testo)}")


def avvisa_tentativo(tentativo):
    """Dice all'utente quanti tentativi ha usato e se può riprovare."""
    # Il numero del tentativo arriva dal for di chi chiama: questa funzione
    # non conta niente, riferisce soltanto.
    if tentativo < TENTATIVI_MASSIMI:
        print(f"Tentativo {tentativo} di {TENTATIVI_MASSIMI} fallito: riprovate.")
    else:
        print(
            f"Tentativo {tentativo} di {TENTATIVI_MASSIMI} fallito: "
            "tentativi esauriti."
        )


def chiedi_intero(prompt, campo):
    """Chiede un intero fino a TENTATIVI_MASSIMI volte; None se non arriva."""
    # range(1, TENTATIVI_MASSIMI + 1) conta 1, 2, 3: i numeri che l'utente
    # legge nel messaggio, senza il +1 che servirebbe partendo da zero.
    #
    # TRABOCCHETTO: scrivere range(1, TENTATIVI_MASSIMI), senza il + 1. Il
    #   ciclo fa DUE giri, non tre, e il messaggio del secondo errore dice
    #   "Tentativo 2 di 3 fallito: riprovate." Poi la domanda non torna:
    #   lo screening si interrompe dopo aver promesso un terzo tentativo.
    for tentativo in range(1, TENTATIVI_MASSIMI + 1):
        # Il testo si tiene separato dal valore convertito: serve all'except
        # per ripetere all'utente che cosa ha scritto.
        testo = input(prompt).strip()
        try:
            valore = int(testo)
        # TRABOCCHETTO: scrivere except Exception as errore, "per stare
        #   larghi". Tutto sembra funzionare finché un refuso nel try, per
        #   esempio int(testoo), non solleva un NameError: l'except lo
        #   raccoglie come se fosse un dato sbagliato, e digitando 29 lo
        #   sportello risponde tre volte di fila
        #   [ERRORE] Eta (NameError): serve un numero intero, avete scritto '29'
        #   Il difetto è nel codice e il messaggio accusa l'utente (Cap. 5.5).
        #   Almeno il nome del tipo, preso dall'eccezione, tradisce il guaio.
        except ValueError as errore:
            # type(errore) è la classe, .__name__ il suo nome come stringa.
            #
            # TRABOCCHETTO: fermarsi a type(errore), senza .__name__. Non
            #   c'è nessun errore, ma dentro la f-string la classe si
            #   presenta per intero e la riga esce
            #   [ERRORE] Eta (<class 'ValueError'>): serve un numero intero
            #   cioè con la sintassi di Python in faccia all'utente.
            segnala_errore(campo, SERVE_UN_INTERO, testo, type(errore).__name__)
            avvisa_tentativo(tentativo)
            # TRABOCCHETTO: dimenticare questo continue. Dopo l'avviso il
            #   programma scende al return qui sotto con valore mai assegnato
            #   e si ferma al primo errore con
            #   UnboundLocalError: cannot access local variable 'valore'
            #   where it is not associated with a value
            #   È la variabile assegnata nel try che dopo l'except non esiste
            #   (Cap. 4.6): dentro una funzione è UnboundLocalError, non
            #   NameError.
            continue
        # Si arriva qui solo se int() ha funzionato: il valore esiste.
        return valore
    # Il for è finito senza un return: tre tentativi, tre errori. None è il
    # segnale per main(), che decide lui come interrompere.
    return None


def chiedi_punteggio(prompt):
    """Chiede il punteggio del test fino a TENTATIVI_MASSIMI volte."""
    for tentativo in range(1, TENTATIVI_MASSIMI + 1):
        testo = input(prompt).strip()
        # Due trasformazioni prima della conversione, prese dal Giorno 03:
        # .strip() e la virgola italiana cambiata in punto. La prevenzione
        # non sparisce con il try: si occupa di ciò che si può correggere,
        # il try di ciò che non si può.
        #
        # TRABOCCHETTO: dimenticare .replace(",", ".") perché "tanto adesso
        #   c'è il try". Il try non ripara niente: raccoglie. Il punteggio
        #   72,5, che è un dato perfettamente valido in Italia, viene
        #   rifiutato con
        #   [ERRORE] Punteggio (ValueError): serve un numero, virgola
        #   ammessa, avete scritto '72,5'
        #   cioè un messaggio che promette la virgola e poi la respinge, per
        #   tre volte di fila.
        try:
            punteggio = float(testo.replace(",", "."))
        except ValueError as errore:
            segnala_errore("Punteggio", SERVE_UN_NUMERO, testo,
                           type(errore).__name__)
            avvisa_tentativo(tentativo)
            continue

        # L'intervallo. Il try ha stabilito che il testo è un numero; se sia
        # un punteggio possibile lo decide questo if. Gestire l'eccezione non
        # esonera dal controllo d'intervallo (Cap. 8.3 e 8.8).
        #
        # La condizione è scritta "dentro l'intervallo" e poi negata, invece
        # che "sotto il minimo oppure sopra il massimo".
        #
        # TRABOCCHETTO: scrivere
        #       if punteggio < PUNTEGGIO_MINIMO or punteggio > PUNTEGGIO_MASSIMO:
        #   sembra identico e non lo è. float() accetta la parola inglese
        #   "nan" (not a number), e nan fallisce OGNI confronto: nan < 0 è
        #   False, nan > 100 è False, quindi il rifiuto non scatta e la scheda
        #   esce con
        #   Punteggio:       nan su 100 (nan%)
        #   Con la forma "dentro e poi negata", nan >= 0 è False, la
        #   condizione "dentro" è falsa e il dato viene respinto (Cap. 6.1,
        #   la chicca su float()).
        dentro_la_scala = (
            punteggio >= PUNTEGGIO_MINIMO and punteggio <= PUNTEGGIO_MASSIMO
        )
        if not dentro_la_scala:
            # Nessuna eccezione qui: il rifiuto lo decide l'if, quindi il
            # tipo è una stringa vuota e la riga esce senza parentesi.
            segnala_errore(
                "Punteggio",
                f"serve un valore fra {PUNTEGGIO_MINIMO} e {PUNTEGGIO_MASSIMO}",
                testo,
                "",
            )
            # Anche un numero fuori scala consuma un tentativo: per chi
            # risponde, 900 è un errore come 72%.
            avvisa_tentativo(tentativo)
            continue
        return punteggio
    return None


def stampa_scheda(nome, eta, punteggio, esperienza):
    """Stampa la scheda del candidato, con dati già convertiti e controllati."""
    # Questa funzione riceve solo dati buoni: tutti i controlli stanno nelle
    # funzioni di domanda, prima di arrivare qui. È la separazione del
    # Giorno 06 fra chi decide e chi mostra, e rende la scheda identica a
    # quella del 03.7.
    quota = punteggio / PUNTEGGIO_MASSIMO
    riga_punteggio = f"{punteggio:.1f} su {PUNTEGGIO_MASSIMO} ({quota:.1%})"
    print()
    print(RIGA_DOPPIA)
    print(AZIENDA)
    print(RIGA_DOPPIA)
    print(f"{'Candidato:':<{LARGHEZZA_ETICHETTA}}{nome}")
    print(f"{'Eta:':<{LARGHEZZA_ETICHETTA}}{eta}")
    print(f"{'Punteggio:':<{LARGHEZZA_ETICHETTA}}{riga_punteggio}")
    print(f"{'Esperienza:':<{LARGHEZZA_ETICHETTA}}{esperienza} anni")
    print(RIGA_DOPPIA)
    print(MESSAGGIO_REGISTRATO)


def main():
    """Raccoglie i quattro dati, ripetendo le domande sbagliate, e stampa."""
    # 1. Il nome non si converte: è testo e resta testo. .strip() e .title()
    #    sono la normalizzazione del Giorno 03, e non possono fallire.
    nome = input("Nome e cognome: ").strip().title()

    # 2. L'età. Nel Giorno 04 questo punto si scriveva prevenendo, con
    #    if not testo_eta.isdecimal(). Qui si prova e si rimedia. Le due
    #    strade danno lo stesso esito su "venti", ma non su tutto: "-4"
    #    viene rifiutato da .isdecimal() e accettato da int() (Cap. 8.3).
    eta = chiedi_intero("Eta: ", "Eta")
    # "is None" chiede se eta È l'oggetto None, non se vale qualcosa di
    # simile. È il modo di scriverlo che raccomanda la guida di stile PEP 8,
    # e il perché si vede al punto 4.
    if eta is None:
        print(MESSAGGIO_INTERRUZIONE)
        return

    # 3. Il punteggio, con la sua funzione: la conversione è diversa (float
    #    e virgola) e c'è in più il controllo d'intervallo.
    punteggio = chiedi_punteggio(
        f"Punteggio del test ({PUNTEGGIO_MINIMO}-{PUNTEGGIO_MASSIMO}): "
    )
    if punteggio is None:
        print(MESSAGGIO_INTERRUZIONE)
        return

    # 4. L'esperienza: un intero, come l'età, e la stessa funzione. Lo zero
    #    qui è un valore normale, ed è per lui che serve is None.
    #
    # TRABOCCHETTO: risparmiare righe mettendo le tre conversioni in un
    #   unico try, con un solo except che stampa il messaggio dell'età.
    #   Funziona su "venti" e mente su tutto il resto: digitando 72% come
    #   punteggio lo sportello accusa l'età, cioè il campo giusto con il
    #   dato giusto. Un except solo non può sapere quale delle tre righe è
    #   saltata (Cap. 4.5).
    esperienza = chiedi_intero("Anni di esperienza: ", "Esperienza")
    # TRABOCCHETTO: scrivere if not esperienza: al posto di is None. Sembra
    #   la stessa cosa, perché None è falso. Ma è falso anche lo zero: un
    #   neodiplomato che scrive 0 anni di esperienza si vede rispondere,
    #   senza nessuna riga [ERRORE],
    #   Screening interrotto: nessun dato registrato.
    #   Un dato valido trattato come tre tentativi falliti.
    if esperienza is None:
        print(MESSAGGIO_INTERRUZIONE)
        return

    # 5. Si arriva qui solo se tutti e quattro i dati sono buoni: ogni None
    #    finisce con return, quindi la scheda non può mai partire con un
    #    dato mancante.
    stampa_scheda(nome, eta, punteggio, esperienza)


if __name__ == "__main__":
    main()
