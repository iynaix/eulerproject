from utils import fib_gen


def euler2():
    return sum(r for r in fib_gen(4000000) if r % 2 == 0)
