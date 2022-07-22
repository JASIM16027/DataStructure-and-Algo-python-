arr = [2, 3, 7, 6, 4, 5, 9]


def insert(arr, temp):
    if not arr or arr[len(arr)-1] >= temp:
        arr.append(temp)
        return
    val = arr[len(arr)-1]
    arr.remove(val)
    insert(arr, temp)
    arr.append(val)


def sorted_arr(arr):
    if len(arr)==1:
        return
    temp = arr[len(arr) - 1]
    print(temp)
    arr.remove(temp)
    sorted_arr(arr)

    insert(arr, temp)


sorted_arr(arr)
print(arr)
