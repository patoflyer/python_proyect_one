print('**********CALIFICACIONES**********')
students = 5
contador = 1
sumalg = 0
sumfis = 0
sumlab = 0
sumcompu = 0
sumcalc = 0
while contador <=students:
    nom = input('Nombre del estudiante: ')
    alg = int(input('Calificacion Algebra: '))
    fis = int(input('Calificacion Fisica: '))
    lab = int(input('Calificacion Lab: '))
    compu = int(input('Calificacion Compu: '))
    calc= int(input('Calificacion Calculo: '))
    sumalg = sumalg + alg
    sumfis = sumfis + fis
    sumlab = sumlab + lab
    sumcompu = sumcompu + compu
    sumcalc = sumcalc + calc
    contador = contador + 1
promalg = sumalg / students
promfis = sumfis / students
promlab = sumlab / students
promcompu = sumcompu / students
promcalc = sumcalc / students

print('*****CALIFICACION PROMEDIO******')
print('Algebra: ',promalg)
print('Fisica: ',promfis)
print('Laboratorio: ',promlab)
print('Computacion: ',promcompu)
print('Calculo: ',promcalc)
