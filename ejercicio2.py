def encajan(ficha1, ficha2):

    if ficha1[0] == ficha2[0] or ficha1[1] == ficha2[1]:
        return True
    elif ficha1[0] == ficha2[1] or ficha1[1] == ficha2[0]:
        return True
    else:
        return False


ficha1 = tuple(map(int, input("Ingrese la primera ficha de dominó separada por una coma: ").split(",")))
ficha2 = tuple(map(int, input("Ingrese la segunda ficha de dominó separada por una coma: ").split(",")))

if encajan(ficha1, ficha2):
    print("Las fichas encajan")
else:
    print("Las fichas no encajan")
