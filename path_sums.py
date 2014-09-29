from heapq import heappush, heappop
from utils import memoize


INF = float('inf')


class Grid(object):
    def __init__(self, grid):
        if isinstance(grid, list):
            self.data = grid
        else:
            if isinstance(grid, basestring):
                fp = open(grid)
            elif isinstance(grid, file):
                fp = grid
            self.data = [[int(e) for e in g.split(',')]
                        for g in fp.read().splitlines()]

        #pre-compute some values
        self.width = len(self.data[0])
        self.height = len(self.data)
        self.graph = self.to_graph()

    def iter_cells(self):
        """returns each cell as a tuple of (value, x coord, y corrd)"""
        for row_no, row in enumerate(self.data):
            for col_no, val in enumerate(row):
                yield (val, col_no, row_no)

    def cell(self, x, y):
        return self.data[y][x]

    def get_next_steps(self, x, y):
        """
        returns a dict of {(x coord, y corrd): value,} of the steps can be
        taken given the current coords
        """
        ret = {}
        #down
        if y + 1 < self.height:
            ret[(x, y + 1)] = self.cell(x, y + 1)
        #right
        if x + 1 < self.width:
            ret[(x + 1, y)] = self.cell(x + 1, y)
        return ret

    def to_graph(self):
        """
        returns a graph of {
            (x coord, y coord): {(x coord, y corrd): value,}
        }
        """
        graph = {}
        for val, x, y in self.iter_cells():
            graph[(x, y)] = self.get_next_steps(x, y)
        return graph


def shortest_path_dag(graph, start, end, initial=0):
    """
    shortest path for a directed acyclic graph (i.e. no cycles)

    adapted from the Python Algorithms book
    """
    @memoize
    def d(u):
        #found the end
        if u == end:
            return 0
        #best of every first step
        return min(graph[u][v] + d(v) for v in graph[u])

    #apply f to actual start node
    return initial + d(start)


def relax(W, u, v, D, P):
    d = D.get(u, INF) + W[u][v]
    if d < D.get(v, INF):
        D[v], P[v] = d, u
        return True


def dijkstra(G, s):
    D, P, Q, S = {s: 0}, {}, [(0, s)], set()
    while Q:
        _, u = heappop(Q)
        if u in S:
            continue
        S.add(u)
        for v in G[u]:
            relax(G, u, v, D, P)
            heappush(Q, (D[v], v))
    return D
