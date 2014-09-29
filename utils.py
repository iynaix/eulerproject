import math
from collections import deque
from functools import wraps
from sympy import primerange, nextprime, divisors, isprime


def prod(arr):
    """returns the product of the given iterable"""
    ret = 1
    for i in arr:
        ret *= i
    return ret


def digits(n):
    """returns the individual digits of the given number"""
    return [int(x) for x in str(n)]


def from_digits(arr):
    """composes an integer from an array of digits"""
    return int("".join([str(x) for x in arr]))


def window(seq, n=2):
    """
    Returns a sliding window (of width n) over data from the iterable
       s -> (s0,s1,...s[n-1]), (s1,s2,...,sn), ...
    """

    it = iter(seq)
    win = deque((next(it, None) for _ in xrange(n)), maxlen=n)
    yield win
    append = win.append
    for e in it:
        append(e)
        yield win


def is_abundant(n):
    return sum(divisors(n)) - n > n


def is_palindrome(n):
    if not isinstance(n, str):
        n = str(n)
    return n == n[::-1]


def is_amicable(n):
    a = sum(divisors(n)) - n
    return a != n and sum(divisors(a)) - a == n


def fibn(n):
    rt5 = math.sqrt(5)
    return int(((1 + rt5) ** n - (1 - rt5) ** n) / ((2 ** n) * rt5))


def primes_gen(*args):
    """
    Prime number generator

    Possible usages:
        primes_gen(): infinite generator
        primes_gen(a): generate all primes below a
        primes_gen(a, b): generate all primes below a and b
    """
    if len(args) == 1:
        for x in primerange(2, args[0]):
            yield x
    elif len(args) == 2:
        for x in primerange(*args):
            yield x
    elif len(args) == 0:
        x = 1
        while 1:
            x = nextprime(x)
            yield x


class SeqGenerator(object):
    """
    Abstract base class for generating a sequence of numbers
    """
    def __init__(self, *args):
        self.n = 1
        self.x = 1
        self.args = args

    def __iter__(self):
        return self

    def _calc(self):
        """
        actual meat of the calculation goes here
        """
        raise NotImplementedError

    def next(self):
        self.x = self._calc()
        self.n += 1

        if len(self.args) == 1:
            if self.x > self.args[0]:
                raise StopIteration()
            return self.x
        elif len(self.args) == 2:
            if self.x > self.args[1]:
                raise StopIteration()
            if self.args[0] <= self.x:
                return self.x
            return self.next()
        else:
            return self.x


class power_gen(SeqGenerator):
    """generates a list of powers"""

    def __init__(self, order, *args):
        self.order = order
        super(power_gen, self).__init__(*args)

    def _calc(self):
        return self.n ** self.order


class polygonal_gen(SeqGenerator):
    """generates a list of polygonal numbers"""

    def __init__(self, order, *args):
        self.order = order
        super(polygonal_gen, self).__init__(*args)

    def _calc(self):
        return self.n * (self.order - 2) * (self.n - 1) / 2 + self.n


class fib_gen(SeqGenerator):
    """generates a list of fibonacci numbers"""

    def __init__(self, *args):
        self.n = 1
        self.x = 0
        self.y = 1
        self.args = args

    def _calc(self):
        self.x, self.y = self.y, self.x + self.y
        return self.x


def is_pandigital(n, length=None):
    d = digits(n)
    if length is not None and len(d) != length:
        return False
    return sorted(d) == range(1, 1 + len(d))


def is_permutation(a, b):
    return sorted(str(a)) == sorted(str(b))


def is_int(n):
    return n == int(n)


def is_triangular(n):
    d = math.sqrt(8 * n + 1)
    x1 = (-d - 1) / 2
    x2 = (d - 1) / 2
    return (x1 > 0 and is_int(x1)) or (x2 > 0 and is_int(x2))


def is_pentagonal(n):
    d = math.sqrt(24 * n + 1)
    x1 = (1 - d) / 6
    x2 = (d + 1) / 6
    return (x1 > 0 and is_int(x1)) or (x2 > 0 and is_int(x2))


def combination(n, r):
    """returns the nCr value given n and r <= n"""
    f = math.factorial
    return f(n) / (f(r) * f(n - r))


def is_square(n):
    return is_int(math.sqrt(n))


def is_hamming_n(x, type_n):
    """returns the prime factorization of the given number as a list"""
    loop = 2
    while loop <= x:
        if x % loop == 0:
            x /= loop
            if loop > type_n:
                return False
        else:
            loop += 1
    return True


def multiplicands(n):
    """returns pairs of numbers of (a, b) such that a * b = c"""
    d = divisors(n)
    l = len(d)
    return [(d[i], d[l - i - 1]) for i in range(l // 2)]


def odd_composite_gen():
    """infinite generator of composite numbers"""
    x = 3
    while 1:
        x += 2
        if not isprime(x):
            yield x


def cumsum(arr):
    """
    returns the cumulative sum of the given array
    """
    ret = []
    s = 0
    for x in arr:
        s += x
        ret.append(s)
    return ret


def pmap(func, arr):
    """
    parallel map
    cheat by mapping func over arr and spreading the workload over cpus
    """
    import multiprocessing
    cpus = multiprocessing.cpu_count()
    p = multiprocessing.Pool(cpus)

    return p.map(func, arr)


def pmaprange(func, arr):
    """
    parallel map
    cheat by splitting the arr into chunks and spreading the workload over cpus
    """
    import multiprocessing
    cpus = multiprocessing.cpu_count()
    p = multiprocessing.Pool(cpus)

    arrs = []
    segment_len, rem = divmod(len(arr), cpus)
    for i in range(cpus):
        arrs.append(arr[i * segment_len:i * segment_len + segment_len])
    #shove the remainder into the last segment
    arrs[-1].extend(arr[-rem:])
    return p.map(func, arrs)


def memoize(func):
    cache = {}

    @wraps(func)
    def wrap(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrap
