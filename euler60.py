import itertools
from sympy import isprime, primerange
from utils import memoize, combination


@memoize
def isprimepair(a, b):
    return isprime(int("%s%s" % (a, b)))


def gen_prime_pairs(limit=1000):
    primes = list(primerange(3, limit))
    primes.remove(5)

    for pair in itertools.product(primes, primes):
        if isprimepair(*pair):
            yield pair


def is_prime_set(grp, N):
    for pair in grp:
        if (pair[1], pair[0]) not in PAIRS:
            return False
    return True


# N = 5
# def euler60():
#     primes = [3, 7, 11, 13, 17]
#     curr = primes[-1]
#     while 1:
#         curr = nextprime(curr)
#         primes.append(curr)
#         for grp in itertools.combinations(primes, N - 1):
#             if is_prime_set(curr, *grp):
#                 return [curr] + list(grp)
#         print curr

# if __name__ == "__main__":
#     print euler60()

N = 4
PAIRS = set(gen_prime_pairs(1000))
for grp in itertools.combinations(PAIRS, N):
    if is_prime_set(grp, N):
        print grp
