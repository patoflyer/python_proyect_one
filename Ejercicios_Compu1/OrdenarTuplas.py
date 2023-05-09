'''Dada una lista de tuplas ordenar de menor a mayor en 
base al total de digitos que aparezcan en cada tupla'''
def digTupla(tupla):
    convertirStr = []
    for x in tupla:
        convertirStr.append(str(x))
    num = 0
    for elemento in convertirStr:
        num=num + len(elemento)
    return num

def ordenar(listaTuplas):
    listaTuplas.sort(key=digTupla)
    return listaTuplas
        
print('BIENVENIDO')
print('Este programa te permite ordenar una lista de tuplas en base a su numero de digitos o caracteres')
listaEjemplo = [("Parangaricutirimicuaro", 215, "Abril"), ("Gato", "Hola", 22), ("Uva", 3), ("Fismat", 5)]
print('EJEMPLO: Si se ingresa la tupla: ' + str(listaEjemplo))
print('Se obtendra: ' + str(ordenar(listaEjemplo)))

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
print('La lista original es: ' + str(miLista))
print('La lista ordenada es: '+ str(ordenar(miLista)))