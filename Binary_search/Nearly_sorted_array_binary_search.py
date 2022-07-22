def BinarySearch(arr, key):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] == key:
            return mid
        elif arr[mid - 1] >= arr[low] and arr[mid - 1] == key:
            return mid - 1
        elif arr[mid + 1] <= arr[high] and arr[mid + 1] == key:
            return mid + 1
        if arr[mid] < key:
            low = mid + 2
        else:
            high = mid - 2

    return -1


arr = [10, 20, 30, 60, 35, 40]
key = 35
print(BinarySearch(arr, key))
