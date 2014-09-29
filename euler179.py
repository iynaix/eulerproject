from sympy import divisor_count
from utils import pmap


def euler179():
    ret = 0
    div_lens = pmap(divisor_count, range(1, 10 ** 7))
    for i in xrange(len(div_lens) - 1):
        ret += div_lens[i] == div_lens[i + 1]
    return ret
