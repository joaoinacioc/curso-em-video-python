# Crie um programa que leia o nome de uma cidade e diga
# se ela começa ou não com o nome "Santo"

cidade = str(input('Digite o nome da sua cidade: ')).strip()
primeiro_nome = cidade.split()
print(f'{'Santo' in primeiro_nome[0].title()}')

cid = str(input('Em que cidade você nasceu? ')).strip()
print(cid[:5].title() == 'Santo')
