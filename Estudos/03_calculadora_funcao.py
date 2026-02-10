def soma (a,b):
   return a+b
def subtracao (a,b):
   return a-b
def multiplicacao (a,b):
   return a*b
def divisao(a, b):
    if b == 0:
        return "Erro: divisão por zero"
    return a / b

a = int(input("Digite o primeiro numero: "))
b = int(input("Digite o segundo numero numero:"))

print("1 - Somar")
print("2 - Subtrair")
print("3 - Multiplicar")
print("4 - Dividir")
opcao = input("Escolha uma opção: ")

if opcao == "1":
    print(soma(a, b))
elif opcao == "2":
        print(subtracao(a, b))
elif opcao == "3":
        print(multiplicacao(a, b))
elif opcao == "4":
        print(divisao(a, b))
else:
        print("Opção inválida")