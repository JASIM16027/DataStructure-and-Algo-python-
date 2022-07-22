# Python3 Program to find n'th fibonacci Number in
# with O(Log n) arithmetic operations
MAX = 1000

# Create an array for memoization
f = [0] * MAX


# Returns n'th fibonacci number using table f[]
def fib(n):

    if n == 0:
        return 0
    if n == 1 or n == 2:
        f[n] = 1
        return f[n]

    # If fib(n) is already computed
    if f[n]:
        return f[n]

    if n & 1:
        k = (n + 1) // 2
        f[n] = (fib(k) * fib(k) + fib(k - 1) * fib(k - 1))
    else:
        k = n // 2
        f[n] = (2 * fib(k - 1) + fib(k)) * fib(k)

    return f[n]


n = int(input())
print(fib(n))
