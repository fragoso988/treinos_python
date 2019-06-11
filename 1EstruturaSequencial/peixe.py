
kg = float(input("Digite o kg de peixe pescado: "))

if( kg <= 50):
	print("Você pescou {}kg, esta dentro do permitido." .format(kg))
else:
	excesso = kg - 50
	multa = excesso * 4.00
	print("Você pescou {}kg.\nO excesso é de {}kg e a multa será de R${}." .format(kg, excesso, multa))

