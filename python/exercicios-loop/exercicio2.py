nums = []
for i in range(10):
    nums.append(int(input(f"Introduza o {i+1}º número: ")))
for num in nums:
    if num % 2 == 0:
        print(f"O número {num} é par")
    else:
        print(f"O número {num} é impar")