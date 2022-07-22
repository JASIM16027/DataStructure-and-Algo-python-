def binary_search(ll, left, right, key):
    if left > right:
        return -1
    mid = (left + right) // 2
    if ll[mid] == key:
        return mid
    elif ll[mid] > key:
        return binary_search(ll, left, mid - 1, key)
    else:
        return binary_search(ll, mid + 1, right, key)


if __name__ == "__main__":
    ll = [1, 2, 3, 4, 5, 6, 7, 8, 12]
    left = 0
    right = len(ll) - 1
    for key in [2, 3, 6, 11]:
       ans = binary_search(ll, left, right, key)
       if ans == -1:
           print(f'{key}' ' is not found')
       else:
           print(f'{ll[ans]}' ' is Found')



