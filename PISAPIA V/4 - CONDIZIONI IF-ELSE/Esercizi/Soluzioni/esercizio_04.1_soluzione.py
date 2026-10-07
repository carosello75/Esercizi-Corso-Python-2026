"""
SOLUZIONE — Esercizio 04.1: Maggiore età allo sportello

Un solo bivio, due strade. La parte interessante non è l'if: è dove
finisce. L'intestazione e la riga di chiusura stanno fuori dal blocco,
perché devono uscire in tutti i casi; il conteggio degli anni mancanti
sta dentro il ramo negativo, perché nell'altro caso non avrebbe senso.

Questa è la prima volta che l'indentazione decide il significato del
programma e non solo il suo aspetto.

I tre dati entrano tutti come testo e vengono trattati ciascuno a modo
suo: il nome con .title(), il documento con .upper(), l'età con int().
Tre dati, tre trattamenti diversi, e il motivo sta nei commenti.
"""

# La soglia di legge, con un nome che dice di che soglia si tratta. Il
# giorno in cui la legge cambia si tocca questa riga e nient'altro.
MAGGIORE_ETA = 18

# La larghezza della scheda è un dato solo, e le due righe di
# separazione la ricavano da lì. Scrivere "=" * 50 e "-" * 50 in due
# punti diversi significa avere due numeri da tenere allineati a mano.
LARGHEZZA_SCHEDA = 50
RIGA_DOPPIA = "=" * LARGHEZZA_SCHEDA
RIGA_SINGOLA = "-" * LARGHEZZA_SCHEDA


def main():
    """Verifica se il richiedente può firmare la domanda da solo."""
    # 1. Lettura del nome: input() restituisce sempre str, anche quando
    #    l'operatore digita solo lettere maiuscole. .strip() toglie gli
    #    spazi ai bordi e .title() mette la maiuscola a ogni parola:
    #    ognuno dei due restituisce una stringa nuova, perché le
    #    stringhe sono immutabili, e il risultato dell'uno entra
    #    nell'altro.
    nome = input("Nome e cognome: ").strip().title()

    # 2. L'età è l'unico dato che cambia tipo, e va guardato due volte:
    #      eta_testo  ->  "17"  (str)   il dato come è stato digitato
    #      eta        ->   17   (int)   il dato su cui si può decidere
    #    Senza int() il confronto più in basso non darebbe un risultato
    #    sbagliato: darebbe TypeError, perché Python si rifiuta di
    #    ordinare un testo e un numero. Che cosa fare quando all'età
    #    viene digitato "diciassette" è il capitolo 13.
    eta_testo = input("Età (anni compiuti): ").strip()
    eta = int(eta_testo)

    # 3. Il documento si uniforma con .upper(), non con .title().
    #
    # TRABOCCHETTO: sul documento .title() sembra la scelta naturale
    #   perché è quella usata sul nome, ed è la trappola vista al
    #   Giorno 03: per .title() l'apostrofo è fine parola, quindi
    #     "carta d'identità".title()  ->  "Carta D'Identità"
    #   con quella D maiuscola in mezzo alla parola. .upper() non ha
    #   parole da riconoscere, quindi non può sbagliarle.
    documento = input("Documento esibito: ").strip().upper()

    print(RIGA_DOPPIA)
    print("COMUNE DI VILLANOVA - SPORTELLO ANAGRAFE")
    print(RIGA_DOPPIA)
    print(f"Richiedente:      {nome}")
    print(f"Età dichiarata:   {eta}")
    print(f"Documento:        {documento}")
    print(RIGA_SINGOLA)

    # TRABOCCHETTO: qui la tentazione è scrivere > invece di >=. La
    #   legge dice "diciotto anni compiuti": chi oggi ha esattamente 18
    #   anni firma da solo. Con > verrebbe respinto, il programma non
    #   darebbe nessun errore e nessuno se ne accorgerebbe fino al
    #   reclamo. È il caso limite che va provato per primo, ed è
    #   l'unico valore su cui i due operatori danno risposte diverse.
    if eta >= MAGGIORE_ETA:
        print("[OK] FIRMA AMMESSA")
        print("Il richiedente può firmare la domanda da solo.")
    else:
        # Gli anni mancanti si calcolano qui dentro e non prima: nel
        # ramo positivo il risultato sarebbe zero o negativo, cioè un
        # numero senza significato da stampare.
        anni_mancanti = MAGGIORE_ETA - eta
        print("[!] FIRMA NON AMMESSA")
        print("Serve la firma di un genitore o di chi ne fa le veci.")
        print(f"Anni mancanti alla maggiore età: {anni_mancanti}")

    # Fuori dall'if/else, incollata al margine del blocco di main():
    # esce sempre, qualunque strada abbia preso il programma. Spostata
    # di quattro spazi a destra diventerebbe parte del ramo negativo, e
    # la scheda di chi firma da solo resterebbe senza chiusura.
    print(RIGA_DOPPIA)


if __name__ == "__main__":
    main()
