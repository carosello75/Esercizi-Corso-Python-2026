from pathlib import Path


def media_da_file(file):
    try:
        with open(file, "r") as f:
            conteggi = []
            for riga in f:
                conteggi.append(int(riga))
            media = sum(conteggi) / len(conteggi)
            print(f"{Path(file).name} > La media e: {media}")
    except FileNotFoundError:
        print(f"{Path(file).name} > File assente")
    except ValueError:
        print(f"{Path(file).name} >Valore non numerico")
    except ZeroDivisionError:
        print(f"{Path(file).name} > Media non calcolabile")


for file in ["primo.txt", "secondo.txt", "terzo.txt", "no_file.txt"]:
    media_da_file(file)
