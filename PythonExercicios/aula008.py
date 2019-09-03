import math
from random import choice, sample

print("Desafio 016")

n = float(input('Digite um número: '))

print('O número real é {}, a parte inteira é {}.' .format(n,math.trunc(n)))

print("\n\nDesafio 017")

ca = float(input('Digite o Cateto adjacente: '))
co = float(input('Digite o cateto oposto: '))

print('Se o cateto adjacente é {}, o cateto oposto é {}.\nO comprimento da hipotenusa é {:.2f}'.format(ca, co, math.hypot(ca,co)))

print("\n\nDesafio 018")

n = int(input("Digite o angulo: "))

print("Angulo: {}°".format(n))
print("Seno: {:.2f}".format(math.sin(math.radians(n))))
print("Conseno: {:.2f}".format(math.cos(math.radians(n))))
print("Tangente: {:.2f}".format(math.tan(math.radians(n))))

print("\n\nDesafio 019")

a1 = input("\nDigite o nome do 1º aluno: ")
a2 = input("Digite o nome do 2º aluno: ")
a3 = input("Digite o nome do 3º aluno: ")
a4 = input("Digite o nome do 4º aluno: ")    

lista = [a1,a2,a3,a4]

sorteio = choice(lista)

print("\nO aluno sorteado foi {}".format(sorteio))

print("\n\nDesafio 020")

a1 = input("\nDigite o nome do 1º aluno: ")
a2 = input("Digite o nome do 2º aluno: ")
a3 = input("Digite o nome do 3º aluno: ")
a4 = input("Digite o nome do 4º aluno: ")    

lista = [a1,a2,a3,a4]

sorteio = sample(lista, k=4)

print("A ordem de apresentação será {}\n\n".format(sorteio))