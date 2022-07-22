def palindrome(n):
    temp = n
    res = 0
    while temp:
        last_digit = temp % 10
        res = res * 10 + last_digit
        temp = temp // 10
    return res


t = int(input())
while t:
    n = int(input())

    i = 0
    res = palindrome(n)
    while res != n:
        i += 1
        n = n + res
        res = palindrome(n)
    print(res, i)
    t -= 1
