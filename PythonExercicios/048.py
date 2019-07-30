("""D""esafio 048
Escreva um programa que some todos os números multiplos de 3 de 1 até 500 """)

n = 0
for c in range(1, 501, 2):
    if (c % 3) == 0:
        n += c
print("Valor da soma total é {}." .format(n))
