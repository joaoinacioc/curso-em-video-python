# Desafio 016: Crie um programa que leia um número real qualquer pelo
# teclado e mostre na tela a sua porção inteira

from math import trunc

num = float(input('Digite um número com três casas decimais: '))
print(f'O número digitado foi {num} e a sua porção inteira é: {trunc(num)}')
