'''Escribir un programa en el que se pregunte al usuario por una frase y una letra, 
y muestre por pantalla el numero de veces que aparece la letra en la frase.'''

print('BIENVENIDO')
print('Este programa cuenta cuantas veces aparece un determinado caracter en una frase')
repetir = True
while repetir == True: 
    frase= input('Ingrea frase: ')
    letra = input('Ingresa la letra: ')
    contador = 0

    for i in frase:
        if i == letra:
            contador+=1
        else:
            pass
    
    print('La letra aparece ' + str(contador) + ' veces en la frase')
    resp = input('Presiona enter para ingresar otra frase o ingresa "X" para salir: ')
    if resp == 'x' or resp == 'X':
        repetir = False