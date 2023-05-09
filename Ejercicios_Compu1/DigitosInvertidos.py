'''Escribir un programa que almacene en una lista los números del 1 al 10 
y los muestre por pantalla en orden inverso separados por comas.'''

lista = list(range(1,11))
listaInvertida = sorted(lista, reverse=True)
print('BIENVENIDO')
print('Los primeros 10 numeros naturales son: ' + str(lista))
print('Ordenados de forma descendente son: ' + str(listaInvertida))