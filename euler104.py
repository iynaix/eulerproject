import math
from utils import is_pandigital


def euler104():
    #http://bit.ly/11cebzg
    rt5 = math.sqrt(5)
    phi = (1 + rt5) / 2

    def fib_first_digits(n, digits=9):
        """n is the n-th fib number"""
        x = n * math.log10(phi) - math.log10(rt5) + 1
        return int(pow(10, x - int(x) + digits - 1))

    tmp = 10 ** 10
    a, b, i = 0, 1, 1
    while 1:
        a, b = b % tmp, (a + b) % tmp
        if is_pandigital(a, 9):
            if is_pandigital(fib_first_digits(i)):
                return i
        i += 1
