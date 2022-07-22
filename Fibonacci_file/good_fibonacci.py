"""


def fib(n):
    if n in [1, 2]:
        return 1
    return fib(n - 1) + fib(n - 2)


print([fib(i) for i in range(1, 30)])



def fibonacci(n):
    if n <= 1:
        return n, 0
    else:
        (a, b) = fibonacci(n - 1)
        return a + b, a


print([fibonacci(i)[0] for i in range(1, 500)])

"""

l = [1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 6, 6, 6, 6, 6]

ll = []
for i in l:
    count = 0
    if i not in ll:
        for j in range(len(l)):

            if i == l[j]:
                count += 1
        ll.append(i)
        print(i, '==', count, 'times')
