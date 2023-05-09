'''Escribir una función que reciba una cantidad de iteraciones de una tirada de 2 dados a realizar 
y devuelva la cantidad de veces que se observa cada valor de la suma de los dos dados. 
Nota: utilizar el módulo random para obtener tiradas aleatorias.'''

import random
def dados(numero):
    tiradas = []
    for x in range(numero):
        suma = random.randrange(1,6) + random.randrange(1,6)
        tiradas.append(suma)
    resultados = set(tiradas)
    totalRest= {}
    for i in resultados:
        repeticiones = tiradas.count(i)
        totalRest['Suma obtenida = '+str(i)]=repeticiones
    print('Resultados obtenidos: ' + str(tiradas))
    print('Numero de repeticiones por valor obtenido: ' + str(totalRest))
    
print('BIENVENIDO')
print('Este programa genera tiradas de dos dados aleatoriamente y te dice cuantas veces se repite cada resultado')
repetir = True
while repetir == True:
    try:
        x = int(input('¿Cuantas veces quieres lanzar los dados? '))
        dados(x)
        seguir = input('Para lanzar los dados de nuevo presiona enter o ingresa "X" para salir: ')
        if seguir == 'x' or seguir == 'X':
            repetir = False
    except: print('ERROR. Dedes ingresar un numero entero')

