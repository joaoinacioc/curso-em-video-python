# Faça um programa que leia um ângulo qualquer e mostre na tela o
# valor do seno, cosseno e tangente desse ângulo.
from math import sin, cos, tan, radians

angulo = float(input('Digite um ângulo: '))
print(f'O valor do seno para este ângulo é: {sin(radians(angulo)):.2f},\n'
      f'o valor do cosseno é: {cos(radians(angulo)):.2f}\n'
      f'e o valor da tangente é de: {tan(radians(angulo)):.2f}.')
