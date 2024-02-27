# Elabore um programa que calcule o valor a ser pago por produto,
# considerando o seu PREÇO NORMAL e CONDIÇÃO DE PAGAMENTO:
# - À vista DINHEIRO / CHEQUE: 10% de desconto; - À vista no cartão:
# 5% de desconto; - Em até 2x no cartão: preço normal; - 3x ou mais no cartão:
# 20% de juros.

print(f'{' LOJAS TABAJARA ':=^40}')
produto = float(input('Informe o preço do produto: R$ '))
forma_pagamento = int(input('''Escolha a forma de pagamento:
1 - À vista dinheiro / cheque - desconto de 10%.
2 - À vista cartão - desconto de 5%.
3 - 2x no cartão - sem desconto.
4 - 3x ou mais no cartão - 20% de juros.
Opção: '''))
if forma_pagamento == 1:
    desconto = produto * 0.1
    print(f'A forma de pagamento escolhida foi à vista no dinheiro / cheque.\nSeu desconto foi de R${desconto:.2f}. '
          f'Preço final R${produto - desconto:.2f} reais.')
elif forma_pagamento == 2:
    desconto = produto * 0.05
    print(f'A forma de pagamento escolhida foi à vista no cartão.\nSeu desconto foi de R${desconto:.2f}. '
          f'Preço final do produto é de R${produto - desconto:.2f} reais.')
elif forma_pagamento == 3:
    print(f'A forma de pagamento de pagamento escolhida foi em 2x no cartão.\nPreço final é de R${produto:.2f} reais.')
elif forma_pagamento == 4:
    juros = produto * 0.2
    n_parcelas = int(input('Informe o número de parcelas desejada: '))
    print(f'A forma de pagamento escolhida foi 3x ou mais no cartão.\nSua compra será parcelada em {n_parcelas}x de '
          f'R${(produto + juros) / n_parcelas:.2f}\n'
          f'O total de juros é de R${juros:.2f} e o preço final do produto é de R${produto + juros:.2f} reais.')
else:
    print('Escolha uma forma de pagamento válida.')
