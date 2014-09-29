import time
from sympy import nextprime


def hamming_n_count(limit, n):
    exclusions = 0

    prime = nextprime(n)
    while prime <= limit:
        print prime, limit // prime
        exclusions += limit // prime
        prime = nextprime(prime)

    print limit, exclusions
    return limit - exclusions


start = time.time()
N = 10 ** 8
N = 1000

print hamming_n_count(N, 5)
print "%ss" % (time.time() - start)
