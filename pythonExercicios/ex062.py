# Melhore o desafio 61, preguntando para o usuário se
# ele quer mostrar mais alguns termos. O programa encerra
# quando ele disser que quer mostrar 0 termos.

primeiro = int(input('Digite o primeiro termno: '))
razao = int(input('Digite a razão: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(f'{primeiro}', end=' -> ')
        termo += razao
        cont += 1
    print('Pausa')
    mais = int(input('Quantos termos a mais deseja mostrar? '))
print('Fim.')
