val = [60, 100, 120, 140]
wt = [10, 20, 30, 18]
W = 50
n = len(val)

dp = [[-1 for i in range(W + 1)] for j in range(n + 1)]

for i in range(n + 1):
    for j in range(W + 1):
        if i == 0 or j == 0:
            dp[i][j] = 0
        if dp[i][j] != -1:
            continue
        if wt[i - 1] <= j:
            dp[i][j] = max(val[i - 1] + dp[i][j - wt[i - 1]], dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[-1][-1])