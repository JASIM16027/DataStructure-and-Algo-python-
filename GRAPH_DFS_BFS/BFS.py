from collections import defaultdict,deque


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

    def BFS(self, s, visited):

        queue = deque()
        queue.append(s)
        visited.add(s)
        while queue:
            s = queue.popleft()
            print(s, end=" ")

            for neighbour in self.graph[s]:
                if neighbour not in visited:
                    queue.append(neighbour)
                    visited.add(neighbour)


# Time complexity: O(V + E), where V is the number of vertices and
# E is the number of edges in the graph.
# Space Complexity: O(V), since an extra visited array of size V is required.

"""
g = Graph()
nodes = int(input())
for i in range(nodes):
    m = list(map(int, input().strip().split()))
    g.addEdge(m[0], m[1])
"""
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
visited = set()
print("Following is Breadth First Traversal"
      " (starting from vertex 2)")

g.BFS(0,visited)
