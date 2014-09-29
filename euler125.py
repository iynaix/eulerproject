import math
from utils import window, is_palindrome


def euler125():
    N = 10 ** 8
    squares = [x * x for x in range(1, int(math.sqrt(N)))]

    ret = set()
    for window_len in range(2, len(squares)):
        for arr in window(squares, window_len):
            s = sum(arr)
            if s >= N:
                break
            if is_palindrome(s):
                ret.add(s)
    return sum(ret)
