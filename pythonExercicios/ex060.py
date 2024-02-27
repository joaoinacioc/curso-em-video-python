# Faça um programa que leia um número qualquer e mostre
# o seu fatorial.

num = int(input('Digite um valor: '))
fatorial = num
while num != 1:
    print(f'{num}', end=' * ')
    num -= 1
    fatorial = fatorial * num
print('1')
print(f'\nO fatorial é {fatorial}')
