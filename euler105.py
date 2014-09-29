import itertools


def combinations_all(arr):
    for n in range(1, len(arr) + 1):
        for x in itertools.combinations(arr, n):
            yield x


def is_special_sum_set(S):
    for b in combinations_all(S):
        for c in combinations_all(S.difference(b)):
            Sb = sum(b)
            Sc = sum(c)

            if Sb == Sc:
                return False

            if len(b) > len(c) and not Sb > Sc:
                return False
    return True


def euler105():
    ret = 0
    for line in open("sets105.txt").readlines():
        S = set(int(x) for x in line.split(','))
        if is_special_sum_set(S):
            ret += sum(S)
    return ret
