from utils import digits


def euler119():
    a = set()
    for x in range(2, 100):
        for y in range(2, 100):
            res = x ** y
            if sum(digits(res)) == x:
                a.add(res)

    return sorted(a)[30 - 1]
