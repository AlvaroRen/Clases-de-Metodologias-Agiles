def sumar(numeros):
    if numeros == "":
        return 0
    partes = numeros.split(",")
    return sum(int(parte) for parte in partes)