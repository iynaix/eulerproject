import math
from utils import digits


def euler74():
    facts = [math.factorial(i) for i in range(10)]
    cache = {}

    def fact_sum(n):
        return sum(facts[i] for i in digits(n))

    def fact_chain_len(n):
        seq = set([n])
        x = n
        while 1:
            x = fact_sum(x)
            if x in cache:
                ret = len(seq) + cache[x]
                cache[n] = ret
                return ret
            if x in seq:
                ret = len(seq)
                cache[n] = ret
                return ret
            seq.add(x)

    ret = 0
    for i in range(1, 1000000):
        ret += fact_chain_len(i) == 60
    return ret
