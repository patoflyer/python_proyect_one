'''Escribir una función que indique si dos fichas de dominó encajan o no. Las fichas son recibidas
en dos tuplas, por ejemplo: (3,4) y (5,4).'''

def domino(tup1,tup2):
    encajan = False
    for i in tup1:
        if encajan == True:
            break
        for j in tup2:
            if i == j: 
                encajan = True
    return encajan

print('BIENVENIDO')
print('Este programa te dice si dos fichas de domino encajan.')
repetir = True
while repetir:
    try:
        ficha1= tuple(int(n) for n in input('Ingresa los valores de la ficha 1 separados por coma. Ej: 0,1: ').split(','))
        ficha2= tuple(int(n) for n in input('Ingresa los valores de la ficha 2 separados por coma. Ej: 3,4: ').split(','))
        if domino(ficha1,ficha2):
            print('LAS PIEZAS ENCAJAN')
        else:
            print('Las piezas no encajan')
        resp = input('Presiona enter para comparar mas fichas o ingresa "X" para salir: ')
        if resp == 'x' or resp == 'X':
            repetir = False
    except:
        print('ERROR. Revisa tu entrada')
