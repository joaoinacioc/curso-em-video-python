# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0.50 por cada Km para viagens
# de até 200Km e R$0.45 para viagens mais longas.

distancia = float(input('Informe a distância da viagem em Km para calcular o preço da passagem: '))
if distancia <= 200.0:
    passagem = distancia * 0.50
    print(f'O preço da passagem será de: R${passagem} reais.')
else:
    passagem = distancia * 0.45
    print(f'O preço da passagem será de: R${passagem} reais.')
