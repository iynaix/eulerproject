def euler73():
    ret = set()
    lower, upper = 1.0 / 3, 0.5

    for d in range(1, 12001):
        for n in range(d // 3 + 1, d // 2 + 1):
            f = n * 1.0 / d
            if lower < f < upper:
                ret.add(f)
    return len(ret)
