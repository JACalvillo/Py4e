# Lectura de email y búsqueda de remitentes

texto = input('Por favor, introduzca el nombre del texto: ')

try:
    fhand = open(texto)

except:
    print('El texto introducido no existe o no se encuentra')
    exit()

cuenta = 0

for linea in fhand:
    linea = linea.rstrip()
    if not linea.startswith('From '): continue
    t = linea.split()
    print(t[1])
    cuenta = cuenta + 1

print('Habia %d lineas que empezaban por From' % cuenta)
