from utils import primes_gen


def rotate_digits(n):
    """rotates the digits of a given number in round robin fashion"""
    n = str(n)

    for i in range(len(n)):
        n = n[-1] + n[:-1]
        yield int(n)


def is_circular_prime(n, prime_set):
    """
    is the given number circular?
    prime_set is a set of primes to check against
    """
    for x in rotate_digits(n):
        if x not in prime_set:
            return False
    return True


def euler35():
    prs = set(primes_gen(10 ** 6))
    return len([p for p in prs if is_circular_prime(p, prs)])
