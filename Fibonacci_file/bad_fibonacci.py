def fib(n):
    if n in [1, 2]:
        return 1
    return fib(n - 1) + fib(n - 2)


print([fib(i) for i in range(1, 40)])