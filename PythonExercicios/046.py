from time import sleep
print("Desafio 046")
print("Escreva um script que faça a contagem regressiva de um estouro de fogos de artificio com intervalo de 1 seg.")

print("\nINICIANDO CONTAGEM!")

for c in range(10, 0, -1):
    print("\n{}!" .format(c))
    sleep (1)

print("\nESTOURO DE FOGOS REALIZADO COM SUCESSO!!")
