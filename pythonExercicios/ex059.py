# Crie um programa que leia dois valores e mostre
# um menu na tela: [1] somar; [2] multiplicar; [3] maior;
# [4] novos números; [5] sair do programa. Seu programa
# deverá realizar a operação solicitada em cada caso.

valor1 = int(input('Digite o 1º valor: '))
valor2 = int(input('Digite o 2º valor: '))
opcao = 0
while opcao != 5:
    print(f'O que deseja fazer?')
    print('[1] Somar\n[2] Multiplicar\n[3] Mostrar maior\n[4] Informar novos números\n[5] Sair')
    opcao = int(input('Opção: '))
    if opcao == 1:
        print(f'A soma dos valores é de {valor1 + valor2}')
    elif opcao == 2:
        print(f'O produto dos valores é de {valor1*valor2}')
    elif opcao == 3:
        if valor1 > valor2:
            print(f'O PRIMEIRO valor é maior.')
        else:
            print(f'O SEGUNDO valor é menor.')
    elif opcao == 4:
        valor1 = int(input('Digite um novo valor para o 1º número: '))
        valor2 = int(input('Digite um novo valor para o 2º número:'))
print('Saindo...')
