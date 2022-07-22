def reverse_linear_sequence(s, start, end):
    if start < end:
        s[start], s[end] = s[end], s[start]
        print(start, end)
        reverse_linear_sequence(s, start + 1, end - 1)


s = [1, 3, 5, 7, 8, 2]
reverse_linear_sequence(s, 0, len(s)-1)
print(s)

