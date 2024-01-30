# Escreva um programa que pergunte o salário de um funcionário e calcule
# o valor do seu aumento. Para salários superiores a R$1250.00, calcule
# um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Digite o seu salário para saber qual será o seu novo salário: '))
if salario > 1250.0:
    aumento = salario * 0.10
else:
    aumento = salario * 0.15
print(f'O seu aumento foi de R${aumento:.2f} reais e o seu novo salário é de R${salario+aumento:.2f} reais.')
