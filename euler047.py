from sympy import primefactors


def euler47():
    n = 2 * 3 * 5 * 7
    while True:
        if len(primefactors(n)) != 4:
            n += 1
            continue
        elif len(primefactors(n + 1)) != 4:
            n += 2
            continue
        elif len(primefactors(n + 2)) != 4:
            n += 3
            continue
        elif len(primefactors(n + 3)) != 4:
            n += 4
            continue
        return n
