# Lectura de números por terminal hasta que escriba done

total = 0
avg = 0
count = 0

while True:
    num = input("Introduzca un número o done para finalizar\n")

    if num == "done":
        print('Done! Realizando cálculos...\n')
        break
    else:
        try:
            num = float(num)
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
