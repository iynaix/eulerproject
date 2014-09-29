from collections import defaultdict
from utils import primes_gen


def euler118():
    #there are no 9 digit pandigital primes as their digital sum is divisible
    #by 3
    prs = defaultdict(set)
    for pr in primes_gen(10 ** 8):
        pr = str(pr)
        if "0" in pr:
            continue
        pr_len = len(pr)
        if len(set(pr)) == pr_len:
            prs[pr_len].add(pr)

    for k, v in prs.iteritems():
        print k, len(v)
