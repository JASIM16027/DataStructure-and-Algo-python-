adj_list = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["B", "F"],
    "D": [],
    "E": ["F"],
    "F": []

}

color = {}
parent = {}
traversal_time = {}
dfs_traversal_output = []

for node in adj_list.keys():
    color[node] = "W"
    parent[node] = None
    traversal_time[node] = [-1, -1]

time = 0


def dfs_util(u):
    global time
    color[u] = "G"
    traversal_time[u][0] = time
    dfs_traversal_output.append(u)

    for v in adj_list[u]:
        if color[v] == "W":
            parent[v] = u
            dfs_util(v)

    color[u] = "B"
    traversal_time[u][1] = time
    time += 1


for u in adj_list.keys():
    if color[u] == "W":
        dfs_util(u)


print(dfs_traversal_output)
print(parent)
print(traversal_time)
