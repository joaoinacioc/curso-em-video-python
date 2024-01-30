# Faça um programa que leia o comprimento do cateto oposto e do cateto
# adjacente da um triângulo retângulo, calcule e mostre o comprimento da
# hipotenusa

from math import hypot

cat_op = float(input('Digite um valor para o cateto oposto: '))
cat_adj = float(input('Digite um valor para o cateto adjacente: '))
hipotenusa = hypot(cat_op, cat_adj)
print(f'O comprimento da hipotenusa deste triângulo retângulo é: {hipotenusa:.2f}.')
