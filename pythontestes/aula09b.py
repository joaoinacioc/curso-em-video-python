# FATIAMENTO

frase = 'Curso em Video Python'
print(frase[9])

# Imprimir de um index até o outro
print(frase[9:14])
print(frase[9:21])

# Mostrando de 2 em 2 index
print(frase[9:21:2])

# Começa do início e vai até o index indicado
print(frase[:5])

# Indicando onde começa e percorre até o final da string
print(frase[15:])

# O 9 indica o index onde começa a percorrer a string, o segundo número, que fica após o primero :,
# está vazio indicando que irá percorrer até o final da string, e o 3 é o terceiro digito indicando
# que deve mostrar de 3 em 3.
print(frase[9::3])


# ANÁLISE

len(frase)

# Conta quantos caracteres
frase.count('o')

# Contagem já com fatiamento, dizendo o seguinte: do index 0 até o index 13,
# eu possuo a contagem de 1 caracter letra 'o'
frase.count('o', 0, 13)

# Diz quantas vezes encontrou 'deo' dizendo em qual index começa e qual index termina
frase.find('deo')

# Irá retornar o valor -1, dizendo que a string 'Android' não foi encontrada
frase.find('Android')

# Retorna True ou False se existir a frase 'Curso'
'Curso' in frase


# TRANSFORMAÇÃO

# Reposiciona o primeiro conjunto de caracteres indicado pelo segundo conjunto de caracteres
print(frase.replace('Python','Android'))

# Transformar todos os caracteres em maiusculas
frase.upper()

# Transforma todos os caracteres em minusculas
frase.lower()

# Transforma todos os caracteres em minusculas e SOMENTE o primeiro caracter em maiuscula
frase.capitalize()

# Transforma todos os caracteres em minusculas e em maiusculas a primeira letra de cada palavra
# separada por espaço
frase.title()

frase2 = '   Aprenda Python  '

# Remove todos os espaços em branco do início e do fim da string
frase2.strip()

# Remove os espaços em branco SOMENTE do final (direita) da string
frase2.rstrip()

# Remove os espaços em branco SOMENTE do começo (esquerda) da string
frase2.lstrip()


# DIVISÃO

# Divide a frase (string total) em strings menores (palavra), que por padrão
# é separada por espaço
frase.split()

# Junta as palavras (strings) em uma única frase (string total) usando o split '-'
'-'.join(frase)
