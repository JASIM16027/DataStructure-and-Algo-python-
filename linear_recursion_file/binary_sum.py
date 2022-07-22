# runtime o(n)
# 2n-1 function call
# memory space is required O(logn)


def binary_sum(s, start, stop):
    if start >= stop:
        return 0
    elif start == stop - 1:
        return s[start]
    else:
        mid = (start + stop) // 2
        return binary_sum(s, start, mid) + binary_sum(s, mid, stop)  # runtime o(n) #2n-1


s = [1, 2, 3, 4, 5, 6, 7, 8]
ans = binary_sum(s, 0, len(s))
print(ans)
