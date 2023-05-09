'''Escribir una función que reciba una cadena y devuelva un diccionario con la cantidad de
apariciones de cada palabra en la cadena.'''

def contar_palabras(cadena):
    lista = cadena.split(' ')
    palabras = set(lista)
    palabrasRep = {}
    totalPalabras = {}
    for i in palabras:
        repeticiones = lista.count(i)
        palabrasRep[str(i)]=repeticiones
    for k in palabrasRep:
        a = palabrasRep[k]
        if palabrasRep[k]!= 0:
            examinar = k.lower()
            for palabra in palabras:
                b = palabrasRep[palabra]
                if examinar == palabra.lower():
                    palabrasRep[k] = a + b
                    palabrasRep[palabra]= 0
    for n in palabrasRep:
        if palabrasRep[n]!= 0:
            totalPalabras[str(n)] = palabrasRep[n]
    return totalPalabras

repetir = True
print('BIENVENIDO')
print('Este programa cuenta las veces que se repite cada palabra en una frase')
while repetir == True:
    x = input('Ingresa frase de prueba (sin signos de puntuacion): ')
    print('La repeticion de palabras obtenida fue: ')
    print(contar_palabras(x))
    seguir = input('Presiona enter para ingresar otra frase o ingresa "X" para salir: ')
    if seguir == 'x' or seguir == 'X':
        repetir = False