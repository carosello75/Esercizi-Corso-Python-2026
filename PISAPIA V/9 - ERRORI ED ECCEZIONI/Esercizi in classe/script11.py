file = open("ordini.txt", "r")

try:
    for riga in file:
        print(riga)
except FileNotFoundError:
    print("Lettura interrotta - file chiuso?", file.closed)
finally:
    file.close()

print("Il file è chiuso? ", file.closed)
