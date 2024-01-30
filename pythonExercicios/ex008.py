# Desafio 008: Escreva um programa que leia um valor em
# metros e o exiba convertido em centimetros e milimetros.

medida = float(input('Digite o número de metros para ser convertido em centímetros e milímetros: '))
print(f'A medida de {medida:.2f} metro(s) convertida em\n'
      f'centímetros é: {medida*100:.0f}cm\n'
      f'milímetros é: {medida*1000:.0f}mm')
