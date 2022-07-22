adj_list = {
    "A": ["C", "B"],
    "B": ["D"],
    "C": [],
    "D": ["A", "E"],
    "E": []
}

color = {}
parent = {}

for u in adj_list.keys():
    color[u] = "W"
    parent[u] = None
    print(parent)


def dfs_graph(u, color, parent):
    color[u] = 'G'
    for v in adj_list[u]:
        if color[v] == "W":
            cycle = dfs_graph(v, color, parent)

            if cycle == True:
                return True

        elif color[v] == "G":
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