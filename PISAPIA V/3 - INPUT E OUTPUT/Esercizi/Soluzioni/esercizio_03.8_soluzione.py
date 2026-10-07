"""
SOLUZIONE — Esercizio 03.8: Totem self-service TalentHub

Mini-progetto della giornata: nove campi raccolti in tre sezioni
dichiarate, tutti normalizzati, due valori calcolati che non esistono in
ingresso (l'età e il codice candidatura), una tabella a due colonne
numeriche e una checklist finale.

La struttura è quella del capitolo 12 applicata nove volte di fila:
richiesta, pulizia, conversione, calcolo, presentazione. Il codice è
lungo ma non è difficile: è lo stesso schema ripetuto.

Il programma assume che l'anno di nascita, gli anni di esperienza, la
retribuzione e i giorni di preavviso siano numeri scritti correttamente,
e che nome e cognome non siano vuoti.
"""

RIGA_DOPPIA = "=" * 50
RIGA_SINGOLA = "-" * 50
AZIENDA = "TALENTHUB"
TITOLO = "TOTEM CANDIDATURE - SEDE DI BATTIPAGLIA"
ISTRUZIONE = "Compilare i campi. INVIO dopo ogni risposta."
ANNO_CORRENTE = 2026
MENSILITA = 13
POSIZIONI_APERTE = 4
CAMPI_ANAGRAFICA = 3
CAMPI_CONTATTI = 2
CAMPI_CANDIDATURA = 4
ETICHETTA_RETRIBUZIONE = "Retribuzione lorda attesa"


def main():
    """Raccoglie una candidatura al totem e stampa la scheda."""
    print(RIGA_DOPPIA)
    print(AZIENDA)
    print(TITOLO)
    print(RIGA_DOPPIA)
    print(ISTRUZIONE)
    print(f"Posizioni aperte in questo momento: {POSIZIONI_APERTE}")
    print(RIGA_DOPPIA)

    print()
    print("--- SEZIONE 1 DI 3: ANAGRAFICA ---")
    nome = input("Nome: ").strip().title()
    cognome = input("Cognome: ").strip().title()
    anno_nascita_grezzo = input("Anno di nascita (4 cifre): ")

    print()
    print("--- SEZIONE 2 DI 3: CONTATTI ---")
    email = input("Email: ").strip().lower()
    telefono_grezzo = input("Telefono: ").strip()
    telefono = telefono_grezzo.replace(" ", "").replace("-", "")

    print()
    print("--- SEZIONE 3 DI 3: CANDIDATURA ---")
    posizione = input("Posizione desiderata: ").strip().upper()
    esperienza_grezza = input("Anni di esperienza: ")
    retribuzione_grezza = input("Retribuzione annua lorda attesa in euro: ")
    preavviso_grezzo = input("Giorni di preavviso: ")

    # Trabocchetto 1: l'anno di nascita va convertito PRIMA della
    # sottrazione. Con la stringa, 2026 - "1994" dà TypeError. E l'età
    # così calcolata è approssimata per difetto o per eccesso di un anno
    # a seconda del mese: qui va bene, in un contesto contrattuale no.
    anno_nascita = int(anno_nascita_grezzo.strip())
    eta = ANNO_CORRENTE - anno_nascita

    esperienza = int(esperienza_grezza.strip())
    preavviso = int(preavviso_grezzo.strip())

    retribuzione_pulita = retribuzione_grezza.strip().replace(",", ".")
    retribuzione_annua = float(retribuzione_pulita)
    retribuzione_mensile = retribuzione_annua / MENSILITA

    iniziali = nome[0] + cognome[0]
    codice = f"TH-{ANNO_CORRENTE}-{iniziali}-{anno_nascita}"

    # Trabocchetto 2: la mensile stampata è arrotondata a due decimali
    # solo in stampa. Moltiplicandola per 13 si ottiene 28500.03, non
    # 28500.00. Il valore vero resta quello annuo: la mensile è un
    # derivato, e da un derivato arrotondato non si risale mai
    # all'originale.
    colonna_annua = f"{retribuzione_annua:>10.2f}"
    colonna_mensile = f"{retribuzione_mensile:>10.2f}"

    print()
    print(RIGA_DOPPIA)
    print("SCHEDA CANDIDATURA")
    print(RIGA_DOPPIA)
    print(f"{'Codice:':<18}{codice}")
    print(f"{'Nome e cognome:':<18}{nome} {cognome}")
    print(f"{'Eta:':<18}{eta} anni")
    print(f"{'Email:':<18}{email}")
    print(f"{'Telefono:':<18}{telefono}")
    print(RIGA_SINGOLA)
    print(f"{'Posizione:':<18}{posizione}")
    print(f"{'Esperienza:':<18}{esperienza} anni")
    print(f"{'Preavviso:':<18}{preavviso} giorni")
    print(RIGA_SINGOLA)
    print(f"{'VOCE':<30}{'ANNUO':>10}{'MENSILE':>10}")
    print(f"{ETICHETTA_RETRIBUZIONE:<30}{colonna_annua}{colonna_mensile}")
    print(RIGA_SINGOLA)
    print("CONTROLLO CAMPI RACCOLTI")
    print(f"[OK] {'Anagrafica':<16}{CAMPI_ANAGRAFICA} campi")
    print(f"[OK] {'Contatti':<16}{CAMPI_CONTATTI} campi")
    print(f"[OK] {'Candidatura':<16}{CAMPI_CANDIDATURA} campi")
    print(RIGA_DOPPIA)
    print("Presentare in reception il codice:")
    print(codice)
    print(RIGA_DOPPIA)


if __name__ == "__main__":
    main()
