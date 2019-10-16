print("""Exercício Python 066: Crie um programa que leia números inteiros pelo teclado. 
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. 
No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).""")
cont = 0
valor = 0
while True:
    n = int(input("Digite um valor (999 para parar): "))
    if n == 999:
        break
    cont = cont + 1
    valor = valor + n
print(f"Você digitou {cont} valores e a soma de todos eles é {valor}.")

