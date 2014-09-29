def euler40():
    s = "".join([str(x) for x in range(1, 200000)])
    ret = 1
    for x in [1, 10, 100, 1000, 10000, 100000, 1000000]:
        ret *= int(s[x - 1])
    return ret
