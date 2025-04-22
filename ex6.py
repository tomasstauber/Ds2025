def quitar_pares(lista):
    listaCopia = lista[:]
    for num in listaCopia:
        if num % 2 == 0:
            lista.remove(num)
    return lista

print(quitar_pares([1, 2, 4, 5, 6, 7, 8, 9, 10])) #Al no hacer una copia de la lista, mientras el for recorre los elementos de la primera, ocurre que cuando encuentra un numero par y lo borra, los indices internos se mueven de lugar lo que casusa que ciertos elementos como el 4 sean salteados porque el for ya dio otra vuelta.