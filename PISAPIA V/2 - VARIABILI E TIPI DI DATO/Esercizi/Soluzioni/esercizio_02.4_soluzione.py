"""
SOLUZIONE — Esercizio 02.4: Ripulitura anagrafiche

Ogni campo viene ripulito con una catena di metodi letta da sinistra a
destra: prima si tolgono gli spazi ai bordi, poi si sistema l'interno,
poi si dà la forma finale. L'ordine non è indifferente, e nei commenti
è spiegato dove.

Il programma stampa il prima e il dopo di ogni campo con la lunghezza in
caratteri, perché gli spazi non si vedono e le parentesi quadre e il
conteggio sono l'unico modo per accorgersene.
"""

RIGA_DOPPIA = "=" * 60
RIGA_SINGOLA = "-" * 60


def main():
    """Normalizza sei campi importati da un vecchio gestionale."""
    nome_grezzo = "   mario   "
    cognome_grezzo = "de  luca "
    email_grezza = "  MARIO.DELUCA@Comune.Villanova.IT "
    telefono_grezzo = " 089 / 12 34 56 "
    indirizzo_grezzo = "via  roma, 12"
    comune_grezzo = " villanova "

    nome_pulito = nome_grezzo.strip().title()

    # Trabocchetto 1: l'ordine conta. Se scrivessimo .title() prima di
    # .replace("  ", " "), il doppio spazio resterebbe dentro e ci
    # ritroveremmo "De  Luca". Prima si sistema il contenuto, poi si dà
    # la forma. Vale per tutte le catene di metodi.
    cognome_pulito = cognome_grezzo.strip().replace("  ", " ").title()

    email_pulita = email_grezza.strip().lower()

    # Il telefono lo vogliamo di sole cifre: via gli spazi interni e via
    # la barra che il vecchio gestionale metteva dopo il prefisso.
    telefono_pulito = telefono_grezzo.strip().replace(" ", "").replace("/", "")

    indirizzo_pulito = indirizzo_grezzo.replace("  ", " ").title()
    comune_pulito = comune_grezzo.strip().upper()

    prefisso = telefono_pulito[0:3]

    print(RIGA_DOPPIA)
    print("COMUNE DI VILLANOVA - BONIFICA ANAGRAFICHE")
    print("Importazione dal vecchio gestionale - pratica 2026/00418")
    print(RIGA_DOPPIA)

    print("NOME")
    print(f"  importato:    [{nome_grezzo}] - {len(nome_grezzo)} caratteri")
    print(f"  normalizzato: [{nome_pulito}] - {len(nome_pulito)} caratteri")
    print("COGNOME")
    print(
        f"  importato:    [{cognome_grezzo}] - "
        f"{len(cognome_grezzo)} caratteri"
    )
    print(
        f"  normalizzato: [{cognome_pulito}] - "
        f"{len(cognome_pulito)} caratteri"
    )
    print("EMAIL")
    print(f"  importato:    [{email_grezza}] - {len(email_grezza)} caratteri")
    print(f"  normalizzato: [{email_pulita}] - {len(email_pulita)} caratteri")
    print("TELEFONO")
    print(
        f"  importato:    [{telefono_grezzo}] - "
        f"{len(telefono_grezzo)} caratteri"
    )
    print(
        f"  normalizzato: [{telefono_pulito}] - "
        f"{len(telefono_pulito)} caratteri"
    )
    print("INDIRIZZO")
    print(
        f"  importato:    [{indirizzo_grezzo}] - "
        f"{len(indirizzo_grezzo)} caratteri"
    )
    print(
        f"  normalizzato: [{indirizzo_pulito}] - "
        f"{len(indirizzo_pulito)} caratteri"
    )
    print("COMUNE")
    print(f"  importato:    [{comune_grezzo}] - {len(comune_grezzo)} caratteri")
    print(f"  normalizzato: [{comune_pulito}] - {len(comune_pulito)} caratteri")

    print(RIGA_SINGOLA)
    print("SCHEDA PRONTA PER IL CARICAMENTO")
    print(f"Intestatario:  {cognome_pulito} {nome_pulito}")
    print(f"Residenza:     {indirizzo_pulito} - {comune_pulito}")
    print(f"Email:         {email_pulita}")
    print(f"Telefono:      {telefono_pulito} (prefisso {prefisso})")

    print(RIGA_SINGOLA)
    print("CONTROLLI AUTOMATICI")
    # Trabocchetto 2: questi controlli vanno fatti sul dato PULITO. Su
    # email_grezza, .endswith(".it") darebbe False, perché in fondo c'è
    # uno spazio invisibile. È il classico controllo che "funziona sul
    # mio computer" e fallisce sul file vero.
    print(f"Una sola chiocciola nell'email: {email_pulita.count('@') == 1}")
    print(f"Email che finisce con .it:      {email_pulita.endswith('.it')}")
    print(f"Telefono di sole cifre:         {telefono_pulito.isdecimal()}")
    print(f"Nome di sole lettere:           {nome_pulito.isalpha()}")
    print(f"Comune uguale al maiuscolo:     {comune_pulito == comune_pulito.upper()}")
    print(RIGA_DOPPIA)


if __name__ == "__main__":
    main()
