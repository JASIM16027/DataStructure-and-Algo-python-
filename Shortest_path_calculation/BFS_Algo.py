graph = {'A': ['B', 'C', 'E'],
         'B': ['A', 'D', 'E'],
         'C': ['A', 'F', 'G'],
         'D': ['B'],
         'E': ['A', 'B', 'D'],
         'F': ['C'],
         'G': ['C']}


def BFS(graph, start, end):
    visited = []
    queue = [[start]]
    if start == end:
        return [start]

    while queue:
        path = queue.pop(0)

        node = path[-1]

        if node not in visited:
            neighbors = graph[node]
            for neighbor in neighbors:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

                if neighbor == end:
                    return new_path
            visited.append(node)


path = BFS(graph, "G", "C")
print(path)
