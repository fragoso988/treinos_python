print("""Desafio 050
Escreve um programa que leia seis números e some apenas os números pares""" )

n = 0

for c in range(1, 7):
    valor = int(input("Digite o {}º valor: " .format(c)))
    if (valor %2) == 0:
        n += valor
print("A soma total dos valores pares é {}" .format(n))
