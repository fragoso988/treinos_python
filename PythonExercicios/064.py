print("Desafio 64 - Tratadno vários valores\n")

n = 0
n1 = 0
cont = 0
while n1 != 999:
    n1 = int(input("Digite um número [999] para parar: "))
    n = n + n1
    if n1 != 999:
        cont = cont + 1
print("\nVocê digitou {} números e a soma deles é {}." .format(cont, n))