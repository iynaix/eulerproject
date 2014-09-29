from sympy import npartitions


def euler78():
    i = 1
    while 1:
        if npartitions(i) % 1000000 == 0:
            return i
        i += 1
