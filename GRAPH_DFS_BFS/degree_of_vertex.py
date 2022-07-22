class Graph:
    def __init__(self, V, E):
        self.V = set(V)
        self.E = set(frozenset((u, v)) for u, v in E)
        # print(self.E)

        self._nbrs = {}
        for v in self.V:
            self._nbrs[v] = set()
        for u, v in self.E:
            self._nbrs[u].add(v)
            self._nbrs[v].add(u)
        print(self._nbrs)

    def degree(self, v):
        # sum(1 for e in self.E if v in e)
        return len(self._nbrs[v])

    def neighbors(self, v):
        return iter(self._nbrs[v])


"""
l = list(map(int, input().split()))
s = set()
n = int(input())
for _ in range(n):
    n = list(map(int, input().split()))
    s.add((n[0], n[1]))
"""

g = Graph([1, 2, 3, 4, 5, 6], {(1, 2), (1, 3), (2, 3), (3, 4), (4, 5), (5, 6)})

assert (g.degree(1) == 2)
assert (g.degree(2) == 2)
assert (g.degree(3) == 3)
print("okay")
print(set(v for v in g.neighbors(3)))
print(set(v for v in g.neighbors(4)))

