# Crie um programa que faça o computador jogar Jokenpô com você.

from time import sleep
from random import randint

cores = {'branco': '\033[m', 'vermelho': '\033[31m', 'verde': '\033[32m', 'amarelo': '\033[33m',
         'azul': '\033[34m', 'roxo': '\033[35m'}
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print(f'{cores['amarelo']}COMPUTADOR: Vamos jogar Jokenpô!!!{cores['branco']}')
print(f'{cores['azul']}=-{cores['branco']}'*20)
print('''Suas opções:
0 - Pedra
1 - Papel
2 - Tesoura''')
jogador = int(input('Faça sua jogada: '))
print(f'{cores['azul']}-={cores['branco']}'*20)
print(f'{cores['roxo']}JOOO')
sleep(1)
print('KEEN')
sleep(1)
print(f'PÔÔÔ!!!{cores['branco']}')
print(f'{cores['azul']}-={cores['branco']}'*20)
print(f'{cores['amarelo']}Computador jogou {itens[computador]}{cores['branco']}')
print(f'{cores['azul']}Você jogou {itens[jogador]}{cores['branco']}')
print(f'{cores['azul']}-={cores['branco']}'*20)
if computador == 0:
    if jogador == 0:
        print(f'{cores['vermelho']}EMPATE!')
    elif jogador == 1:
        print(f'{cores['verde']}Você venceu!')
    elif jogador == 2:
        print(f'{cores['vermelho']}O computador venceu!')
    else:
        print(f'{cores['vermelho']}JOGADA INVÁLIDA!')
elif computador == 1:
    if jogador == 0:
        print(f'{cores['vermelho']}O computador venceu!')
    elif jogador == 1:
        print(f'{cores['vermelho']}EMPATE!')
    elif jogador == 2:
        print(f'{cores['verde']}Você venceu!')
    else:
        print(f'{cores['vermelho']}JOGADA INVÁLIDA!')
elif computador == 2:
    if jogador == 0:
        print(f'{cores['verde']}Você venceu!')
    elif jogador == 1:
        print(f'{cores['vermelho']}O computador venceu!')
    elif jogador == 2:
        print(f'{cores['vermelho']}EMPATE!')
    else:
        print(f'{cores['vermelho']}JOGADA INVÁLIDA!')
