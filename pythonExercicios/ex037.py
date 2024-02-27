# Escreva um programa que leia um número inteiro qualquer e peça para
# o usuário escolher qual será a BASE DE CONVERSÃO.
# - 1 para binário; 2 - para octal; 3 - para hexadecimal.

n = int(input('Digite um número para fazer a conversão: '))
opcao = int(input('Para qual base você deseja converter?\n1 - binário\n2 - octal\n3 - hexadecimal\nOpção: '))
if opcao == 1:
    print(f'A conversão de {n} para BINÁRIO resulta em: {bin(n)[2:]}')
elif opcao == 2:
    print(f'A conversão de {n} para OCTAL resulta em: {oct(n)[2:]}')
elif opcao == 3:
    print(f'A conversão de {n} para HEXADECIMAL resulta em: {hex(n)[2:]}')
else:
    print('Opção inválida. Tente novamente.')
