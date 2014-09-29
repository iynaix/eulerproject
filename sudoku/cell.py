class SudokuCell(object):
    _cands = range(1, 10)

    def __init__(self, idx, sudoku, is_given=False, cands=None, notify=False):
        """sudoku is a pointer to the parent sudoku object"""
        self.sudoku = sudoku
        self.idx = idx
        self.is_given = is_given

        self.row = idx // 9 + 1
        self.col = idx % 9 + 1
        self.box = ((idx % 9) // 3) + 3 * (idx // 9 // 3) + 1

        #used for debugging purposes
        self.notify = notify

        if cands is not None:
            self.cands = cands

    def get_cands(self):
        return self._cands

    def set_cands(self, cands):
        if isinstance(cands, list):
            self._cands = cands
        elif isinstance(cands, int):
            self._cands = [cands]

    cands = property(get_cands, set_cands)

    def __len__(self):
        return len(self.cands)

    def __repr__(self):
        return self.cand_str

    @property
    def rc(self):
        return "R%sC%s" % (self.row, self.col)

    @property
    def coord(self):
        return "(%s, %s)" % (self.row, self.col)

    @property
    def cand_str(self):
        """returns the candidates as a simple string"""
        return "".join([str(x) for x in self.cands])

    def debug(self):
        #pretty printing with coordinates for debugging purposes
        return "(%s, %s) %s" % (self.row, self.col, repr(self))

    def __cmp__(self, other):
        #gives weight to the row, followed by the column
        return cmp(self.row * 10 + self.col, other.row * 10 + other.col)

    def iter_row(self, inclusive=False, **kwargs):
        """
        returns all the cells in the same row, without the current cell
        inclusive determines if the cell itself is included
        """
        ret = self.sudoku.row(self.row, **kwargs)
        if not inclusive:
            ret -= self
        return ret

    def iter_col(self, inclusive=False, **kwargs):
        """
        returns all the cells in the same col, without the current cell
        inclusive determines if the cell itself is included
        """
        ret = self.sudoku.col(self.col, **kwargs)
        if not inclusive:
            ret -= self
        return ret

    def iter_box(self, inclusive=False, **kwargs):
        """
        returns all the cells in the same box, without the current cell
        inclusive determines if the cell itself is included
        """
        ret = self.sudoku.box(self.box, **kwargs)
        if not inclusive:
            ret -= self
        return ret

    def iter_rowcol(self, inclusive=False, **kwargs):
        """
        returns all the cells in the same row or col, without the current cell
        inclusive determines if the cell itself is included
        """
        ret = self.sudoku.row(self.row, **kwargs) + \
                self.sudoku.col(self.col, **kwargs)
        if not inclusive:
            ret -= self
        return ret

    def iter_related(self, inclusive=False, **kwargs):
        """
        returns all the cells in the same row, col or box, without the current
        cell
        inclusive determines if the cell itself is included
        """
        ret = self.sudoku.row(self.row, **kwargs) + \
               self.sudoku.col(self.col, **kwargs) + \
               self.sudoku.box(self.box, **kwargs)
        if not inclusive:
            ret -= self
        return ret

    def _remove_cand(self, x):
        #removes a single candidate
        if len(self) > 1:
            try:
                new_cands = self.cands[:]
                new_cands.remove(x)

                #print a notification
                if self.notify:
                    print "%s: Removes %s from %s" % \
                        (self.sudoku.current_technique, x, self.rc)

                self.cands = new_cands
            except ValueError:
                #not found, do nothing
                pass

    def __sub__(self, other):
        #single digit, subtract the digit from the candidates
        if isinstance(other, int):
            self._remove_cand(other)
        #list of digits, subtract all the digits from the candidates
        elif isinstance(other, (list, set)):
            for x in other:
                self._remove_cand(x)

    def __contains__(self, x):
        #single digit
        if isinstance(x, int):
            return x in self.cands
        #list of digits
        elif isinstance(x, list):
            return all([(a in self.cands) for a in x])
