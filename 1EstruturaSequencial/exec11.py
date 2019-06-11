#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre: 
#a.o produto do dobro do primeiro com metade do segundo . 
#b.a soma do triplo do primeiro com o terceiro. 
#c. o terceiro elevado ao cubo. 

import random

n1 = int(input("Digite o primeiro número inteiro: "))
n2 = int(input("Digite o segundo número inteiro: "))
nR = float(input("Digite o número real: "))

na = (n1 * 2) / n2

nb = (n1 * 3) + nR 

nc = nR * nR * nR

print("a.o produto do dobro do primeiro com metade do segundo: {}" .format(na))

print("b.a soma do triplo do primeiro com o terceiro: {} " .format(nb))

print("c. o terceiro elevado ao cubo: {} " .format(nc))

