# Lectura de fichero, búsqueda de palabra y localizar y sacar el número horas

fich = input('Por favor, inserte el nombre del fichero: ')
histo = dict()

try:
    fhand = open(fich)
except:
    print('No se ha podido encontrar el fichero %s' %nombre)
    exit()

for linea in fhand:
    if linea.startswith('From '):
        texto = linea.split()
        horminsec = texto[5]
        hora_lista = horminsec.split(':')
        hora = hora_lista[0]

        if hora not in histo:
            histo[hora] = 1
        else:
            histo[hora] = histo[hora] + 1
    else: continue

lista = list(histo.items())
lista.sort()

for key,val in lista:
    print(key,val)
