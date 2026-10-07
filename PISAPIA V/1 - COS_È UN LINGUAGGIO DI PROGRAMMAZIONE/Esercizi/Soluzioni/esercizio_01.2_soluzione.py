"""
SOLUZIONE — Esercizio 01.2: Etichetta di scaffale

Tutta l'etichetta è costruita con print, cambiando ogni volta il modo di
tenere insieme i pezzi: sep per il codice e l'intestazione, sep="" per la
riga del prezzo, end per la riga della posizione costruita a metà.

La sigla dell'azienda e l'anno sono costanti perché non dipendono
dall'articolo; categoria, progressivo, prezzo e posizione sono variabili.
"""

SIGLA_AZIENDA = "NS"
ANNO = 2026
RIGA_CHIUSURA = "------------------------------"


def main():
    """Stampa il cartellino di scaffale di un articolo NovaStore."""
    nome_prodotto = "Cuffie Bluetooth"
    categoria = "CUF"
    # Trabocchetto 1: il progressivo sta fra virgolette perché è un
    # codice, non una quantità. Scritto come numero (0007) Python lo
    # leggerebbe come 7 e sul cartellino finirebbe "NS-2026-CUF-7".
    progressivo = "0007"
    prezzo = 49.90
    scaffale = "A3"
    ripiano = 2

    # sep=" - " mette il separatore FRA i due pezzi, e solo fra loro:
    # non prima del primo e non dopo l'ultimo.
    print("NOVASTORE", "REPARTO INFORMATICA", sep=" - ")
    print(nome_prodotto)

    # La riga del codice nasce da due print: il primo non chiude la riga
    # (end=" "), il secondo incolla i quattro pezzi con i trattini.
    # Notate che ANNO è un numero e sep lo gestisce senza problemi:
    # con il "+" avremmo preso un TypeError.
    print("Codice:", end=" ")
    print(SIGLA_AZIENDA, ANNO, categoria, progressivo, sep="-")

    # Trabocchetto 2: qui serve sep="". Con la virgola e il separatore
    # normale uscirebbe "Prezzo:  49.9  euro" con gli spazi doppi,
    # perché print aggiunge il suo spazio a quelli già scritti da noi.
    print("Prezzo: ", prezzo, " euro", sep="")

    # Una riga sola prodotta da due print: il primo la lascia aperta.
    print("Scaffale:", scaffale, end=" | ")
    print("Ripiano:", ripiano)

    print(RIGA_CHIUSURA)


if __name__ == "__main__":
    main()
