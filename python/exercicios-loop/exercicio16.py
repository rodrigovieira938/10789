media = 0
for i in range(30):
    num = 0
    while True:
        num = int(input(f"Introduze o {i+1}º número par de 1 - 50: "))
        if num % 2 != 0 or num < 1 or num > 50:
            print("O número tem de ser par e estar entre 1 e 50!")
        else:
            break
    media += num
media /= 30
print(f"A média é {media}")