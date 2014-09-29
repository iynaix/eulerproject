import itertools
from utils import from_digits


def euler24():
    for i, x in enumerate(itertools.permutations(range(0, 10), 10)):
        if i == 1000000 - 1:
            return from_digits(x)
