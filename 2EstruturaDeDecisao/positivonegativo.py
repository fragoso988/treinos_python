#Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo. 

n = int(input("Digite um número: "))

if(n > 0):
    print("O valor é positivo")
elif(n < 0):
    print("O valor é negativo")
else:
    print("O valor é zero")