"""
SOLUZIONE — Esercizio 03.2: Cassa del negozio

Tre conversioni e quattro calcoli. Il cuore dell'esercizio è il passaggio
da stringa a numero: senza float() e int() nessuna delle moltiplicazioni
funziona, e senza .replace(",", ".") il programma muore sul primo cliente
che scrive 49,90.

L'IVA viene scorporata, non aggiunta: il prezzo sul cartellino è già
comprensivo di imposta, quindi l'imponibile si ottiene dividendo per
1 + aliquota.

Il programma assume che prezzo, quantita e contante siano numeri scritti
correttamente e che il contante basti a coprire il totale.
"""

ALIQUOTA_IVA = 0.22
RIGA_DOPPIA = "=" * 50
RIGA_SINGOLA = "-" * 50
NEGOZIO = "NOVASTORE - CASSA 1"


def main():
    """Calcola totale, IVA scorporata e resto di un acquisto."""
    articolo_grezzo = input("Articolo: ")
    prezzo_grezzo = input("Prezzo unitario in euro (es. 49.90): ")
    quantita_grezza = input("Quantita (numero intero): ")
    contante_grezzo = input("Contante ricevuto in euro: ")

    articolo = articolo_grezzo.strip().title()

    # Trabocchetto 1: la .replace(",", ".") si mette sempre, anche se
    # l'esempio nel prompt usa il punto. In Italia metà delle persone
    # scrive 49,90 e float() su quella stringa si ferma con ValueError.
    # Su una stringa senza virgola .replace() non fa niente e non
    # protesta: non c'è motivo di ometterla.
    prezzo = float(prezzo_grezzo.strip().replace(",", "."))
    contante = float(contante_grezzo.strip().replace(",", "."))
    quantita = int(quantita_grezza.strip())

    totale = prezzo * quantita

    # Trabocchetto 2: l'imponibile si ricava DIVIDENDO per 1.22, non
    # moltiplicando per 0.78. Sono due conti diversi: 99.80 / 1.22 fa
    # 81.80, 99.80 * 0.78 fa 77.84. La seconda strada sembra ragionevole
    # e sbaglia di quasi quattro euro.
    imponibile = totale / (1 + ALIQUOTA_IVA)
    iva = totale - imponibile
    resto = contante - totale

    etichetta_iva = f"IVA {ALIQUOTA_IVA:.0%}:"

    print()
    print(RIGA_DOPPIA)
    print(NEGOZIO)
    print(RIGA_DOPPIA)
    print(f"{'Articolo:':<19}{articolo}")
    print(f"{'Prezzo unitario:':<19}{prezzo:>10.2f} euro")
    print(f"{'Quantita:':<19}{quantita:>10}")
    print(RIGA_SINGOLA)
    print(f"{'Totale da pagare:':<19}{totale:>10.2f} euro")
    print(f"{'Imponibile:':<19}{imponibile:>10.2f} euro")
    print(f"{etichetta_iva:<19}{iva:>10.2f} euro")
    print(RIGA_SINGOLA)
    print(f"{'Contante:':<19}{contante:>10.2f} euro")
    print(f"{'Resto:':<19}{resto:>10.2f} euro")
    print(RIGA_DOPPIA)


if __name__ == "__main__":
    main()
