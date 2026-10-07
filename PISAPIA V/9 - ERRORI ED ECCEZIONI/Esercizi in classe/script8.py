from pathlib import Path


def media_da_file(file):
    try:
        with open(file, "r") as f:
            conteggi = []
            for riga in f:
                conteggi.append(int(riga))
            media = sum(conteggi) / len(conteggi)
            print(f"{Path(file).name} > La media e: {media}")
    except Exception as e:
        print(f"Errore: {e}")


for file in ["primo.txt", "secondo.txt", "terzo.txt", "no_file.txt"]:
    media_da_file(file)
