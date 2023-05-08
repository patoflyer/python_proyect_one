import random

def tirar_dados(iteraciones):
    resultados = [0] * 11 
    for i in range(iteraciones):
        dado1 = random.randint(1, 6) 
        dado2 = random.randint(1, 6) 
        suma = dado1 + dado2 
        resultados[suma-2] += 1 
    return resultados

resultados = tirar_dados(10000)
for i, resultado in enumerate(resultados):
    print(f"Se obtuvo {resultado} veces la suma {i+2}")
