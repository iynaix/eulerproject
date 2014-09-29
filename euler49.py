import itertools
from collections import defaultdict
from utils import primes_gen, from_digits


#get the differences of every ascending pair
def ascending_pairs(arr):
    #defaultdict with key being the difference and values being a list
    #of 2-tuples of the numbers making up the difference
    ret = defaultdict(list)
    for x in reversed(arr):
        for y in arr:
            diff = x - y
            if diff <= 0:
                break
            ret[diff].append(sorted((x, y)))
    return ret


def euler49():
    #organize the primes into groups of permutations of their digits
    grps = defaultdict(list)
    for pr in primes_gen(1000, 10000):
        grps["".join(sorted(str(pr)))].append(pr)

    for k, arr in grps.iteritems():
        #the lists will be sorted
        if len(arr) >= 3 and 1487 not in arr:
            pairs = ascending_pairs(arr)
            for k, v in pairs.iteritems():
                if len(v) >= 2:
                    #need to have matching endpoints
                    final = sorted(set(itertools.chain(*v)))
                    if len(final) == 3:
                        return from_digits(final)
