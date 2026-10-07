def posizione_zero(zone, cercato):
    """
    Posizione dell'elemento, oppure dammi -1 se non esiste
    :param elenco:
    :param cercato:
    :return:
    """
    if cercato in zone:
        return zone.index(cercato)

    return -1


zone = ["N", "S", "C"]

posizione1 = posizione_zero(zone, "S")
posizione2 = posizione_zero(zone, "I")

print(posizione1)
print(posizione2)
