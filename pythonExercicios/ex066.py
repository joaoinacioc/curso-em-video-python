# Crie um programa que leia vários números inteiros pelo
# teclado. O programa só vai parar quando o usuário digita
# o valor 999, que é a condição de parada. No final mostre
# quantos números foram digitados e qual foi a soma entre
# eles desconsiderando o flag.

num = soma = cont = 0
while num != 999:
    num = int(input('Digite um número (999 para o programa): '))
    if num == 999:
        break
    soma += num
    cont += 1
print(f'A soma dos {cont} números digitados é de {soma}')
