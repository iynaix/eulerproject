from utils import fib_gen


def euler25():
    for i, x in enumerate(fib_gen(10 ** 999)):
        pass
    return i + 1 + 1
