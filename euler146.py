import math
from collections import deque
from sympy import nextprime

start = 10 * 10 + 1
primes = deque([start] + [nextprime(start, x + 1) for x in range(5)])

def prime_pattern(arr):
    if not ((arr[5] - arr[0] == 26) and \
            (arr[4] - arr[0] == 12) and \
            (arr[3] - arr[0] == 8) and \
            (arr[2] - arr[0] == 6) and \
            (arr[1] - arr[0] == 2)):
        return 0
    n2 = arr[0] - 1
    n = int(math.sqrt(n2))
    if n * n == n2:
        return n
    else:
        return 0

limit = 10 ** 6
ret = 10
while 1:
    primes.popleft()
    primes.append(nextprime(primes[-1]))
    if primes[-1] >= limit:
        break
    ret += prime_pattern(primes)

print ret
