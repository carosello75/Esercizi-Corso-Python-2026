"""
SOLUZIONE — Esercizio 04.3: Triage al pronto soccorso

Il protocollo appeso al muro è già una catena di `elif`: si legge
dall'alto, il primo caso che si verifica assegna il colore e chiude la
partita. Tradurlo è quasi una trascrizione, a patto di non cambiare
l'ordine delle righe.

Ogni ramo assegna tre variabili invece di stampare. La scheda esce da
un unico punto del programma: se domani cambia il formato, si cambia
lì e non in quattro posti.

Le condizioni sono unite da `or` perché il protocollo dice OPPURE, e
il ramo del giallo ne ha tre. Una delle tre è scritta con un operatore
diverso dalle altre, e non è una svista: è quello che c'è scritto sul
foglio.
"""

# Le soglie del dolore: sono numeri di reparto, non scelte di chi
# programma. Il nome della costante dice quale colore aprono.
DOLORE_ROSSO = 8
DOLORE_GIALLO = 5
DOLORE_VERDE = 2

FEBBRE_ALTA = 39.0
FEBBRE_LIEVE = 37.5

# Il protocollo dice "sopra i 120 battiti", non "da 120 in su": il
# nome della costante dice il valore, il confronto dirà il resto.
FREQUENZA_ALLARME = 120

RISPOSTA_AFFERMATIVA = "si"

LARGHEZZA_SCHEDA = 50
RIGA_DOPPIA = "=" * LARGHEZZA_SCHEDA
RIGA_SINGOLA = "-" * LARGHEZZA_SCHEDA


def main():
    """Assegna il codice colore di triage a un paziente."""
    # 1. I dati testuali si normalizzano appena entrano: .strip() per
    #    gli spazi invisibili, .lower() per le maiuscole. "Si " e "si"
    #    a schermo si somigliano, per == sono due stringhe diverse.
    nome = input("Nome del paziente: ").strip().title()
    risposta_cosciente = input("È cosciente? (si/no): ").strip().lower()

    # 2. I due dati numerici cambiano tipo, e in due modi diversi:
    #      dolore       ->   6     (int)    una scala a numeri interi
    #      temperatura  ->  38.2   (float)  i decimali contano
    #      frequenza    ->  88     (int)    battiti, non mezzi battiti
    dolore = int(input("Dolore dichiarato (0-10): ").strip())
    testo_temperatura = input("Temperatura in gradi: ").strip()
    temperatura = float(testo_temperatura.replace(",", "."))
    frequenza = int(input("Frequenza cardiaca (battiti al minuto): ").strip())

    # TRABOCCHETTO: qui non serve un if. Il confronto == produce già
    #   True o False, ed è quello che ci serve. Scrivere
    #       if risposta_cosciente == RISPOSTA_AFFERMATIVA:
    #           cosciente = True
    #       else:
    #           cosciente = False
    #   funziona, ma sono cinque righe per dire quello che il confronto
    #   dice da solo. Il tipo cambia un'ultima volta:
    #       risposta_cosciente  ->  "si"   (str)
    #       cosciente           ->  True   (bool)
    #   e il nome della variabile fa il resto del lavoro, perché
    #   "not cosciente" si legge come italiano.
    cosciente = risposta_cosciente == RISPOSTA_AFFERMATIVA

    # TRABOCCHETTO: la frequenza usa > e tutte le altre soglie usano
    #   >=, perché il foglio dice "sopra i 120" e non "da 120 in su".
    #   Su un solo valore, il 120 esatto, i due operatori danno
    #   risposte diverse: con >= quel paziente diventa giallo contro
    #   protocollo. Un carattere, un colore sbagliato, e nessun errore.
    #   Anche questo confronto prende un nome, per la stessa ragione di
    #   `cosciente`: dentro la catena si legge come una frase, e il ramo
    #   del giallo resta su una riga sola invece di doppiarsi.
    polso_alterato = frequenza > FREQUENZA_ALLARME

    # 3. La catena: si legge dall'alto come il foglio, e il primo ramo
    #    vero chiude la partita. I rami sotto non vengono valutati.
    #
    # TRABOCCHETTO: le condizioni sono legate da `or`, non da `and`.
    #   Con `and` sul primo ramo servirebbe un paziente incosciente E
    #   con dolore 8, cioè quasi nessuno: il rosso non uscirebbe mai e
    #   il programma non darebbe il minimo segno di essere rotto.
    if not cosciente or dolore >= DOLORE_ROSSO:
        colore = "ROSSO"
        attesa = "accesso immediato"
        nota = "[!] Chiamare subito il medico di guardia."
    elif dolore >= DOLORE_GIALLO or temperatura >= FEBBRE_ALTA or polso_alterato:
        colore = "GIALLO"
        attesa = "entro 30 minuti"
        nota = "[!] Rivalutare se l'attesa supera i 30 minuti."
    elif dolore >= DOLORE_VERDE or temperatura >= FEBBRE_LIEVE:
        colore = "VERDE"
        attesa = "entro 2 ore"
        nota = "[--] Far accomodare in sala di attesa."
    else:
        colore = "BIANCO"
        attesa = "oltre 2 ore"
        nota = "[--] Valutare l'invio all'ambulatorio."

    # 4. La stampa, da un punto solo. Le etichette sono portate a
    #    larghezza fissa dal formato, così le colonne restano allineate
    #    senza contare gli spazi a mano quando un'etichetta cambia.
    print(RIGA_DOPPIA)
    print("POLIAMBULATORIO AURORA - TRIAGE")
    print(RIGA_DOPPIA)
    print(f"{'Paziente:':<15}{nome}")
    print(f"{'Cosciente:':<15}{risposta_cosciente}")
    print(f"{'Dolore:':<15}{dolore} su 10")
    print(f"{'Temperatura:':<15}{temperatura:.1f} gradi")
    print(f"{'Frequenza:':<15}{frequenza} battiti")
    print(RIGA_SINGOLA)
    print(f"{'CODICE ASSEGNATO:':<18}{colore}")
    print(f"{'Attesa stimata:':<18}{attesa}")
    print(nota)
    print(RIGA_DOPPIA)


if __name__ == "__main__":
    main()
