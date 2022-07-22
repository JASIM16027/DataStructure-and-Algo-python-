def fib(n, dp):
    if n == 0 or n == 1:
        return n
    if dp[n - 1] == -1:
        dp[n - 1] = fib(n - 1, dp)

    if dp[n - 2] == -1:
        dp[n - 2] = fib(n - 2, dp)
    return dp[n-1]+dp[n-2]


n = int(input())
dp = [-1] * n
print(fib(n, dp))
