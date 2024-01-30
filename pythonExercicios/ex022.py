# Crie um programa que leia o nome completo de uma pessoa:
# O nome com todas as letras maiúsculas
# O nome com todas as letras minúsculas
# Quantas letras ao todo (sem considerar espaços)
# quantas letras tem o primeiro nome

nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print(f'Em maiúsculas: {nome.upper()}')
print(f'Em minúsculas: {nome.lower()}')
print(f'Seu nome possui {len(nome) - nome.count(' ')} letras ao todo.')
print(f'Seu primeiro nome possui {nome.find(' ')} letras.')
nome_separado = nome.split()
print(f'Seu primeiro nome possio {len(nome_separado[0])} letras.')
