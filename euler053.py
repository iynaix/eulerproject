from utils import combination


def euler53():
    ret = 0
    for n in range(1, 101):
        for r in range(1, n + 1):
            ret += combination(n, r) > 1000000
    return ret
