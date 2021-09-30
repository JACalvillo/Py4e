# Lectura de ficheros y búsqueda

nombre = input('Introduce el nombre del fichero: ')

try:
    fhand = open(nombre)
except:
    print("El fichero no existe")
    exit()

count = 0
total = 0

for line in fhand:
    if line.startswith('X-DSPAM-Confidence:'):
        line = line.rstrip()
        pos = line.find(':')
        data = float(line[pos+2:])
        count = count + 1
        total = total + data


print('La cuenta es de %d y el total es %f' % (count, total))
avg = float(total/count)
print('Average spam confidence: %f' % (avg))
