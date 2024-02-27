inicio = int(input('Digite o início: '))
fim =  int(input('Digite o fim: '))
passo = int(input('Digite o passo: '))
for i in range(inicio, fim+1, passo):
    print(i)
print('Fim!')

s = 0
for i in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n
print(f'A soma de todos os número é de :{s}')
