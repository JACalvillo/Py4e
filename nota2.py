# Programa de notas por funciones

def computegrade(score):
    try:
      nota = float(score)

      if nota < 0 or nota > 1:
        print('Por favor, inserte un valor mayor que 0 y menor que 1\n')
      else:
        if nota < 0.6:
          grade = 'F'
        elif nota < 0.7:
          grade = 'D'
        elif nota < 0.8:
          grade = 'C'
        elif nota < 0.9:
          grade = 'B'
        else:
          grade = 'A'

        print('Tu nota es un ' + grade + '\n')

    except:
      print('Por favor inserte un valor numérico')

nota = input('Por favor, introduzca su puntuación\n')
computegrade(nota)
