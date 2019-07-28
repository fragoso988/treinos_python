from datetime import date
import random

print("\nDesafio 36")
print("""\nEscreva um programa que solicita o valor da casa, o valor do Salário e em quanto anos será pago.
    O valor da parcela não pode passar de 30% do valor do salário.\n """)

valor_casa = float(input("Digite o valor da casa: "))
salario = float(input("Digite o valor do salário: "))
anos = int(input("Digite em quantos anos deseja pagar: "))

n_parcelas = anos * 12
valor_parcela = valor_casa/n_parcelas
base_salario = salario * .30

if(valor_parcela > base_salario):
    print("Empréstimo não autorizado!")
else:
    print("Empréstimo autorizado!\nO valor de cada parcela é de R${:.2f}, em {} vezes." .format(valor_parcela, n_parcelas))

print("*"*20)
print("*"*20)

print("\n\nDesafio 037")
print("Escreva um número e escolha sua base de conversão.")
n = int(input("Digite um número: "))

print("""Escolha a base de conversão:
1 - Binário
2 - Octal
3 - Hexadecimal\n""")

conv = int(input("Digite a opção desejada: "))

if(conv == 1):
    b = bin(n)
    print("O número {} em binário é {}." .format(n, b[2:]))
elif(conv == 2):
    o = oct(n)
    print("O número {} em octal é {}." .format(n, o[2:]))
elif(conv == 3):
    h = hex(n)
    print("O número {} em hexadecimal é {}" .format(n, h[2:]))
else:
    print("Opção não disponível.")

print("*"*20)
print("*"*20)

print("\nDesafio 038")
print("\nEscreva dois números e compare qual é maior")

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

if(n1 > n2):
    print("O primero número é maior!")
elif(n1 < n2):
    print("O segundo número é maior!")
else:
    print("Os número são iguais!")

print("*"*20)
print("*"*20)

print("\nDesafio 039")
print("Escreva um programa que leia o ano de nascimento e verifique se ele deve se alistar.")

ano = int(input("Digite o ano do seu nascimento: "))
ano_atual = date.today().year
idade = ano_atual - ano
print(ano_atual)
print(idade)
if(idade == 18):
    print("Você deve se alistar.")
elif(idade < 18):
    print("Você ainda não tem idade para se alistar.")
else:
    print("Você já passou da idade do alistamento.")

print("*"*20)
print("*"*20)

print("\nDesafio 040")
print("Escreva duas notas e tire a média.\n")

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
media = (n1+n2)/2

if(media >= 7):
    print("Média: {}. APROVADO!" .format(media))
elif(media >= 5 and media <= 6.9 ):
    print("Média: {}. RECUPERAÇÃO!" .format(media))
elif(media < 5):
    print("Média: {}. REPROVADO!" .format(media))
elif(media > 10):
    print("Média inválida.")

print("*"*20)
print("*"*20)

print("\nDesafio 041")
print("Escreva um programa que leia o ano de nascimento de um atleta e por sua idade defina sua categoria\n")

ano = int(input("Digite o ano de nascimento: "))
ano_atual=date.today().year
idade = ano_atual - ano

if( idade <= 9):
    print("Idade {}. Categoria Mirim" .format(idade))
elif(idade > 9 and idade <= 14):
    print("Idade {}. Categoria Infantil" .format(idade))
elif(idade > 14 and idade <= 19):
    print("Idade {}. Categoria Junior" .format(idade))
elif(idade == 20):
    print("Idade {}. Categoria Senior" .format(idade))
else:
    print("Idade {}. Categoria Master" .format(idade))

print("*"*20)
print("*"*20)

print("\nDesafio 042")    

print("*"*20)
print("*"*20)

print("\nDesafio 043")
print("Faça um programa que calcule o IMC")

altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso: "))
imc = peso/(altura ** 2)

if(imc < 18.5):
    print("Seu IMC é {:.1f}. Você esta abaixo do Peso". format(imc))
elif(imc >= 18.5 and imc < 25):
    print("Seu IMC é {:.1f}. Você esta no peso ideal". format(imc))
elif(imc >= 25 and imc < 30):
    print("Seu IMC é {:.1f}. Você esta com sobrepeso". format(imc))
elif(imc >= 30 and imc < 40):
    print("Seu IMC é {:.1f}. Você esta obeso". format(imc))
else:
    print("Seu IMC é {:.1f}. Você esta com obesidade mórbida". format(imc))

print("*"*20)
print("*"*20)

print("\nDesafio 044")
valor=float(input("Digite o valor do produto: "))
print("""\nDigite a forma de pagamento:
    1 - Dinheiro/Cheque a vista
    2 - Cartão a vista
    3 - Cartão em 2x
    4 - Cartão em 3x""")

pgto=int(input("\nQUal será a forma de pagamento: "))

if(pgto == 1):
    total = valor - (valor * .10)
    print("Você escolheu a forma de pagamento a vista.\n Então pagará R${:.2f}!" .format(total))
elif(pgto == 2):
    total = valor - (valor * .05)
    print("Você escolheu a forma de pagamento a vista no cartão.\nEntão pagará R${:.2f}" .format(total))
elif(pgto == 3):
    total = valor
    parc = total/2
    print("Você escolheu pagar em 2x.\nEntão pagará R${:.2f} em 2x de R${:.2f}." .format(total, parc))
elif(pgto == 4):
    total = valor + (valor * .20)
    parc = total/3
    print("Você escolheu pagar em 2x no cartão.\nEntão pagará R${:.2f} em 3x de R${:.2f}." .format(total, parc))
else:
    print("Forma de pagamento inválida") 