# Faça um programa que mostre a tabuada de vários números
# um de cada vez, para cada valor digitado pelo usuário. O
# programa será interompido quando o número solicitado for
# negativo.

num = cont = 1
while True:
    num = int(input('Digite um número para ver sua tabuada: '))
    cont = 1
    if num < 0:
        break
    print('-='*20)
    while cont <= 10:
        print(f'{num} x {cont} = {num*cont}')
        cont += 1
    print('=-'*20)
print('Fim')
