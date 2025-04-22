num = int(input("Introduze um número: "))
print(f"Tabuada do {num}")
for i in range(1,11):
    print(num * i, end="")
    if i == 10:
        print("")
    else:
        print(end=", ")