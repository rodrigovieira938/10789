i = 0
num = 2
while i < 10:
    primo = True
    for j in range(2, num):
        if num % j == 0 and 2 != num:
            primo = False
            num += 1
            break
    if primo:
        print(f"{num}")
        num += 1
        i+=1;