"""
ESERCIZIO PER CASA 07.4 — Segmentazione clienti   ⭐⭐⭐⭐ (difficile)

CASO D'USO REALE
NovaStore ha dodici clienti e due numeri per ciascuno: quanto spende in
media e quanti ordini fa. Il marketing vuole tre gruppi, ma nessuno sa
dire quali: non c'è nessuna etichetta scritta da qualcuno, ci sono solo i
numeri. Si parte da tre centri scelti a occhio, si assegna ogni cliente
al centro più vicino, si spostano i centri sulla media dei loro membri e
si ricomincia. Dodici clienti, tre centri, tre giri: il programma forma
da solo dei gruppi che nessuno gli ha detto di cercare, e dentro ci sono
solo cose di oggi.

ARGOMENTI TEORICI: Cap. 6 — Scorrere una lista · Cap. 9 — Conti su una
lista · Cap. 14 — Lista di tuple. Assegnare un cliente al centro più
vicino è un confronto solo; ripetuto su dodici clienti e su tre giri
diventa la segmentazione completa.

ISTRUZIONI
1) Costruite la lista clienti con dodici tuple (nome, spesa, ordini) e
   due dizionari per i centri: centro_spesa e centro_ordini, con le
   chiavi "A", "B", "C". Due dizionari piatti, non uno di dizionari.
2) Scrivete distanza(spesa, ordini, spesa_centro, ordini_centro) che
   restituisce la distanza a passi: la somma delle due differenze prese
   con abs(). Non è la distanza in linea d'aria: è quella che si fa
   muovendosi in una direzione per volta, e qui basta e avanza.
3) Scrivete assegna(clienti, centro_spesa, centro_ordini) che restituisce
   una LISTA di lettere lunga quanto la lista dei clienti: in posizione i
   c'è il gruppo del cliente i. Due liste parallele, come il 07.3.
4) Scrivete nuovo_centro(clienti, gruppi, lettera) che restituisce la
   nuova coppia (spesa media, ordini medi) del gruppo, arrotondata a
   interi con round(). Se il gruppo è vuoto restituisce i vecchi valori:
   un gruppo che si svuota è un caso vero e non deve far esplodere niente.
5) Scrivete conta_cambi(prima, dopo) che conta in quante posizioni le due
   liste di gruppi sono diverse.
6) Scrivete membri(clienti, gruppi, lettera) che restituisce la lista dei
   nomi assegnati a quel gruppo.
7) Ciclo principale: per tre giri, stampate i centri di partenza, i tre
   gruppi con i loro membri, il numero di cambi rispetto al giro
   precedente e i centri spostati. Al primo giro i cambi sono tutti,
   perché prima non c'era nessuna assegnazione.
8) Alla fine stampate la tabella dell'assegnazione finale con la distanza
   di ogni cliente dal proprio centro, la sezione con i nomi da dare ai
   gruppi e le righe di lettura dell'esempio.

DATI DI PARTENZA (copiateli così come sono)
     CLIENTI = [
         ("Rossi Anna", 30, 2),
         ("Bianchi Marco", 40, 3),
         ("Verdi Luca", 35, 1),
         ("Neri Sara", 55, 11),
         ("Gallo Pietro", 65, 9),
         ("Costa Elena", 60, 13),
         ("Ricci Paolo", 170, 4),
         ("Moro Giulia", 190, 3),
         ("Rizzo Dario", 180, 5),
         ("Fabbri Ilaria", 47, 2),
         ("Greco Marta", 72, 10),
         ("Sala Nicola", 200, 4),
     ]
     LETTERE = ["A", "B", "C"]
     CENTRO_SPESA_INIZIALE = {"A": 40, "B": 80, "C": 120}
     CENTRO_ORDINI_INIZIALE = {"A": 4, "B": 6, "C": 8}
     GIRI = 3
     LARGHEZZA = 60

SUGGERIMENTI
- Per trovare il centro più vicino non serve una catena di if: si scorre
  LETTERE con un for, si calcola la distanza e si tiene da parte la più
  piccola trovata finora. È l'accumulatore del Giorno 05, applicato a
  un minimo invece che a una somma.
- Alla prima iterazione di quel for non c'è ancora nessun minimo: usate
  una variabile migliore inizializzata alla stringa vuota e controllate
  `if migliore == "" or distanza_nuova < distanza_minima`.
- round() su un numero che finisce per .5 arrotonda al pari più vicino,
  non sempre per eccesso. Con questi dati non capita mai, e sapere che
  esiste vi evita mezz'ora di stupore in un altro esercizio.
- La lista dei gruppi del giro precedente va salvata PRIMA di calcolare
  quella nuova, altrimenti confrontate una lista con se stessa e i cambi
  vi escono sempre zero.
- Per le righe con i nomi dei membri usate ", ".join(lista_di_nomi).

SE HAI FINITO PRIMA (opzionale)
- Aggiungete un quarto centro D e osservate che cosa cambia. Poi
  chiedetevi come fareste a decidere se tre gruppi sono meglio di quattro:
  la risposta onesta è che con questi strumenti non si può, e chi vi dice
  il contrario vi sta vendendo qualcosa.
- Fate fermare il ciclo da solo con un break quando i cambi sono zero,
  invece di fare sempre tre giri. Stampate a quale giro si è fermato.

ESEMPIO OUTPUT
============================================================
NOVASTORE - Segmentazione della clientela
============================================================
Dodici clienti, due caratteristiche a testa: spesa media in
euro e numero di ordini. Tre centri di partenza scelti a mano,
e tre giri di assegnazione e spostamento.
------------------------------------------------------------
CLIENTE          SPESA  ORDINI
------------------------------------------------------------
Rossi Anna          30       2
Bianchi Marco       40       3
Verdi Luca          35       1
Neri Sara           55      11
Gallo Pietro        65       9
Costa Elena         60      13
Ricci Paolo        170       4
Moro Giulia        190       3
Rizzo Dario        180       5
Fabbri Ilaria       47       2
Greco Marta         72      10
Sala Nicola        200       4
============================================================
GIRO 1
  Centri di partenza: A ( 40,  4)  B ( 80,  6)  C (120,  8)
  A (5): Rossi Anna, Bianchi Marco, Verdi Luca, Neri Sara, Fabbri Ilaria
  B (3): Gallo Pietro, Costa Elena, Greco Marta
  C (4): Ricci Paolo, Moro Giulia, Rizzo Dario, Sala Nicola
  Cambi di gruppo:    12 (primo giro: si contano tutti)
  Centri spostati:    A ( 41,  4)  B ( 66, 11)  C (185,  4)
============================================================
GIRO 2
  Centri di partenza: A ( 41,  4)  B ( 66, 11)  C (185,  4)
  A (4): Rossi Anna, Bianchi Marco, Verdi Luca, Fabbri Ilaria
  B (4): Neri Sara, Gallo Pietro, Costa Elena, Greco Marta
  C (4): Ricci Paolo, Moro Giulia, Rizzo Dario, Sala Nicola
  Cambi di gruppo:    1
  Centri spostati:    A ( 38,  2)  B ( 63, 11)  C (185,  4)
============================================================
GIRO 3
  Centri di partenza: A ( 38,  2)  B ( 63, 11)  C (185,  4)
  A (4): Rossi Anna, Bianchi Marco, Verdi Luca, Fabbri Ilaria
  B (4): Neri Sara, Gallo Pietro, Costa Elena, Greco Marta
  C (4): Ricci Paolo, Moro Giulia, Rizzo Dario, Sala Nicola
  Cambi di gruppo:    0
  Centri spostati:    A ( 38,  2)  B ( 63, 11)  C (185,  4)
============================================================
ASSEGNAZIONE FINALE
CLIENTE          SPESA  ORDINI  GRUPPO  DISTANZA
------------------------------------------------------------
Rossi Anna          30       2  A              8
Bianchi Marco       40       3  A              3
Verdi Luca          35       1  A              4
Neri Sara           55      11  B              8
Gallo Pietro        65       9  B              4
Costa Elena         60      13  B              5
Ricci Paolo        170       4  C             15
Moro Giulia        190       3  C              6
Rizzo Dario        180       5  C              6
Fabbri Ilaria       47       2  A              9
Greco Marta         72      10  B             10
Sala Nicola        200       4  C             15
------------------------------------------------------------
I NOMI DEI GRUPPI LI METTETE VOI
A ( 38,  2) - spende poco e ordina di rado
B ( 63, 11) - spende poco per volta ma ordina spesso
C (185,  4) - spende molto e ordina di rado
------------------------------------------------------------
Dal primo al secondo giro si è mosso un cliente solo; dal
secondo al terzo, nessuno. Quando nessuno cambia gruppo, il
giro dopo darebbe lo stesso risultato: si è fermato da solo.
------------------------------------------------------------
Nessuno ha detto al programma quali gruppi cercare: li ha
formati da solo. Non c'è altro nel raggruppamento: assegna,
sposta, ripeti finché smette.
============================================================
"""

# Scrivi il tuo codice qui
