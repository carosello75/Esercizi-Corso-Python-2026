"""
SOLUZIONE — Esercizio 03.1: Accettazione paziente

Cinque dati raccolti uno alla volta, ognuno con la pulizia adatta al suo
tipo: title() per nome e cognome, upper() per il codice fiscale,
capitalize() per la frase libera del motivo.

La variabile grezza è tenuta separata da quella pulita. Oggi non serve a
niente; quando arriveranno i controlli, la stringa originale dovrà
essere ancora disponibile e chi l'ha buttata via dovrà riscrivere tutto.

Il programma assume che chi digita risponda a tutte e cinque le domande.
"""

RIGA_DOPPIA = "=" * 50
RIGA_SINGOLA = "-" * 50
AMBULATORIO = "POLIAMBULATORIO AURORA"
SPORTELLO = "Sportello 2"
SALA_ATTESA = "Sala d'attesa piano terra"


def main():
    """Registra un paziente allo sportello e stampa il promemoria."""
    nome_grezzo = input("Nome del paziente: ")
    cognome_grezzo = input("Cognome: ")
    codice_fiscale_grezzo = input("Codice fiscale: ")
    medico_grezzo = input("Medico (solo cognome): ")
    motivo_grezzo = input("Motivo della visita: ")

    # Trabocchetto 1: .strip() va messo anche quando "tanto l'utente non
    # mette spazi". Allo sportello i dati arrivano incollati da un altro
    # programma, e uno spazio davanti al codice fiscale non si vede a
    # occhio ma rende diverso il valore archiviato.
    nome = nome_grezzo.strip().title()
    cognome = cognome_grezzo.strip().title()
    codice_fiscale = codice_fiscale_grezzo.strip().upper()
    medico = medico_grezzo.strip().title()

    # Trabocchetto 2: qui è capitalize() e non title(). Il motivo della
    # visita è una frase, non un nome proprio: con title() uscirebbe
    # "Controllo Della Pressione", che sembra il titolo di un libro.
    motivo = motivo_grezzo.strip().capitalize()

    print()
    print(RIGA_DOPPIA)
    print(AMBULATORIO + " - ACCETTAZIONE")
    print(RIGA_DOPPIA)
    print(f"{'Paziente:':<17}{nome} {cognome}")
    print(f"{'Codice fiscale:':<17}{codice_fiscale}")
    print(f"{'Medico:':<17}Dott. {medico}")
    print(f"{'Motivo:':<17}{motivo}")
    print(RIGA_SINGOLA)
    print(f"{'Presentarsi a:':<17}{SPORTELLO}")
    print(f"{'Attesa in:':<17}{SALA_ATTESA}")
    print(RIGA_DOPPIA)


if __name__ == "__main__":
    main()
