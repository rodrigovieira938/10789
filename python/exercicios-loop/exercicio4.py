num = int(input("Introduza o número: "))
primo = True
for i in range(2, num):
    if num % i == 0:
        primo = False
        break
if primo:
    print(f"O número {num} é um número primo")
else:
    print(f"O número {num} não é um número primo")