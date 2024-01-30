# Desafio 014: Escreva um programa que converta uma temperatura
# digitada em ºC e a converta para ºF.

celsius = float(input('Digite a temperatura em graus ºC para converte-la para graus ºF: '))
print(f'A temperatura de {celsius:.1f}ºC equivale a {(celsius*9/5)+32:.1f}ºF.')
