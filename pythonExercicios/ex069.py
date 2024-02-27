# Crie um programa que leia a idade e o sexo de várias
# pessoas. A cada pessoa cadastrada, o programa deverá
# perguntar se o usuário quer continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos. B) quantos homens
# foram cadastrados. C) quantas mulheres tem menos de 20 anos.

cont_mais18 = 0
cont_homens = 0
cont_mulheres = 0
while True:
    idade = int(input('Quantos anos você tem? '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Qual é o seu sexo? [M/F]: '))[0].strip().upper()
    if idade >= 18:
        cont_mais18 += 1
    if sexo == 'F' and idade < 20:
        cont_mulheres += 1
    elif sexo == 'M':
        cont_homens += 1
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Quer continar? [S/N]: '))[0].strip().upper()
    if opcao == 'N':
        break
print(f'Foi cadastrado {cont_mais18} pessoas maiores de 18 anos, sendo {cont_homens} homens e {cont_mulheres}'
      f' mulheres que possuem de 20 anos.')
