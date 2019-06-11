#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês. 

import random

valor = float(input("O valor da hora trabalhada: "))
horas = float(input("AS horas trabalhadas: "))

salario = valor * horas

print("Seu salário será de R${}" .format(salario))