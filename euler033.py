from fractions import Fraction
from utils import digits


def euler33():
    ret = 1
    for a in range(10, 100):
        for b in range(a + 1, 100):
            f = Fraction(a, b)
            d_a = set(digits(a))
            d_b = set(digits(b))
            intersect = d_a & d_b
            if len(intersect) == 1 and list(intersect) != [0]:
                try:
                    if Fraction(list(d_a - d_b)[0],
                                list(d_b - d_a)[0]) == f:
                        ret *= f
                except:
                    pass
    return ret.denominator
