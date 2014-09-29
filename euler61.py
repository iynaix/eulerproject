from utils import polygonal_gen


N = 6
polygonals = {}

for n in range(3, 3 + N):
    arr = []
    for x in polygonal_gen(n):
        if x >                                                         9999:
            break
        if 999 < x < 10000:
            arr.append(str(x))
    polygonals[n] = arr


def find_nums(exclude, num):
    global polygonals
    for n, v in polygonals.iteritems():
        if n == exclude:
            continue
        for x in v:
            if x[:2] == num[2:]:
                yield (x, n)


# create the graph
graph = {}
for n, nums in polygonals.iteritems():
    for num in nums:
        graph[(num, n)] = list(find_nums(n, num))


class Chain(object):

    def __init__(self, initial=[]):
        self.chain = []
        self.nums = set()
        self.polygon_types = set()

        for elem in initial:
            self.append(elem)

    def append(self, elem):
        v, n = elem
        if v in self.nums:
            raise ValueError
        if n in self.polygon_types:
            raise ValueError

        # addition check
        if self.chain and self.chain[-1][0][2:] != v[:2]:
            raise ValueError

        # too long
        if len(self.chain) + 1 > N:
            raise ValueError

        self.nums.add(v)
        self.polygon_types.add(n)
        self.chain.append(elem)

    def __len__(self):
        return len(self.chain)

    def __str__(self):
        return str(self.chain)

    def __getitem__(self, k):
        return self.chain[k]

    def sum(self):
        """returns the sum of the chain"""
        return sum(int(x) for x in self.nums)


def iter_dfs(G, start):
    S, Q = set(), []
    Q.append(start)
    while Q:
        u = Q.pop()
        if u in S:
            continue
        S.add(u)
        Q.extend(G[u])
        yield u


def euler61():
    for start in graph:
        path = Chain()
        for node in iter_dfs(graph, start):
            try:
                path.append(node)
            except ValueError:
                pass

        if len(path) == N:
            if path[-1][0][2:] == path[0][0][:2]:
                return path.sum()
