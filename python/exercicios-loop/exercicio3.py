notas = []
for i in range(10):
    notas.append(int(input(f"Introduza a nota do {i+1}º aluno: ")))
media = 0
for nota in notas:
    media += nota
media /= 10
print(f"A média da turma é {media}")