class Graph:
    def __init__(self, V, E):
        self.E = set(frozenset((u, v)) for u, v in E)
        print(self.E)

        self._nbrs = {}

        for v in V:
            self.addvertex(v)

        for u, v in self.E:
            self._nbrs[u].add(v)
            self._nbrs[v].add(u)
        print(self._nbrs)

    def addvertex(self, v):
        if v not in self._nbrs:
            self._nbrs[v] = set()

    def addedge(self, u, v):
        self.addvertex(u)
        self.addvertex(v)
        self.E.add(frozenset([u, v]))
        self._nbrs[u].add(v)
        self._nbrs[v].add(u)
        print(self.E)

    def degree(self, v):
        # sum(1 for e in self.E if v in e)
        return len(self._nbrs[v])

    def neighbors(self, v):
        return iter(self._nbrs[v])

    @property
    def n_adge(self):
        return len(self.E)

    @property
    def num_vertex(self):
        return len(self._nbrs)

    def remove_edge(self, u, v):
        e = frozenset([u, v])
        if e in self.E:
            self.E.remove(e)
            self._nbrs[u].remove(v)
            self._nbrs[v].remove(u)
        print(self._nbrs)
        print(self.E)

    def remove_vertex(self, u):
        for v in list(self.neighbors(u)):
            self.remove_edge(u, v)
        del self._nbrs[u]
        print(self.E)


g = Graph([1, 2, 3, 4, 5, 6], {(1, 2), (1, 3), (2, 3), (3, 4), (4, 5), (5, 6)})
assert (g.degree(1) == 2)
assert (g.degree(2) == 2)
assert (g.degree(3) == 3)

print("okay")
g.addedge(6, 7)
#print(set(v for v in g.neighbors(3)))
#print(set(v for v in g.neighbors(7)))
# assert ()
assert (g.num_vertex == 7 and g.n_adge == 7)
print(g.n_adge, g.num_vertex)
g.remove_edge(1, 2)
assert (g.num_vertex == 7 and g.n_adge == 6)

g.remove_edge(2, 3)
assert (g.num_vertex == 7 and g.n_adge == 5)

g.remove_edge(3, 4)
assert (g.num_vertex == 7 and g.n_adge == 4)

g.remove_edge(9, 0)  # this value is not in frozenset
g.addedge(1,5)
assert (g.num_vertex == 7 and g.n_adge == 5)
g.addedge(1,3)
print(set(v for v in g.neighbors(3)))
g.remove_vertex(5)