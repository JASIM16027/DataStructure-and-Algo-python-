def linear_sum(s, n):
    if n == 0:
        return n
    else:
        a = linear_sum(s, n - 1) + s[n-1]
        print(a)
        return a


l = [4, 5, 6, 7]
ans = linear_sum(l, len(l))
print(ans)

