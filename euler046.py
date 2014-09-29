from sympy import isprime
from utils import odd_composite_gen


def euler46():
    sq2 = [2 * x * x for x in range(1, 1001)]

    def is_goldbach(n):
        """can n can be written as the sum of a prime and twice a square?"""
        for s in sq2:
            if s >= n:
                break
            if isprime(n - s):
                return True
        return False

    for x in odd_composite_gen():
        if not is_goldbach(x):
            return x
