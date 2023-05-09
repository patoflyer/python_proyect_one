def match(tup1,tup2):	
    if tup1[0]==tup2[0] or tup1[0]==tup2[1]:
        return "Si coincide!"
    elif tup1[1]==tup2[0] or tup1[1]==tup2[1]:
        return "Si coincide!"
    else:
        return "No coincide"
ficha1a=input("Numero de la ficha 1 lado A: ")
ficha1b=input("Numero de la ficha 1 lado B: ")
ficha2a=input("Numero de la ficha 2 lado A: ")
ficha2b=input("Numero de la ficha 2 lado B: ")

print(match((ficha1a,ficha1b),(ficha2a,ficha2b)))
