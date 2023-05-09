def tup(mylist):
    mydict = {}
    for i in mylist:
        if i[0] in mydict:
            mydict[i[0]] = mydict[i[0]],i[1]
        else:
            mydict[i[0]] =  i[1]
    return mydict
mylist = [ ('Nola', 'don Pepito'), ('Nola', 'don Jose'),('Buenos', 'días') ]
print(tup(mylist))
tup(mylist)