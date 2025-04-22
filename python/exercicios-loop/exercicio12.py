num = int(input("Introduza quantos números quer que se efetue a soma: "))

soma = 0
sub = 0
div = 0
mul = 0

for i in range(1, num):
    print(f"{num} + {i} = {num + i}")
    soma += 1
    print(f"{num} - {i} = {num - i}")
    sub += 1
    print(f"{num} / {i} = {num / i}")
    div += 1
    print(f"{num} * {i} = {num * i}")
    mul += 1
print(f"Foi executado um total de {soma + sub + div + mul} operações!")