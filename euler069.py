from sympy import totient


def euler69():
    ret = 0
    max_calc = 0
    for n in xrange(2, 1000001):
        t = n * 1.0 / totient(n)
        if max(max_calc, t) == t:
            max_calc = t
            ret = n
    return ret
