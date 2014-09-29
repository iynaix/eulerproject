from sympy import isprime


def euler27():
    max_n, max_a, max_b = -5000, -5000, -5000
    for a in range(-999, 1000):
        for b in range(-999, 1000):
            n = 0
            while 1:
                if not isprime(n * n + a * n + b):
                    # print a, b, n, n * n + a * n + b
                    if n > max_n:
                        max_n = n
                        max_a = a
                        max_b = b
                    break
                n += 1
    return max_a * max_b
