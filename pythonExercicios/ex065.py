# Crie um programa que leia vários números inteiros pelo
# teclado. No final da execução, mostre a média entre todos
# os valores e qual foi o maior e o menor valor lido. O
# programa deve pergutar ao usuário se ele quer ou não
# continuar a digitar valores.

num = 0
cont = 0
soma = 0
maior = 0
menor = 0
opcao = 1

while opcao != 2:
    cont += 1
    num = int(input(f'Digite o {cont}º valor: '))
    soma += num
    if cont == 1:
        maior = menor = num
    if num > maior:
        maior = num
    else:
        menor = num
    opcao = int(input('Deseja continuar digitando os valores?\n[1] Sim\n[2] Não\nOpção: '))
print(f'A média entre os {cont} número informador é de {soma/cont}')
print(f'O maior valor lido foi {maior} e o menor valor lido foi {menor}')
