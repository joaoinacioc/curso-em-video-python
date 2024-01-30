# Desenvolva um programa que leia o comprimento de 3 retas e diga ao
# usuário se elas podem ou não formar um triângulo.

print('=-'*20)
print('Analisador de Triângulos!')
print('=-'*20)
lado1 = float(input('Digite o valor do primeiro lado: '))
lado2 = float(input('Digite o valor do segundo lado: '))
lado3 = float(input('Digite o valor do terceiro lado: '))
if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    print('É possível formar um triângulo!')
else:
    print('Não é possível formar um triâmgulo com estas medidas.')
'''if lado1 < lado2 + lado3:
    print('É possível formar um triângulo com estas medidas.')
elif lado2 < lado1 + lado3:
    print('É possível formar um triângulo com estas medidas.')
elif lado3 < lado1 + lado2:
    print('É possível formar um triângulo com estas medidas.')
else:
    print('Não é possível formar um triângulo com estas medidas.')'''
