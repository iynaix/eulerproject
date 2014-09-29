def euler29():
    ret = set()
    for a in range(2, 101):
        for b in range(2, 101):
            ret.add(a ** b)
    return len(ret)
