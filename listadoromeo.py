# Hacer listado de palabras que aparecen en un texto

texto = input('Introduzca el nombre del texto: ')

try:
    fhand = open(texto)
except:
    print('No existe el fichero introducido')
    exit()

t=list()

for linea in fhand:
    frase = linea.rstrip().split()
    for palabra in frase:
        if palabra not in t: t.append(palabra)

t.sort()
print(t)
