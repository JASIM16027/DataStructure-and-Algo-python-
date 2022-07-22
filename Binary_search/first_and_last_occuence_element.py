def BinarySearch(arr, key):
    def first_occurence(arr, key):
        res = -1
        low, high = 0, len(arr) - 1
        while low <= high:
            mid = low + ((high - low) // 2)
            if arr[mid] == key:
                res = mid
                high = mid - 1
            elif arr[mid] > key:
                high = mid - 1
            else:
                low = mid + 1
        return res

    def second_occurence(arr, key):
        res = -1
        low, high = 0, len(arr) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if arr[mid] == key:
                res = mid
                low = mid + 1
            elif arr[mid] > key:
                high = mid - 1
            else:
                low = mid + 1
        return res

    return [first_occurence(arr, key), second_occurence(arr, key)]


arr = [1, 2, 3, 10, 10, 10, 12, 12, 13]

key = 10
print(BinarySearch(arr, key))
