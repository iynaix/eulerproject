import math
from utils import digits


def euler20():
    return sum(digits(math.factorial(100)))
