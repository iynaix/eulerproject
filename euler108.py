from sympy.solvers.diophantine import diop_quadratic
from sympy.abc import x, y, t


def num_solutions(n):
    ret = set()
    for a, b in diop_quadratic(n * y + n * x - x * y, t):
        if a <= 0 or b <= 0:
            continue
        ret.add(frozenset((a, b)))
    return len(ret)


i = 4
while 1:
    if num_solutions(i) > 1000:
        print i
        break
    i += 1
