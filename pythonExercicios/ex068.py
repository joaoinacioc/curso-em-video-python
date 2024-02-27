# Faça um programa que jogue par um ímpar com o computador
# O jogo só sera interrompido quando o jogador PERDER, mostrando
# o total de vitórias consecutivas que ele conquistou no final do
# jogo.

from random import randint

cont = 0
while True:
    jogador = int(input('Qual é a sua jogada? '))
    computador = randint(0, 10)
    resultado = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I]: ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador jogou: {computador}')
    print('Deu PAR' if resultado % 2 == 0 else 'Deu ÍMPAR')
    if tipo == 'P':
        if resultado % 2 == 0:
            cont += 1
            print('Você VENCEU!')
        else:
            break
    elif tipo == 'I':
        if resultado % 2 != 0:
            cont += 1
            print('Você VENCEU!')
        else:
            break
print(f'Você PERDEU!\nVocê obteve um total de {cont} vitórias consecutivas.')
