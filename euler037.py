import math
from utils import primes_gen


def trunc_left_gen(n):
    while n:
        yield n
        n %= 10 ** int(math.log10(n))


def trunc_right_gen(n):
    while n:
        yield n
        n //= 10


def euler37():
    trunc_primes = []
    prs = set()
    for pr in primes_gen():
        prs.add(pr)
        if pr < 10:
            continue
        if set(trunc_left_gen(pr)).issubset(prs) and \
           set(trunc_right_gen(pr)).issubset(prs):
            trunc_primes.append(pr)
        if len(trunc_primes) == 11:
            break
    return sum(trunc_primes)
