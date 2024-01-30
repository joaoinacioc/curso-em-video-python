# Escreva um programa que leia a velocidade de um carro. Se ele
# ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7.00 por cada Km acima do limite.

velocidade = float(input('Qual foi a velocidade do carro? '))
if velocidade > 80.0:
    multa = (velocidade - 80.0)*7.0
    print(f'A velocidade está acima da permitida! Você foi multado em R${multa:.1f} reais.')
else:
    print('Você está dentro da velocidade permitida.')
