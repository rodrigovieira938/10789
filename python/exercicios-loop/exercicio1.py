pares = []
impares = []
for i in range(1, 61):
    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)
print(f"Primeiros 30 números pares: {pares}")
print(f"Primeiros 30 números impares: {impares}")