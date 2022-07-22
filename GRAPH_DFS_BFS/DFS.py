from collections import defaultdict

visited = set()


class Graph:

    # Constructor
    def __init__(self):

        # default dictionary to store graph
        self.graph = defaultdict(list)

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    # print(self.graph)

    # A function used by DFS

    def DFS(self, v, visited):

        visited.add(v)
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.DFS(neighbour, visited)


# Time complexity: O(V + E), where V is the number of vertices and
# E is the number of edges in the graph.
# Space Complexity: O(V), since an extra visited array of size V is required.


g = Graph()
while True:
    edges = int(input())
    nodes = list(map(int, input().strip().split()))
    for i in range(edges):
        m = list(map(int, input().strip().split()))
        g.addEdge(m[0], m[1])

    cnt = 0

    for i in nodes:
        if i in visited:
            continue
        g.DFS(i, visited)
        cnt += 1

    print(visited)
    print(cnt)
