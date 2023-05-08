contraseña = "misterio"
while True:
    clave = input("Introduce la contraseña: ")
    if clave == contraseña:
        print("Contraseña correcta")
        break
    else:
        print("Contraseña incorrecta, Inténtalo de nuevo")
