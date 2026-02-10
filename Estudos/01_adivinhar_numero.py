import random
numero = random.randint(1,100)
contador=0
chute = int(input("adivinhe o número de 1 a 100"))
while chute != numero:
    if chute == numero:
        print("você acertou o número")
    elif chute < numero:
        print("o chute é menor que o número")
    else:
         print("o chute é maior que o número")
    chute = int(input("adivinhe o número de 1 a 100"))
    contador=contador+1
    
print(f"Você acertou! Número: {numero}")
print(f"Tentativas: {contador}") 


 