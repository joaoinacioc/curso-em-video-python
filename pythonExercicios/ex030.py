# Crie um programa que um número inteiro e mostre na tela se ele é
# PAR ou ÍMPAR.

numero = int(input('Digite um valor para verificar se é par ou ímpar: '))
if numero % 2 == 0:
    print(f'O número {numero} é par!')
else:
    print(f'O número {numero} é ímpar!')
