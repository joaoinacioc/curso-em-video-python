# Crie um programa que simule o funcionamento de um caixa
# eletronico. No inicio, pergunte ao usuario qual será o
# valor a ser sacado (numero int) e o programa vai informar
# quantas cedulas de cada valor seão entregues. OBS: Considere
# que o caixa pussui cedulas de R$50, R$20, R$10 e R$1.

valor = int(input('Qual valor você quer sacar? R$'))
total = valor
cedula = 50
total_cedula = 0
while True:
    if total >= cedula:
        total -= cedula
        total_cedula += 1
    else:
        if total_cedula > 0:
            print(f'Total de {total_cedula} cédulas de R${cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        total_cedula = 0
        if total == 0:
            break
