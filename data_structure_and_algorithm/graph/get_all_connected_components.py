class Graph:
    def __init__(self, nVertices):
        self.nVertices = nVertices
        self.adjMatrix = [[0 for i in range(self.nVertices)]
                          for j in range(self.nVertices)]

    def addEdge(self, v1, v2):
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1

    def __dfsHelper(self, starting_vertex, visited_array, path):
        path.append(starting_vertex)
        visited_array[starting_vertex] = True
        for i in range(self.nVertices):
            if self.adjMatrix[starting_vertex][i] > 0 and visited_array[i] is False:
                self.__dfsHelper(i, visited_array, path)
        return path

    def all_connected_components(self):
        visited_array = [False] * self.nVertices
        final_components = []
        for i in range(self.nVertices):
            if visited_array[i] is False:
                component = self.__dfsHelper(i, visited_array, [])
                final_components.append(component)
        return final_components

    def __str__(self):
        return str(self.adjMatrix)


n = int(input())
gg = int(input())
g = Graph(gg)
while n:
    v1 = int(input())
    v2 = int(input())
    g.addEdge(v1,v2)
    n-=1


print(g)
print(g.all_connected_components())
