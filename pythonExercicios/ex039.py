# Faça um programa que leia o ano de nascimento de um jovem e informe,
# de acordo com sua idade: - Se ele AINDA VAI SE ALISTAR ao serviço
# militar. - Se é a HORA DE SE ALISTAR. - Se já PASSOU DO TEMPO do
# alistamento. Seu programa também deverá mostrar o tempo que falta
# ou que passou do prazo.

from datetime import date

ano_nascimento = int(input('Informe o ano em que nasceu: '))
ano_atual = date.today().year
idade_candidato = ano_atual - ano_nascimento
print(f'Você está com {idade_candidato} anos de idade.')
if idade_candidato == 18:
    print(f'HORA DE SE ALISTAR ao servico militar!')
elif idade_candidato < 18:
    saldo = 18 - idade_candidato
    print(f'Ainda faltam {saldo} ano(s) para o alistamento.')
    print(f'Seu alistamento será em {ano_atual + saldo}.')
else:
    saldo = idade_candidato - 18
    print(f'Você já deveria ter se alistado há {saldo} anos.')
    print(f'Seu alistamento foi em {ano_atual - saldo}')
