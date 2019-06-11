#Faça um Programa que leia três números e mostre o maior deles. 

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))

lista = (n1, n2, n3)

maior = max(lista)

print(f'O maior número da lista é {maior}')