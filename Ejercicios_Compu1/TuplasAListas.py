'''Escribir un programa que convierta listas de tuplas en listas tomando la entrada que se muestra
a continuación:'''
test_list = [(7, 8), (5, 6), (7, 5), (10, 4), (10, 1)]

def convertir_A_Listas(lista_tuplas):
    lista_listas= []
    for tupla in lista_tuplas:
        lista = []
        for x in tupla:
            lista.append(x)
        lista_listas.append(lista)
    return lista_listas

print('BIENVENIDO')
print('Este programa convierte listas de tuplas a listas de listas. Ejemplo:')
print('Si se ingresa: ' + str(test_list))
print('Se obtendrá como resultado: ' + str(convertir_A_Listas(test_list)))
miLista = []
NTuplas = int(input('¿Cuantas tuplas tendra la lista? '))
for i in range(NTuplas):
    listaE = []
    NElementos = int(input('¿Cuantos elementos tendra la tupla ' +str(i+1)+ '? '))
    print('TUPLA ' + str(i+1))
    for j in range(NElementos):
        Ingresa = str(input('Ingresa elemento y da enter: '))  
        listaE.append(Ingresa)
    tuplaCreada= tuple(listaE)
    miLista.append(tuplaCreada)
print('La lista de tuplas es: ' + str(miLista))
print('La lista de listas es: '+ str(convertir_A_Listas(miLista)))