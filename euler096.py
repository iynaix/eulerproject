from sudoku.sudoku import Sudoku


def chunks(l, n):
    """ Yield successive n-sized chunks from l."""
    for i in xrange(0, len(l), n):
        yield l[i:i + n]


def load_sudokus():
    with open("sudoku96.txt") as fp:
        lines = fp.readlines()

    sudokus = []
    for block in chunks(lines, 10):
        block = ''.join(l.strip() for l in block[1:])
        sudokus.append(Sudoku(block))
    return sudokus


def euler96():
    ret = 0
    for puzzle in load_sudokus():
        puzzle.solve()
        ret += int(''.join(str(cell) for cell in puzzle.cells[:3]))
    return ret
