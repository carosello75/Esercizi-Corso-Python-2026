# writelines()

ZONE = ["NORD", "CENTRO", "SUD"]

with open("zone.txt", "w") as f:
    f.writelines(ZONE)

with open("zone.txt", "r") as f:
    print(f"writelines grezzo: {f.read()}")

print("><" * 50)

# A
righe = []

for zona in ZONE:
    righe.append(zona + "\n")

with open("zone.txt", "w") as f:
    f.writelines(righe)

with open("zone.txt", "r") as f:
    print(f"Soluzione A:\n{f.read()}")

print("><" * 50)

# B
with open("zone.txt", "w") as f:
    f.write("\n".join(ZONE))

with open("zone.txt", "r") as f:
    print(f"Soluzione B:\n{f.read()}")
