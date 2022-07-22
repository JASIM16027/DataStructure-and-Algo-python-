def power(x, n):
    if n == 0:
        return 1

    else:
        return x * power(x, n - 1)


print(f"{power(2, 13)}")
