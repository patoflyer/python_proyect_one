'''Escribir una función empaquetar para una lista, donde epaquetar significa indicar la repetición
de valores consecutivos mediante una tupla (valor, cantidad de repeticiones).'''

def empaquetar(lista):  
    empaquetado = []
    x = 0
    while x < len(lista):
        i = x + 1
        while i < len(lista) and lista[i] == lista[x]:
            i += 1
        empaquetado.append((lista[x], i - x))
        x = i
    return empaquetado

print('BIENVENIDO')
print('Este progra te dice el numero de repeticiones de un valor consecutivo en una lista de numeros enteros.')
repetir = True
while repetir == True:
    try: 
        cadena = input('Ingresa una lista de numeros enteros separados por coma: ')
        mi_lista = [int(num) for num in cadena.split(',')]
        print('Repeticiones consecutivas: ' + str(empaquetar(mi_lista)))
        seguir = input('Presiona enter para ingresar otra lista o ingresa "X" para salir: ')
        if seguir == 'x' or seguir == 'X':
            repetir = False
    except:
        print('ERROR. Debes ingresar una lista de enteros.')