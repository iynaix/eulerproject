from path_sums import Grid, dijkstra


GRID = [
    [131, 673, 234, 103, 18],
    [201, 96, 342, 965, 150],
    [630, 803, 746, 422, 111],
    [537, 699, 497, 121, 956],
    [805, 732, 524, 37, 331],
]


class Grid4(Grid):
    def get_next_steps(self, x, y):
        """
        returns a dict of {(x coord, y corrd): value,} of the steps can be
        taken given the current coords
        """
        ret = {}
        #down
        if y + 1 < self.height:
            ret[(x, y + 1)] = self.cell(x, y + 1)
        #up
        if y - 1 >= 0:
            ret[(x, y - 1)] = self.cell(x, y - 1)
        #right
        if x + 1 < self.width:
            ret[(x + 1, y)] = self.cell(x + 1, y)
        #left
        if x - 1 >= 0:
            ret[(x - 1, y)] = self.cell(x - 1, y)
        return ret


def euler83():
    grid = Grid4("matrix83.txt")

    start = (0, 0)
    end = (grid.width - 1, grid.height - 1)
    path_sums = dijkstra(grid.graph, start)

    #dijkstra calculates the distance from the starting cell to every
    #other cell
    return grid.cell(*start) + dijkstra(grid.graph, start)[end]

print euler83()
