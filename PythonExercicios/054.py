print("Desafio 054")
#Escreva um programa que leia o ano de nascimento de 7 pessoas e separe os maiores e os menores de idade.

from datetime import date

i1 = int(input("Digite o ano de nascimento da 1ª pessoa: "))
i2 = int(input("Digite o ano de nascimento da 2ª pessoa: "))
i3 = int(input("Digite o ano de nascimento da 3ª pessoa: "))
i4 = int(input("Digite o ano de nascimento da 4ª pessoa: "))
i5 = int(input("Digite o ano de nascimento da 5ª pessoa: "))
i6 = int(input("Digite o ano de nascimento da 6ª pessoa: "))
i7 = int(input("Digite o ano de nascimento da 7ª pessoa: "))

idades =[i1,i2,i3,i4,i5,i6,i7]

ano_atual = date.today().year
maior = 0
menor = 0

for i in idades:
    dif_idade = ano_atual - i
    if(dif_idade >= 18):
        maior = maior + 1
    else:
        menor = menor + 1

print("Temos um grupo com {} pessoas de maior." .format(maior))
print("E temos um grupo com {} pessoas de menor." .format(menor))
