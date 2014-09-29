import itertools
from utils import memoize
from sympy import primerange, isprime


def gen_triplet_paths():
    def neighbours(start_x, start_y):
        for x in (-1, 0, 1):
            for y in (-1, 0, 1):
                if x == 0 and y == 0:
                    continue
                yield (start_x + x, start_y + y)

    for cell in neighbours(0, 0):
        for cell2 in neighbours(*cell):
            if cell2 == (0, 0):
                continue
            if cell == (-1, 0):
                continue
            if cell == (1, 0):
                continue
            yield cell[0], cell[1], cell2[0], cell2[1]

    cells = list(neighbours(0, 0))
    cells.remove((-1, 0))
    cells.remove((1, 0))
    for cell, cell2 in itertools.combinations(cells, 2):
        yield cell[0], cell[1], cell2[0], cell2[1]

TRIPLET_PATHS = list(gen_triplet_paths())


@memoize
def grid(x, y):
    if x < 0 and y < 1:
        raise IndexError
    #exceed row length
    if x >= y:
        raise IndexError
    n = (2 - y + y * y) / 2 + x
    if not isprime(n):
        raise IndexError
    return n


def are_primes(x1, y1, x2, y2):
    """
    checks if the given 2 sets of coordinates result in both prime numbers
    """
    try:
        grid(x1, y1)
        grid(x2, y2)
    except:
        return False
    return True


def is_prime_triplet(x, y):
    """
    returns if the given cell coordinates are part of a prime triplet,
    assuming the current cell is prime
    """
    for coords in TRIPLET_PATHS:
        try:
            res = are_primes(x + coords[0],
                             y + coords[1],
                             x + coords[2],
                             y + coords[3])
        except IndexError:
            pass
        if res:
            return True
    return False


def S(n):
    """return sum of triplet primes in the row"""

    ret = 0
    #yields the primes and their coordinates
    start = (2 - n + n * n) / 2
    for pr in primerange(start, start + n):
        #coordinates of the prime are (pr - start, n)
        if is_prime_triplet(pr - start, n):
            ret += pr
    return ret


def euler196():
    return S(5678027) + S(7208785)
