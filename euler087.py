import itertools
from utils import primes_gen


def euler87():
    upper = 50 * 10 ** 6
    squares = [x ** 2 for x in primes_gen(int(upper ** (1.0 / 2)))]
    cubes = [x ** 3 for x in primes_gen(int(upper ** (1.0 / 3)))]
    quads = [x ** 4 for x in primes_gen(int(upper ** (1.0 / 4)))]

    ret = set()
    for a, b, c in itertools.prod(squares, cubes, quads):
        res = a + b + c
        if res < upper:
            ret.add(res)
    return len(ret)
