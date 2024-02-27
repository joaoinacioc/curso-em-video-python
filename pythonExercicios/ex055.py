# Faça um programa que leia o peso de 5 pessoas. No final, mostre
# qual foi o maior e o menor peso lidos.

maior_peso = 0
menor_peso = 0
for i in range(1, 6):
    peso = float(input(f'Informe o peso da {i}ª pessoa: '))
    if i == 1:
        maior_peso = peso
        menor_peso = peso
    else:
        if peso > maior_peso:
            maior_peso = peso
        if peso < menor_peso:
            menor_peso = peso
print(f'O maior peso lido foi {maior_peso:.2f}Kg.')
print(f'E o menor peso lido foi {menor_peso:.2f}Kg.')
