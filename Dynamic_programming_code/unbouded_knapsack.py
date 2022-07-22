val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(val)

dp = [[-1 for i in range(W + 1)] for j in range(n + 1)]


def unbounded_knapsack(wt, val, w, n):
    if n == 0 or w == 0:
        return 0
    if dp[n][w] != -1:
        return dp[n][w]
    if wt[n - 1] <= w:
        dp[n][w] = max(val[n - 1] + unbounded_knapsack(wt, val, w - wt[n - 1], n),
                       unbounded_knapsack(wt, val, w, n-1))
        return dp[n][w]
    else:
        dp[n][W] = unbounded_knapsack(wt, val, W, n - 1)
        return dp[n][W]


print(unbounded_knapsack(wt, val, W, n))
