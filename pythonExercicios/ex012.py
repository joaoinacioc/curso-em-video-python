# Desafio 012: Faça um algoritmo que leia o preço de um
# produto e mostre seu novo preço, com 5% de desconto.

preco_produto = float(input('Digite o preço do produto: '))
print(f'O desconto foi de R${preco_produto*0.05:.2f} reais e o preço do produto '
      f'com desconto de 5% é de: R${preco_produto-(preco_produto*0.05):.2f} reais')
