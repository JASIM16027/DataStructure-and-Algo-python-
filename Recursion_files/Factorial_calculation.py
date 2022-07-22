def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


inp = int(input("Enter the factorial number : "))
fact = factorial(inp)
print(f'factorial of {inp} is {fact}')
