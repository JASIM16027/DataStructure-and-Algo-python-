dp = [-1 for i in range(1000)]


def fib(n):
    if (n <= 1):
        return n
    global dp

    # Temporary variables to store
    # values of fib(n-1) & fib(n-2)

    if dp[n - 1] != -1:
        first = dp[n - 1]
    else:
        first = fib(n - 1)
    if dp[n - 2] != -1:
        second = dp[n - 2]
    else:
        second = fib(n - 2)
    dp[n] = first + second

    # Memoization
    return dp[n]


# Driver Code
if __name__ == '__main__':
    n = int(input())
    print(fib(n))