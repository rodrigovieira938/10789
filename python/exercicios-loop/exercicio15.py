for i in range(256):
    if i % 20 == 0 and i != 0:
        res = input("Deseja continuar? S ou N: ")
        if res == 'N':
            break
    print(f"ASCII {i} -- '{chr(i)}'")