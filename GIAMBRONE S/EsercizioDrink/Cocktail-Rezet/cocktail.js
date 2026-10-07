// ============================================================
//  RICERCA COCKTAIL - esempio di chiamata a un'API REST pubblica
// ============================================================
//
//  L'API che usiamo è TheCocktailDB: https://www.thecocktaildb.com/api.php
//  Un'API REST si interroga con una semplice richiesta HTTP a un URL.
//  Il server risponde con un testo in formato JSON, che JavaScript
//  sa trasformare in un normale oggetto.
//
//  Flusso generale della pagina:
//    1. l'utente scrive un nome e invia il form
//    2. costruiamo l'URL e facciamo la richiesta con fetch()
//    3. aspettiamo la risposta e la convertiamo da JSON a oggetto
//    4. leggiamo i dati e creiamo gli elementi HTML per mostrarli
// ------------------------------------------------------------


// Chiave API. "1" è la chiave gratuita di test: va bene per imparare,
// ma limita alcuni endpoint (la ricerca per ingrediente restituisce un
// solo risultato). Con la chiave Premium basta sostituire questo valore.
const CHIAVE_API = "1";

// URL base comune a tutti gli endpoint. La chiave fa parte del percorso.
const URL_BASE = `https://www.thecocktaildb.com/api/json/v1/${CHIAVE_API}/`;

// Endpoint usati dalla pagina. Il valore dopo "=" va aggiunto in coda.
//   search.php?s=  ricerca per nome      -> schede complete
//   filter.php?i=  ricerca per ingrediente -> solo id, nome, immagine
//   lookup.php?i=  dettaglio per id       -> scheda completa di un cocktail
const URL_RICERCA_NOME = URL_BASE + "search.php?s=";
const URL_FILTRO_INGREDIENTE = URL_BASE + "filter.php?i=";
const URL_DETTAGLIO = URL_BASE + "lookup.php?i=";

// Lingua delle istruzioni di preparazione.
// L'API non accetta un parametro lingua nella richiesta: restituisce
// sempre le istruzioni in tutte le lingue disponibili, in campi separati:
//   strInstructions        -> inglese (sempre presente)
//   strInstructionsIT      -> italiano
//   strInstructionsES      -> spagnolo
//   strInstructionsDE      -> tedesco
//   strInstructionsFR      -> francese
//   strInstructionsZH-HANS -> cinese semplificato
//   strInstructionsZH-HANT -> cinese tradizionale
// Sta a noi scegliere quale campo leggere. Cambiando questa costante
// (es. "DE") la pagina mostrerà le istruzioni in quella lingua.
// Nota: nome, ingredienti, categoria e bicchiere sono solo in inglese.
const LINGUA = "IT";


// ------------------------------------------------------------
//  Riferimenti agli elementi della pagina
// ------------------------------------------------------------
// Li recuperiamo una volta sola all'avvio invece di cercarli
// ogni volta che servono: è più veloce e più leggibile.
const form = document.getElementById("form-ricerca");
const campo = document.getElementById("campo-ricerca");
const formIngrediente = document.getElementById("form-ingrediente");
const campoIngrediente = document.getElementById("campo-ingrediente");
// Tutti i pulsanti di invio: li disabilitiamo insieme durante l'attesa.
const bottoni = document.querySelectorAll(".ricerca button");
const stato = document.getElementById("stato");
const contenitore = document.getElementById("risultati");
// Riquadro del partner REZET: lo mostriamo solo quando ci sono risultati,
// così la pagina all'apertura resta pulita.
const riquadroRezet = document.getElementById("rezet");


// ------------------------------------------------------------
//  1. Ascoltiamo l'invio del form
// ------------------------------------------------------------
// L'evento "submit" scatta sia cliccando il pulsante sia premendo
// Invio nel campo di testo. La funzione è "async" perché al suo
// interno useremo "await" per aspettare la risposta del server.
form.addEventListener("submit", async (evento) => {
  // Di default il browser ricaricherebbe la pagina inviando il form.
  // Lo blocchiamo: vogliamo gestire tutto noi con JavaScript.
  evento.preventDefault();

  // trim() toglie gli spazi all'inizio e alla fine del testo.
  const nome = campo.value.trim();
  if (!nome) return; // campo vuoto: non facciamo nulla

  await cercaCocktail(nome);
});

// Stesso schema per la ricerca per ingrediente.
formIngrediente.addEventListener("submit", async (evento) => {
  evento.preventDefault();

  const ingrediente = campoIngrediente.value.trim();
  if (!ingrediente) return;

  await cercaPerIngrediente(ingrediente);
});


// ------------------------------------------------------------
//  2 e 3. Chiamata all'API
// ------------------------------------------------------------
async function cercaCocktail(nome) {
  // Feedback immediato all'utente: la richiesta può richiedere
  // qualche istante e la pagina non deve sembrare "morta".
  mostraStato("Ricerca in corso...");
  contenitore.innerHTML = "";   // svuotiamo i risultati precedenti
  riquadroRezet.hidden = true;  // riquadro partner nascosto durante l'attesa
  abilitaBottoni(false);        // evitiamo doppi click durante l'attesa

  // try/catch: tutto ciò che può fallire (rete assente, server giù,
  // risposta malformata) viene intercettato nel blocco catch.
  try {
    // encodeURIComponent() rende sicuro il testo da inserire in un URL:
    // spazi, accenti e simboli come "&" o "?" vengono codificati,
    // es. "piña colada" diventa "pi%C3%B1a%20colada".
    //
    // fetch() invia la richiesta HTTP (GET, di default) e restituisce
    // una Promise. "await" mette in pausa la funzione finché il server
    // non risponde, senza bloccare il resto della pagina.
    const risposta = await fetch(URL_RICERCA_NOME + encodeURIComponent(nome));

    // fetch() NON considera errore una risposta 404 o 500: lo dobbiamo
    // verificare noi. risposta.ok è true solo per i codici 200-299.
    if (!risposta.ok) {
      throw new Error(`Errore HTTP ${risposta.status}`);
    }

    // Il corpo della risposta è testo JSON. Il metodo .json() lo legge
    // e lo converte in un oggetto JavaScript. Anche questa operazione
    // è asincrona (i dati arrivano a pezzi dalla rete), quindi "await".
    const dati = await risposta.json();

    // Struttura della risposta di TheCocktailDB:
    //   { "drinks": [ {...}, {...} ] }   se ci sono risultati
    //   { "drinks": null }               se non ne trova nessuno
    const cocktails = dati.drinks;

    if (!cocktails) {
      mostraStato(`Nessun cocktail trovato per "${nome}".`);
      return;
    }

    mostraStato(`${cocktails.length} risultat${cocktails.length === 1 ? "o" : "i"} per "${nome}".`);

    // Per ogni cocktail dell'array creiamo una scheda e la aggiungiamo
    // alla pagina.
    cocktails.forEach((cocktail) => {
      contenitore.appendChild(creaScheda(cocktail));
    });

    // Ci sono cocktail da mostrare: rendiamo visibile il riquadro REZET.
    // L'attributo HTML "hidden" si controlla da JavaScript con la
    // proprietà omonima: true nasconde, false mostra.
    riquadroRezet.hidden = false;

  } catch (errore) {
    // Qui arriviamo se fetch() fallisce (es. nessuna connessione),
    // se abbiamo lanciato noi l'errore HTTP, o se il JSON non è valido.
    mostraStato("Impossibile contattare il servizio. Riprova più tardi.", true);
    console.error(errore); // dettagli tecnici nella console del browser

  } finally {
    // "finally" viene eseguito sempre, sia in caso di successo che di
    // errore: il posto giusto per riabilitare i pulsanti.
    abilitaBottoni(true);
  }
}


// ------------------------------------------------------------
//  Ricerca per ingrediente: DUE chiamate concatenate
// ------------------------------------------------------------
// L'endpoint filter.php restituisce solo una lista "leggera":
//   { "drinks": [ { idDrink, strDrink, strDrinkThumb }, ... ] }
// Mancano ingredienti e istruzioni. Per avere la scheda completa
// dobbiamo fare una seconda chiamata a lookup.php per OGNI cocktail.
//
// Attenzione: con la chiave di test "1" filter.php restituisce un solo
// cocktail. Il codice è comunque scritto per gestirne molti.
async function cercaPerIngrediente(ingrediente) {
  mostraStato("Ricerca in corso...");
  contenitore.innerHTML = "";
  riquadroRezet.hidden = true;
  abilitaBottoni(false);

  try {
    // --- Prima chiamata: la lista degli id ---
    const risposta = await fetch(URL_FILTRO_INGREDIENTE + encodeURIComponent(ingrediente));
    if (!risposta.ok) {
      throw new Error(`Errore HTTP ${risposta.status}`);
    }

    const dati = await risposta.json();
    const lista = dati.drinks;

    // Se l'ingrediente non esiste l'API restituisce drinks: null oppure,
    // in alcuni casi, una stringa vuota: controlliamo che sia un array.
    if (!Array.isArray(lista) || lista.length === 0) {
      mostraStato(`Nessun cocktail trovato con "${ingrediente}".`);
      return;
    }

    mostraStato(`Trovati ${lista.length} cocktail, carico i dettagli...`);

    // --- Seconda fase: il dettaglio di ogni cocktail ---
    // Invece di aspettare una chiamata alla volta (lenta), le avviamo
    // tutte insieme: .map() crea un array di Promise e Promise.all()
    // aspetta che siano TUTTE completate, restituendo i risultati
    // nello stesso ordine della lista.
    const dettagli = await Promise.all(
      lista.map((voce) => caricaDettaglio(voce.idDrink))
    );

    // Qualche dettaglio potrebbe essere null (chiamata fallita): lo saltiamo.
    const cocktails = dettagli.filter((c) => c !== null);

    mostraStato(`${cocktails.length} risultat${cocktails.length === 1 ? "o" : "i"} con "${ingrediente}".`);
    cocktails.forEach((cocktail) => {
      contenitore.appendChild(creaScheda(cocktail));
    });

    riquadroRezet.hidden = cocktails.length === 0;

  } catch (errore) {
    mostraStato("Impossibile contattare il servizio. Riprova più tardi.", true);
    console.error(errore);

  } finally {
    abilitaBottoni(true);
  }
}


// ------------------------------------------------------------
//  Funzione di supporto: dettaglio di un singolo cocktail
// ------------------------------------------------------------
// lookup.php?i=ID restituisce { "drinks": [ {...} ] } con un solo
// elemento, nello stesso formato della ricerca per nome.
// In caso di errore restituiamo null invece di lanciare un'eccezione:
// così un singolo cocktail che fallisce non fa saltare tutta la ricerca.
async function caricaDettaglio(id) {
  try {
    const risposta = await fetch(URL_DETTAGLIO + encodeURIComponent(id));
    if (!risposta.ok) return null;

    const dati = await risposta.json();
    return dati.drinks ? dati.drinks[0] : null;
  } catch (errore) {
    console.error(`Dettaglio ${id} non caricato`, errore);
    return null;
  }
}


// ------------------------------------------------------------
//  Funzione di supporto: abilita/disabilita i pulsanti
// ------------------------------------------------------------
function abilitaBottoni(abilitati) {
  bottoni.forEach((b) => (b.disabled = !abilitati));
}


// ------------------------------------------------------------
//  Funzione di supporto: messaggio di stato
// ------------------------------------------------------------
function mostraStato(messaggio, errore = false) {
  stato.textContent = messaggio;
  // Aggiunge la classe CSS "errore" se errore è true, la toglie altrimenti.
  stato.classList.toggle("errore", errore);
}


// ------------------------------------------------------------
//  Funzione di supporto: estrazione ingredienti
// ------------------------------------------------------------
// TheCocktailDB non restituisce gli ingredienti come array, ma come
// 15 coppie di campi separati:
//   strIngredient1, strMeasure1, strIngredient2, strMeasure2, ...
// I campi non usati valgono null o stringa vuota.
// Questa funzione li raccoglie in un array di oggetti { nome, dose },
// molto più comodo da usare.
function estraiIngredienti(cocktail) {
  const ingredienti = [];

  for (let i = 1; i <= 15; i++) {
    // Con la notazione a parentesi quadre possiamo costruire il nome
    // della proprietà in modo dinamico: cocktail["strIngredient3"]
    const ingrediente = cocktail[`strIngredient${i}`];
    const dose = cocktail[`strMeasure${i}`];

    if (ingrediente && ingrediente.trim()) {
      ingredienti.push({
        nome: ingrediente.trim(),
        dose: dose ? dose.trim() : ""
      });
    }
  }

  return ingredienti;
}


// ------------------------------------------------------------
//  4. Costruzione della scheda HTML di un cocktail
// ------------------------------------------------------------
// Riceve l'oggetto restituito dall'API e restituisce un elemento
// <article> pronto da inserire nella pagina.
//
// Creiamo gli elementi con document.createElement() e assegniamo il
// testo con .textContent invece di comporre una stringa HTML:
// così il testo che arriva dall'API viene mostrato letteralmente e
// non può essere interpretato come codice HTML (protezione XSS).
function creaScheda(cocktail) {
  const scheda = document.createElement("article");
  scheda.className = "scheda";

  // Immagine del cocktail
  const immagine = document.createElement("img");
  immagine.src = cocktail.strDrinkThumb;   // URL fornito dall'API
  immagine.alt = cocktail.strDrink;
  immagine.loading = "lazy";               // scaricata solo quando visibile

  const corpo = document.createElement("div");
  corpo.className = "scheda-corpo";

  // Nome
  const titolo = document.createElement("h2");
  titolo.textContent = cocktail.strDrink;

  // Etichette: alcolico / categoria / bicchiere
  const etichette = document.createElement("div");
  etichette.className = "etichette";
  [
    { testo: cocktail.strAlcoholic, classe: "alcolico" },
    { testo: cocktail.strCategory },
    { testo: cocktail.strGlass }
  ].forEach(({ testo, classe }) => {
    if (!testo) return; // campo assente: saltiamo l'etichetta
    const etichetta = document.createElement("span");
    etichetta.className = "etichetta" + (classe ? ` ${classe}` : "");
    etichetta.textContent = testo;
    etichette.appendChild(etichetta);
  });

  // Lista ingredienti
  const sezioneIngredienti = document.createElement("div");
  const titoloIngredienti = document.createElement("h3");
  titoloIngredienti.textContent = "Ingredienti";
  const lista = document.createElement("ul");
  lista.className = "ingredienti";

  estraiIngredienti(cocktail).forEach(({ nome, dose }) => {
    const voce = document.createElement("li");
    const nomeSpan = document.createElement("span");
    nomeSpan.textContent = nome;
    const doseSpan = document.createElement("span");
    doseSpan.className = "dose";
    doseSpan.textContent = dose;
    voce.append(nomeSpan, doseSpan);
    lista.appendChild(voce);
  });

  sezioneIngredienti.append(titoloIngredienti, lista);

  // Istruzioni di preparazione nella lingua scelta.
  // Costruiamo il nome del campo in modo dinamico: con LINGUA = "IT"
  // leggiamo cocktail["strInstructionsIT"]. Non tutti i cocktail hanno
  // la traduzione, quindi l'operatore || prende il primo valore "vero":
  // lingua scelta se c'è, altrimenti inglese, altrimenti un fallback.
  const sezioneIstruzioni = document.createElement("div");
  const titoloIstruzioni = document.createElement("h3");
  titoloIstruzioni.textContent = "Preparazione";
  const istruzioni = document.createElement("p");
  istruzioni.className = "istruzioni";
  istruzioni.textContent =
    cocktail[`strInstructions${LINGUA}`] || cocktail.strInstructions || "Istruzioni non disponibili.";
  sezioneIstruzioni.append(titoloIstruzioni, istruzioni);

  // Pulsante per aggiungere il cocktail alla simulazione REZET.
  // Qui non mettiamo nessun codice di gestione del click: ci pensa
  // rezet.js ascoltando i click sull'intero contenitore dei risultati
  // (tecnica detta "event delegation"). Il nome del cocktail viaggia
  // nell'attributo data-nome, leggibile in JS con button.dataset.nome.
  const aggiungi = document.createElement("button");
  aggiungi.type = "button";
  aggiungi.className = "aggiungi-drink";
  aggiungi.dataset.nome = cocktail.strDrink;
  aggiungi.textContent = "+ Aggiungi alla serata";

  // Assembliamo tutti i pezzi e restituiamo la scheda completa
  corpo.append(titolo, etichette, sezioneIngredienti, sezioneIstruzioni, aggiungi);
  scheda.append(immagine, corpo);

  return scheda;
}
