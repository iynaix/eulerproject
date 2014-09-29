def is_small_digits(x):
    return not str(x).strip("012")


def f(n):
    i = 1
    while 1:
        if is_small_digits(n * i):
            return i
        i += 1


def euler303():
    ret = 11363107
    for x in range(101, 1001):
        print x
        ret += f(x)
    return ret


x = 999 * 3
print f(999 * 3)
