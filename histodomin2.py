# Lectura de fichero, búsqueda de palabra y localizar y sacar el número de direcciones

fich = input('Por favor, inserte el nombre del fichero: ')
histo = dict()

try:
    fhand = open(fich)
except:
    print('No se ha podido encontrar el fichero %s' %nombre)
    exit()

for linea in fhand:
    if not linea.startswith('From '): continue
    else:
        lista = linea.split()
        direcc = lista[1]

        if direcc not in histo:
            histo[direcc] = 1
        else:
            histo[direcc] = histo[direcc] + 1

# print(histo)

lista = list()

for key, value in list(histo.items()):
    lista.append((value,key))

lista.sort(reverse=True)

print(lista[0])
