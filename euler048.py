from utils import digits, from_digits


def euler48():
    return from_digits(digits(sum([x ** x for x in range(1, 1001)]))[-10:])
