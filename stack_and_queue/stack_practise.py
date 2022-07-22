n = int(input())
stack = []

for _ in range(n):
    dn = input().split()
    m = int(dn[0])
    if m == 1:
        mn = int(dn[1])
        stack.append(mn)
    elif m == 2:
        stack.pop()
    elif m == 3:
        print(map(int, x) for x in stack)
        stack.pop()



