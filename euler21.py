from utils import is_amicable


def euler21():
    return sum([x for x in range(1, 10000) if is_amicable(x)])
