# O mesmo professor quer sortear a ordem de apresentação de trabalhos
# dos alunos. Faça um programa que leia o nome dos quatro alunos e
# mostre a ordem sorteada.

from random import shuffle

aluno1 = str(input('Digite o nome do primeiro aluno: '))
aluno2 = str(input('Digite o nome do segundo aluno: '))
aluno3 = str(input('Digite o nome do terceiro aluno: '))
aluno4 = str(input('Digite o nome do quarto aluno: '))
alunos_sorteados = [aluno1, aluno2, aluno3, aluno4]
shuffle(alunos_sorteados)
print(f'A ordem de apresentação será: {alunos_sorteados}')
