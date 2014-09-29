from utils import is_pentagonal


def pentagonal(n):
    """returns the n-th pentagonal numer"""
    return int((n / 2.0) * (3 * n - 1))


def euler44():

    pentagonals = [pentagonal(1)]
    pent_start = 2
    while True:
        p_k = pentagonal(pent_start)
        pentagonals.append(p_k)
        for p_j in pentagonals[:-1]:
            if is_pentagonal(p_k - p_j) and is_pentagonal(p_k + p_j):
                return p_k - p_j
        pent_start += 1
