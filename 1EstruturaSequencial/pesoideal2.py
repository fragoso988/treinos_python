#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas: 

sexo = int(input("Digite seu sexo (1)Homem - (2)Mulher: "))

altura = float(input("Digite sua altura: "))

if(sexo == 1):
	peso = (72.7 * altura) - 58
	print("Se você é do sexo masculino, tem {} de altura. Seu peso ideal é {}" .format(altura, peso))
elif(sexo == 2):
	peso = (62.1 * altura) - 44.7
	print("Se você é do sexo feminino, tem {} de altura. Seu peso ideal é {}" .format(altura, peso))
else:
	print("Valor do sexo inválido")


