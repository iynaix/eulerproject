from utils import primes_gen
from sympy import totient


cache = {}


def totient_chain_length(n):
    global cache
    if n == 1:
        return 1
    if n not in cache:
        cache[n] = totient_chain_length(totient(n))
    return 1 + cache[n]


def euler214():
    ret = 0
    for pr in primes_gen(40000000):
        if totient_chain_length(pr) == 25:
            ret += pr

    return ret
