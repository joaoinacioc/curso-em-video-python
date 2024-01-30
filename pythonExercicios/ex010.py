# Desafio 010: Crie um programa que leia quanto dinheiro
# uma pessoa tem na carteira e mostre quantos dólares ela
# pode comprar.

reais = float(input('Digite a quantia em reais que você possui: R$'))
dolar = 3.27
dolar2024 = 4.98
print(f'Você pode comprar ${reais/dolar:.2f} dólares com a quantia disponível.')
print(f'Você pode comprar ${reais/dolar2024:.2f} dólares com a quantia disponível.')
