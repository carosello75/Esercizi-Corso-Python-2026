numeri = [1, 2, 4, 5, 6]

for numero in numeri[:]:
    if numero % 2 == 0:
        numeri.remove(numero)

print(numeri)
