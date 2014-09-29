from path_sums import Grid, shortest_path_dag


GRID = [
    [131, 673, 234, 103, 18],
    [201, 96, 342, 965, 150],
    [630, 803, 746, 422, 111],
    [537, 699, 497, 121, 956],
    [805, 732, 524, 37, 331],
]


def euler81():
    grid = Grid("matrix81.txt")
    return shortest_path_dag(grid.graph,
                             (0, 0),
                             (grid.width - 1, grid.height - 1),
                             grid.cell(0, 0))
