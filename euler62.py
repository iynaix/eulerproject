from collections import defaultdict


def euler62():
    i = 1
    tbl = defaultdict(list)
    while 1:
        cube = i * i * i
        #normalise the permutation
        key = "".join(sorted(str(cube)))
        tbl[key].append(cube)
        if len(tbl[key]) == 5:
            return tbl[key][0]
        i += 1
