from utils import is_abundant


def euler23():
    limit = 28123
    abundant_nums = [i for i in range(12, limit) if is_abundant(i)]

    abundant_nums_sums = set()
    for i in abundant_nums:
        for j in abundant_nums:
            s = i + j
            if s < limit:
                abundant_nums_sums.add(s)

    ret = 0
    for i in range(1, limit):
        if i not in abundant_nums_sums:
            ret += i
    return ret
