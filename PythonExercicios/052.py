("""Desafio 052
Escreva um número e verifique se ele é um número primo""")

n = int(input("Digite um valor: "))

cont = 0

for c in range(2, n+1):
    if(n % c) == 0:
        cont += 1
if (cont == 2): 
    print("O valor {} é PRIMO" .format(n))
else:
    print("O valor {} NÃO é PRIMO" .format(n))