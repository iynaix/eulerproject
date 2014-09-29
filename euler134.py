from sympy import nextprime


def S(p1, p2):
    mult = 10 ** len(str(p1))
    res = mult + p1
    while 1:
        res += mult
        if res % p2 == 0:
            return res


def euler134():
    ret = 0
    p1, p2 = 3, 5
    while p2 < 1000000:
        p1, p2 = p2, nextprime(p2)
        ret += S(p1, p2)
    return ret
