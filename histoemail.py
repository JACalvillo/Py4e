# Histograma de número de mensajes que vienen de cada Email. Además,
# muestra cual es la dirección que más correos ha mandado.

histo = dict()
nombre = input('Inserte el nombre del listado de mensajes: ')
max = 0


try:
    fhand = open(nombre)
except:
    print('El fichero %s no se encuentra en el directorio' %nombre)
    exit()

for line in fhand:
    if not line.startswith('From '):
        continue
    else:
        linea = line.split()
        if linea[1] not in histo:
            histo[linea[1]] = 1
        else:
            histo[linea[1]] = histo[linea[1]] + 1

for clave in histo:
    if histo[clave] > max:
        max = histo[clave]
        pesado = clave

print(histo)
#print(pesado + str(histo[pesado]))
print(pesado + " " + str(histo[pesado]))
