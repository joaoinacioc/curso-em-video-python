# Desafio 015: Escreva um programa que pergunte a quantidade de Km
# percorridos por um carro alugado e a quantidade de dias pelo quais
# ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa
# R$60 por dia e R$0,15 por Km rodado.

dias_alugados = int(input('Digite quantos dias o carro ficou alugado: '))
km_rodados = float(input('Digite quantos km foram rodados: '))
total_pagar = dias_alugados*60 + km_rodados*0.15
print(f'O total a pagar é de R${total_pagar} reais.')
