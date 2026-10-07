with open("output.txt", "w") as f:
    f.write("Valerio")
    f.write("Mario")
    scritti = f.write("Verdi\n")
    accentata = f.write("perchè\n")

with open("output.txt", "r") as f:
    print(f.read(), end="")

colli = 100
with open("output.txt", "w") as f:
    f.write(colli)
