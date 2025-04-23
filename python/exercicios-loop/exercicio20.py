def e_primo(num:int):
    for i in range(2, num):
        if num % i == 0 and num != 2:
            return False
    return True
def num_divisores(num:int):
    divs = 1
    for i in range(2, num):
        if num % i == 0:
            divs+=1    
    return divs
def num_perfeitos(limite:int):
    num = 0
    for i in range(1, limite+1):
        soma = 0
        for n in range(i-1, 0, -1):
            if i % n == 0:
                soma += n
        if soma == i:
            num+=1
    return num
num = int(input("Introduza um número: "))
vezes = 0
operacao = ""
for i in range(num, 0, -1):
    if vezes % 10 == 0 and vezes != 0:
        res = input("Deseja continuar? S ou N: ")
        if res == 'N':
            break
    print(f"O número {i}, tem {num_divisores(i)} divisores, tem {num_perfeitos(i)} número perfeito ", end="")
    if e_primo(i):
        print("e é primo")
    else:
        print("não é primo")
    vezes+=1
while True:
    operacoes = "+-*/."
    print("Calculadora")
    print("\t+")
    print("\t-")
    print("\t*")
    print("\t/")
    print("\t. - para mostrar a tabuada\n")
    operacao = input("Introduza a operação: ")
    if operacao in operacoes:
        break
if operacao == ".":
    num = int(input("Introduza o número: "))
    i = 0
    while True:
        if i % 20 == 0 and i != 0:
            res = input("Deseja continuar? S ou N: ")
            if res == 'N':
                break
        print(num*(i+1))
        i+=1
    print("")
else:
    num1 = int(input("Introduza o primeiro número: "))
    num2 = int(input("Introduza o segundo número: "))
    res = 0

    if operacao == "+":
        res = num1 + num2
    elif operacao == "-":
        res = num1 - num2
    elif operacao == "*":
        res = num1 * num2
    elif operacao == "/":
        res = num1 / num2

    print(f"{num1}{operacao}{num2}={num1+num2}")