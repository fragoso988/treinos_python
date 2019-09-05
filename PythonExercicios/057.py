print("""Faça um programa que digite o sexo como M ou F
caso seja digitado errado, solicitar novamente a digitação.""")

S = str(input("\nDigite o sexo: ")).strip().upper()[0]

while S not in 'mMfF':
   S = str(input("Sexo inválido, digite novamente: ")).strip().upper()[0]

   
