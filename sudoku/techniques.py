import re
import itertools
from cell_array import SudokuCellArray

class Technique(object):
    """
    Implements the basic structure of a technique

    Executes steps in this order:
        1. gets the possible sets
        2. filters out the valid sets using a callable
        3. applies the relevant elimination
    """
    min_set_length = 2
    max_set_length = 9
    debug = False

    def __init__(self, sudoku):
        self.sudoku = sudoku
        self.sudoku.current_technique = self.name

        #set should be larger than 1
        possible_sets = []
        for x in self.get_possible_sets():
            if self.min_set_length <= len(x) <= self.max_set_length:
                possible_sets.append(x)
        possible_sets = set(possible_sets)

        #no matches, don't bother continuing
        if not possible_sets:
            return

        if self.debug:
            print self.name
            print "POSSIBLE SETS"
            for x in possible_sets:
                print x
            print

        #filter out only the valid sets
        filtered_sets = []
        for x in possible_sets:
            if self.is_valid_set(x):
                filtered_sets.append(x)
        if self.debug:
            print "FILTERED SETS"
            for x in filtered_sets:
                print x

        #perform the necessary elimination
        for s in filtered_sets:
            self.eliminate(s)

    @property
    def name(self):
        return re.sub(r"([A-Z0-9])([a-z])", r" \1\2",
                      self.__class__.__name__).strip()

    def get_possible_sets(self):
        """
        returns all the sets that could possibly comtain the solving technique
        """
        return self.sudoku.iter_all()

    def is_valid_set(self, s):
        """
        returns a boolean on whether the set is a valid set
        """
        return True

    def eliminate(self, s):
        """
        performs whatever elimination the needs to be done on the sudoku
        given the set
        """
        pass


class HiddenSingles(Technique):
    score = 14
    min_set_length = 1

    def get_possible_sets(self):
        ret = []
        for coll in self.sudoku.iter_all():
            for i in range(1, 10):
                tmp = coll.filter(digits=i)
                if len(tmp) == 1:
                    tmp.digit = i
                    ret.append(tmp)
        return ret

    def eliminate(self, s):
        s[0].cands = s.digit


class NakedSet(Technique):
    """Solves for naked sets, where n is the size of the naked set"""
    n = 2

    def get_possible_sets(self):
        ret = []

        for coll in self.sudoku.iter_all(length__lte=self.n):
            #get all the cells with n or less candidates and
            #get all the possible combinations
            ret.extend(coll.combinations(self.n))
        return ret

    def is_valid_set(self, s):
        return len(s.cands) == self.n

    def eliminate(self, s):
        s.iter_related() - s.cands


class NakedPair(NakedSet):
    n = 2
    score = 40



class NakedTriple(NakedSet):
    n = 3
    score = 60



class NakedQuad(NakedSet):
    n = 4
    score = 120



class HiddenSet(NakedSet):
    """Solves for hidden sets, where n is the size of the hidden set"""
    def __init__(self, sudoku, **kwargs):
        #hidden sets are the 9-complements of naked sets
        self.n = 9 - self.n
        super(HiddenSet, self).__init__(sudoku, **kwargs)


class HiddenPair(HiddenSet):
    n = 2
    score = 70


class HiddenTriple(HiddenSet):
    n = 3
    score = 100


class HiddenQuad(HiddenSet):
    n = 4
    score = 150


class PointingCandidates(Technique):
    score = 50

    """Solves for pointing candidates (aka box-line reduction)"""
    def get_possible_sets(self):
        ret = []

        #loop over the rows and cols, and store the set for each digit
        for i in range(1, 10):
            for box in self.sudoku.iter_box(digits=i):
                if len(box) == 2 or len(box) == 3:
                    box.digit = i
                    ret.append(box)
        return ret

    def is_valid_set(self, s):
        if s.is_same_row():
            s.same = "row"
            return True
        if s.is_same_col():
            s.same = "col"
            return True
        return False

    def eliminate(self, s):
        (getattr(s[0], "iter_" + s.same)() - s) - s.digit


class LockedCandidates(Technique):
    """Solves for locked candidates (aka box-line reduction)"""
    score = 50

    def get_possible_sets(self):
        ret = []

        #loop over the rows and cols, and store the set for each digit
        for i in range(1, 10):
            for box in self.sudoku.iter_rowcol(digits=i):
                if len(box) == 2 or len(box) == 3:
                    box.digit = i
                    ret.append(box)
        return ret

    def is_valid_set(self, s):
        return s.is_same_box()

    def eliminate(self, s):
        (s[0].iter_box() - s) - s.digit


class StandardFish(Technique):
    """Solves generic standard fish, where n is the size of the fish"""
    n = 2

    def get_possible_sets(self):
        ret = []
        for i in range(1, 10):
            #only accept rows / cols which have >=2 cells with the digit
            row_coll = []
            for r in self.sudoku.iter_row():
                tmp = r.filter(digits=i)
                if 2 <= len(tmp) <= self.n:
                    row_coll.append(tmp)
            for coll in itertools.combinations(row_coll, self.n):
                #merge the cell arrays into 1
                tmp = coll[0]
                for c in coll[1:]:
                    tmp += c
                tmp.digit = i
                ret.append(tmp)

            col_coll = []
            for r in self.sudoku.iter_col():
                tmp = r.filter(digits=i)
                if 2 <= len(tmp) <= self.n:
                    col_coll.append(tmp)
            for coll in itertools.combinations(col_coll, self.n):
                #merge the cell arrays into 1
                tmp = coll[0]
                for c in coll[1:]:
                    tmp += c
                tmp.digit = i
                ret.append(tmp)
        return ret

    def is_valid_set(self, s):
        return len(set(s.rows)) == self.n and len(set(s.cols)) == self.n

    def eliminate(self, s):
        #remove everything else that is from the other rows and columns
        related = SudokuCellArray()
        for rowno in set(s.rows):
            related += self.sudoku.row(rowno)
        for colno in set(s.cols):
            related += self.sudoku.col(colno)
        related -= s

        related - s.digit


class XWing(StandardFish):
    n = 2
    score = 140


class Swordfish(StandardFish):
    n = 3
    score = 150


class Jellyfish(StandardFish):
    n = 4
    score = 160


class UniqueRectangle1(Technique):
    """Solves for unique rectangle type 1, aka 'Unique Corner'"""
    doubles_len = 3
    score = 100

    def get_possible_sets(self):
        #gets all the possible rectangles
        ret = []
        rows = [r.combinations(2) for r in self.sudoku.iter_row()
                if len(r) >= 2]
        for rowno, row in enumerate(rows):
            #set the top 2 vertices, then try getting the other 2
            for coll in row:
                for other_row in rows[rowno+1:]:
                    for other_coll in other_row:
                        vertices = coll + other_coll
                        #vertices cannot be in the same box
                        if vertices.is_rect() and not vertices.is_same_box() \
                           and len(vertices.cands_intersection) == 2:
                            ret.append(vertices)

        #further filtering based on the double candidate cells in the rect
        ret1 = []
        for coll in ret:
            doubles = coll.filter(length=2)
            if len(doubles) != self.doubles_len:
                continue
            if len(doubles.cands_intersection) != 2:
                continue
            #store the doubles
            coll.doubles = doubles
            #store the cells other than doubles
            coll.others = coll - doubles
            ret1.append(coll)

        return ret1

    def eliminate(self, s):
        s.others - s.cands_intersection


class UniqueRectangle2(UniqueRectangle1):
    """Solves for unique rectangle type 2, aka 'Unique Side'"""
    doubles_len = 2
    score = 100

    def is_valid_set(self, s):
        return (s.doubles.is_same_row() or s.doubles.is_same_col()) and \
                len(s.cands) == 3 and len(s.others.cands_intersection) == 2

    def eliminate(self, s):
        #get the digit to eliminate
        digit = set(s.cands).difference(s.doubles.cands).pop()
        s.others.iter_related() - digit


class UniqueRectangle3(UniqueRectangle2):
    """Solves for unique rectangle type 3, aka 'Unique Subset'"""
    score = 100

    def is_valid_set(self, s):
        return (s.doubles.is_same_row() or s.doubles.is_same_col()) and \
                len(s.cands) > 3 and len(s.others.cands_intersection) >= 2

    def eliminate(self, s):
        #get the extra candidates
        extra_cands = set(s.cands).difference(s.doubles.cands)

        #get the rest of the cells within that row or column
        if s.others.is_same_row():
            rest = s.others.iter_related(row=s.others[0].row)
        else:
            rest = s.others.iter_related(col=s.others[0].col)

        #start searching for a "naked" subset
        #calculate the number of cells we need to extract and get the
        #combinations
        for coll in rest.combinations(len(extra_cands) + 1 - 2):
            if len(extra_cands.union(coll.cands)) == len(extra_cands):
                rest -= coll
                break
        else:
            return

        #finally remove extra candidates
        rest - extra_cands


class UniqueRectangle4(UniqueRectangle3):
    """Solves for unique rectangle type 4, aka 'Unique Pair'"""
    score = 100

    def eliminate(self, s):
        #get the extra candidates
        cands = list(s.cands_intersection)

        #get the rest of the cells within that row or column
        if s.others.is_same_row():
            rest = s.others.iter_related(row=s.others[0].row)
        else:
            rest = s.others.iter_related(col=s.others[0].col)

        #only one of candidates should have other matches
        cand_matches1 = len(rest.filter(digits=cands[0])) == 0
        cand_matches2 = len(rest.filter(digits=cands[1])) == 0
        if cand_matches1 and not cand_matches2:
            s.others - cands[1]
        elif not cand_matches1 and cand_matches2:
            s.others - cands[0]
        else:
            return


class UniqueRectangle5(UniqueRectangle1):
    """Solves for unique rectangle type 5"""
    doubles_len = 1
    score = 100

    def is_valid_set(self, s):
        return len(s.cands) == 3

    def eliminate(self, s):
        digit = set(s.cands).difference(s.cands_intersection).pop()
        s.others.iter_related() - digit


class UniqueRectangle6(UniqueRectangle1):
    """Solves for unique rectangle type 6"""
    doubles_len = 2
    score = 100

    def is_valid_set(self, s):
        #doubles should be diagonal
        return (not s.doubles.is_same_row() and not s.doubles.is_same_col()) \
                and len(s.cands) > 3 and len(s.others.cands_intersection) == 2

    def eliminate(self, s):
        #find out which candidate is responsible for the x wing
        digit = None
        for cand in s.cands_intersection:
            if len(self.sudoku.iter_cells(digits=cand)) == 4:
                digit = cand
                break

        if not digit:
            return

        #eliminate the candidate from others
        s.others - digit


class BUG(Technique):
    """Solves for BUG +1 (Bivalue Universal Graves)"""
    min_set_length = 1
    score = 100

    def get_possible_sets(self):
        #get all the multivalued cells
        cells = self.sudoku.iter_cells()
        multivalue_cells = cells.filter(length__gt=2)
        if len(multivalue_cells) == 1:
            return [multivalue_cells]
        return []

    def eliminate(self, s):
        digit = None
        for c in s.cands:

            if len(s[0].iter_row(inclusive=True, digits=c)) == 3 \
                and len(s[0].iter_col(inclusive=True, digits=c)) == 3 \
                and len(s[0].iter_box(inclusive=True, digits=c)) == 3:
                digit = c
                break

        if digit is None:
            return

        #set the digit to the cell
        s[0].cands = digit


class XYWing(Technique):
    """Solves for XY wings"""
    score = 160

    def get_possible_sets(self):
        ret = []
        #get all the cells with 2 digits
        for pivot in self.sudoku.iter_cells(length=2):
            #search the column and row of the pivot for possible pairs
            for pincers in pivot.iter_related(length=2).combinations(2):
                pincers_intersection = pincers.cands_intersection
                if len(pincers_intersection) != 1:
                    continue
                tmp = SudokuCellArray(pincers.cells + [pivot])
                #store the pincers and the pivot candidate
                tmp.pincers = pincers
                tmp.digit = pincers_intersection.pop()
                ret.append(tmp)
        return ret

    def is_valid_set(self, s):
        if len(s) != 3:
            return False
        if s.is_same_row() or s.is_same_col() or s.is_same_box():
            return False
        if len(s.cands) != 3:
            return False
        #all 3 cells should have different candidates
        if len(s.cands_intersection) != 0:
            return False
        return True

    def eliminate(self, s):
        s.pincers.iter_related() - s.digit


class XYZWing(Technique):
    """Solves for XYZ wings"""
    score = 180

    def get_possible_sets(self):
        ret = []
        #look for the 3 digit pivots
        for pivot in self.sudoku.iter_cells(length=3):
            #look for the pincers
            for pincers in pivot.iter_related(length=2).combinations(2):
                pincers_intersection = pincers.cands_intersection
                if len(pincers_intersection) != 1:
                    continue
                tmp = SudokuCellArray(pincers.cells + [pivot])
                #store the pincers and the pivot candidate
                tmp.pincers = pincers
                tmp.digit = pincers_intersection.pop()
                ret.append(tmp)
        return ret

    def is_valid_set(self, s):
        if len(s) != 3:
            return False
        if s.is_same_row() or s.is_same_col() or s.is_same_box():
            return False
        if len(s.cands) != 3:
            return False
        if len(s.cands_intersection) != 1:
            return False
        return True

    def eliminate(self, s):
        s.iter_related() - s.digit


class WXYZWing(Technique):
    """Solves for WXYZ wings"""
    score = 200

    def get_possible_sets(self):
        ret = []
        #look for the 3 digit pivots
        for pivot in self.sudoku.iter_cells(length__gte=3, length__lte=4):
            #look for the pincers
            for pincers in pivot.iter_related(length=2).combinations(3):
                pincers_intersection = pincers.cands_intersection
                if len(pincers_intersection) != 1:
                    continue
                tmp = SudokuCellArray(pincers.cells + [pivot])
                #store the pincers and the pivot candidate
                tmp.pincers = pincers
                tmp.digit = pincers_intersection.pop()
                ret.append(tmp)
        return ret

    def is_valid_set(self, s):
        if len(s) != 4:
            return False
        if s.is_same_row() or s.is_same_col() or s.is_same_box():
            return False
        if len(s.cands) != 4:
            return False
        if len(s.cands_intersection) != 1:
            return False
        return True

    def eliminate(self, s):
        s.iter_related() - s.digit


class WWing(Technique):
    """Solves for W wings (not to be confused with WXYZ Wings)"""
    score = 150

    def get_possible_sets(self):
        ret = []
        for pair in self.sudoku.iter_strong_links():
            #search for a bivalue cell on each side of the pair
             edge1 = pair[0].iter_related(length=2, digits=pair.digit)
             edge2 = pair[1].iter_related(length=2, digits=pair.digit)
             if edge1 and edge2:
                #try every possible combination from both sets
                for vertices in list(itertools.product(edge1, edge2)):
                    if vertices[0].cands == vertices[1].cands:
                        tmp = SudokuCellArray(list(vertices) + pair.cells)
                        d = vertices[0].cands[:]
                        d.remove(pair.digit)
                        tmp.digit = d[0]
                        tmp.edges = SudokuCellArray(vertices)
                        ret.append(tmp)
        return ret

    def is_valid_set(self, s):
        return (not s.edges.is_same_row() and not s.edges.is_same_col() \
                and not s.edges.is_same_box()) and len(s) == 4

    def eliminate(self, s):
        s.edges.iter_related() - s.digit
