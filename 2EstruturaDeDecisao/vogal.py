#Faça um Programa que verifique se uma letra digitada é vogal ou consoante. 

letra = input("Digite uma letra: ")

if(letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u'):
    print("A letra digitada é uma Vogal.")
else:
    print("A letra digitada é uma Consoante.")