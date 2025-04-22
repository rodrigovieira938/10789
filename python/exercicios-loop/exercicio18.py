limite = int(input("Introduze o número: "))
for i in range(1, limite+1):
    soma = 0
    str = ""
    for n in range(i-1, 0, -1):
        if i % n == 0:
            soma += n
            str += f"{n}+"
    if soma == i:
        print(f"{i}={str[0:-1]}")