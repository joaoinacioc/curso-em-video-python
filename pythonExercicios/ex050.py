# Desenvolva um progama que leia 6 numeros inteiros e mostre a soma
# apenas daqueles que forem pares. Se o valor digitado for impar,
# desconsidere-o.

soma = 0
cont = 0
for i in range(0, 6):
    num = int(input(f'Digite o {i}º valor: '))
    if num % 2 == 0:
        cont += 1
        soma += num
print(f'Você informou {cont} números pares e a soma deles é de: {soma}.')
