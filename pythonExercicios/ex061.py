# Refaça o desafio 51, lendo o primeiro termo e a razão
# de uma PA, mostrando os 10 primeiros termos da progressão
# usando a estrutura while.

primeiro_termo = int(input('Digite o primeiro termno: '))
razao = int(input('Digite a razão: '))
termo = primeiro_termo
cont = 1
while cont < 10:
    print(f'{primeiro_termo}', end=' -> ')
    termo += razao
    cont += 1
print('Fim.')

''' Minha solução
primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
decimo_termo = primeiro_termo + 10 * razao
while primeiro_termo != decimo_termo:
    print(f'{primeiro_termo}', end=' -> ')
    primeiro_termo = primeiro_termo + razao
print('Fim') '''
