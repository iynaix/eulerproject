from sympy import isprime


def euler58():
    cnt = 1
    prime_cnt = 0
    n = 2
    while True:
        prime_cnt += isprime(4 * n * n - 10 * n + 7)
        prime_cnt += isprime(4 * n * n - 8 * n + 5)
        prime_cnt += isprime(4 * n * n - 6 * n + 3)
        cnt += 4
        if prime_cnt * 1.0 / cnt < 0.1:
            return n * 2 + 1
        n += 1
