import math
from utils import digits, memoize


"""
Define f(n) as the sum of the factorials of the digits of n. For example, f(342) = 3! + 4! + 2! = 32.

Define sf(n) as the sum of the digits of f(n). So sf(342) = 3 + 2 = 5.

Define g(i) to be the smallest positive integer n such that sf(n) = i. Though sf(342) is 5, sf(25) is also 5, and it can be verified that g(5) is 25.

Define sg(i) as the sum of the digits of g(i). So sg(5) = 2 + 5 = 7.

Further, it can be verified that g(20) is 267 and ∑ sg(i) for 1 ≤ i ≤ 20 is 156.

What is ∑ sg(i) for 1 ≤ i ≤ 150?
"""

FACTORIALS = {}
for i in range(10):
    FACTORIALS[i] = math.factorial(i)


def f(n):
    return sum(FACTORIALS[d] for d in digits(n))


@memoize
def sf(n):
    return sum(digits(f(n)))


g_dict = {}

n = 1
limit = 150
limit = 50
while 1:
    sfn = sf(n)
    if 0 < sfn <= limit and sfn not in g_dict:
        print sfn, len(g_dict), n
        g_dict[sfn] = n
    if len(g_dict) == limit:
        break
    n += 1

print sum(sum(digits(x)) for x in g_dict.values())
