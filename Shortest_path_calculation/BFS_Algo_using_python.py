from queue import Queue

adj_list = {
    "A": ["C", "B"],
    "B": ["A", "C", "E", "F"],
    "C": ["A", "B", "D"],
    "D": ["C"],
    "E": ["B"],
    "F": ["B"]
}

visited = {}
parent = {}
level = {}
bfs_traversal_output = []
queue = Queue()

for node in adj_list.keys():
    visited[node] = False
    parent[node] = None
    level[node] = -1

s = "A"
visited[s] = True
level[s] = 0
queue.put(s)

while not queue.empty():
    u = queue.get()  # pop the first element of the queue
    bfs_traversal_output.append(u)
    for v in adj_list[u]:
        if not visited[v]:
            visited[v] = True
            parent[v] = u
            level[v] = level[u] + 1
            queue.put(v)
v = "E"

path = []
while v is not None:
    path.append(v)
    v = parent[v]
path.reverse()
print(path)
