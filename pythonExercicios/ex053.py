# Crie um programa que leia um frase qualquer e diga se ela é
# um palindromo, desconsiderando os espaços. EX: APOS A SOPA

frase = str(input('Digite uma frase qualquer: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
# inverso = junto[::-1] Elimina a necessidade do for
inverso = ''
for i in range(len(junto) - 1, -1, -1):
    inverso += junto[i]
print(f'O inverso de {junto} é {inverso}')
if inverso == junto:
    print('Temos um PALÍMDROMO.')
else:
    print('A frase digitada não é um palíndromo.')
