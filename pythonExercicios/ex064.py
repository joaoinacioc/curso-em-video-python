# Crie um programa que leia vários números inteiros
# pelo teclado. O programa só vai parar quando o
# usuário digirar o valor 999, que é a condição de
# parada. No final, mostre quantos números foram
# digitados e qual foi a soma entre eles. (desconsiderar 999)

cont = 0
soma = 0
num = 0
print(f'{'ATENÇÃO':=^44}')
print('Ao digitar o número 999 você para o programa')
while num != 999:
    cont += 1
    num = int(input(f'Digite o {cont}º número: '))
    soma += num
print(f'Foram digitados {cont-1} números e a soma entres eles é de {soma-999}')
