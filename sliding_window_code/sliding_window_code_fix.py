arr = [1, 2, 3, 2, 5, 7, 9, 4, 9]
k = 3

i, j = 0, 0
n = len(arr)
sm = 0
res = -float("inf")
for j in range(n):
    sm += arr[j]
    if j - i + 1 == k:
        res = max(res, sm)
        sm = sm - arr[i]
        i += 1
        j += 1
print(res)