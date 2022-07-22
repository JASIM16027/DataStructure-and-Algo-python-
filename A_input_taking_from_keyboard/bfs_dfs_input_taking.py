def graph(cities):
    g = {}
    print(cities)
    for i, j in cities:
        g[i].append(j)
        g[j].append(i)
    print(g)


q = int(input().strip())

for q_itr in range(q):
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    cities = []

    for _ in range(m):
        cities.append(list(map(int, input().rstrip().split())))
    print(cities)
    graph(cities)