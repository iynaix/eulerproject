from utils import is_triangular, is_pentagonal


def euler45():
    n = 2
    while True:
        x = n * (2 * n - 1)
        if is_triangular(x) and is_pentagonal(x) and n != 143:
            return x
        n += 1
