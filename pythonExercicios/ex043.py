# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule
# seu IMC e mostre seu status, de acordo com a tabela abaixo:
# - Abaixo de 18.5: Abaixo do peso; - Entre 18.5 e 25.5: Peso ideal;
# - 25 até 30: Sobrepeso; - 30 até 40: Obesidade; - Acima de 40: Obesidade
# mórbida.

peso = float(input('Informe seu peso (Kg): '))
altura = float(input('Informe sua altura (m): '))
imc = peso / altura**2
print(f'Seu IMC é de {imc:.2f}')
if imc < 18.5:
    print('Você está abaixo do peso.')
elif imc < 25:
    print('Você está no peso ideal.')
elif imc < 30:
    print('Você está sobrepeso.')
elif imc < 40:
    print('Você está obeso(a).')
else:
    print('Você está em obesidade mórbida.')
