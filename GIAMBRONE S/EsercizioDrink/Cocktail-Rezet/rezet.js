// ============================================================
//  SIMULAZIONE REZET - alcol nel sangue durante la serata
// ============================================================
//
//  Questo file è indipendente da cocktail.js: non condividono
//  variabili. Comunicano solo attraverso la pagina (il DOM):
//  cocktail.js crea i pulsanti ".aggiungi-drink" sulle schede,
//  rezet.js ascolta i click su quei pulsanti.
//
//  ATTENZIONE: il modello qui sotto è una semplificazione didattica
//  e illustrativa, con numeri scelti per rendere leggibile il grafico.
//  Non rappresenta misure reali e non va usato per decidere se guidare.
//
//  Struttura del file:
//    1. parametri del modello
//    2. stato della simulazione (drink e momento REZET)
//    3. calcolo delle due curve (con e senza REZET)
//    4. disegno del grafico SVG
//    5. animazione con requestAnimationFrame
//    6. collegamento ai pulsanti
// ------------------------------------------------------------


// ------------------------------------------------------------
//  1. Parametri del modello (unità arbitrarie)
// ------------------------------------------------------------
const DURATA_ORE = 8;             // la finestra temporale del grafico
const PASSO_MIN = 1;              // calcoliamo un punto ogni minuto
const ALCOL_PER_DRINK = 0.3;      // quanto alza il livello un cocktail
const MINUTI_ASSORBIMENTO = 30;   // in quanti minuti il drink "entra" nel sangue
const SMALTIMENTO_ORARIO = 0.15;  // quanto scende il livello ogni ora, naturalmente
const FATTORE_REZET = 3;          // di quanto accelera lo smaltimento dopo REZET
const ATTESA_REZET_MIN = 25;      // minuti prima che REZET faccia effetto (dal rituale)
const PRIMO_DRINK_ORE = 0.5;      // il primo cocktail arriva a mezz'ora dall'inizio
const INTERVALLO_DRINK_ORE = 0.75;// distanza tra un cocktail e il successivo


// ------------------------------------------------------------
//  2. Stato della simulazione
// ------------------------------------------------------------
// Tutto ciò che l'utente può cambiare sta in questo oggetto.
// Ogni volta che cambia, ricalcoliamo le curve e ridisegniamo.
const serata = {
  drink: [],        // es. [{ nome: "Negroni", ora: 0.5 }, ...]
  oraRezet: null    // null finché non si preme "Prendi REZET"
};


// ------------------------------------------------------------
//  Riferimenti agli elementi della pagina
// ------------------------------------------------------------
const svg = document.getElementById("sim-grafico");
const griglia = document.getElementById("sim-griglia");
const asse = document.getElementById("sim-asse");
const area = document.getElementById("sim-area");
const curvaCon = document.getElementById("sim-curva-con");
const curvaSenza = document.getElementById("sim-curva-senza");
const gruppoDrink = document.getElementById("sim-drink");
const marcatoreRezet = document.getElementById("sim-marcatore-rezet");
const clipRect = document.getElementById("sim-clip-rect");
const playhead = document.getElementById("sim-playhead");
const fialaLivello = document.getElementById("fiala-livello");
const fialaValore = document.getElementById("fiala-valore");
const simStato = document.getElementById("sim-stato");
const btnDrink = document.getElementById("sim-btn-drink");
const btnRezet = document.getElementById("sim-btn-rezet");
const btnReset = document.getElementById("sim-btn-reset");
const risultati = document.getElementById("risultati");
const riquadroRezetSim = document.getElementById("rezet");

// Geometria del grafico: il viewBox dell'SVG è 640x240, lasciamo
// margini per le etichette. Queste costanti servono a convertire
// "ore" e "livello" in pixel.
const GRAFICO = { sinistra: 40, destra: 620, alto: 20, basso: 210 };


// ------------------------------------------------------------
//  3. Calcolo delle curve
// ------------------------------------------------------------
// Simuliamo minuto per minuto. Il parametro "conRezet" decide se
// applicare l'accelerazione dello smaltimento: chiamando la funzione
// due volte otteniamo le due curve da confrontare.
//
// Restituisce un array di punti { ora, livello }.
function calcolaCurva(conRezet) {
  const punti = [];
  let livello = 0;
  const totaleMinuti = DURATA_ORE * 60;

  // Il drink entra gradualmente: ogni minuto, per 30 minuti,
  // aggiunge una frazione del suo alcol totale.
  const assorbimentoAlMinuto = ALCOL_PER_DRINK / MINUTI_ASSORBIMENTO;

  for (let minuto = 0; minuto <= totaleMinuti; minuto += PASSO_MIN) {
    const ora = minuto / 60;

    // Assorbimento: sommiamo i contributi dei drink "in corso"
    for (const d of serata.drink) {
      const inizio = d.ora * 60;
      if (minuto >= inizio && minuto < inizio + MINUTI_ASSORBIMENTO) {
        livello += assorbimentoAlMinuto;
      }
    }

    // Smaltimento: naturale, oppure accelerato se REZET è attivo
    let smaltimentoAlMinuto = SMALTIMENTO_ORARIO / 60;
    const rezetAttivo =
      conRezet &&
      serata.oraRezet !== null &&
      minuto >= serata.oraRezet * 60 + ATTESA_REZET_MIN;
    if (rezetAttivo) {
      smaltimentoAlMinuto *= FATTORE_REZET;
    }

    // Math.max evita che il livello scenda sotto zero
    livello = Math.max(0, livello - smaltimentoAlMinuto);

    punti.push({ ora, livello });
  }

  return punti;
}

// Trova dopo quante ore il livello torna a zero (dopo l'ultimo drink).
// Restituisce null se non arriva a zero entro la finestra.
function oraDiAzzeramento(punti) {
  const ultimoDrink = serata.drink.length
    ? serata.drink[serata.drink.length - 1].ora
    : 0;

  const punto = punti.find((p) => p.ora > ultimoDrink + 0.1 && p.livello < 0.005);
  return punto ? punto.ora : null;
}

// Formatta 3.25 ore come "3 h 15 min"
function formattaOre(ore) {
  const h = Math.floor(ore);
  const m = Math.round((ore - h) * 60);
  return m ? `${h} h ${m} min` : `${h} h`;
}


// ------------------------------------------------------------
//  4. Disegno del grafico SVG
// ------------------------------------------------------------
// Conversione da dati a coordinate SVG.
// L'asse Y dell'SVG cresce verso il basso, quindi per il livello
// partiamo dal bordo inferiore e sottraiamo.
function xDiOra(ora) {
  const larghezza = GRAFICO.destra - GRAFICO.sinistra;
  return GRAFICO.sinistra + (ora / DURATA_ORE) * larghezza;
}

function yDiLivello(livello, massimo) {
  const altezza = GRAFICO.basso - GRAFICO.alto;
  return GRAFICO.basso - (livello / massimo) * altezza;
}

// Costruisce l'attributo "d" di un <path> a partire dai punti.
// "M" sposta la penna al primo punto, "L" traccia linee ai successivi.
function pathDaPunti(punti, massimo) {
  return punti
    .map((p, i) => `${i === 0 ? "M" : "L"}${xDiOra(p.ora).toFixed(1)},${yDiLivello(p.livello, massimo).toFixed(1)}`)
    .join(" ");
}

// Variante "chiusa" per l'area colorata sotto la curva: dopo la
// linea scendiamo al bordo inferiore e torniamo all'inizio ("Z").
function pathArea(punti, massimo) {
  const linea = pathDaPunti(punti, massimo);
  const fine = xDiOra(punti[punti.length - 1].ora).toFixed(1);
  const inizio = xDiOra(punti[0].ora).toFixed(1);
  return `${linea} L${fine},${GRAFICO.basso} L${inizio},${GRAFICO.basso} Z`;
}

// Mostra o nasconde un elemento SVG.
// Gli elementi HTML hanno la proprietà JavaScript "hidden", quelli SVG
// no: su di essi dobbiamo agire direttamente sull'attributo, e il CSS
// (#sim-grafico [hidden]) si occupa di nasconderli davvero.
function mostraSvg(elemento, visibile) {
  if (visibile) {
    elemento.removeAttribute("hidden");
  } else {
    elemento.setAttribute("hidden", "");
  }
}

// Crea un elemento SVG. Serve il namespace, altrimenti il browser
// crea un normale elemento HTML che non viene disegnato nell'SVG.
function elementoSvg(nome, attributi = {}) {
  const el = document.createElementNS("http://www.w3.org/2000/svg", nome);
  for (const [chiave, valore] of Object.entries(attributi)) {
    el.setAttribute(chiave, valore);
  }
  return el;
}

// Griglia e asse del tempo: disegnati una volta sola all'avvio
function disegnaGriglia() {
  for (let ora = 0; ora <= DURATA_ORE; ora += 2) {
    const x = xDiOra(ora);
    griglia.appendChild(elementoSvg("line", { x1: x, y1: GRAFICO.alto, x2: x, y2: GRAFICO.basso }));
    const etichetta = elementoSvg("text", { x, y: GRAFICO.basso + 20 });
    etichetta.textContent = ora === 0 ? "inizio" : `${ora} h`;
    asse.appendChild(etichetta);
  }
  for (let frazione = 0.25; frazione < 1; frazione += 0.25) {
    const y = GRAFICO.basso - frazione * (GRAFICO.basso - GRAFICO.alto);
    griglia.appendChild(elementoSvg("line", { x1: GRAFICO.sinistra, y1: y, x2: GRAFICO.destra, y2: y }));
  }
}

// Ridisegna tutto ciò che dipende dallo stato. Restituisce le due
// curve e il massimo, che servono anche all'animazione.
function disegna() {
  const con = calcolaCurva(true);
  const senza = calcolaCurva(false);

  // Scala verticale: almeno 1, altrimenti il 10% sopra il picco,
  // così la curva non tocca mai il bordo superiore.
  const picco = Math.max(...senza.map((p) => p.livello));
  const massimo = Math.max(1, picco * 1.1);

  curvaCon.setAttribute("d", pathDaPunti(con, massimo));
  curvaSenza.setAttribute("d", pathDaPunti(senza, massimo));
  area.setAttribute("d", pathArea(con, massimo));

  // Un pallino con bicchiere per ogni drink, posizionato sulla curva
  gruppoDrink.innerHTML = "";
  for (const d of serata.drink) {
    const puntoCurva = con[Math.round(d.ora * 60)];
    const x = xDiOra(d.ora);
    const y = yDiLivello(puntoCurva.livello, massimo);
    gruppoDrink.appendChild(elementoSvg("circle", { cx: x, cy: y, r: 5, fill: "#ffffff" }));
    const icona = elementoSvg("text", { x, y: y - 10 });
    icona.textContent = "🍸";
    const titolo = elementoSvg("title");
    titolo.textContent = d.nome;
    icona.appendChild(titolo);
    gruppoDrink.appendChild(icona);
  }

  // Linea verticale nel momento in cui si prende REZET
  if (serata.oraRezet !== null) {
    const x = xDiOra(serata.oraRezet);
    marcatoreRezet.querySelector("line").setAttribute("x1", x);
    marcatoreRezet.querySelector("line").setAttribute("x2", x);
    marcatoreRezet.querySelector("text").setAttribute("x", x);
    mostraSvg(marcatoreRezet, true);
  } else {
    mostraSvg(marcatoreRezet, false);
  }

  return { con, senza, massimo };
}


// ------------------------------------------------------------
//  5. Animazione
// ------------------------------------------------------------
// Il trucco: le curve sono già disegnate per intero, ma un
// <clipPath> con un rettangolo di larghezza 0 le nasconde. Allargando
// il rettangolo un po' alla volta, le curve "appaiono" da sinistra a
// destra, come se venissero tracciate in tempo reale.
//
// requestAnimationFrame chiede al browser di richiamare la nostra
// funzione prima del prossimo ridisegno dello schermo (circa 60
// volte al secondo): è il modo corretto di fare animazioni in JS.
let animazioneInCorso = null;

function anima({ con, massimo }) {
  // Se un'animazione precedente è ancora in corso la fermiamo
  if (animazioneInCorso) cancelAnimationFrame(animazioneInCorso);

  const DURATA_MS = 2500;
  let partenza = null;
  mostraSvg(playhead, true);

  function passo(timestamp) {
    if (partenza === null) partenza = timestamp;

    // Avanzamento da 0 a 1 in DURATA_MS millisecondi
    const avanzamento = Math.min(1, (timestamp - partenza) / DURATA_MS);
    const oraCorrente = avanzamento * DURATA_ORE;
    const x = xDiOra(oraCorrente);

    // Allarghiamo la finestra visibile e spostiamo la linea verticale
    clipRect.setAttribute("width", x);
    playhead.setAttribute("x1", x);
    playhead.setAttribute("x2", x);

    // La fiala segue la curva "con REZET" nel momento corrente
    const punto = con[Math.min(con.length - 1, Math.round(oraCorrente * 60))];
    aggiornaFiala(punto.livello, massimo);

    if (avanzamento < 1) {
      animazioneInCorso = requestAnimationFrame(passo);
    } else {
      mostraSvg(playhead, false);
      animazioneInCorso = null;
    }
  }

  animazioneInCorso = requestAnimationFrame(passo);
}

// La fiala è verticale su schermi larghi e orizzontale su quelli
// stretti (vedi CSS): impostiamo sia height che width, il CSS userà
// quella giusta.
function aggiornaFiala(livello, massimo) {
  const percentuale = Math.round((livello / massimo) * 100);
  fialaLivello.style.height = `${percentuale}%`;
  fialaLivello.style.width = `${percentuale}%`;
  fialaValore.textContent = livello.toFixed(2);
}


// ------------------------------------------------------------
//  Aggiornamento completo: ricalcola, ridisegna, anima, messaggio
// ------------------------------------------------------------
function aggiorna() {
  const dati = disegna();
  anima(dati);

  // Pulsanti: dopo REZET il rituale dice "niente più alcol"
  const rezetPreso = serata.oraRezet !== null;
  btnDrink.disabled = rezetPreso;
  btnRezet.disabled = rezetPreso || serata.drink.length === 0;
  document.querySelectorAll(".aggiungi-drink").forEach((b) => (b.disabled = rezetPreso));

  // Messaggio di riepilogo
  const n = serata.drink.length;
  if (n === 0) {
    simStato.textContent = "Nessun drink ancora.";
    return;
  }

  const zeroCon = oraDiAzzeramento(dati.con);
  const zeroSenza = oraDiAzzeramento(dati.senza);
  const testoZero = (ore) => (ore === null ? `oltre ${DURATA_ORE} h` : formattaOre(ore));

  if (rezetPreso) {
    simStato.textContent =
      `${n} drink. A zero in ${testoZero(zeroCon)} con REZET, ${testoZero(zeroSenza)} senza.`;
  } else {
    simStato.textContent = `${n} drink. Senza REZET torni a zero in ${testoZero(zeroSenza)}.`;
  }
}


// ------------------------------------------------------------
//  6. Azioni dell'utente
// ------------------------------------------------------------
function aggiungiDrink(nome) {
  if (serata.oraRezet !== null) return; // dopo REZET niente più alcol

  // Il primo drink a mezz'ora dall'inizio, poi uno ogni 45 minuti
  const ora = serata.drink.length === 0
    ? PRIMO_DRINK_ORE
    : serata.drink[serata.drink.length - 1].ora + INTERVALLO_DRINK_ORE;

  // Non oltre la finestra del grafico
  if (ora > DURATA_ORE - 1) {
    simStato.textContent = "La serata è già abbastanza lunga!";
    return;
  }

  serata.drink.push({ nome, ora });
  aggiorna();
}

function prendiRezet() {
  if (serata.drink.length === 0 || serata.oraRezet !== null) return;

  // Dal rituale: REZET si prende 10 minuti dopo l'ultimo bicchiere
  const ultimo = serata.drink[serata.drink.length - 1].ora;
  serata.oraRezet = ultimo + 10 / 60;
  aggiorna();
}

function ricomincia() {
  serata.drink = [];
  serata.oraRezet = null;
  aggiorna();
}

btnDrink.addEventListener("click", () => aggiungiDrink("Un drink"));
btnRezet.addEventListener("click", prendiRezet);
btnReset.addEventListener("click", ricomincia);

// Event delegation: un solo ascoltatore sul contenitore dei risultati
// intercetta i click su TUTTI i pulsanti delle schede, anche quelli
// creati dopo (le schede cambiano a ogni ricerca). closest() risale
// dall'elemento cliccato fino al pulsante, se il click era al suo interno.
risultati.addEventListener("click", (evento) => {
  const pulsante = evento.target.closest(".aggiungi-drink");
  if (!pulsante) return;

  aggiungiDrink(pulsante.dataset.nome);

  // Portiamo il grafico in vista, così si vede subito l'effetto
  riquadroRezetSim.scrollIntoView({ behavior: "smooth", block: "start" });
});


// ------------------------------------------------------------
//  Avvio: griglia fissa e primo disegno (curva piatta)
// ------------------------------------------------------------
disegnaGriglia();
aggiorna();
