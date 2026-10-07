"""
GESTIONE ERRORI IN PYTHON - ESEMPI COMPLETI E COMMENTATI
========================================================

File didattico unico con esempi progressivi su:
- try / except
- eccezioni specifiche
- ValueError, TypeError, FileNotFoundError, IndexError, KeyError
- else / finally
- raise
- eccezioni personalizzate
- traceback
- retry pattern
- logging
- propagazione
- re-raising
- exception chaining
- assert
- guard clause
- errori in JSON / CSV
- async
- mini progetti finali

OBIETTIVO:
Scrivere programmi Python robusti, capaci di reagire agli errori
senza bloccarsi in modo brutale.
"""

import csv
import json
import time
import asyncio
import logging
import traceback
from pathlib import Path

BASE_DIR = Path("demo_errori_python")
BASE_DIR.mkdir(exist_ok=True)

print("\nCartella demo:", BASE_DIR.resolve())

print("\n--- 1. PERCHÉ GESTIRE GLI ERRORI ---")
print("Ogni programma reale può fallire.")
print("La gestione errori evita crash brutali e rende il software più professionale.")

print("\n--- 2. ERRORE NON GESTITO: ESEMPIO COMMENTATO ---")
print("10 / 0 genera ZeroDivisionError se non viene gestito.")
# x = 10 / 0

print("\n--- 3. TRY / EXCEPT BASE ---")
try:
    x = 10 / 0
except:
    print("Si è verificato un errore generico.")

print("\n--- 4. ECCEZIONE SPECIFICA ---")
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Non puoi dividere per zero.")

print("\n--- 5. ValueError ---")
try:
    numero = int("ciao")
except ValueError:
    print("Conversione non valida: 'ciao' non può diventare intero.")

print("\n--- 6. INPUT UTENTE SICURO - SIMULATO ---")
input_simulato = "abc"
try:
    numero = int(input_simulato)
    print("Numero:", numero)
except ValueError:
    print("Errore: devi inserire un numero valido.")

print("\n--- 7. PIÙ EXCEPT SEPARATI ---")
valore = "0"
try:
    x = int(valore)
    y = 10 / x
except ValueError:
    print("Input non valido.")
except ZeroDivisionError:
    print("Non puoi dividere per zero.")

print("\n--- 8. PIÙ ECCEZIONI INSIEME ---")
valore = "abc"
try:
    x = int(valore)
    y = 10 / x
except (ValueError, ZeroDivisionError):
    print("Errore nei dati inseriti.")

print("\n--- 9. MESSAGGIO DELL'ERRORE ---")
try:
    x = 10 / 0
except ZeroDivisionError as e:
    print("Errore dettagliato:", e)

print("\n--- 10. BLOCCO ELSE ---")
valore = "25"
try:
    x = int(valore)
except ValueError:
    print("Errore input.")
else:
    print("Valore valido:", x)

print("\n--- 11. BLOCCO FINALLY ---")
try:
    x = 10 / 2
except ZeroDivisionError:
    print("Errore divisione.")
finally:
    print("Operazione completata.")

print("\n--- 12. FILE NON TROVATO ---")
try:
    with open(BASE_DIR / "dati_inesistenti.txt", "r", encoding="utf-8") as f:
        print(f.read())
except FileNotFoundError:
    print("File non trovato.")

print("\n--- 13. ValueError vs TypeError ---")
try:
    x = int("10.5")
except ValueError:
    print("ValueError: il valore non è convertibile in int.")

try:
    risultato = "ciao" + 10
except TypeError:
    print("TypeError: stai usando tipi incompatibili.")

print("\n--- 14. IndexError ---")
lista = [1, 2, 3]
try:
    print(lista[5])
except IndexError:
    print("Indice fuori range.")

print("\n--- 15. KeyError ---")
d = {"nome": "Daniele"}
try:
    print(d["eta"])
except KeyError:
    print("Chiave non esistente.")

eta = d.get("eta", "Non disponibile")
print("Età con get():", eta)

print("\n--- 16. RAISE ---")
def dividi(a, b):
    """Divide due numeri e genera errore se b è zero."""
    if b == 0:
        raise ValueError("b non può essere zero")
    return a / b

try:
    print(dividi(10, 0))
except ValueError as e:
    print("Errore gestito:", e)

print("\n--- 17. ECCEZIONE PERSONALIZZATA ---")
class PrezzoNegativoError(Exception):
    pass

def set_prezzo(prezzo):
    if prezzo < 0:
        raise PrezzoNegativoError("Prezzo non valido: non può essere negativo.")
    return prezzo

try:
    set_prezzo(-10)
except PrezzoNegativoError as e:
    print("Errore prezzo:", e)

print("\n--- 18. TRACEBACK ---")
print("Il traceback mostra file, riga e tipo di errore.")
print("È una mappa per capire dove intervenire.")

print("\n--- 19. NON ABUSARE DEI TRY ---")
print("Evitare try molto grandi con except: pass, perché nascondono errori importanti.")

print("\n--- 20. PATTERN RETRY ---")
valori = ["0", "abc", "2"]
risultato = None

for tentativo, valore in enumerate(valori, start=1):
    try:
        print("Tentativo:", tentativo, "- valore:", valore)
        risultato = 10 / int(valore)
        break
    except (ValueError, ZeroDivisionError):
        print("Riprova: valore non valido.")

print("Risultato finale:", risultato)

print("\n--- 21. ERRORI IN LOOP ---")
for val in ["10", "a", "5"]:
    try:
        print("Convertito:", int(val))
    except ValueError:
        print("Valore non valido:", val)

print("\n--- 22. LOGGING ---")
log_path = BASE_DIR / "errori.log"
logging.basicConfig(
    filename=log_path,
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    force=True
)

try:
    x = 10 / 0
except ZeroDivisionError:
    logging.error("Divisione per zero intercettata.")
    print("Errore scritto nel file log:", log_path)

print("\n--- 23. ECCEZIONI ANNIDATE ---")
try:
    try:
        x = 10 / 0
    except ZeroDivisionError:
        print("Errore interno intercettato.")
        raise
except ZeroDivisionError:
    print("Errore propagato al blocco esterno.")

print("\n--- 24. FINALLY PER CHIUDERE RISORSE ---")
conn = None
file_risorsa = BASE_DIR / "risorsa.txt"
file_risorsa.write_text("contenuto demo", encoding="utf-8")

try:
    conn = open(file_risorsa, "r", encoding="utf-8")
    print(conn.read())
finally:
    if conn:
        conn.close()
        print("File chiuso nel finally.")

print("\n--- 25. PROPAGAZIONE ---")
def dividi_base(a, b):
    return a / b

def calcola():
    return dividi_base(10, 0)

try:
    calcola()
except ZeroDivisionError:
    print("Errore nato in dividi_base, propagato fino al chiamante.")

print("\n--- 26. INTERCETTARE AL LIVELLO CORRETTO ---")
def calcola_sicuro(a, b):
    if b == 0:
        raise ValueError("Divisione per zero non consentita.")
    return a / b

try:
    risultato = calcola_sicuro(10, 0)
except ValueError as e:
    print("Errore di calcolo:", e)

print("\n--- 27. RE-RAISING ---")
try:
    try:
        x = 10 / 0
    except ZeroDivisionError as e:
        print("Log errore prima del rilancio:", e)
        raise
except ZeroDivisionError:
    print("Errore rilanciato e gestito più in alto.")

print("\n--- 28. EXCEPTION CHAINING ---")
try:
    try:
        int("abc")
    except ValueError as e:
        raise RuntimeError("Errore conversione numero") from e
except RuntimeError as e:
    print("Errore nuovo:", e)
    print("Causa originale:", type(e.__cause__).__name__, "-", e.__cause__)

print("\n--- 29. GERARCHIA ECCEZIONI CUSTOM ---")
class AppError(Exception):
    pass

class ConfigError(AppError):
    pass

class APIError(AppError):
    pass

def carica_config():
    raise ConfigError("Configurazione mancante.")

try:
    carica_config()
except AppError as e:
    print("Errore applicativo:", e)

print("\n--- 30. VALIDAZIONE INPUT AVANZATA ---")
def valida_eta(val):
    try:
        eta = int(val)
        if eta < 0 or eta > 120:
            raise ValueError("Età fuori range.")
        return eta
    except ValueError as e:
        print("Errore età:", e)
        return None

print("Età valida:", valida_eta("35"))
print("Età non valida:", valida_eta("150"))
print("Età testo:", valida_eta("abc"))

print("\n--- 31. TIMEOUT RETE - CONCETTO ---")
print("Nelle API reali è importante impostare timeout.")
print('Esempio: requests.get("https://api.example.com", timeout=3)')

print("\n--- 32. TRANSAZIONE LOGICA E ROLLBACK ---")
def salva_file():
    print("File salvato.")

def aggiorna_database():
    raise RuntimeError("Database offline.")

def rollback_operazioni():
    print("Rollback: annullo operazioni già fatte.")

try:
    salva_file()
    aggiorna_database()
except RuntimeError as e:
    print("Errore:", e)
    rollback_operazioni()

print("\n--- 33. ECCEZIONI DENTRO CLASSI ---")
class Conto:
    def __init__(self, saldo):
        self.saldo = saldo

    def preleva(self, importo):
        if importo <= 0:
            raise ValueError("Importo non valido.")
        if importo > self.saldo:
            raise ValueError("Saldo insufficiente.")
        self.saldo -= importo
        return self.saldo

conto = Conto(100)

try:
    conto.preleva(200)
except ValueError as e:
    print("Errore conto:", e)

print("\n--- 34. ASSERT ---")
x = 10
assert x > 0, "x deve essere positivo"
print("Assert superato.")

print("\n--- 35. GUARD CLAUSE ---")
def dividi_guard(a, b):
    if b == 0:
        return None
    return a / b

print("Divisione valida:", dividi_guard(10, 2))
print("Divisione non valida:", dividi_guard(10, 0))

print("\n--- 36. NON USARE ECCEZIONI PER FLUSSO NORMALE ---")
dizionario = {"nome": "Daniele"}
valore = dizionario.get("eta")
print("Valore con get:", valore)

print("\n--- 37. LOGGING TRACEBACK ---")
try:
    1 / 0
except ZeroDivisionError:
    errore_completo = traceback.format_exc()
    logging.error(errore_completo)
    print("Traceback salvato nel log.")

print("\n--- 38. ECCEZIONI NEI THREAD - CONCETTO ---")
print("Nei thread gli errori possono essere meno visibili.")
print("In sistemi concorrenti bisogna gestire esplicitamente le eccezioni.")

print("\n--- 39. ECCEZIONI ASYNC ---")
async def main_async():
    raise ValueError("Errore async")

try:
    asyncio.run(main_async())
except ValueError as e:
    print("Errore async propagato al loop principale:", e)

print("\n--- 40. TRY ANNIDATI MULTILIVELLO ---")
try:
    try:
        int("abc")
    except ValueError:
        print("Errore interno.")
        raise
except ValueError:
    print("Errore finale.")

print("\n--- 41. FALLBACK ---")
def carica_config_da_file():
    raise FileNotFoundError("Config non trovata.")

def carica_config_default():
    return {"lang": "it", "theme": "dark"}

try:
    cfg = carica_config_da_file()
except FileNotFoundError:
    cfg = carica_config_default()

print("Config caricata:", cfg)

print("\n--- 42. RETRY CON DELAY ---")
for i in range(3):
    try:
        print("Tentativo", i + 1)
        risultato = 10 / 0
        break
    except ZeroDivisionError:
        print("Errore, attendo e riprovo...")
        time.sleep(0.2)

print("Retry terminato.")

print("\n--- 43. DECORATORE SAFE ---")
def safe(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print("Errore gestito dal decoratore:", e)
            return None
    return wrapper

@safe
def funzione_rischiosa():
    return 10 / 0

print("Risultato funzione rischiosa:", funzione_rischiosa())

print("\n--- 44. ERRORI JSON ---")
try:
    json.loads("invalid json")
except json.JSONDecodeError:
    print("JSON malformato.")

print("\n--- 45. ERRORI CSV ---")
try:
    with open(BASE_DIR / "file_inesistente.csv", "r", encoding="utf-8") as f:
        reader = csv.reader(f)
except FileNotFoundError:
    print("CSV non trovato.")

print("\n--- 46. VALIDAZIONE PARAMETRI API ---")
def api_call(url):
    if not url.startswith("http"):
        raise ValueError("URL non valido.")
    return "Chiamata API simulata"

try:
    print(api_call("ftp://example.com"))
except ValueError as e:
    print("Errore URL:", e)

print("\n--- 47. INPUT ROBUSTO - SIMULATO ---")
inputs = ["abc", "10"]
indice_input = 0

while True:
    try:
        valore = inputs[indice_input]
        indice_input += 1
        x = int(valore)
        print("Input valido:", x)
        break
    except ValueError:
        print("Riprova, valore non valido.")

print("\n--- 48. SEPARARE LOGICA ED ERROR HANDLING ---")
def calcola_pulito(a, b):
    return a / b

try:
    calcola_pulito(10, 0)
except ZeroDivisionError:
    print("Errore gestito fuori dalla funzione.")

print("\n--- 49. HANDLER STILE MICROSERVIZIO ---")
def handler():
    try:
        10 / 0
        return {"ok": True}
    except Exception as e:
        return {"ok": False, "error": str(e)}

print("Risposta handler:", handler())

print("\n--- 50. FAIL FAST ---")
def imposta_prezzo(prezzo):
    if prezzo < 0:
        raise ValueError("Prezzo negativo.")
    return prezzo

try:
    imposta_prezzo(-5)
except ValueError as e:
    print("Fail fast:", e)

print("\n--- 51. MINI PROGETTO: VALIDATORE ROBUSTO ---")
def valida_email(email):
    if "@" not in email or "." not in email:
        raise ValueError("Email non valida.")
    return email

def valida_numero(valore):
    try:
        return int(valore)
    except ValueError as e:
        raise ValueError("Numero non valido.") from e

def valida_url(url):
    if not url.startswith("http://") and not url.startswith("https://"):
        raise ValueError("URL non valido.")
    return url

def valida_utente(email, eta, url):
    return {
        "email": valida_email(email),
        "eta": valida_numero(eta),
        "url": valida_url(url)
    }

try:
    utente = valida_utente("test@email.com", "35", "https://example.com")
    print("Utente valido:", utente)
except ValueError as e:
    print("Errore validazione:", e)

print("\n--- 52. MINI PROGETTO: API RESILIENTE ---")
tentativi_falliti = 0

def chiamata_api_simulata():
    global tentativi_falliti
    tentativi_falliti += 1

    if tentativi_falliti < 3:
        raise ConnectionError("API temporaneamente non disponibile.")

    return {"ok": True, "data": "Risposta API"}

def chiama_con_retry(max_retry=3):
    for tentativo in range(1, max_retry + 1):
        try:
            print("Tentativo API:", tentativo)
            return chiamata_api_simulata()
        except ConnectionError as e:
            logging.warning("Tentativo fallito: %s", e)
            print("Errore:", e)

    return {"ok": False, "error": "API non disponibile dopo vari tentativi"}

print("Risposta finale:", chiama_con_retry())

print("\nFINE FILE GESTIONE ERRORI")
