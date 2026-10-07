"""
SOLUZIONE — Esercizio 02.1: Anagrafica cliente

La scheda usa le f-string nella forma minima: il nome della variabile fra
graffe, e Python ci infila dentro il valore. Le etichette sono testo fisso
e gli spazi stanno dentro le virgolette: incolonnare valori di lunghezza
variabile è un'altra cosa e arriva nel pomeriggio, al capitolo 13.

La seconda metà del programma stampa il tipo di ogni campo con type().
Non serve al cliente: serve a chi carica i dati nel gestionale, perché
un'età scritta come testo supera il controllo a occhio e fa saltare
l'importazione alle due di notte.
"""

CODICE_CLIENTE = "NS-00417"
ETA_MAGGIORE_ETA = 18
SOGLIA_CLIENTE_TOP = 1000.00

RIGA_DOPPIA = "=" * 50
RIGA_SINGOLA = "-" * 50


def main():
    """Stampa la scheda di un cliente NovaStore e il tipo di ogni campo."""
    # Assegnazione multipla: nome e cognome arrivano insieme dal modulo di
    # registrazione, ma restano due dati distinti e vanno tenuti separati.
    nome, cognome = "Giulia", "Ferrante"
    nome_completo = nome + " " + cognome

    email = "giulia.ferrante@novastore.it"
    eta, ordini_2026 = 34, 7
    spesa_totale = 1284.50
    carta_fedelta = True

    # Trabocchetto 1: lo scontrino medio è un conto, non un dato. Scriverlo
    # a mano (183.5) vuol dire che al prossimo ordine la scheda mente, e
    # nessuno se ne accorge perché il numero è plausibile.
    scontrino_medio = spesa_totale / ordini_2026

    print(RIGA_DOPPIA)
    print("NOVASTORE - SCHEDA CLIENTE")
    print(RIGA_DOPPIA)
    print(f"Nome:            {nome_completo}")
    print(f"Email:           {email}")
    print(f"Codice cliente:  {CODICE_CLIENTE}")
    print(f"Eta:             {eta}")
    print(f"Ordini nel 2026: {ordini_2026}")
    print(f"Spesa totale:    {spesa_totale:.2f} EUR")
    print(f"Scontrino medio: {scontrino_medio:.2f} EUR")
    print(f"Carta fedelta:   {carta_fedelta}")

    print(RIGA_DOPPIA)
    print("CONTROLLO TIPI PRIMA DELL'IMPORT")
    print(RIGA_SINGOLA)
    # Trabocchetto 2: type(eta) non stampa "int", stampa <class 'int'>.
    # Non è un errore vostro, è il modo in cui Python descrive un tipo.
    # E guardate CODICE_CLIENTE: contiene delle cifre ma è str, e deve
    # restare str. Se qualcuno lo convertisse a numero, il prefisso NS-
    # sparirebbe e con lui la possibilità di ritrovare il cliente.
    print(f"nome_completo    -> {type(nome_completo)}")
    print(f"email            -> {type(email)}")
    print(f"CODICE_CLIENTE   -> {type(CODICE_CLIENTE)}")
    print(f"eta              -> {type(eta)}")
    print(f"ordini_2026      -> {type(ordini_2026)}")
    print(f"spesa_totale     -> {type(spesa_totale)}")
    print(f"scontrino_medio  -> {type(scontrino_medio)}")
    print(f"carta_fedelta    -> {type(carta_fedelta)}")

    print(RIGA_SINGOLA)
    print("VERIFICHE (per ora si limitano a comparire nel report)")
    # Un confronto produce True o False e basta. Farci prendere una
    # decisione al programma è materia del Giorno 04.
    print(f"Cliente maggiorenne:      {eta >= ETA_MAGGIORE_ETA}")
    print(f"Spesa oltre i 1000 euro:  {spesa_totale > SOGLIA_CLIENTE_TOP}")
    print(f"Email di dominio interno: {email.endswith('novastore.it')}")
    print(RIGA_DOPPIA)


if __name__ == "__main__":
    main()
