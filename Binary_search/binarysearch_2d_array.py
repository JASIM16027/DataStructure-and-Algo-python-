def BinarySearch(arr, key):
    n, m = len(arr), len(arr[0])
    j = m - 1
    i = 0
    while (0 <= i <= n - 1) and (0 <= j <= m - 1):
        if arr[i][j] == key:
            return [i, j]
        elif arr[i][j] > key:
            j = j-1
        else:
            i = i + 1
    return -1


arr = [[10, 20, 30, 40],
       [15, 25, 35, 45],
       [27, 29, 37, 45],
       [32, 33, 39, 50]]
key = 32
print(BinarySearch(arr, key))
