def euler71():
    target = 3.0 / 7
    min_diff = 1
    ret = 0

    for d in xrange(3, 1000001):
        n = int(target * d)
        f = n / (d * 1.0)
        if f == target:
            n -= 1
            f = n / (d * 1.0)

        new_diff = target - f
        if new_diff < min_diff:
            min_diff = new_diff
            ret = n
    return ret
