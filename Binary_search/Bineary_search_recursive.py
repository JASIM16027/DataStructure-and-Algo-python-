def binarySearchR(a, l, h, key):
    if l == h:
        if a[l] == key:
            return l
        else:
            return -1
    else:
        mid = (l + h) // 2
        if a[mid] == key:
            return mid
        elif a[mid] < key:
            return binarySearchR(a, mid + 1, h, key)
        else:
            return binarySearchR(a, l, mid - 1, key)


a = [1, 2, 3, 6, 7, 8, 9, 10]
key = int(input("Enter the key value = "))

ans = binarySearchR(a, 0, len(a)-1, key)
if ans == -1:
    print(f"{key} is not founded")
else:
    print(ans)


