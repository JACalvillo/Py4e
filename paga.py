# Cálculo de paga con pregunta por terminal

horas = input('¿Cuantas horas has trabajado este mes?\n')
horas = float(horas)

rate = input('A cuánto te pagan las horas?\n')
rate = float(rate)

payment = rate * horas;
print('Tu paga este mes asciende a ' + str(payment) + ' €\n')
