# Categorización de mail según el día de la semana que se envió.

categ = dict()

try:
    fhand = open('mbox-short.txt')
except:
    print('El fichero mbox.txt no se encuentra')
    exit()

for line in fhand:
    if 'From ' in line:
        line = line.rstrip()
        lista = line.split()
        dia = lista[2]
        if dia in categ:
            categ[lista[2]] = categ[lista[2]] + 1
        else:
            categ[lista[2]] = 1

print(categ)
