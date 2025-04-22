def fibonacci_str(n, primeiro=True):
    if n <= 0:
        return "1"
    elif n == 1:
        return "1"
    if primeiro:
        return f"{fibonacci_str(n-1, False)} + {fibonacci_str(n-2, False)}"
    else:
        return f"{fibonacci(n)}"
def fibonacci(n):
    if n <= 0:
        return 1
    elif n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)
for i in range(0, 60):
    print(f"{fibonacci(i)} = {fibonacci_str(i)}")