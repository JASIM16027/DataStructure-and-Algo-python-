from collections import defaultdict

MAX = 100
visited = [False] * MAX


class Graph:

    # Constructor
    def __init__(self):

        # default dictionary to store graph
        self.graph = defaultdict(list)

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)
        print(self.graph)

    # A function used by DFS

    def DFS(self, v, visited):

        visited[v] = True
        for neighbour in self.graph[v]:
            if not visited[neighbour]:
                visited[neighbour] = True
                self.DFS(neighbour, visited)


# Time complexity: O(V + E), where V is the number of vertices and
# E is the number of edges in the graph.
# Space Complexity: O(V), since an extra visited array of size V is required.


g = Graph()
edges = int(input())
nodes = list(map(int, input().strip().split()))
for i in range(edges):
    m = list(map(int, input().strip().split()))
    g.addEdge(m[0], m[1])

cnt = 0
for i in nodes:
    if not visited[i]:
        g.DFS(i, visited)
        cnt += 1
print(cnt)
