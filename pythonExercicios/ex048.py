# Faça um programa que calcule a soma de todos os números ímpares
# e que são multiplos de 3 e que se encontram no intervalo de 1 até 500

s = 0
cont = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        cont += 1
        s += i
print(f'A soma de todos os {cont} valores é {s}')
