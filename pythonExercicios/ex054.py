# Crie um programa que leia o ano de nascimento de 7 pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade
# e quantas já são maiores.

from datetime import date

ano_atual = date.today().year
menor_idade = 0
maioridade = 0
for i in range(1, 8):
    ano_nasc = int(input(f'Informe o ano de nascimento da {i}ª pessoa: '))
    if ano_atual - ano_nasc < 18:
        menor_idade += 1
    else:
        maioridade += 1
print(f'{menor_idade} pessoas ainda não atingiram a maioridade.')
print(f'{maioridade} pessoas já são maiores.')
