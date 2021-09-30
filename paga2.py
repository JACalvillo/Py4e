# Cálculo de paga con horas extras, IF-ELSE Statements

horas = input('¿Cuántas horas has trabajado este mes?\n')
ratio = input('¿A cuanto te pagan las horas que has trabajado?\n')

try:
  horas = float(horas)
  ratio = float(ratio)

  if horas > 40:
    horas_ext = horas - 40
    paga = (horas-horas_ext) * ratio + 1.5 * horas_ext * ratio

  else:
    paga = horas * ratio

  print('La paga que le corresponde es de ' + str(paga) + '€')

except:
  print('Por favor inserte valores numéricos')
