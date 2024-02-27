# Refaça o desafio 009, mostrando a tabuada de um numero que o usuario
# escolher, so que agora utilizando um laço for.

num = int(input('Digite o número da tabuada que deseja ver: '))
for i in range(1, 11):
    print(f'{num} x {i} = {num * i}')
