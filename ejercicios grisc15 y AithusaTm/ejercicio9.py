def lista_a_diccionario(lista_tuplas):

    diccionario = {}
    for tupla in lista_tuplas:
        if tupla[0] in diccionario:
            diccionario[tupla[0]].append(tupla[1])
        else:
            diccionario[tupla[0]] = [tupla[1]]
    return diccionario

lista_tuplas = [("a", 1), ("b", 2), ("c", 3), ("a", 4), ("b", 5), ("c", 6)]
diccionario = lista_a_diccionario(lista_tuplas)
print(diccionario)
