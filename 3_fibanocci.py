fibonacci = lambda n: n if n <= 1 else (fibonacci(n-1) + fibonacci(n-2))

fib_num = 50
fib_series = []
for i in range(fib_num):
    fib_series.append(fibonacci(i))

print(fib_series)