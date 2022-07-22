def graph(edge):
    d = {}
    for i in range(len(edge)-1):
        for j in range(len(edge[0])-1):
            d[edge[i][j]].append(edge[i][j + 1])
            d[edge[i][j + 1]].append(edge[i][j])


t = int(input().strip())
for i in range(t):
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])
    edges = []
    for _ in range(m):
        edges.append(list(map(int, input().rstrip().split())))
    starting_position = int(input().strip())
    print(edges)
    graph(edges)
