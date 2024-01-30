# Faça um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes aparece a letra "A".
# Em que posição ela aparece na primeira vez.
# Em que posição ela aparece a última vez.

frase = str(input('Digite um frase qualquer: ')).upper().strip()
print(f'A letra A apareceu {frase.count('A')} vezes.')
print(f'A primeira posição em que a letra A apareceu foi a: {frase.find('A')+1}ª')
print(f'A última posição em que a letra A apareceu foi a: {frase.rfind('A')+1}ª')
