from utils import primes_gen


def euler187():
    composites = set()
    limit = 10 ** 8

    prs = list(primes_gen(limit // 2))
    for x in prs:
        for y in prs:
            res = x * y
            if res > limit:
                break
            composites.add(res)
    return len(composites)
