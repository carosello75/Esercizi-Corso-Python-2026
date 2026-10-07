NOME_FILE = "test_aula.txt"

with open(NOME_FILE, "x", encoding="utf-8") as f:
    f.write("Aggiornamento report di Aula\n")

with open(NOME_FILE, "x", encoding="utf-8") as f:
    f.write("Report di Aula\n")
