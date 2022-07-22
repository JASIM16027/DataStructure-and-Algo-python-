def longestSubarray(arr):
    # Write your code here
    d = {}
    res = []
    for i in range(len(arr)):
        if arr[i] not in d:
            d[arr[i]] = 1
        elif d[arr[i]] <= 2:
            d[arr[i]] += 1

    for i, value in d.items():

        if value <= 2:
            res.extend([i] * value)


arr = [1, 1, 1, 2, 2, 3, 3]
print(longestSubarray(arr))
