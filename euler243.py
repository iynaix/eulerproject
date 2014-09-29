from fractions import Fraction
from sympy import totient

def R(d):
    """
    The number of resilient fractions can be given as the Euler totient of the
    given number n as we are looking for the number of coprime integers less
    than n.

    So R(d) = totient(d) / (d-1)
    """
    return Fraction(totient(d), d - 1)

def euler243():
    goal = Fraction(15499, 94744)
    n = 12
    while 1:
        rn = R(n)
        print n, rn
        if rn < goal:
            return n
        n += 1


print euler243()
