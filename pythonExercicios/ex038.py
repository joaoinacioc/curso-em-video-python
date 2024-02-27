# Escreva um programa que leia DOIS NÚMEROS inteiros e compare-se,
# mostrando na tela uma mensagem:
# - O PRIMEIRO VALOR é maior; - O SEGUNDO VALOR é maior; - NÃO EXISTE
# valor maior, os número são iguais.

print('Bem vindo(a) ao comparador de números!')
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
if n1 == n2:
    print('Os dois valores são iguais.')
elif n1 > n2:
    maior = n1
    print('O PRIMEIRO valor é maior.')
else:
    maior = n2
    print('O SEGUNDO valor é maior.')
