def BinarySearch(arr, key):
    if len(arr) == 1:
        if arr[0] == key:
            return 0

    if arr[0] < arr[1]:
        low, high = 0, len(arr) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if arr[mid] == key:
                return mid
            elif arr[mid] > key:
                high = mid - 1
            else:
                low = mid + 1
        return -1

    if arr[0] > arr[1]:
        low, high = 0, len(arr) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if arr[mid] == key:
                return mid
            elif arr[mid] > key:
                low = mid + 1
            else:
                high = mid - 1
        return -1


arr = [6, 5, 4, 3, 2, 1, 0]
arr1 = [1, 2, 3, 4, 5, 6]
key = 5
print(BinarySearch(arr1, key))
print(BinarySearch(arr, key))
