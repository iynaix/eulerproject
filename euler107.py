from collections import defaultdict

GRID = [
    "-,16,12,21,-,-,-",
    "16,-,-,17,20,-,-",
    "12,-,-,28,-,31,-",
    "21,17,28,-,18,19,23",
    "-,20,-,18,-,-,11",
    "-,-,31,19,-,-,27",
    "-,-,-,23,11,27,-",
]
GRID = [line.split(",") for line in GRID]


with open("network107.txt") as fp:
    GRID = []
    for line in fp:
        GRID.append(line.split(","))


def find(C, u):
    if C[u] != u:
        C[u] = find(C, C[u])
    return C[u]


def union(C, R, u, v):
    u, v = find(C, u), find(C, v)
    if R[u] > R[v]:
        C[v] = u
    else:
        C[u] = v
    if R[u] == R[v]:
        R[v] += 1


def kruskal(G):
    E = [(G[u][v], u, v) for u in G for v in G[u]]
    T = set()
    C, R = {u: u for u in G}, {u: 0 for u in G}
    for _, u, v in sorted(E):
        if find(C, u) != find(C, v):
            T.add((u, v))
            union(C, R, u, v)
    return T


def total_grid_weight(grid):
    ret = 0
    for y, row in enumerate(grid):
        for x, col in enumerate(row):
            if x >= y:
                continue
            try:
                ret += int(col)
            except ValueError:
                pass
    return ret


def to_graph(grid):
    graph = defaultdict(dict)

    for y, row in enumerate(grid):
        for x, col in enumerate(row):
            try:
                graph[y][x] = int(col)
            except ValueError:
                pass

    graph = dict(graph)
    return graph


def euler107():
    graph = to_graph(GRID)
    total_weight = total_grid_weight(GRID)
    minimal_spanning_weight = sum(graph[a][b] for a, b in kruskal(graph))
    return total_weight - minimal_spanning_weight
