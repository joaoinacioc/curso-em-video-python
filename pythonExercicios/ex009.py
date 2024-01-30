# Desafio 009: Faça um programa que leia um número inteiro
# qualquer e mostre na tela a sua tabuada.

numero = int(input('Digite um número para ver sua tabuada: '))

for i in range(10):
    i += 1
    print(f'{numero} x {i} = {numero*i}')
