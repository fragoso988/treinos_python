#Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Farenheit. 

c = float(input("Digite a temperatura Celsius: "))

f =  ((c/5) * 9) + 32

print("{} Celsius equivale a {}° Farenheit " .format(c, f))