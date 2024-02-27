# Faça um programa que leia um número inteiro e diga se ele é
# ou não um número primo.

print(f'{'Verificador de Primos':=^40}')
num = int(input('Digite um valor: '))
total = 0
for i in range(1, num + 1):
    if num % i == 0:
        total += 1
        print('\033[33m', end='')
    else:
        print('\033[31m', end='')
    print(f'{i}\033[m', end=' ')
print(f'\nO número {num} foi divisível {total} vezes.')
if total == 2:
    print('E por isto ele é PRIMO')
else:
    print('E por isso ele NÃO é PRIMO')
