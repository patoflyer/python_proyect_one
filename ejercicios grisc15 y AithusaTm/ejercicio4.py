def empaquetar(lista):
    
    emp = []
    i = 0
    while i < len(lista):
        j = i + 1
        while j < len(lista) and lista[j] == lista[i]:
            j += 1
        emp.append((lista[i], j - i))
        i = j
    return emp


# Solicitar al usuario que ingrese una lista de números separados por comas
numeros = input("Ingrese una lista de números separados por comas: ")

# Convertir la cadena de entrada en una lista de números
lista = [int(n) for n in numeros.split(",")]

# Aplicar la función empaquetar a la lista de entrada
empaquetado = empaquetar(lista)

# Imprimir el resultado
print(empaquetado)
