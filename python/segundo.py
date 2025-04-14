num = int(input("Introduze um número de 1 - 13: "))
if (num % 2 != 0 or num == 2) and(num % 3 != 0 or num == 3) and(num % 5 != 0 or num == 5):
    print("O número é primo")
else:
    print("O número não é primo")