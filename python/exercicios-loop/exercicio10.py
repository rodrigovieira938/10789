num = int(input("Introduza um número inteiro: "))
print(f"Divisores do número {num}:")
for i in range(1, num):
    if num % i == 0:
        print(f"\t{i}")