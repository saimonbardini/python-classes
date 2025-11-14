#Faça um programa que leia o comprimento do cateto oposto e cateto adjacente de um retângulo retângulo, calcule e mostre o comprimento da hipotenusa.
from math import hypot
co = float(input('Informe o cateto oposto: '))
ca = float(input('Informe o cateto adjacente: '))

hi = hypot(co, ca)

print(f'A hipotenusa é: {hi:.2f}')

