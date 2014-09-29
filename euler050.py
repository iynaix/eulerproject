from utils import cumsum, primes_gen


def euler50():
    #get the cumulative sums for primes up to 1000000
    s, limit = 0, 1000000
    prs = list(primes_gen(limit))
    cum_prs = cumsum(prs)
    prs = set(prs)

    #find consecutive sums by iterating forward and backward through the
    #cumulative sums
    ret = 0
    for x in reversed(cum_prs):
        for y in cum_prs:
            diff = x - y
            if diff >= limit:
                break
            if diff <= 0:
                break
            if diff in prs:
                ret = max(diff, ret)
    return ret
