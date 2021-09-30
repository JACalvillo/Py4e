# Cálculo de la paga mensual a través de función

def paga(horas, ratio):
    try:
        horas = float(horas)
        ratio = float(ratio)
        horas_ext = horas - 40

        nomina = horas_ext * 1.5 * ratio + (horas - horas_ext)*ratio
        print(nomina)
    except:
        print("Por favor, incluya valores numéricos")

horas = input("Introduzca el numero de horas trabajadas\n")
ratio = input('Introduzca el ratio de €/horas\n')

paga(horas, ratio)
     
