'''for i in range(1, 10):
    print(i)

r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N]: ')).upper()
print('FIM')'''

num = 1
impar = 0
par = 0
while num != 0:
    num = int(input('Informe um valor: '))
    if num != 0:
        if num % 2 == 0:
            par += 1
        else:
            impar += 1
print(f'Foi contado {impar} números ímpares.')
print(f'Foi contado {par} números pares.')
