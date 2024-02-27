# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre: a média de idade do grupo; qual é o
# nome do homem mais velho; quantas mulheres tem menos de 20 anos.

media_idade = 0
idade_homem_mais_velho = 0
homem_mais_velho = ''
cont_mulheres = 0
for i in range(1, 5):
    nome = str(input(f'Qual é o nome da {i}ª pessoa? ')).strip().title()
    idade = int(input(f'Qual é a idade da {i}ª pessoa? '))
    sexo = int(input(f'''Qual é o sexo da {i}ª pessoa?
[1] - Masculino
[2] - Feminino
Opção: '''))
    media_idade += idade
    if sexo == 1 and idade > idade_homem_mais_velho:
        idade_homem_mais_velho = idade
        homem_mais_velho = nome
    elif sexo == 2 and idade < 20:
        cont_mulheres += 1
print(f'A média de idade do grupo é de {media_idade/4} anos.')
print(f'O  homem mais velho se chama {homem_mais_velho} e tem {idade_homem_mais_velho}.')
print(f'Existe {cont_mulheres} mulheres com menos de 20 anos.')
