# Refaça o EX035 dos triângulos, acrescentando o recurso de mostrar
# que tipo de triângulo será formado: - EQUILÁTERO: todos os lados
# iguais; - ISÓSCELES: dois lados iguais; - ESCALENO: todos os lados
# diferentes.

a = float(input('Informe a medida do segmento A: '))
b = float(input('Informe a medida do segmento B: '))
c = float(input('Informe a medida do segmento C: '))
if a < b + c and b < a + c and c < a + b:
    print('Com estes segmentos é possível formar um triângulo e ele é do tipo:')
    if a == b == c:
        print('EQUILÁTERO')
    elif a != b != c != a:
        print('ESCALENO')
    else:
        print('ISÓCELES')
else:
    print('Não é possível formar um triângulo.')
