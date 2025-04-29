def eliminarNegativos(lista):
    listaCopia = lista[:]
    for num in listaCopia:
        if num < 0:
            lista.remove(num)
    return lista

print(eliminarNegativos([-3, -2, -1, 0, 1, 2]))