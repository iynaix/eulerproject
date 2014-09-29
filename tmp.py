from sympy.ntheory import npartitions

def solution():
    n = 6
    while 1:
        if npartitions(6) % 100== 0:
            return n
        n += 1


print solution()
