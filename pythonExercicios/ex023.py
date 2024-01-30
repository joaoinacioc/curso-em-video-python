# Faça um programa que leia um número de 0 a 9999 e mostre na tela
# cada um dos dígitos separados.

''' numero = str(input('Digite um número de 0 a 9999: '))
print(f'Analisando o número {numero}...')
print(f'Unidade: {numero[3]}')
print(f'Dezena: {numero[2]}')
print(f'Centena: {numero[1]}')
print(f'Milhar: {numero[0]}') '''

num = int(input('Digite um número de 0 a 9999: '))
unidade = num // 1 % 10
dezena = num // 10 % 10
centeza = num // 100 % 10
milhar = num // 1000 % 10
print(f'Analisando o número {num}...')
print(f'Unidade: {unidade}')
print(f'Dezena: {dezena}')
print(f'Centena: {centeza}')
print(f'Milhar: {milhar}')
