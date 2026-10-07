ZONE = ["NORD", "CENTRO", "SUD"]

with open("zone.txt", "a") as f:
    f.write(f"\nISOLE")

with open("zone.txt", "r") as f:
    print(f.read(), end="")
