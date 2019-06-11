#Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius. 

f = float(input("Digite a temperatura Farenheit: "))

c = (5 * (f - 32) / 9)

print("{} Farenheit equivale a {}° Celsius" .format(f, c))