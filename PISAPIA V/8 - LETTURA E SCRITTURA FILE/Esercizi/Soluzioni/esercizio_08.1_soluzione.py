"""
SOLUZIONE — Esercizio 08.1: Il registro dello sportello

IL PROBLEMA
Lo sportello unico del Comune di Villanova segna gli accessi su un quaderno.
Un quaderno non si somma: a fine mese qualcuno riconta a mano, e ogni volta
esce un numero diverso. Serve un registro che resti quando il programma si
chiude, e che il programma stesso sappia rileggere e contare.

LA STRATEGIA
Tre passi, e ciascuno ha la sua funzione:
    scrivi_registro(percorso, accessi)   la lista -> il file, e quanti
                                         caratteri sono finiti sul disco
    rileggi_registro(percorso)           il file -> una lista di tuple, e
                                         quanti caratteri si sono riletti
    conta_per_servizio(registrazioni)    la lista riletta -> un dizionario
Il conteggio per servizio si fa sulle righe RILETTE, non sulla costante
ACCESSI. È il punto dell'esercizio: se il conteggio torna, il file contiene
davvero i dati, e un altro programma potrebbe rileggerlo domani senza sapere
niente di questa lista.

LA CONTROPROVA DEI CARATTERI
write() restituisce quanti caratteri ha scritto (Cap. 6.1). Sommati, dicono
quanto deve essere lungo il file. Rileggendo, la somma delle lunghezze delle
righe, a capo compreso, deve dare lo stesso numero. Se i due numeri non
tornano, uno dei due conti è sbagliato: è la stessa regola della controprova
del Giorno 07 (07.7), applicata al disco.

    "Esposito;ANAGRAFE" + a capo   ->  8 + 1 + 8 + 1  = 18 caratteri
    sei righe                      ->  101 caratteri in tutto

Si contano CARATTERI, non byte. I byte cambierebbero su Windows, dove ogni a
capo sul disco ne occupa due: il numero stampato non sarebbe più lo stesso su
ogni macchina, e l'output di un programma deve esserlo.

LA RIPARTENZA PULITA
Il file si apre in "w": a ogni esecuzione si riscrive da capo. Lanciato due
volte, il programma lascia sei righe, non dodici (Cap. 3.3).

Concetti di teoria: Cap. 3 (with open e modalità), Cap. 4.3 (for riga in f),
Cap. 5.1-5.2 (l'a capo che non si vede), Cap. 6.1 (write e il suo valore di
ritorno), Cap. 7.4 (il percorso dallo script), Cap. 8.3 (mkdir). Dal Giorno
03 lo split con unpacking, dal Giorno 06 il return di due valori, dal Giorno
07 il conta-occorrenze con .get() e enumerate().
"""

# Il primo import della giornata: solo libreria standard, e solo pathlib.
# Path rappresenta un percorso sul disco e sa comporlo con l'operatore /.
from pathlib import Path

# --- Costanti -----------------------------------------------------------
ACCESSI = [
    ("Esposito", "ANAGRAFE"),
    ("Russo", "TRIBUTI"),
    ("Greco", "ANAGRAFE"),
    ("Romano", "SERVIZI SOCIALI"),
    ("Colombo", "TRIBUTI"),
    ("Ricci", "ANAGRAFE"),
]
NOME_FILE = "registro_accessi.txt"
LARGHEZZA = 60

# La convenzione del corso (Cap. 7.4). __file__ è il percorso di QUESTO
# script; .resolve() lo rende assoluto; il primo .parent è la cartella
# soluzioni, il secondo è giorno_08. Da lì si scende in output.
# Così il file finisce sempre nello stesso posto, da qualunque cartella
# lanciate il programma: dal tasto verde di PyCharm o da un terminale aperto
# altrove.
#
# TRABOCCHETTO: scrivere open("output/registro_accessi.txt", "w") con un
#   percorso relativo. Il percorso relativo parte dalla DIRECTORY DI LAVORO,
#   cioè da dove lanciate il programma, non da dove sta lo script. Lanciato
#   dalla cartella soluzioni, cerca soluzioni/output, che non esiste, e si
#   ferma con FileNotFoundError: [Errno 2] No such file or directory:
#   'output/registro_accessi.txt'. Lanciato da giorno_08 funziona: lo stesso
#   programma funziona o no a seconda di chi lo lancia (Cap. 7.1).
CARTELLA_OUTPUT = Path(__file__).resolve().parent.parent / "output"

# Separatore dei campi dentro una riga del file. In costante perché lo usano
# due funzioni diverse, chi scrive e chi rilegge: se un giorno cambia, deve
# cambiare per tutte e due insieme, o il file scritto non si rilegge più.
SEPARATORE = ";"

# Larghezza della colonna delle etichette nel blocco per servizio: i puntini
# riempiono lo spazio fra il nome del servizio e il numero.
LARGHEZZA_ETICHETTA = 22


def scrivi_registro(percorso, accessi):
    """Scrive una riga per accesso e restituisce i caratteri scritti."""
    caratteri = 0
    # "w" apre in scrittura e CANCELLA il contenuto precedente: è la
    # ripartenza pulita. encoding="utf-8" sempre, anche se qui non ci sono
    # lettere accentate: la regola del corso non ha eccezioni, perché il
    # giorno che il cognome sarà "Nicolò" nessuno si ricorderà di aggiungerla.
    #
    # TRABOCCHETTO: "a" al posto di "w". La prima esecuzione è perfetta. Dalla
    #   seconda il file ha 12 righe, poi 18: la rilettura stampa gli accessi
    #   due volte, "Righe rilette ... 12", "Caratteri riletti ... 202" contro
    #   101 scritti, e il verdetto diventa [!]. Nessun errore, solo numeri
    #   che crescono a ogni lancio (Cap. 6.5).
    with open(percorso, "w", encoding="utf-8") as f:
        for cognome, servizio in accessi:
            # La riga si compone PRIMA, con la f-string, e poi si scrive: così
            # quello che finisce sul disco si vede in un punto solo.
            riga = f"{cognome}{SEPARATORE}{servizio}\n"
            # write() restituisce il numero di caratteri scritti. Lo si
            # accumula come un totale qualsiasi del Giorno 05.
            #
            # TRABOCCHETTO: dimenticare "\n" in fondo alla riga. write() non
            #   va a capo da sola: le sei righe diventano una sola,
            #   "Esposito;ANAGRAFERusso;TRIBUTIGreco;...". La scrittura non
            #   protesta e annuncia "6 righe, 95 caratteri", ma la controprova
            #   non arriva mai: il programma si ferma prima, nella rilettura,
            #   dove lo split trova 7 campi invece di 2:
            #   ValueError: too many values to unpack (expected 2, got 7).
            #   Su Python 3.12 il messaggio non riporta il "got 7".
            caratteri += f.write(riga)
    # Uscendo dal with il file è chiuso e tutto quello che è stato scritto è
    # davvero sul disco: la rilettura qui sotto lo trova completo (Cap. 3.2).
    return caratteri


def rileggi_registro(percorso):
    """Rilegge il registro: restituisce le coppie e i caratteri letti."""
    registrazioni = []
    caratteri = 0
    with open(percorso, "r", encoding="utf-8") as f:
        # for riga in f: una riga alla volta, a capo compreso (Cap. 4.3).
        for riga in f:
            # I caratteri si contano PRIMA di pulire la riga: il file sul disco
            # contiene anche gli a capo, e il confronto con i caratteri
            # scritti deve contare le stesse cose.
            #
            # TRABOCCHETTO: contare dopo la pulizia, len(pulita). Ogni riga
            #   perde il suo a capo, i caratteri riletti diventano 95 contro
            #   101 scritti e il verdetto dice [!] su un file perfetto. Il
            #   difetto sta nel conteggio, non nel file.
            caratteri += len(riga)
            # rstrip("\n") toglie solo l'a capo finale e nient'altro (Cap. 5.2).
            pulita = riga.rstrip("\n")
            # Split e unpacking a due nomi: il gesto del Giorno 03, sulla
            # stessa forma di riga che scrivi_registro ha prodotto.
            #
            # TRABOCCHETTO: fare lo split sulla riga senza togliere l'a capo.
            #   L'a capo resta attaccato al servizio: "ANAGRAFE\n". Nessun
            #   errore, e il conteggio per servizio torna perché tutte le
            #   chiavi hanno lo stesso difetto. Il sintomo è solo a video:
            #   nella tabella il numero finisce sulla riga sotto, e fra una
            #   registrazione e l'altra compare una riga vuota.
            cognome, servizio = pulita.split(SEPARATORE)
            # Una tupla per registrazione: la lista di tuple del Giorno 07.
            registrazioni.append((cognome, servizio))
    # Due valori restituiti insieme, il return multiplo del Giorno 06.
    return registrazioni, caratteri


def conta_per_servizio(registrazioni):
    """Restituisce il dizionario servizio -> numero di accessi."""
    conteggi = {}
    for cognome, servizio in registrazioni:
        # Il conta-occorrenze del Giorno 07 (Cap. 12.2), identico: .get() con
        # ripiego a zero, così un servizio mai visto parte da 0.
        #
        # TRABOCCHETTO: conteggi[servizio] += 1 con l'accesso diretto. Alla
        #   primissima riga la chiave non esiste ancora, e il programma si
        #   ferma con KeyError: 'ANAGRAFE'.
        conteggi[servizio] = conteggi.get(servizio, 0) + 1
    return conteggi


def servizio_piu_richiesto(conteggi):
    """Restituisce il servizio con più accessi e il suo numero."""
    # max(conteggi.values()) darebbe il NUMERO, non il nome del servizio.
    # Per il nome si scorrono le coppie tenendo da parte il migliore trovato
    # finora: è zona_piu_cara() di 07.4, identica nella forma.
    migliore = ""
    massimo = 0
    for servizio, quanti in conteggi.items():
        # Maggiore stretto: a parità vince il primo incontrato, cioè il
        # servizio comparso per primo nel file. È una scelta, ed è dichiarata.
        if quanti > massimo:
            migliore = servizio
            massimo = quanti
    return migliore, massimo


def main():
    """Scrive il registro, lo rilegge dal disco e lo conta."""
    print("=" * LARGHEZZA)
    print("COMUNE DI VILLANOVA - Registro degli accessi allo sportello")
    print("=" * LARGHEZZA)

    # 1. La cartella di output si crea se non c'è. exist_ok=True: se c'è già
    #    non è un errore (Cap. 8.3).
    #
    # TRABOCCHETTO: saltare questa riga. Su una macchina dove output non
    #   esiste ancora, open(..., "w") si ferma con FileNotFoundError: [Errno 2]
    #   No such file or directory, seguito dal percorso completo del file.
    #   Sorprende, perché il file doveva essere creato: "w" crea il FILE, non
    #   la cartella che lo contiene. Sulla vostra macchina non lo vedete se un
    #   esercizio precedente l'ha già creata: lo vede il collega.
    CARTELLA_OUTPUT.mkdir(exist_ok=True)
    percorso = CARTELLA_OUTPUT / NOME_FILE

    # 2. Scrittura. A video il NOME del file, non il percorso: il percorso
    #    intero è diverso su ogni macchina (Cap. 7.5).
    caratteri_scritti = scrivi_registro(percorso, ACCESSI)
    print(f"[OK] Scritto {percorso.name}: {len(ACCESSI)} righe, "
          f"{caratteri_scritti} caratteri")
    print("-" * LARGHEZZA)

    # 3. Rilettura dal disco, e stampa numerata. enumerate(..., 1) fa partire
    #    il numero da 1, come si conta in un registro (Giorno 07, Cap. 6.3).
    registrazioni, caratteri_letti = rileggi_registro(percorso)
    print("RILETTURA DAL DISCO")
    print(f"  {'N.':<4}{'COGNOME':<14}SERVIZIO")
    for numero, (cognome, servizio) in enumerate(registrazioni, 1):
        print(f"  {numero:>2}  {cognome:<14}{servizio}")
    print(f"Righe rilette ............ {len(registrazioni)}")
    print(f"Caratteri riletti ........ {caratteri_letti}")

    # 4. La controprova. Due conti fatti da due funzioni diverse, su due
    #    momenti diversi: se coincidono, il file è quello che volevamo.
    if caratteri_letti == caratteri_scritti:
        print("[OK] Il file contiene esattamente quello che è stato scritto.")
    else:
        print(f"[!] Scritti {caratteri_scritti} caratteri, "
              f"riletti {caratteri_letti}: uno dei due conti è sbagliato.")
    print("-" * LARGHEZZA)

    # 5. Il conteggio per servizio, sulle righe RILETTE. I puntini si
    #    costruiscono moltiplicando una stringa per un numero (Giorno 02):
    #    tanti quanti mancano per arrivare alla larghezza dell'etichetta.
    conteggi = conta_per_servizio(registrazioni)
    print("ACCESSI PER SERVIZIO")
    for servizio, quanti in conteggi.items():
        puntini = "." * (LARGHEZZA_ETICHETTA - len(servizio))
        print(f"  {servizio} {puntini} {quanti}")
    migliore, massimo = servizio_piu_richiesto(conteggi)
    print(f"Servizio più richiesto ... {migliore} ({massimo} accessi)")
    print("=" * LARGHEZZA)


# Il programma parte solo se il file viene eseguito direttamente, non se
# qualcuno lo importa: è la formula fissa di ogni soluzione del corso.
if __name__ == "__main__":
    main()
