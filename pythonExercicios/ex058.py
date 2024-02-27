# Melhore o jogo do desafio 28 onde o computador vai
# pensar em um número entre 0 a 10. Só que agora o jogador
# vai tentar adivinhar até acertar, mostrando no final quantos
# palpites foram necessários para vencer.

from random import randint

computador = randint(0, 10)
jogador = 11
cont_palpite = 0
while jogador != computador:
    jogardor = int(input('Em qual número eu pensei? '))
    if jogardor != computador:
        print('Você errou. Tente novamente.')
        cont_palpite += 1
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        else:
            print('Menos... Tente mais uma vez.')
    else:
        jogador = computador
        print('Você adivinhou!')
print(f'Foram nescessários {cont_palpite} palpites até acertar.')

''' computador = randint(0, 10)
print('Sou seu computador... Acebei de pensar num número entre 0 e 10.')
print('Sera que você consegue adivinhar qual foi? ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogardor < computador:
            print('Mais... Tente mais uma vez.')
        else:
            print('Menos... Tente mais uma vez.')
print(f'Acertou com {palpites} tentativas. Parabéns!') '''
