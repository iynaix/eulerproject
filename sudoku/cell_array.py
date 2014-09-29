from collections import defaultdict
from itertools import combinations
from cell import SudokuCell
from utils import intersection

class SudokuCellArray(object):
    """A collection of sudoku cells"""

    cells = []

    def __init__(self, arr=[], **kwargs):
        #set any extra attributes that are provided
        for k , v in kwargs.iteritems():
            setattr(self, k, v)

        if arr:
            self.cells = list(sorted(arr))

    def __iter__(self):
        return self.cells.__iter__()

    def __getitem__(self, idx):
        return self.cells.__getitem__(idx)

    def __repr__(self):
        out = ""

        attrs = self.__dict__.copy()
        attrs.pop("cells")

        if attrs.pop("digit", None) is not None:
            out = "DIGIT: %s " % self.digit
        elif attrs.pop("digits", None) is not None:
            out = "DIGITS: %s " % self.digits

        out += "(%s)" % (", ".join([c.cand_str for c in self.cells]), )

        #print out all the extra params
        if attrs:
            out += " %s" % attrs
        return out

    def __len__(self):
        return len(self.cells)

    def __add__(self, other):
        #another sudoku cell array, take the union
        if isinstance(other, SudokuCellArray):
            return SudokuCellArray(set(self.cells).union(other.cells))

    def __sub__(self, other):
        #remove the given sudoku cell from the list
        if isinstance(other, SudokuCell):
            try:
                self.cells.remove(other)
                return SudokuCellArray(self.cells)
            except ValueError:
                #not found in current collection, just return
                return self
        #remove all the given sudoku cells from the list
        elif isinstance(other, SudokuCellArray):
            return SudokuCellArray(set(self.cells).difference(other.cells))

        #remove the values from the cells
        elif isinstance(other, (int, list, set)):
            for c in self.cells:
                c = c - other
            return self

    def __contains__(self, other):
        if isinstance(other, SudokuCell):
            return self.cells.__contains__(other)

    @property
    def cands(self):
        cands = []
        for c in self.cells:
            cands += c.cands
        return sorted(list(set(cands)))

    @property
    def cands_intersection(self):
        cands = [c.cands for c in self.cells]
        return intersection(*cands)

    @property
    def rows(self):
        """returns a list of the row numbers for the cells"""
        return [c.row for c in self.cells]

    @property
    def cols(self):
        """returns a list of the col numbers for the cells"""
        return [c.col for c in self.cells]

    @property
    def boxes(self):
        """returns a list of the boxes numbers for the cells"""
        return [c.box for c in self.cells]

    def cands_dict(self):
        """
        returns a dictionary with the candidates as keys and a list of cells
        with only those candidates as the value
        """
        ret = defaultdict(list)
        for c in self.cells:
            ret[c.cand_str].append(c)
        return ret

    def filter(self, **kw):
        """
        post processes the result, possibly filtering it somemore
            singles: keep the singles, default is False
            length: django style syntax for filtering, supports lt, lte, gt
                    and gte
            digits: filter by a digit or list of digits
            row, box, col: filters by matching row, box or col
            func: filter by a callable that returns a boolean
        """
        coll = self.cells

        #filter out the singles if needed
        singles = kw.pop("singles", False)
        if not singles:
            coll = [x for x in coll if len(x) > 1]

        #filter by length, django style
        if "length" in kw:
            coll = [x for x in coll if len(x) == kw["length"]]
        if "length__lt" in kw:
            coll = [x for x in coll if len(x) < kw["length__lt"]]
        if "length__lte" in kw:
            coll = [x for x in coll if len(x) <= kw["length__lte"]]
        if "length__gt" in kw:
            coll = [x for x in coll if len(x) > kw["length__gt"]]
        if "length__gte" in kw:
            coll = [x for x in coll if len(x) >= kw["length__gte"]]

        #filter by digits
        digits = kw.pop("digits", None)
        if digits is not None:
            coll = [x for x in coll if digits in x]

        #filter by row, box or col
        if "row" in kw:
            coll = [x for x in coll if x.col == kw["row"]]
        if "col" in kw:
            coll = [x for x in coll if x.col == kw["col"]]
        if "box" in kw:
            coll = [x for x in coll if x.col == kw["box"]]

        #filter by a function
        func = kw.pop("func", None)
        if func is not None:
            coll = [x for x in coll if func(x)]

        return SudokuCellArray(coll)

    def iter_related(self, inclusive=False, **kwargs):
        """
        returns all the cells that are shared amongst all the cells in this
        collection
        inclusive determines if the cell itself is included
        """
        if not len(self):
            return SudokuCellArray()

        cells = [c.iter_related() for c in self.cells]
        related = SudokuCellArray(intersection(*cells))
        if not inclusive:
            related -= c
        return SudokuCellArray(related).filter(**kwargs)

    def combinations(self, n):
        """
        returns all combinations of size n
        """
        if n > len(self):
            return []
        elif n == len(self):
            return [self]
        else:
            return [SudokuCellArray(x) for x in combinations(self.cells, n)]

    def intersection(self, *others):
        """
        returns the intersection of cells between the this cell array and the
        given arrays
        """
        others = [self.cells] + [c.cells for c in others]
        return SudokuCellArray(intersection(*others))

    def _is_same(self, func):
        """
        utility function that checks if all the cells return the same value
        when passed through the function
        """
        return len(set([func(c) for c in self.cells])) == 1

    def is_same_row(self):
        """are all the cells in the same row?"""
        return self._is_same(lambda c: c.row)

    def is_same_col(self):
        """are all the cells in the same col?"""
        return self._is_same(lambda c: c.col)

    def is_same_box(self):
        """are all the cells in the same box?"""
        return self._is_same(lambda c: c.box)

    def is_rect(self):
        """
        do the cells form a rectangle?
        a rectangle can have only 3 points specified
        """

        #too little vertices
        if len(self) < 3 or len(self) > 4:
            return False

        return len(set(self.rows)) == 2 and len(set(self.cols)) == 2
