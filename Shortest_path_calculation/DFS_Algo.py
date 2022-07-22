"""
graph = {'A': ['B', 'C', 'E'],
         'B': ['A','D', 'E'],
         'C': ['A', 'F', 'G'],
         'D': ['B'],
         'E': ['A', 'B','D'],
         'F': ['C'],
         'G': ['C']}


# finds shortest path between 2 nodes of a graph using BFS
def bfs_shortest_path(graph, start, goal):
    # keep track of explored nodes
    visited = []
    print('visited = ', visited)
    # keep track of all the paths to be checked
    queue = [[start]]
    print("queue = ", queue)

    # return path if start is goal
    if start == goal:
        return [start]

    # keeps looping until all possible paths have been checked
    while queue:
        # pop the first path from the queue
        path = queue.pop(0)
        print("path = ", path)
        # get the last node from the path
        node = path[-1]
        print("node = ", node)

        if node not in visited:
            neighbours = graph[node]
            print("neighbours", neighbours)
            # go through all neighbour nodes, construct a new path and
            # push it into the queue
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)

                # return path if neighbour is goal
                if neighbour == goal:
                    return new_path
            print("update queue = ", queue)
            # mark node as explored
            visited.append(node)
            print('visited = ', visited)
    # in case there's no path between the 2 nodes
    return "So sorry, but a connecting path doesn't exist :("


c = bfs_shortest_path(graph, 'A', 'D')  # returns ['G', 'C', 'A', 'B', 'D']
print(c)

"""


















