opcao=0
print("Bem vindo")
print("\tprima 1 para nome cliente")
print("\tprima 2 para Iban")
opcao = int(input("Insira a opção: "))

match opcao:
    case 1:
        print("Nome")
    case 2:
        print("Iban")
    case default:
        print("Falhou opcao")

# entre 3 numeros saber maior, meio e menor
num1 = 4
num2 = 8
num3 = 3
max = max(num1, num2, num3)

if num1 == max:
    print("Número 1 é o maior, ", end="")
    if num2 > num3:
        print("Número 2 é o meio e o Número 3 é o menor")
    else:
        print("Número 3 é o meio e o Número 2 é o menor")
elif num2 == max:
    print("Número 2 é o maior, ", end="")
    if num1 > num3:
        print("Número 1 é o meio e o Número 3 é o menor")
    else:
        print("Número 3 é o meio e o Número 1 é o menor")
else:
    print("Número 3 é o maior, ", end="")
    if num1 > num2:
        print("Número 1 é o meio e o Número 2 é o menor")
    else:
        print("Número 2 é o meio e o Número 1 é o menor")