from path_sums import Grid, dijkstra


GRID = [
    [131, 673, 234, 103, 18],
    [201, 96, 342, 965, 150],
    [630, 803, 746, 422, 111],
    [537, 699, 497, 121, 956],
    [805, 732, 524, 37, 331],
]


class Grid3(Grid):
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
        #up
        if y - 1 >= 0:
            ret[(x, y - 1)] = self.cell(x, y - 1)
        return ret


def euler82():
    grid = Grid3("matrix81.txt")

    ret = float('inf')
    for start_y in range(grid.height):
        start = (0, start_y)
        path_sums = dijkstra(grid.graph, start)

        #dijkstra calculates the distance from the starting cell to every
        #other cell
        #we filter out the endpoints on the far right
        path_sums = [grid.cell(*start) + distance
                     for node, distance in
                     dijkstra(grid.graph, start).iteritems()
                     if node[0] == grid.width - 1]
        ret = min(ret, min(path_sums))
    return ret
