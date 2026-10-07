"""
ESERCIZIO 03.6 — Disposizione di bonifico   ⭐⭐⭐ (impegnativa)

CASO D'USO REALE
Allo sportello di Banca Meridiana la disposizione di bonifico si compila
su un modulo cartaceo e poi si ridigita a video. Due passaggi, due
occasioni di sbagliare. Vi hanno chiesto una maschera di inserimento che
raccolga i sei campi e stampi un riquadro di conferma da far leggere al
cliente prima di eseguire. Sul riquadro l'IBAN va mascherato: si vedono
i primi quattro e gli ultimi quattro caratteri, il resto sono asterischi.

Il programma assume un IBAN italiano di 27 caratteri (con o senza spazi)
e un importo scritto senza separatore delle migliaia.


ISTRUZIONI
Struttura standard: docstring, costanti, main(), guard.
In ingresso i sei campi della disposizione, ricopiati da un modulo
compilato a mano allo sportello: ordinante, beneficiario, IBAN, importo,
causale, data valuta. In uscita il riquadro di conferma da far leggere
al cliente prima di eseguire, nel formato dell'ESEMPIO OUTPUT qui sotto.

Vincoli
- Il riquadro è largo 50 caratteri, e i cancelletti di destra restano
  allineati riga per riga qualunque sia la lunghezza del contenuto.
- L'IBAN si archivia compatto e maiuscolo, comunque il cliente lo abbia
  scritto sul modulo. Sul riquadro compare mascherato, come nell'esempio.
- Il mascheramento non contiene numeri scritti a mano: la lunghezza
  dell'IBAN (27) e i caratteri visibili in testa e in coda (4 e 4) stanno
  in costante, e il giorno che la banca ne chiede sei visibili deve
  cambiare una riga sola.
- I sei campi non ricevono tutti lo stesso trattamento: una ragione
  sociale, un codice e una causale scritta a mano non sono la stessa
  cosa.
- La commissione è 1.50 euro, e sul riquadro va anche il totale
  addebitato.

SUGGERIMENTI
- Il numero di asterischi non è un numero da scrivere: è una
  sottrazione, e i suoi termini li avete già in costante.
- Costruire cornice e contenuto in un'unica espressione funziona, ma
  alla terza riga il codice è illeggibile e alla quarta non si corregge
  più. Chiedetevi se le due cose devono per forza nascere insieme
  (Cap. 10.4).
- Se i cancelletti di destra non stanno in colonna, il conto della
  larghezza non torna da qualche parte: cinquanta caratteri in tutto, e
  il contenuto sta in mezzo a due cancelletti e due spazi (Cap. 9.4).

SE HAI FINITO PRIMA (opzionale)
- Stampate accanto all'IBAN mascherato la sua lunghezza, e verificate a
  occhio che sia 27.
- Ristampate l'IBAN completo a gruppi di quattro caratteri, come è
  scritto sul modulo, usando lo slicing del Giorno 02.

ESEMPIO OUTPUT
Ordinante (nome e cognome):  elena marino
Beneficiario (nome o ragione sociale): studio tecnico aurora srl
IBAN beneficiario: it60 x054 2811 1010 0000 0123 456
Importo in euro (senza separatore migliaia): 1250,00
Causale:  saldo fattura 118/2026
Data valuta (gg/mm/aaaa): 22/09/2026

##################################################
# BANCA MERIDIANA - DISPOSIZIONE DI BONIFICO     #
##################################################
# Ordinante:      Elena Marino                   #
# Beneficiario:   Studio Tecnico Aurora Srl      #
# IBAN:           IT60*******************3456    #
# Causale:        saldo fattura 118/2026         #
# Data valuta:    22/09/2026                     #
##################################################
# Importo:             1250.00 euro              #
# Commissione:            1.50 euro              #
# TOTALE ADDEBITO:     1251.50 euro              #
##################################################
Disposizione registrata. Conservare la contabile.
"""

# Scrivi il tuo codice qui
