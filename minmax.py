# Lectura de números por terminal hasta que escriba done y máx y min

total = 0
avg = 0
count = 0
max = None
min = None

while True:
    num = input("Introduzca un número o done para finalizar\n")

    if num == "done":
        print('Done! Realizando cálculos...\n')
        break
    else:
        try:
            num = float(num)

            if max is None or max < num:
                max = num
            if min is None or min > num:
                min = num

            total = total + num
            count = count + 1
            print('Leido número ' + str(num))
        except:
            print('Por favor inserte un valor numérico o done\n')
            continue

avg = total/count

print("Se han introducido un total de " + str(count) + " números")
print("La suma total es de " + str(total))
print("La media es de " + str(avg))
print("El mínimo es " + str(min) + " y el máximo es " + str(max))
