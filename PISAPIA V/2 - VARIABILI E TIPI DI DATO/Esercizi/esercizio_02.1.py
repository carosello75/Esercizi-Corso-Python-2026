"""
ESERCIZIO 02.1 — Anagrafica cliente   ⭐ (base)

CASO D'USO REALE
Il gestionale di NovaStore va sostituito e i clienti vanno ricaricati nel
sistema nuovo. Il fornitore ha mandato una regola secca: ogni campo deve
arrivare del tipo giusto, altrimenti il caricamento si ferma e va rifatto
da capo. L'anno scorso è andata male proprio così: qualcuno aveva
esportato le età come testo e il caricamento si è bloccato a metà, di
notte, senza che nessuno se ne accorgesse fino al mattino. Giulia ha
ricevuto il compito di preparare una scheda di controllo che, per ogni
campo, dica anche di che tipo è.


ISTRUZIONI
1) Struttura standard: docstring, costanti, main().
2) In costante vanno il codice del cliente, l'età della maggiore età e
   la soglia oltre la quale un cliente è considerato "top".
3) Dentro main() create le variabili del cliente. Nome e cognome vanno
   creati con una sola riga di assegnazione multipla, poi uniti in un
   nome completo.
4) Lo scontrino medio non si scrive: si calcola, dividendo la spesa
   totale per il numero di ordini.
5) Stampate la scheda con le f-string nella forma minima: il nome della
   variabile fra graffe. Gli importi in euro vogliono due decimali.
6) Stampate poi il tipo di otto valori usando type().
7) Chiudete con tre confronti stampati: maggiore età, spesa sopra la
   soglia, email del dominio interno. Sono espressioni che valgono True
   o False: oggi si stampano e basta.

DATI DI PARTENZA
     nome, cognome = "Giulia", "Ferrante"
     email = "giulia.ferrante@novastore.it"
     eta, ordini_2026 = 34, 7
     spesa_totale = 1284.50
     carta_fedelta = True
     CODICE_CLIENTE = "NS-00417"

SUGGERIMENTI
- L'assegnazione multipla si scrive nome, cognome = "Giulia", "Ferrante".
- Il codice cliente contiene delle cifre ma è testo: le lettere e il
  trattino non si possono togliere.
- carta_fedelta non va fra virgolette: True è un valore, non una parola.
- type(eta) non stampa "int", stampa <class 'int'>. È corretto così.
- Per le righe di separazione usate "=" * 50, senza contare i caratteri.
- Per i due decimali: {spesa_totale:.2f}.

SE HAI FINITO PRIMA (opzionale)
- Aggiungete una variabile sconto_fedelta (0.05) e stampatela come
  percentuale con {sconto_fedelta:.1%}, poi stampate anche il suo tipo.
- Provate a scrivere eta = "34" con le virgolette e rilanciate: cosa
  cambia nella riga del tipo? E il confronto con la maggiore età cosa
  fa? Annotate il messaggio d'errore e rimettete tutto a posto.

ESEMPIO OUTPUT
==================================================
NOVASTORE - SCHEDA CLIENTE
==================================================
Nome:            Giulia Ferrante
Email:           giulia.ferrante@novastore.it
Codice cliente:  NS-00417
Eta:             34
Ordini nel 2026: 7
Spesa totale:    1284.50 EUR
Scontrino medio: 183.50 EUR
Carta fedelta:   True
==================================================
CONTROLLO TIPI PRIMA DELL'IMPORT
--------------------------------------------------
nome_completo    -> <class 'str'>
email            -> <class 'str'>
CODICE_CLIENTE   -> <class 'str'>
eta              -> <class 'int'>
ordini_2026      -> <class 'int'>
spesa_totale     -> <class 'float'>
scontrino_medio  -> <class 'float'>
carta_fedelta    -> <class 'bool'>
--------------------------------------------------
VERIFICHE (per ora si limitano a comparire nel report)
Cliente maggiorenne:      True
Spesa oltre i 1000 euro:  True
Email di dominio interno: True
==================================================
"""

# Scrivi il tuo codice qui
