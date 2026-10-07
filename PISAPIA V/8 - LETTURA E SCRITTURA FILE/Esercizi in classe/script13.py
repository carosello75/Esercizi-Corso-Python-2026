from pathlib import Path

CARTELLA_OUTPUT = Path("output")
FILE = CARTELLA_OUTPUT / "files"

FILE.mkdir(parents=True, exist_ok=True)
print("Esiste la cartella output? ", CARTELLA_OUTPUT.is_dir())

destinazione = FILE / "file.txt"

with open(destinazione, "w") as f:
    f.write("test test test ")
