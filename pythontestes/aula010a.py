nome = str(input('Qual é o seu nome? ')).strip()
if nome == 'João':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão normal!')
print(f'Bom dia, {nome}!')

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1+nota2)/2
# print('Parabéns, você foi aprovado!' if media >= 6 else 'Reprovado. Estude mais!')
if media >= 6:
    print(f'A sua média foi {media}. Parabéns, você está aprovado!')
else:
    print(f'A sua média foi {media}. Você está reprovado.')
