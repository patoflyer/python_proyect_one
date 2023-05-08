directorio="nif;nombre;email;teléfono;descuento\n01234567L;Luis González;luisgonzalez@mail.com;656343576;12.5\n71476342J;Macarena Ramírez;macarena@mail.com;692839321;8\n63823376M;Juan José Martínez;juanjo@mail.com;664888233;5.2\n98376547F;Carmen Sánchez;carmen@mail.com;667677855;15.7"

clientes = []
campos = directorio.split("\n")[0].split(";")
for linea in directorio.split("\n")[1:]:
    valores = linea.split(";")
    if len(valores) == len(campos):
        cliente = {}
        for i in range(len(campos)):
            cliente[campos[i]] = valores[i]
        clientes.append(cliente)

nif_buscado = input("Introduzca el NIF del cliente a buscar: ")

cliente_encontrado = None
for cliente in clientes:
    if cliente["nif"] == nif_buscado:
        cliente_encontrado = cliente
        break
    
if cliente_encontrado:
    print(f'Información del cliente con NIF {nif_buscado}:')
    print(f'Nombre: {cliente_encontrado["nombre"]}')
    print(f'Email: {cliente_encontrado["email"]}')
    print(f'Teléfono: {cliente_encontrado["teléfono"]}')
    print(f'Descuento: {cliente_encontrado["descuento"]}')
else:
    print(f'No se encontró ningún cliente con NIF {nif_buscado}')
