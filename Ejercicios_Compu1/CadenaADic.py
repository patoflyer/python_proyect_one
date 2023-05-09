'''Escribir un programa que convierta la cadena en una 
lista de diccionarios con los campos correspondientes'''

directorio = "nif;nombre;email;teléfono;descuento\n01234567L;Luis González;luisgonzalez@mail.com;656343576;12.5\n71476342J;Macarena Ramírez;macarena@mail.com;692839321;8\n63823376M;Juan José Martínez;juanjo@mail.com;664888233;5.2\n98376547F;Carmen Sánchez;carmen@mail.com;667677855;15.7"

personas = []
valores = directorio.split('\n')[0].split(';')
for renglon in directorio.split('\n')[1:]:
    datos = renglon.split(';')
    persona = {}
    for i in range(len(valores)):
        persona[valores[i]] = datos[i]
    personas.append(persona)

print('DIRECTORIO')
repetir = True
while repetir == True:
    x = input('Ingresa el nif del cliente deseado para consultar sus datos: ')
    resultado = None
    for p in personas:
        if p['nif'] == x:
            resultado = p
    if resultado:
        print(resultado)
    else:
        print('El nif buscado no corresponde a ningun cliente registrado.')
    seguir = input('Para buscar otro cliente presiona enter o ingresa "X" para salir: ')
    if seguir == 'x' or seguir == 'X':
        repetir = False
        