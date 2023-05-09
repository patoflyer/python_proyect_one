Nombres = ('Hidrogeno', 'Helio', 'Litio', 'Berilio', 'Boro', 'Carbono', 'Nitrogeno', 'Oxigeno', 'Fluor', 'Neon', 'Sodio', 'Manganeso')
Simbolos =  ('H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na', 'Be')
Numeros_Atomicos = list(range(1,13))
Pesos_Atomicos = (1.0079, 4.0026, 6.941, 9.0122, 10.811, 12.0107, 14.0067, 15.9994, 18.9984, 20.1797, 22.9897, 24.305)
Elementos = []

for i in range(len(Nombres)):
    elemento = {}
    elemento["Nombre"] = Nombres[i]
    elemento["Simbolo"] = Simbolos[i]
    elemento["Numero_Atomico"] = Numeros_Atomicos[i]
    elemento["Peso_Atomico"] = str(Pesos_Atomicos[i]) + 'g/mol'
    Elementos.append(elemento)

print('TABLA PERIODICA')
print('BIENVENIDO. Este programa contiene unicamente los primeros 12 elementos de la tabla periodica.')
repetir = True
while repetir == True:
    x = input('Ingresa el numero atomico del elemento que quieras consultar: ')
    try:
        print(Elementos[int(x)-1])
        s = input('Presiona enter para consultar otro elemento o ingresa "X" para salir del programa: ')
        if s == 'x' or s == 'X':
            repetir = False
    except:
        print("ERROR. Debes ingresar un numero entero entre 1 y 12")