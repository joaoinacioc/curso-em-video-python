# Crie um programa que leia um nome e o preço de vários
# produtos. O programa deverá perguntar se o usuário vai
# continuar. No final, mostre: A) qual é o total de gasto
# na compra b) quantos produtos custam mais de R$1000
# c) qual é o nome do produto mais barato.

total_gasto = produto_mais_mil = menor_preco = cont = 0
nome_produto_barato = ' '
while True:
    nome_produto = str(input('Informe o nome do produto: ')).strip()
    preco = float(input('Digite o preço do produto: '))
    cont += 1
    total_gasto += preco
    if preco > 1000:
        produto_mais_mil += 1
    if cont == 1 or preco < menor_preco:
        menor_preco = preco
        nome_produto_barato = nome_produto
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Quer continuar? [S/N]: '))[0].strip().upper()
    if opcao == 'N':
        break
print(f'O total da compra é de R${total_gasto:.2f} reais.\n{produto_mais_mil} custam mais de R$1000.00 reais.')
print(f'Sendo que o(a) {nome_produto_barato} é o produto mais barato custando R${menor_preco:.2f} reais.')
