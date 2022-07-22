def binarySearch(a, n, key):
    l = 1
    h = n

    while l <= h:
        mid = l + (h - l) // 2
        if key == a[mid]:
            return mid
        if key > a[mid]:
            l = mid + 1
        else:
            h = mid - 1

    return -1


a = [1, 2, 3, 6, 7, 8, 9, 10]

length = len(a)
key = 78
ans = binarySearch(a, length - 1, key)
print(ans)
