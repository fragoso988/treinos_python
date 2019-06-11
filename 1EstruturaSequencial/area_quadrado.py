#Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário. 

import random

quadrado = float(input('Digite a altura e largura do quadrado: '))

area = quadrado * quadrado

dobro = area * 2

print("A área do quadrado é {} e seu dobro é {}" .format(area, dobro))
