import random
from datetime import date

print("Desafio 028")
print("""\nEscreva um programa que faça o computador pensar em um número inteiro entre 0 e 5.
Peça para o usuário descobrir qual o número.\n""")

sorteio = random.randint(0,5)

n = int(input("Digite um número de 0 a 5: "))

if(n == sorteio):
    print("Parabéns, você acertou!")
else:
    print("Você errou, você escolheu o número {} e o número certo era {}." .format(n, sorteio))


print("\nDesafio 029")
print("""Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80Km/h mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada km acima do limite.\n""")

velocidade = float(input("Digite a velocidade: "))

if (velocidade > 80):
    print("Você ultrapassou o limite de 80Km/h, dirigindo a {}." .format(velocidade))
    multa = (velocidade - 80) * 7.00
    print("Você deverá pagar uma multa de R${:.2f}." .format(multa))
else:
    print("Você passou dentro do limite de velocidade.")

print("\nDesafio 030")
print("""Cria um programa que leia um número inteiro e mostre na tela se ele é par ou impar""")

n = int(input("Digite um número: "))

if ((n % 2)==0):
    print("O número é par.")
else:
    print("O número é impar.")

print("\nDesafio 031")
print("""Desenvolva um programa que pergunte a distancia de uma viagem em KM.
Para viagens até 200Km, cobre a passagem por R$0.50 o Km.
Acima de 200Km cobre R$0.45""")

km = float(input("Quantos Km será a viagem: "))

if (km <= 200):
    valor = km * 0.50
    print("O valor da viagem será de R${:.2f}" .format(valor))
else:
    valor = km * 0.45
    print("O valor da viagem será de R${:.2f}." .format(valor))

print("""\nDesafio 032
Faça um programa que leia um ano qualquer e mostre se ele é bissexto""")

ano = int(input('\nQue ano quer analisar? Coloque 0 para o ano atual. '))
if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print("O ano {} é BISSEXTO" .format(ano))
else:
    print("O ano {} NÃO é BISSEXTO" .format(ano))

print("""\nDesafio 033
Faça um programa que leia 3 números e mostre qual é o maior e qual o menor.""")

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))

lista = (n1, n2, n3)

maior = max(lista)
menor = min(lista)

print("O maior número é {} e o menor número é {}." .format(maior, menor))

print("""\nDesafio 034
Escreva um programa que aumente o salário de um funcionário em 10% caso os salário seja acima de R$1250,00.
Caso seja maior ou igual, o aumento deve ser de 15%\n""")

salario = float(input("Digite o salário: "))

if (salario > 1250):
    aumento = (salario * 0.10) + salario 
    porcentagem = 10
else:
    aumento = (salario * .15) + salario
    porcentagem = 15
print("Seu salário é de R${}, então terá um aumento de {}%. Passando agora a ser R${:.2f}". format(salario, porcentagem, aumento))

print("\nDesafio 35")
print("Analizador de triangulo")
r1 = float(input("Digite o primeiro segmento: "))
r2 = float(input("Digite o segundo segmento: "))
r3 = float(input("Digite o terceiro segmento: "))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Os segmentos podem formar triangulo!")
else:
    print("Os segmentos não podem formar triangulo.")


