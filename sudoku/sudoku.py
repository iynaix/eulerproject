# sudoku.py
import techniques as solving_techniques
from cell import SudokuCell
from cell_array import SudokuCellArray

class Sudoku(object):
    #stores the current solving technique being used
    current_technique = None

    def __init__(self, givens=None):
        #init the cells (1d array to empty)
        self.cells  = []
        for i in range(81):
            self.cells.append(SudokuCell(i, self))

        if not givens:
            return

        if len(givens) == 81:
            self.from_givens(givens)

        else:
            raise NotImplementedError

        self.prune_singles()

    def from_givens(self, givens):
        #create the cells one at a time
        for idx, char in enumerate(givens):
            if char not in (".", "*", "0", " "):
                self.cells[idx].cands = int(char)
                self.cells[idx].is_given = True


    def techniques(self, **kwargs):
        """
        returns a list of sudoku techniques, takes a couple of keyword args:
            fishes: boolean on whether to include fishes (default True)
            wings: boolean on whether to include wings (default True)
            uniqueness: boolean on whether to include fishes (default True)
            excludes: list of methods to exclude
        """

        #basic techniques
        ret = [
            "HiddenSingles",
            "NakedPair",
            "NakedTriple",
            "HiddenPair",
            "HiddenTriple",
            "NakedQuad",
            "HiddenQuad",
            "PointingCandidates",
            "LockedCandidates",
        ]

        if kwargs.get("fishes", True):
            ret += [
                "XWing",
                "Swordfish",
                "Jellyfish",
            ]

        if kwargs.get("wings", True):
            ret += [
                "WWing",
                "XYWing",
                "XYZWing",
                "WXYZWing",
            ]

        if kwargs.get("uniqueness", True):
            ret += [
                "UniqueRectangle1",
                "UniqueRectangle2",
                "UniqueRectangle3",
                "UniqueRectangle4",
                "UniqueRectangle5",
                "UniqueRectangle6",
                "BUG",
            ]

        #remove any methods to exclude
        for x in kwargs.get("excludes", []):
            ret.remove(x)
        return ret

    @property
    def state(self):
        return [c.cands for c in self.cells][:]

    def __repr__(self):
        def pad_spaces(s, length):
            """right pads the given string to the given length"""
            return s + " " * (length - len(s))

        #what is the max number of candidates for each column?
        max_col_widths = [max([len(cell) for cell in col]) \
                          for col in self.iter_col(singles=True)]

        row_strs = []
        for row in self.iter_row(singles=True):
            new_row = []
            for c in row:
                new_row.append(pad_spaces(c.cand_str,
                                          max_col_widths[c.col - 1]))
            row_strs.append("| {} {} {} | {} {} {} | {} {} {} |".format(
                            *new_row))

        blank_row = ["-" * len(row_strs[0])]
        out = [''] + blank_row + row_strs[:3] + blank_row + row_strs[3:6] + \
                blank_row + row_strs[6:] + blank_row
        return "\n".join(out)

    def __eq__(self, other):
        return self.state == other.state

    def __getitem__(self, idx):
        if isinstance(idx, int):
            return self.cells[idx]
        elif isinstance(idx, tuple):
            #x, y coordinates, convert to straight indexing
            return self.cells[(idx[1] -1) * 9 - 1 + idx[0]]

    def iter_cells(self, **kwargs):
        """returns an iterator across the cells of the sudoku"""
        return SudokuCellArray(self.cells).filter(**kwargs)

    def row(self, colno, **kwargs):
        """returns the given col, where the col no is from 1-9"""
        return SudokuCellArray([self[(rowno, colno)] for rowno in \
                                range(1, 10)]).filter(**kwargs)

    def iter_row(self, **kwargs):
        """returns an iterator across the rows of the sudoku"""
        return [self.row(rowno, **kwargs) for rowno in range(1, 10)]

    def col(self, rowno, **kwargs):
        """returns the given row, where the row no is from 1-9"""
        return SudokuCellArray([self[(rowno, colno)] for colno in \
                                range(1, 10)]).filter(**kwargs)

    def iter_col(self, **kwargs):
        """returns an iterator across the cols of the sudoku"""
        return [self.col(colno, **kwargs) for colno in range(1, 10)]

    def box(self, boxno, **kwargs):
        """returns the given box, where the box no is from 1-9"""
        start_cells = [0, 3, 6, 27, 30, 33, 54, 57, 60]
        start = start_cells[boxno - 1]

        idxs = range(start, start + 3) + range(start + 9, start + 12) +\
            range(start + 18, start + 21)
        return SudokuCellArray([self[i] for i in idxs]).filter(**kwargs)

    def iter_box(self, **kwargs):
        """returns an iterator across the cols of the sudoku"""
        return [self.box(boxno).filter(**kwargs) for boxno in range(1, 10)]

    def iter_rowcol(self, **kwargs):
        """iterates over the rows then cols"""
        return self.iter_row(**kwargs) + self.iter_col(**kwargs)

    def iter_all(self, **kwargs):
        """iterates over the rows, then cols, then boxes"""
        return self.iter_rowcol(**kwargs) + self.iter_box(**kwargs)

    def iter_strong_links(self):
        """iterates over all the strong links for the sudoku"""

        ret = []
        for i in range(1, 10):
            for coll in self.iter_all(digits=i):
                if len(coll) == 2:
                    coll.digit = i
                    ret.append(coll)
        return ret


    def is_solved(self):
        """returns if the puzzle has been completely solved"""
        if sum([len(c) for c in self.cells]) == 81:
            if not self.is_valid():
                print self
                raise ValueError("Sudoku is not valid!")
            return True
        return False

    def is_valid(self):
        #checks if the sudoku is valid
        #looks through all the singles, looking for repeats
        for coll in self.iter_all(singles=True, length=1):
            singles = set([c.cands[0] for c in coll])
            if len(singles) != len(coll):
                return False
        return True

    def prune_singles(self):
        """
        prunes away all the singles from the candidates
        """
        while 1:
            old_state = self.state
            for c in self.iter_cells(singles=True, length=1):
                for x in c.iter_related():
                    x - c.cands[0]
            if self.state == old_state:
                break

    def solve(self, *args, **kwargs):
        """
        solves the sudoku via logic
        args can be a string representing the most advanced method to use or
        None to use all methods (default)
        kwargs is passed directly through to methods
        """

        techniques = self.techniques(**kwargs)
        if args:
            mtds = techniques[:techniques.index(args[0]) + 1]
        else:
            mtds = techniques

        i = 0
        while i < len(mtds):
            self.prune_singles()

            old_state = self.state
            mtd = getattr(solving_techniques, mtds[i])
            mtd(self)

            if self.is_solved():
                return
            if self.state == old_state:
                i += 1
            else:
                i = 0


if __name__ == "__main__":
    givens = "6..95..7...9.2.....58.31...164389752...175946597246..8925417683...562.....6893..."

    sd = Sudoku(givens)
    sd.solve("WWing")

    print sd
