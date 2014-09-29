from utils import is_palindrome


def euler36():
    ret = 0
    for i in range(1, 1000000):
        if is_palindrome(i):
            if is_palindrome(bin(i)[2:]):
                ret += i
    return ret
