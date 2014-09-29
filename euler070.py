from sympy import totient
from utils import is_permutation, pmaprange


def euler70():
    def min_totient_ratio(arr):
        ret, min_ratio = 0, 1000
        for n in arr:
            t = totient(n)
            if is_permutation(n, t):
                ratio = n * 1.0 / t
                if ratio < min_ratio:
                    min_ratio = ratio
                    ret = n
        return min_ratio, ret

    return min(pmaprange(min_totient_ratio, range(2, 10 ** 7)))[-1]
