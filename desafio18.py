from math import sin, cos, tan, radians

angulo = float(input('Informe o ângulo: '))
seno = sin(radians(angulo))
coseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print(f'O ângulo de {angulo} tem o seno: {seno:.2f}\n'
      f'o ângulo de {angulo} tem o coseno: {coseno:.2f}\n'
      f'o ângulo de {angulo} tem a tangente: {tangente:.2f}')