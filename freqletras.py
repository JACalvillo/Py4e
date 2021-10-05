# Frecuencia de numero de letras en un fichero

import string

fich = input('Inserte el nombre del fichero: ')

try:
    fhand = open(fich)
except:
    print('No se ha podido abrir, sorry')
    exit()

histo = dict()

for linea in fhand:
    linea = linea.lower().strip()
    linea = linea.translate(linea.maketrans('','',string.punctuation))
    words = linea.split()
    for word in words:
        for letter in word:
            if letter not in histo:
                histo[letter] = 1
            else:
                histo[letter] = histo[letter] + 1

lista = list()

for key,val in list(histo.items()):
    lista.append((val,key))

lista.sort(reverse=True)

for val,key in lista:
    print(key,val)
