# Escreva um programa para aprovar o empréstimo bancário para a compra
# de uma casa. O programa vai perguntar o VALOR DA CASA, o SALÁRIO do
# comprador e em QUANTOS ANOS ele vai pagar. Calcule o valor da prestaçao
# mensal, sabendo que ela não pode exceder 30% do salário ou então o
# empréstimo será negado.

cores = {'vermelho': '\033[31m', 'verde': '\033[32m', 'azul': '\033[34m', 'branco': '\033[m'}
print(f'{cores['azul']}Bem vindo ao simulador de Empréstimo Bancário!{cores['branco']}')
print('='*60)
valor_casa = float(input('Qual é o valor da casa? '))
salario = float(input('Qual é o salário? '))
anos = int(input('Em quantos anos quer pagar? '))
prestacao = valor_casa / (anos * 12)
minimo = salario * 30 / 100
if prestacao <= minimo:
    print(f'{cores['verde']}PARABÉNS{cores['branco']}, o empréstimo no valor '
          f'de R${valor_casa:.2f}{cores['verde']} reais foi aprovado!!!\n'
          f'O valor da prestação será de R${prestacao:.2f} reais por mês.')
else:
    print(f'{cores['vermelho']}Empréstimo negado!{cores['branco']}\n'
          f'O valor mínimo da prestação é de R${minimo:.2f} reais.\n'
          f'Este valor excede os 30% do seu salário em R${prestacao-minimo:.2f} reais.')
