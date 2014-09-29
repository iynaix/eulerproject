from utils import digits


def euler30():
    ret = 0
    for i in range(2, (9 ** 5) * 5 + 1):
        if sum([x ** 5 for x in digits(i)]) == i:
            ret += i
    return ret
