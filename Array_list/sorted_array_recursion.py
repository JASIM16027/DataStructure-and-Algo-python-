def sorted_arr(arr):
    n = len(arr)
    if n == 0:
        return
    temp = arr[n - 1]

    arr.remove(temp)
    print('sorted_arr', arr)
    sorted_arr(arr)

    insert(arr, temp)


def insert(arr, temp):
    print(arr, temp)
    if len(arr) == 0 or arr[len(arr) - 1] <= temp:
        arr.append(temp)
        return
    val = arr[len(arr) - 1]

    arr.remove(val)
    print('arr temp', arr, temp)
    insert(arr, temp)
    arr.append(val)


arr = [1, 4, 2, 3, 0]
n = len(arr)
sorted_arr(arr)
print(arr)
