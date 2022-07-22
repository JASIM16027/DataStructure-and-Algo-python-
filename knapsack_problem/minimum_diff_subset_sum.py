nums = [1, 2, 3, 4]
sm = 0
n = len(nums)
for i in nums:
    sm += i
m = sm

dp = [[-1 for _ in range(m + 1)] for _ in range(n + 1)]


def knapsack(m, n):
    for i in range(n + 1):
        for j in range(m + 1):
            if i == 0:
                dp[i][j] = False
            if j == 0:
                dp[i][j] = True

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if dp[i][j] != -1:
                return dp[i][j]

            if nums[i - 1] <= j:
                dp[i][j] = dp[i - 1][j - nums[i - 1]] + dp[i - 1][j]

            else:
                dp[i][j] = dp[i - 1][j]

    return dp[n][m]


print(knapsack(m, n))
r = len(dp)
c = len(dp[0])
v = []
for i in range(c // 2):
    if dp[r - 1][i]:
        v.append(i)
print(v, sm)
minimum = float('inf')
for i in range(len(v)):
    minimum = min(minimum, abs(sm - 2 * v[i]))

print(minimum)
