# Crie um programa que leia o nome de um pessoa e diga se ela tem
# "Silva" em qualquer lugar do nome.

nome = str(input('Digite seu nome: ')).strip()
print(f'Seu nome tem Silva? {'silva' in nome.lower()}')
