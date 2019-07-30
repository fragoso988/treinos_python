print("""Desafio 051
Escreva um programa que leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão""")

t= int(input("\nDigite o 1º termo: "))
r= int(input("Digite a razão: "))

print(t, end=" -> ")
for c in range(0,9):
    t += r
    print(t, end = ' -> ')
