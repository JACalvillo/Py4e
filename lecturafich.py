# Lectura de ficheros

nombre = input('Introduce el nombre del fichero: ')

try:
    fhand = open(nombre)
except:
    print("El fichero no existe")
    exit()

for line in fhand:
    line = line.upper().rstrip()
    print(line)
