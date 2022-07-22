import math


def fibo(n):
    f = (1 + math.sqrt(5)) / 2

    return round(pow(f, n) / math.sqrt(5))


if __name__ == '__main__':
    n = int(input())

    print(fibo(n))
