frase = '   Curso em Vídeo Python  '
print(frase[::2])

print(frase.upper().count('O'))

print(len(frase))

frase = frase.strip()
print(frase)
print(len(frase))

frase = frase.replace('Python','Android')
print(frase)

print(frase.find('Vídeo'))
print(frase.find('video'))
print(frase.lower().find('vídeo'))

dividido = frase.split()
print(dividido[2])
print(dividido[2][3])


'''print("""Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
Varius vel pharetra vel turpis nunc eget. Lectus proin nibh nisl condimentum id venenatis a condimentum vitae.
Maecenas volutpat blandit aliquam etiam. Lorem donec massa sapien faucibus. Odio tempor orci dapibus ultrices in iaculis nunc sed.
Cursus sit amet dictum sit amet. Morbi tristique senectus et netus et.""")'''
