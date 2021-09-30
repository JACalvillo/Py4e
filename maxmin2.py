# Lectura de números por terminal hasta que escriba done y máx y min

t = list()

while True:
    num = input("Introduzca un número o done para finalizar: ")

    if num == "done":
        print('Done! Realizando cálculos...\n')
        break
    else:
        try:
            t.append(float(num))

        except:
            print('Por favor inserte un valor numérico o done: ')
            continue

maximo = max(t)
minimo = min(t)

print('El máximo es %d' %maximo)
print('El mínimo es %d' %minimo)
