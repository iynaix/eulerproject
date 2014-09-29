from sympy import totient


def euler72():
    ret = 0
    for d in xrange(2, 1000001):
        ret += totient(d)
    return ret
