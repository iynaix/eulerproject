from fractions import Fraction


def euler57():
    fracs = []
    frac = Fraction(5, 2)
    for x in range(2, 1000):
        frac = 2 + 1 / frac
        fracs.append(frac)

    fracs = [Fraction(3, 2), Fraction(7, 5)] + [1 + 1 / x for x in fracs]
    cnt = 0
    for x in fracs:
        if len(str(x.numerator)) > len(str(x.denominator)):
            cnt += 1
    return cnt
