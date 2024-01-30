# Desafio 013: Faça um algoritmo que leia o salário de um
# funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Digite o valor do salário: R$'))
print(f'O salário com aumento de 15% agora é R${salario+(salario*0.15):.2f} reais.')
