def sumar(numeros):
    if numeros == "":
        return 0
    numeros = numeros.replace("\n", ",")
    partes = numeros.split(",")
    return sum(int(parte) for parte in partes)