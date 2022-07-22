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


arr = [7, 8, 9, 10, 12, 1, 4, 5, 6]
index = BinarySearch(arr)
print(index)
key = 10


def BinarySearch(arr, low, high, key):

    while low <= high:
        mid = low + ((high - low) // 2)
        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            high = mid - 1
        else:
            low = mid + 1


n = len(arr) - 1
s1 = BinarySearch(arr, 0, index - 1, key)
s2 = BinarySearch(arr, index, n, key)
print(s1, s2)
