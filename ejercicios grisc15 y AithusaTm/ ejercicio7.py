precios = {'Plátano': 1.35, 'Manzana': 0.80, 'Pera': 0.85, 'Naranja': 0.70}

producto = input('Introduzca el nombre del producto: ')
kilos = float(input('Introduzca la cantidad en kilos: '))

if producto in precios:
    precio_kilo = precios[producto]
    precio_total = precio_kilo * kilos
    print('El precio de', kilos, 'kilos de', producto, 'es', precio_total, 'pesos.')
else:
    print('Lo siento, el producto', producto, 'no está en nuestra lista de precios.')