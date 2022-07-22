adj_list = {
    "A": ["C", "B"],
    "B": ["A", "C", "E", "F"],
    "C": ["A", "B", "D"],
    "D": ["C"],
    "E": ["B"],
    "F": ["B"]
}

color = {}
parent = {}

for u in adj_list.keys():
    color[u] = "W"
    parent[u] = None
    

def dfs_graph(u, color, parent):
    color[u] = 'G'
    for v in adj_list[u]:
        if color[v] == "W":
            cycle = dfs_graph(v, color, parent)

            if cycle == True:
                return True

        elif color[v] == "G" and parent[u]!=v:
            print(u, v)
            return True

    color[u] = "B"
    return False


is_cycle = False
for u in adj_list.keys():
    if color[u] == 'W':
        is_cycle = dfs_graph(u, color, parent)

        if is_cycle == True:
            break
print(is_cycle)