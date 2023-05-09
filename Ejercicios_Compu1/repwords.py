dict = {}
oracion = input("Escriba una oracion: ")
wordlist = oracion.split(" ")
for i in wordlist:
    if i in dict:
        dict[i]+=1
    else: 
        dict[i]=1
for length,value in dict.items():
    a = (length,":",value)
    print(a)