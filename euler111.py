import itertools
from collections import Counter, defaultdict
from sympy import primerange, isprime


def euler111_brute_force():
    digit_counts = defaultdict(int)
    for pr in primerange(10 ** (10 - 1), 10 ** (10 - 1 + 1)):
        cnts = Counter(str(pr))
        for x in cnts.most_common():
            if x[1] < 2:
                break
            digit_counts[x] += pr

    Sd = defaultdict(list)
    for digit_cnt, s in sorted(digit_counts.items()):
        Sd[digit_cnt[0]].append(s)

    return sum(a[-1] for a in Sd.values())


def replace_repeats(digit, length, replacements):
    digit = str(digit)
    rngs = [list("0123456789") for x in range(replacements)]
    for combi in itertools.combinations(range(length), replacements):
        for x in itertools.product(*rngs):
            s = list(digit * length)
            for place_no, place in enumerate(combi):
                s[place] = x[place_no]
            s = ''.join(s)
            if s[0] != "0" and isprime(int(s)):
                yield int(s)


def S(digit, length):
    for replacements in range(1, length):
        results = list(replace_repeats(digit, length, replacements))
        if results:
            return sum(results)


def euler111():
    return sum(S(d, 10) for d in range(10))


print euler111()
