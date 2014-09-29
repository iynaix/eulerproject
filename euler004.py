from utils import is_palindrome


def euler4():
    three_digits = range(100, 1000)
    ret = 0
    for x in three_digits:
        for y in three_digits:
            p = x * y
            if is_palindrome(p) and p > ret:
                ret = p
    return ret
