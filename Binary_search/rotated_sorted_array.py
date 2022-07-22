def BinarySearch(arr):
    low, high = 0, len(arr) - 1
    if len(arr) == 1:
        return 0
    while low <= high:
        mid = low + (high - low) // 2
        if 0 < mid < len(arr) - 1:
            if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
                return mid + 1
            elif arr[mid] < arr[mid - 1]:
                high = mid - 1
            else:
                low = mid + 1
        if arr[mid] == arr[len(arr) - 1]:
            return len(arr)
    return -1


arr = [5, 6, 7, 8, 9, 10, 12, 1, 4]
print(BinarySearch(arr))

ar = [7, 8, 9, 10, 12, 1, 4, 5, 6]
res = 0
for i in range(1, len(ar)):
    if ar[i - 1] > ar[i]:
        res = i
        break
print(res)
