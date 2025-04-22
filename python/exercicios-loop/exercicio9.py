num = 0
while True:
    num = int(input("Introduza um número de um 1 - 100: "))
    if num >= 1 and num <= 100:
        break
    else:
        print("O número tem que estar entre 1 e 100!")
print(f"O número introduzido foi {num}")