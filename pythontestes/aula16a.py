lanche = ('Hambuerger', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
print(lanche[-3:])

for comida in lanche:
    print(f'Eu vou comer {comida}')

for cont in range(0, len(lanche)):
    print(lanche[cont])

for posicao, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {posicao}')

print(sorted(lanche))

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
print(c)
print(len(c))
print(c.count(5))
print(c.index(5, 1))


pessoa = ('João', 26, 'M', 117.5)
print(pessoa)
del pessoa
