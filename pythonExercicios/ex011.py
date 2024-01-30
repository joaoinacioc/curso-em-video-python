# Desafio 011: Faça um programa que leia a largura e a
# altura de uma parede em metros, calcule a quantidade
# de tinta necessária para pintá-la, sabendo que cada
# litro de tinta pinta uma área de 2 m quadrados.

largura = float(input('Digite a largura da parede em metros: '))
altura = float(input('Digite a altura da parede em metros: '))
print(f'Sua parede tem a dimensão de {largura}x{altura} e sua área é de {largura*altura}m².\n'
      f'Para pintar essa parede, você precisará de {(largura*altura)/2}l de tinta')
