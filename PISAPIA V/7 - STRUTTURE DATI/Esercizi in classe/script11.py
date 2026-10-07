conteggi = {"VERDE": 3, "GIALLO": 5, "ROSSO": 4, "BIANCO": 10}

totale = sum(conteggi.values())

for colore, quanti in conteggi.items():
    quota = quanti / totale

    print(f"{colore:<7} {quanti} {quota:>8.1%} {'#' * quanti}")
