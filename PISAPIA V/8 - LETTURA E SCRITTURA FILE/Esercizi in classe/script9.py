SPEDIZIONI = [("LS-2026-MI-0042", "NORD", 12.5),
              ("LS-2026-NA-0913", "SUD", 6.7),
              ("LS-2026-CA-1806", "ISOLE", 36.4)]

with open("report_colli.txt", "w") as f:
    f.write(f"{'CODICE':<18}{'ZONA':<8}{'KG':<8}\n")

    for codice, zona, peso in SPEDIZIONI:
        f.write(f"{codice:<18}{zona:<8}{peso:<8}\n")

with open("report_colli.txt", "r") as f:
    print(f.read(), end="")

print("*" * 50)

with open("scontrino.txt", "w") as f:
    print("Scontrino Cassa", file=f)
    print("Numero articoli: 3", file=f)
    print("Totale", 300.14, "€", sep=" | ", file=f)
    print("Grazie", end="!\n", file=f)

with open("scontrino.txt", "r") as f:
    print(f.read(), end="")
