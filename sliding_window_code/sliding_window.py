arr = [1, 2, 3, 2, 5, 7, 9, 4, 9, 10]
k = 5

i, j = 0, 0
n = len(arr) - 1
sm = 0
res = -float("inf")
while j <= n:
    sm += arr[j]
    if j-i+1 < k:
        j += 1
    elif j - i + 1 == k:
        res = max(res, sm)
        sm = sm - arr[i]
        i += 1
        j += 1
print(res)
