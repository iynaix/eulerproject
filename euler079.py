import itertools
from collections import defaultdict


def euler79():
    def is_correct_order(arr, after_constraints):
        for k, v in after_constraints.iteritems():
            for x in v:
                #whoops, comes before
                if arr.index(x) < arr.index(k):
                    return False
        return True

    with open("keylog79.txt", "rU") as fp:
        nums = set(fp.read().splitlines())

    #construct lists of what digit can occur before and after another digit
    afters = defaultdict(set)
    digits = set()
    for n in nums:
        digits.update(n)
        afters[n[0]].add(n[1])
        afters[n[1]].add(n[2])

    for perm in itertools.permutations(digits):
        if is_correct_order(perm, afters):
            return ''.join(perm)
