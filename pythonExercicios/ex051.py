# Desenvolva um programa que leia o primeiro termo e a razao de uma PA
# No final, mostre os 10 primeiros termos dessa progressão.

print('='*50)
print(f'{'10 TERMOS DE UMA PA':^40}')
print('='*50)
primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo_termo = primeiro_termo + (10 - 1) * razao
for i in range(primeiro_termo, decimo_termo + razao, razao):
    print(f'{i}', end=' -> ')
print('FIM')
