from utils import digits


def euler56():
    ret = 0
    for a in range(1, 100):
        for b in range(1, 100):
            ret = max(ret, sum(digits(a ** b)))
    return ret
