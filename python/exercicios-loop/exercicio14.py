num = int(input("Introduze um número: "))
print(f"Tabuada do {num}")
for i in range(1,101):
    print(num * i, end="")
    if i == 100:
        print("")
    else:
        print(end=", ")