# Escreva um programa que faça o computador "pensar" em um número
# entre 0 a 5 e peça para o usuário tentar descobrir qual foi o número
# escolhido pelo computador. O programa deverá escrever na tela se o
# usuário venceu ou perdeu.

from random import randint
from time import sleep

print('='*60)
print('Estou pensando em um número de 0 a 5. Tente adivinhar...')
print('='*60)
pensado = randint(0, 5)
numero = int(input('Digite aqui o número que estou pensado: '))
print('Processando...')
sleep(2)
if 0 < numero > 5:
    print('Número digitado invádo. Por favor, digite algo entre 0 e 5.')
elif numero == pensado:
    print('Você adivinhou! Parabéns!')
else:
    print(f'Você errou! O número em que eu pensei foi o {pensado}.\nTente novamente.')
