"""
SOLUZIONE — Esercizio 05.4: Chiedi finché non è giusto

Il problema: chiedere il CAP finché non è valido, ma non all'infinito, e a
ogni rifiuto dire che cosa non va invece di un generico "errore".

La strategia: un `while` con due condizioni unite da `and`. Si resta nel
ciclo finché il dato NON è valido E ci sono ancora tentativi. Dentro, una
catena `if/elif/elif/else` ordinata dal controllo più grossolano a quello
di dominio, così ogni errore riceve il messaggio che lo riguarda. La
bandiera `valido` sopravvive al ciclo e dice da quale delle due porte si è
usciti.

Perché `while` e non `for`: il numero di giri dipende dai dati. Può essere
uno (CAP giusto subito), due, o tre. MAX_TENTATIVI è solo il tetto, non il
numero di giri. Un `for` su range(MAX_TENTATIVI) con un `break` farebbe lo
stesso lavoro, ma nasconderebbe nel corpo una delle due ragioni per restare
dentro; il `while` le scrive tutte e due sulla stessa riga, dove si leggono
(Cap. 11 e 13.2).

I tre obblighi del `while` (Cap. 7.2), dove stanno:
    inizializzare   valido = False e tentativi = 0, prima del ciclo
    condizionare    not valido and tentativi < MAX_TENTATIVI
    aggiornare      tentativi += 1 a ogni giro, valido = True nel ramo else
Basta che una delle due parti della condizione diventi falsa per uscire.

Che cosa sopravvive al ciclo: `valido`, `tentativi` e `cap`. Servono
tutte e tre al riepilogo.

I bordi:
    CAP giusto al primo colpo   un giro solo, "Tentativi usati ....... 1".
    CAP giusto all'ultimo       è il caso dell'esempio: valido diventa True
                                proprio mentre i tentativi finiscono.
    tre errori                  si esce con valido ancora False, e il
                                riepilogo rinvia allo sportello.

Concetti di teoria: Cap. 13 (ciclo di validazione, messaggi distinti, tetto
ai tentativi), Cap. 7 (i tre obblighi di un `while`), Cap. 6.6 (la bandiera
booleana).
"""

# --- Costanti -----------------------------------------------------------
# Larghezza delle righe di separazione, comune agli esercizi della giornata.
LARGHEZZA = 60

# Le cifre di un CAP italiano. Usata due volte, nel controllo e nel
# messaggio d'errore: se cambiasse, cambierebbero insieme.
LUNGHEZZA_CAP = 5

# Le prime due cifre dei CAP della provincia servita dallo sportello.
# È una STRINGA, non un numero, per due ragioni: si confronta con
# .startswith(), che lavora su testo; e un CAP non è una quantità ma un
# codice, come si vede con quelli che iniziano per zero ("00100").
PREFISSO_PROVINCIA = "84"

# Il tetto ai tentativi: oltre, l'operatore smette di insistere e il
# cittadino va all'assistenza. Senza un tetto, un cittadino che non ricorda
# il proprio CAP terrebbe lo sportello fermo per sempre (Cap. 13.2).
MAX_TENTATIVI = 3

# Il numero dello sportello a cui mandare chi esaurisce i tentativi.
SPORTELLO_ASSISTENZA = 2


def main():
    """Chiede il CAP finché non è valido o finché i tentativi non finiscono."""
    # 1. Intestazione e regole per chi digita, costruite dalle costanti:
    #    il testo non può contraddire il controllo, perché nasce dagli stessi
    #    valori.
    print("=" * LARGHEZZA)
    print("COMUNE DI VILLANOVA - Sportello unico: verifica del CAP")
    print("=" * LARGHEZZA)
    print(f"Il CAP ha {LUNGHEZZA_CAP} cifre e inizia per {PREFISSO_PROVINCIA}.")
    print(f"Hai {MAX_TENTATIVI} tentativi.")
    print()

    # 2. Le tre variabili che devono esistere prima del ciclo e restare
    #    leggibili dopo.
    #      cap        (str)   l'ultimo dato digitato. Parte vuoto: dopo il
    #                         ciclo si legge solo se valido è True, quindi
    #                         è di sicuro assegnato, ma inizializzarlo fa sì
    #                         che il nome esista comunque, anche se il ciclo
    #                         facesse zero giri (Cap. 4.2).
    #      valido     (bool)  la bandiera: False finché nessun CAP ha
    #                         superato tutti e tre i controlli.
    #      tentativi  (int)   il contatore che fa finire il ciclo quando
    #                         il dato continua a essere sbagliato.
    cap = ""
    valido = False
    tentativi = 0

    # 3. Il ciclo di validazione.
    #    Che cosa ripete: chiedi il CAP, controllalo, spiega che cosa non va.
    #    Quando si ferma: al primo CAP valido, oppure al terzo tentativo.
    #    Che cosa aggiorna: tentativi a ogni giro, valido una volta sola.
    #
    # TRABOCCHETTO: la condizione è la NEGAZIONE della validità: descrive
    #   quando si RESTA dentro. Scrivere "while valido and ..." sembra
    #   naturale leggendolo in italiano, ma valido nasce False e il ciclo
    #   fa zero giri. Sintomo: nessuna domanda, e subito il riepilogo con
    #   "CAP registrato ........ nessuno", "Tentativi usati ....... 0" e il
    #   rinvio allo sportello. Nessun errore (Cap. 7.3).
    #
    # TRABOCCHETTO: < e non <=. Con tentativi <= MAX_TENTATIVI il ciclo fa
    #   un giro in più, e il sintomo si legge nel prompt stesso:
    #   "CAP (tentativo 4 di 3)". È l'off-by-one del Cap. 14.4 in forma di
    #   while.
    while not valido and tentativi < MAX_TENTATIVI:
        # Obbligo "aggiornare", prima della domanda: il prompt deve dire
        # "tentativo 1 di 3" già al primo giro, quindi il contatore sale
        # PRIMA di input().
        #
        # TRABOCCHETTO: dimenticare questa riga. La seconda metà della
        #   condizione resta vera per sempre, e il ciclo finisce solo se
        #   arriva un CAP giusto. Sintomo: il prompt dice sempre
        #   "CAP (tentativo 0 di 3)" e continua a chiedere; con un
        #   cittadino che non ricorda il CAP si esce solo con Ctrl+C
        #   (Cap. 8.1).
        tentativi += 1
        # Il CAP resta str e non si converte mai: non ci si fa nessun
        # conto, e int("00100") perderebbe gli zeri iniziali.
        #   cap  ->  "84091"  (str)
        #
        # TRABOCCHETTO: senza .strip(), uno spazio battuto per sbaglio dopo
        #   "84091" rende la stringa lunga 6. Sintomo: un CAP giusto
        #   rifiutato con "[ERRORE] servono 5 cifre, tu ne hai 6", e
        #   l'operatore che conta cinque cifre sullo schermo non capisce.
        cap = input(f"CAP (tentativo {tentativi} di {MAX_TENTATIVI}): ").strip()

        # 4. I tre controlli, dal più grossolano al più specifico. La
        #    catena si ferma al primo ramo vero: ogni CAP riceve un solo
        #    messaggio, quello della prima regola che viola.
        #
        # TRABOCCHETTO: l'ordine decide quale messaggio vede l'operatore.
        #   Con .isdecimal() per primo, chi preme solo Invio si sente dire
        #   "[ERRORE] solo cifre: niente lettere, spazi o trattini", perché
        #   "".isdecimal() è False, mentre con la lunghezza per prima legge
        #   "tu ne hai 0", che è il suo errore vero. E con il prefisso per
        #   primo, "abcde" riceverebbe il messaggio sulla provincia invece
        #   di quello sulle lettere (Cap. 13.2).
        if len(cap) != LUNGHEZZA_CAP:
            # len() dà un int, e il messaggio lo riporta: dire all'operatore
            # quante cifre ha scritto è più utile che dirgli "sbagliato".
            print(f"  [ERRORE] servono {LUNGHEZZA_CAP} cifre, tu ne hai {len(cap)}")
        elif not cap.isdecimal():
            # Qui la lunghezza è giusta: il problema è il contenuto, come
            # la lettera o al posto dello zero in "84o91".
            print("  [ERRORE] solo cifre: niente lettere, spazi o trattini")
        elif not cap.startswith(PREFISSO_PROVINCIA):
            # Cinque cifre, ma di un'altra provincia: la regola di dominio,
            # che ha senso controllare solo su un dato già ben formato.
            print(f"  [ERRORE] i CAP della provincia iniziano per {PREFISSO_PROVINCIA}")
        else:
            # Obbligo "aggiornare", seconda parte: è l'unica riga del
            # programma che porta valido a True, e basta da sola a far
            # uscire dal ciclo al prossimo controllo della condizione.
            valido = True
            print(f"  [OK] CAP accettato al tentativo {tentativi}.")

    # 5. Dopo il ciclo. Il while si è fermato per una di due ragioni, e le
    #    due uscite portano a due comportamenti diversi allo sportello: è
    #    qui che la bandiera serve.
    #
    # TRABOCCHETTO: decidere l'esito con tentativi < MAX_TENTATIVI invece
    #   che con valido. Sembra equivalente e non lo è: un CAP accettato
    #   proprio al terzo tentativo lascia tentativi a 3. Sintomo: con i dati
    #   dell'esempio, "[OK] CAP accettato al tentativo 3." seguito da
    #   "[!] Troppi tentativi". Solo la bandiera sa perché si è usciti
    #   (Cap. 6.6).
    print()
    print("-" * LARGHEZZA)
    if valido:
        print(f"CAP registrato ........ {cap}")
        print(f"Tentativi usati ....... {tentativi}")
        print("-" * LARGHEZZA)
        print("Pratica avviata. Ritira il numero e attendi la chiamata.")
    else:
        # Qui cap contiene l'ultimo tentativo sbagliato: non si stampa,
        # perché registrare un dato rifiutato è l'errore che il programma
        # esiste per evitare.
        print("CAP registrato ........ nessuno")
        print(f"Tentativi usati ....... {tentativi}")
        print("-" * LARGHEZZA)
        print(f"[!] Troppi tentativi: sportello {SPORTELLO_ASSISTENZA}.")
    print("=" * LARGHEZZA)


# Il programma parte solo se il file viene eseguito direttamente: è la
# formula fissa di ogni soluzione del corso.
if __name__ == "__main__":
    main()
