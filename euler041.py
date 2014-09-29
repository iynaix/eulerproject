from utils import primes_gen, is_pandigital


def euler41():
    #there are no 8 or 9 digit pandigital primes, as the sum of the digits wil
    #always be a multiple of 9

    #search backwards to save time
    for pr in reversed(list(primes_gen(10000000))):
        if is_pandigital(pr):
            return pr
